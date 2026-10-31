# WARM GATE (5.33.200): cold-start gate of the WARM system.
# Sequence (Rob): (1) splash first (2) skin windows/layouts/controls build under splash
# (3) artwork cache (4) splash fades — no pop / no blank.
# 5.33.199: non-modal BezelWarmGateOverlay (bz_warm_gate) on Startup + Music + Videos.
# 5.33.200: splash display MIN 5.0 s, CAP/max 15.0 s; dismiss fade-out 3.0 s (overlay Hidden anim).
# Doc: behaviors/mm-warm.md
import json, time, threading, xbmc, xbmcgui
home = xbmcgui.Window(10000); mon = xbmc.Monitor()
MIN = 5.0    # never fade before this
CAP = 15.0   # force dismiss by this even if work incomplete
FADE = 3.0   # seconds for overlay Hidden fade after clearing bz_warm_gate
PATHS = {'music': ('musicdb://artists/', 'music'), 'movies': ('videodb://movies/titles/', 'video'), 'tv': ('videodb://tvshows/titles/', 'video')}
LAND = {
    'music':  'Window.IsActive(music) + !Container(60).IsUpdating + Integer.IsGreater(Container(60).NumItems,0)',
    'movies': 'Window.IsActive(videos) + [Container.Content(movies) | Container.Content(sets)] + !Container(60).IsUpdating + Integer.IsGreater(Container(60).NumItems,0)',
    'tv':     'Window.IsActive(videos) + Container.Content(tvshows) + !Container(60).IsUpdating + Integer.IsGreater(Container(60).NumItems,0)',
}
_lock = threading.Lock()

def warm(sec):
    path, media = PATHS[sec]
    try:
        xbmc.executeJSONRPC(json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': 'Files.GetDirectory',
                                         'params': {'directory': path, 'media': media, 'properties': ['thumbnail', 'art'], 'limits': {'start': 0, 'end': 400}}}))
    except Exception:
        pass
    home.setProperty('bz_warm_ready_' + sec, '1')

def hold_until(t0, secs):
    while not mon.abortRequested():
        left = secs - (time.time() - t0)
        if left <= 0:
            return
        mon.waitForAbort(min(0.05, left))

def dismiss(vis):
    with _lock:
        if home.getProperty('bz_splash_done') == '1':
            return
        # Start overlay fade (BezelWarmGateOverlay Hidden = FADE ms in XML)
        home.clearProperty('bz_warm_gate')
        if vis and xbmc.getCondVisibility('Window.IsVisible(1113)'):
            xbmc.executebuiltin('Dialog.Close(1113,true)')
    # Fade outside lock so watchdog/main don't deadlock; wait for 3 s anim
    if vis:
        end = time.time() + FADE
        while time.time() < end and not mon.abortRequested():
            if home.getProperty('bz_splash_done') == '1':
                return
            mon.waitForAbort(0.05)
    with _lock:
        if home.getProperty('bz_splash_done') == '1':
            return
        home.setProperty('bz_splash_done', '1')
        home.clearProperty('bz_warmgate_running')

def main():
    if home.getProperty('bz_warmgate_running'):
        return
    home.setProperty('bz_warmgate_running', '1')
    t0 = time.time()
    vis = xbmc.getInfoLabel('Skin.String(bz_at_warmsplash)') != 'Off'
    if not vis:
        home.clearProperty('bz_warm_gate')
    elif home.getProperty('bz_warm_gate') != '1':
        home.setProperty('bz_warm_gate', '1')
    try:
        for s in PATHS:
            home.clearProperty('bz_warm_ready_' + s)
        try:
            r = min(max(int(xbmc.getInfoLabel('Skin.String(bz_at_mmdef)') or '3'), 1), 3) - 1
        except Exception:
            r = 2
        order = ['music', 'movies', 'tv']
        first = order[r]
        land = LAND[first]
        ready = False

        def watchdog():
            end = t0 + CAP
            while time.time() < end and not mon.abortRequested():
                if home.getProperty('bz_splash_done') == '1':
                    return
                mon.waitForAbort(0.1)
            if home.getProperty('bz_splash_done') != '1':
                hold_until(t0, MIN)
                dismiss(vis)
        threading.Thread(target=watchdog, daemon=True).start()

        # Phase 2: underlay land (up to CAP)
        while time.time() - t0 < CAP and not mon.abortRequested():
            if home.getProperty('bz_splash_done') == '1':
                break
            if xbmc.getCondVisibility(land):
                break
            mon.waitForAbort(0.05)

        # Phase 3: art warm
        if home.getProperty('bz_splash_done') != '1':
            def run_warms():
                warm(first)
                for s in order:
                    if s != first:
                        warm(s)
            threading.Thread(target=run_warms, daemon=True).start()
            while time.time() - t0 < CAP and not mon.abortRequested():
                if home.getProperty('bz_splash_done') == '1':
                    break
                if all(home.getProperty('bz_warm_ready_' + s) for s in PATHS):
                    ready = True
                    break
                mon.waitForAbort(0.05)
    finally:
        # Ready early → still hold to MIN; never past CAP (watchdog); then 3 s fade
        hold_until(t0, MIN)
        dismiss(vis)
        # Allow late warms to finish quietly after fade started (up to CAP)
        while time.time() - t0 < CAP and not mon.abortRequested():
            if all(home.getProperty('bz_warm_ready_' + s) for s in PATHS):
                break
            mon.waitForAbort(0.1)
main()
