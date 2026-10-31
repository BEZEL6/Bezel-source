# WARM GATE (5.33.198): cold-start gate of the WARM system.
# Splash 1113 is first paint; warm-caches Music/Movies/TV lists (Tuner Startup highlight first, other two after),
# sets bz_warm_ready_<sec>; last flag (or ~5 s hard cap) -> fade-out dismiss, then bz_splash_done=1.
# 5.33.196: ALL Files.GetDirectory warms run off the main thread so the 5 s cap / Dialog.Close always run
# even if a JSON-RPC hangs on Shield. Ready flags flip after each warm attempt (success or fail).
# 5.33.198: do NOT wait for landing list paint to dismiss — 1113 is a modal dialog and blocks
# ActivateWindow(StartupWindow)/Music, so the land condition could never become true (blank after splash).
# Dismiss as soon as all ready flags are set (or at CAP). After close, re-assert StartupWindow if needed.
# Focus/highlight is untouched (MM-first: strip 6996, no list highlight). Doc: behaviors/mm-warm.md
import json, time, threading, xbmc, xbmcgui
home = xbmcgui.Window(10000); mon = xbmc.Monitor()
CAP = 5.0
PATHS = {'music': ('musicdb://artists/', 'music'), 'movies': ('videodb://movies/titles/', 'video'), 'tv': ('videodb://tvshows/titles/', 'video')}
_lock = threading.Lock()

def warm(sec):
    path, media = PATHS[sec]
    try:
        xbmc.executeJSONRPC(json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': 'Files.GetDirectory',
                                         'params': {'directory': path, 'media': media, 'properties': ['thumbnail', 'art'], 'limits': {'start': 0, 'end': 400}}}))
    except Exception:
        pass
    home.setProperty('bz_warm_ready_' + sec, '1')   # always flip — success or fail

def dismiss(vis):
    with _lock:
        if home.getProperty('bz_splash_done') == '1':
            return
        home.clearProperty('bz_warm_gate')
        if vis:
            xbmc.executebuiltin('Dialog.Close(1113,true)')   # force close; WindowClose fade still plays when possible
        home.setProperty('bz_splash_done', '1')
        home.clearProperty('bz_warmgate_running')
        # 5.33.198: modal 1113 blocked ReplaceWindow(StartupWindow) — nudge it now that the dialog is closing
        sw = xbmc.getInfoLabel('System.StartupWindow') or ''
        if sw and not xbmc.getCondVisibility('Window.IsActive(%s)' % sw):
            xbmc.executebuiltin('ActivateWindow(%s)' % sw)

def main():
    if home.getProperty('bz_warmgate_running'):
        return
    home.setProperty('bz_warmgate_running', '1')
    t0 = time.time()
    vis = xbmc.getInfoLabel('Skin.String(bz_at_warmsplash)') != 'Off'   # Tuner toggle: visuals only; warm always runs
    if not vis:
        home.clearProperty('bz_warm_gate')
    else:
        # Startup no longer ActivateWindow(1113) in onload (that blocked RunScript/ReplaceWindow). Open it here ASAP.
        if not xbmc.getCondVisibility('Window.IsVisible(1113)'):
            xbmc.executebuiltin('ActivateWindow(1113)')
    try:
        for s in PATHS:
            home.clearProperty('bz_warm_ready_' + s)
        try:
            r = min(max(int(xbmc.getInfoLabel('Skin.String(bz_at_mmdef)') or '3'), 1), 3) - 1
        except Exception:
            r = 2
        order = ['music', 'movies', 'tv']
        first = order[r]
        # Focused section first, then the other two — ALL off the main thread so CAP cannot hang
        def run_warms():
            warm(first)
            for s in order:
                if s != first:
                    warm(s)
        threading.Thread(target=run_warms, daemon=True).start()
        # Watchdog: force dismiss at CAP even if the wait loop is disrupted
        def watchdog():
            end = t0 + CAP
            while time.time() < end and not mon.abortRequested():
                if home.getProperty('bz_splash_done') == '1':
                    return
                mon.waitForAbort(0.1)
            if home.getProperty('bz_splash_done') != '1':
                dismiss(vis)
        threading.Thread(target=watchdog, daemon=True).start()

        while time.time() - t0 < CAP and not mon.abortRequested():
            if home.getProperty('bz_splash_done') == '1':
                break
            # Keep splash visible only while gate property is set (cleared in dismiss — never re-open after)
            if vis and home.getProperty('bz_warm_gate') == '1' and not xbmc.getCondVisibility('Window.IsVisible(1113)'):
                xbmc.executebuiltin('ActivateWindow(1113)')
            # 5.33.198: ready flags alone — do not wait for land (modal 1113 blocks StartupWindow)
            if all(home.getProperty('bz_warm_ready_' + s) for s in PATHS):
                break
            mon.waitForAbort(0.05)
    finally:
        dismiss(vis)
        # Keep the script alive until CAP so background warms can finish after early dismiss
        while time.time() - t0 < CAP and not mon.abortRequested():
            if all(home.getProperty('bz_warm_ready_' + s) for s in PATHS):
                break
            mon.waitForAbort(0.1)
main()
