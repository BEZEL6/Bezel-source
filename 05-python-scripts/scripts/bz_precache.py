# BEZEL 3.0: artwork pre-cache. Starts ~1 min after boot, one image at a time, through a hidden 1 px image control
# (BezelPrecacheImg) so Kodi's own texture cache does the work. Pauses while scrolling / playing / fullscreen and resumes
# ~3 s after the last key press. Off with Skin.ToggleSetting(bz_precache_off).
import json, xbmc, xbmcgui
home = xbmcgui.Window(10000); mon = xbmc.Monitor()
def rpc(m, p):
    try: return json.loads(xbmc.executeJSONRPC(json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': m, 'params': p}))).get('result', {}) or {}
    except Exception: return {}
def cached(u):
    return bool(rpc('Textures.GetTextures', {'filter': {'field': 'url', 'operator': 'is', 'value': u}, 'properties': ['url']}).get('textures'))
def busy():
    if home.getProperty('bz_quit'): raise SystemExit   # BEZEL 3.0 exit fix
    return xbmc.getCondVisibility('Skin.HasSetting(bz_precache_off) | Player.HasMedia | Window.IsActive(fullscreenvideo) | '
                                  'Container.Scrolling | !System.IdleTime(3) | Window.IsActive(1113) | !String.IsEmpty(Window(Home).Property(bz_warm_gate))')
def urls():
    for k, m, key, props in (('albums', 'AudioLibrary.GetAlbums', 'albums', ['thumbnail']),
                             ('artists', 'AudioLibrary.GetArtists', 'artists', ['thumbnail', 'fanart']),
                             ('movies', 'VideoLibrary.GetMovies', 'movies', ['art']),
                             ('tvshows', 'VideoLibrary.GetTVShows', 'tvshows', ['art'])):
        for it in rpc(m, {'properties': props}).get(key, []):
            for u in [it.get('thumbnail'), it.get('fanart')] + [it.get('art', {}).get(a) for a in ('poster', 'fanart', 'thumb')]:
                if u: yield u
if home.getProperty('bz_precache_running') != 'true':
    home.setProperty('bz_precache_running', 'true')
    try:
        _w = 0
        while _w < 120 and not home.getProperty('bz_quit') and not mon.waitForAbort(0.5): _w += 1   # BEZEL 3.0 exit fix: 60 s start delay, quit-aware
        if _w >= 120:
            for u in urls():
                while busy():
                    if mon.waitForAbort(1): raise SystemExit
                if cached(u): continue
                home.setProperty('bz_pc_img', u)
                for _ in range(16):          # up to 8 s per image
                    if mon.waitForAbort(0.5): raise SystemExit
                    if cached(u): break
                home.clearProperty('bz_pc_img')
                if mon.waitForAbort(0.3) or home.getProperty('bz_quit'): break
    except SystemExit: pass
    finally:
        if not mon.abortRequested(): home.clearProperty('bz_pc_img'); home.clearProperty('bz_precache_running')   # BEZEL 3.0 exit fix
