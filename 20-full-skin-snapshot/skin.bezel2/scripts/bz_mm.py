# BEZEL 4.1 O46/O47: strip-list Main menu actions. Stores the leaving section's art (bz_lastart_<sec>) then runs the item.
import sys, time, xbmc, xbmcgui
home = xbmcgui.Window(10000)
def cursec():
    if xbmc.getCondVisibility('Window.IsActive(music)'): return 'music'
    if xbmc.getCondVisibility('Window.IsActive(videos) + Container.Content(musicvideos)'): return 'mv'
    if xbmc.getCondVisibility('Window.IsActive(videos) + [Container.Content(tvshows) | Container.Content(seasons) | Container.Content(episodes)]'): return 'tv'
    if xbmc.getCondVisibility('Window.IsActive(videos)'): return 'movies'
    return ''
def store():
    s = cursec()
    if not s: return
    for k in ('Art(fanart)', 'Art(poster)', 'Art(thumb)', 'Art(tvshow.poster)'):
        a = xbmc.getInfoLabel('Container(60).ListItem.%s' % k)
        if a and 'DefaultFolderBack' not in a: xbmc.executebuiltin('Skin.SetString(bz_lastart_%s,%s)' % (s, a)); return
GO = {
 'music': ['SetProperty(bz_navroot,musicdb://albums/,home)', 'RunScript(special://skin/scripts/bz_cmd.py,tomusic,musicdb://albums/)'],
 'movies': ['SetProperty(bz_navroot,videodb://movies/titles/,home)', 'RunScript(special://skin/scripts/bz_cmd.py,go,videodb://movies/titles/)'],
 'tv': ['SetProperty(bz_navroot,videodb://tvshows/titles/,home)', 'RunScript(special://skin/scripts/bz_cmd.py,go,videodb://tvshows/titles/)'],
 'mv': ['RunScript(special://skin/scripts/bz_cmd.py,go,videodb://musicvideos/)'],
 'recent': ['SetProperty(bz_navroot,musicdb://recentlyplayedalbums/,home)', 'RunScript(special://skin/scripts/bz_cmd.py,tomusic,musicdb://recentlyplayedalbums/)'],
 'fav': ['ClearProperty(bz_nav,home)', 'ActivateWindow(favouritesbrowser)'],
 'playlists': ['RunScript(special://skin/scripts/bz_cmd.py,tomusic,special://musicplaylists/)'],
 'search': ['ClearProperty(bz_nav,home)', 'ActivateWindow(1107)'],
 'pictures': ['ClearProperty(bz_nav,home)', 'ActivateWindow(pictures)'],
 'files': ['SetProperty(bz_setopen,1,home)', 'ClearProperty(bz_nav,home)', 'ActivateWindow(filemanager)'],
 'addons': ['SetProperty(bz_setopen,1,home)', 'ClearProperty(bz_nav,home)', 'ActivateWindow(1131)'],  # 5.33.220 Warm strip Add-ons dialog over the section (was ActivateWindow(addonbrowser))
 'settings': ['SetProperty(bz_setopen,1,home)', 'ClearProperty(bz_nav,home)', 'ActivateWindow(1130)'],  # 5.33.215 MM-style Settings dialog over the section (was ActivateWindow(Settings))
 'manageart': ['SetProperty(bz_setopen,1,home)', 'ClearProperty(bz_nav,home)', 'ActivateWindow(1133)'],  # 5.33.477 MANAGEART shell (dialog over the section, like Settings 1130)
 'kodi': ['SetProperty(bz_setopen,1,home)', 'ClearProperty(bz_nav,home)', 'ActivateWindow(systeminfo)'],
}
# 4.2.0 O59 (D3): music / movies / tv open the primed sub (home bz_mmsub_<sec>, 1-based; empty = default Artists / Titles / Shows)
SUBS = {
 'music': ('tomusic', ['musicdb://artists/', 'musicdb://albums/', 'musicdb://genres/', 'musicdb://recentlyaddedsongs/', 'musicdb://recentlyaddedalbums/'], 1),
 'movies': ('go', ['videodb://movies/titles/', 'videodb://recentlyaddedmovies/', 'videodb://movies/years/'], 1),  # 5.33.393 Rob: Movies pill Titles/Recent/Years (Actors/Sets/Genres deleted)
 'tv': ('go', ['videodb://tvshows/titles/', 'videodb://inprogresstvshows/', 'videodb://tvshows/years/', 'videodb://tvshows/actors/', 'videodb://recentlyaddedepisodes/', 'videodb://tvshows/genres/'], 1),
}
def subgo(key):
    act, paths, d = SUBS[key]
    explicit = home.getProperty('bz_mmsub_' + key) != ''   # t4149: any set pill (incl. 1=Artists) opens that pill; empty = keep last location
    try: i = int(home.getProperty('bz_mmsub_' + key) or d)
    except ValueError: i = d
    if not 1 <= i <= len(paths): i = d
    xbmc.executebuiltin('Skin.SetString(bz_last_mmsub_%s,%d)' % (key, i)); home.setProperty('bz_mmsub_' + key, str(i))   # t4075 keep pill at last used
    p = paths[i - 1]
    if key == 'music':
        home.clearProperty('bz_music_underlay')   # 5.33.164: real Music entry — underlay artists no longer owns the window
        if not explicit and home.getProperty('bz_lastmusic'): p = home.getProperty('bz_lastmusic')   # MMQUEUE keep last Music location
    return ['SetProperty(bz_navroot,%s,home)' % p, 'RunScript(special://skin/scripts/bz_cmd.py,%s,%s)' % (act, p)]
def restore():   # t4075: Home props die on ReloadSkin; restore pill from Skin.String
    for k in SUBS:
        v = xbmc.getInfoLabel('Skin.String(bz_last_mmsub_%s)' % k)
        if v and v.isdigit() and int(v) > len(SUBS[k][1]): v = ''   # 5.33.393 clamp removed pills
        if v and not home.getProperty('bz_mmsub_' + k): home.setProperty('bz_mmsub_' + k, v)
MMLOCK_S = 0.30   # 5.32: Select ignore window (seconds)
if __name__ == '__main__':
    key = sys.argv[1] if len(sys.argv) > 1 else ''
    if key == 'restore': restore(); sys.exit()
    if key in SUBS: GO[key] = subgo(key)
    if key in GO:
        # 5.32 band-aid (Rob voice): 300 ms ignore window after a Select - repeat taps inside it are dropped
        try: t0 = float(home.getProperty('bz_mmlock') or 0)
        except ValueError: t0 = 0
        if time.time() - t0 < MMLOCK_S: sys.exit()
        home.setProperty('bz_mmlock', '%.3f' % time.time())
        store()
        # 5.33.429 VLANDPICK: snapshot the virtual MM item NOW - Music->Videos clears bz_nav before the window loads and vwarm wipes bz_vland on MM close
        if home.getProperty('bz_vland') and key in ('music', 'movies', 'tv') and home.getProperty('bz_vland').split('|')[0] == key: home.setProperty('bz_vpick', home.getProperty('bz_vland'))
        else: home.clearProperty('bz_vpick')
        xbmcgui.Window(10000).setProperty('bz_mmpick', 'true')   # MMHIDE: a pick may focus the list under MM
        if xbmc.getCondVisibility('Window.IsActive(1112)'): xbmc.executebuiltin('Dialog.Close(1112,true)')
        for b in GO[key]: xbmc.executebuiltin(b)
