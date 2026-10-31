# v0.1.17: toggle the playing song in Kodi favourites; remember the state for the skin's lit Favorite button
import xbmc, xbmcgui, json
path = xbmc.getInfoLabel('Player.Filenameandpath')
title = xbmc.getInfoLabel('MusicPlayer.Title') or xbmc.getInfoLabel('Player.Title') or path
thumb = xbmc.getInfoLabel('Player.Art(thumb)')
if path:
    def favs():
        r = json.loads(xbmc.executeJSONRPC(json.dumps({"jsonrpc":"2.0","id":1,"method":"Favourites.GetFavourites","params":{"properties":["path"]}})))
        return [f.get('path') for f in (r.get('result',{}).get('favourites') or [])]
    was = path in favs()
    # AddFavourite toggles: adding an existing favourite removes it
    xbmc.executeJSONRPC(json.dumps({"jsonrpc":"2.0","id":2,"method":"Favourites.AddFavourite","params":{"title":title,"type":"media","path":path,"thumbnail":thumb}}))
    now = path in favs()
    xbmcgui.Window(10000).setProperty('bz_favpath', path if now else '')
    xbmc.log('bezel fav: %s was=%s now=%s' % (path, was, now), xbmc.LOGINFO)
