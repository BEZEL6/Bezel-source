# 5.0.3 t4004: old Kodi context-menu actions folded into Options+Info > More options (no ContextMenu window anywhere)
import xbmc, xbmcgui, json, sys
def rpc(m, p):
    return json.loads(xbmc.executeJSONRPC(json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': m, 'params': p})))
a = sys.argv[1] if len(sys.argv) > 1 else ''
L = xbmc.getInfoLabel
if a == 'fav':
    path = L('ListItem.FileNameAndPath') or L('ListItem.FolderPath')
    fav = {'title': L('ListItem.Label'), 'type': 'media', 'path': path, 'thumbnail': L('ListItem.Art(poster)') or L('ListItem.Art(thumb)') or L('ListItem.Icon')}
    aid = L('ListItem.Property(Addon.ID)')   # 5.33.18 t203: section menu Favourite on add-ons (Programs/Games/Add-ons)
    if aid and xbmc.getCondVisibility('Window.IsActive(programs) | Window.IsActive(games) | Window.IsActive(addonbrowser)'):
        fav.update({'type': 'script', 'path': aid}) if not path.startswith('plugin://') else fav.update({'type': 'window', 'window': 'videos', 'windowparameter': path, 'path': None})
        fav.pop('path') if fav.get('path') is None else None
    r = rpc('Favourites.AddFavourite', fav)
    xbmcgui.Dialog().notification('BEZEL', 'Added to favourites' if 'result' in r else 'Could not add favourite', xbmcgui.NOTIFICATION_INFO, 2000)
elif a == 'remove':
    t, i = sys.argv[2], sys.argv[3]
    m = {'movie': ('VideoLibrary.RemoveMovie', 'movieid'), 'episode': ('VideoLibrary.RemoveEpisode', 'episodeid'),
         'tvshow': ('VideoLibrary.RemoveTVShow', 'tvshowid'), 'musicvideo': ('VideoLibrary.RemoveMusicVideo', 'musicvideoid')}.get(t)
    if m and i.isdigit() and xbmcgui.Dialog().yesno('Remove from library', 'Remove "%s" from the library?[CR](Files are not deleted.)' % L('ListItem.Label')):
        xbmc.executebuiltin('Dialog.Close(all,true)'); rpc(m[0], {m[1]: int(i)}); xbmc.executebuiltin('Container.Refresh')
