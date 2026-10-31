# WARM GATE (5.33.199): cold-start gate of the WARM system.
# Sequence (Rob): (1) splash first (2) skin windows/layouts/controls build under splash
# (3) artwork cache (4) splash fades — no pop / no blank.
# 5.33.199: do NOT ActivateWindow(1113). Custom_1113 is type=dialog (modal) and blocked
# ReplaceWindow → Music 10502 ("Activate … refused because there are active modal dialogs")
# on 196/197. Splash is BezelWarmGateOverlay (property bz_warm_gate) on Startup + Music + Videos.
# Doc: behaviors/mm-warm.md
import json, time, threading, xbmc, xbmcgui
home = xbmcgui.Window(10000); mon = xbmc.Monitor()
CAP = 5.0
PATHS = {'music': ('musicdb://artists/', 'music'), 'movies': ('videodb://movies/titles/', 'video'), 'tv': ('videodb://tvshows/titles/', 'video')}
# Landing underlay painted: list 60 on the Startup-highlight section (bz_at_mmdef)
LAND = {
    'music':  'Window.IsActive(music) + !Container(60).IsUpdating + Integer.IsGreater(Container(60).NumItems,0)',
    'movies': 'Window.IsActive(videos) + [Container.Content(movies) | Container.Content(sets)] + !Container(60).IsUpdating + Integer.IsGreater(Container(60).NumItems,0)',
    'tv':     'Window.IsActive(videos) + Container.Content(tvshows) + !Container(60).IsUpdating + Integer.IsGreater(Container(60).NumItems,0)',
}
# Softer land: section window active (layouts building) even before list items exist
_lock = threading.Lock()

def warm(sec):
    path, media = PATHS[sec]
    try:
        xbmc.executeJSONRPC(json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': 'Files.GetDirectory',
                                         'params': {'directory': path, 'media': media, 'properties': ['thumbnail', 'art'], 'limits': {'start': 0, 'end': 400}}}))
    except Exception:
        pass
    home.setProperty('bz_warm_ready_' + sec, '1')

def dismiss(vis):
    with _lock:
        if home.getProperty('bz_splash_done') == '1':
            return
        # Clear gate → BezelWarmGateOverlay Hidden fade (500 ms). Never Dialog.Close(1113) — not opened.
        home.clearProperty('bz_warm_gate')
        if vis and xbmc.getCondVisibility('Window.IsVisible(1113)'):
            xbmc.executebuiltin('Dialog.Close(1113,true)')
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
    # Intentionally NO ActivateWindow(1113) — modal deadlock fixed in 5.33.199
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

        def watchdog():
            end = t0 + CAP
            while time.time() < end and not mon.abortRequested():
                if home.getProperty('bz_splash_done') == '1':
                    return
                mon.waitForAbort(0.1)
            if home.getProperty('bz_splash_done') != '1':
                dismiss(vis)
        threading.Thread(target=watchdog, daemon=True).start()

        # Phase 2: wait for StartupWindow underlay to activate + list paint (possible now — no modal)
        while time.time() - t0 < CAP and not mon.abortRequested():
            if home.getProperty('bz_splash_done') == '1':
                break
            if xbmc.getCondVisibility(land):
                break
            mon.waitForAbort(0.05)
        else:
            # Cap path: if window at least active, continue to art; else dismiss soon via finally
            pass

        # Phase 3: artwork cache AFTER underlay is up (or late in CAP). Focused section first.
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
                    break
                mon.waitForAbort(0.05)
    finally:
        dismiss(vis)
        while time.time() - t0 < CAP and not mon.abortRequested():
            if all(home.getProperty('bz_warm_ready_' + s) for s in PATHS):
                break
            mon.waitForAbort(0.1)
main()
