# BEZEL 3.0: Select on the artist button (album / song list) opens that artist's albums. First (album) artist wins.
import sys, json, xbmc
def rpc(m, p):
    return json.loads(xbmc.executeJSONRPC(json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': m, 'params': p}))).get('result', {})
try:
    kind, dbid = sys.argv[1], int(sys.argv[2] or 0)
    ids = []
    if kind == 'song' and dbid:
        d = rpc('AudioLibrary.GetSongDetails', {'songid': dbid, 'properties': ['albumartistid', 'artistid']}).get('songdetails', {})
        ids = d.get('albumartistid') or d.get('artistid') or []
    elif kind == 'album' and dbid:
        ids = rpc('AudioLibrary.GetAlbumDetails', {'albumid': dbid, 'properties': ['artistid']}).get('albumdetails', {}).get('artistid') or []
    if not ids and len(sys.argv) > 3 and sys.argv[3]:
        name = sys.argv[3].split(' / ')[0]
        a = rpc('AudioLibrary.GetArtists', {'filter': {'field': 'artist', 'operator': 'is', 'value': name}}).get('artists') or []
        ids = [a[0]['artistid']] if a else []
    if ids:
        xbmc.executebuiltin('Container.Update(musicdb://artists/%d/)' % ids[0])
        xbmc.executebuiltin('SetFocus(60)')
    else:
        xbmc.executebuiltin('Notification(BEZEL,Artist not in library,2000)')
except Exception as e:
    xbmc.log('bz_artist: %r' % e, xbmc.LOGERROR)
