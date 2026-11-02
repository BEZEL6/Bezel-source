# BEZEL 3.0: Select on the artist button (album / song list) opens that artist's albums. First (album) artist wins.
import sys, json, xbmc, xbmcgui
def rpc(m, p):
    return json.loads(xbmc.executeJSONRPC(json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': m, 'params': p}))).get('result', {})
def meta(kind, dbid, name):
    # 5.33.224 3B artist meta: Home props bz_am_* for BezelArtistMeta3B
    W = xbmcgui.Window(10000)
    for k in ['n1','n2','counts','thumb'] + ['g%d' % i for i in range(1,7)]:
        W.clearProperty('bz_am_' + k)
    aid = 0
    if kind == 'artist':
        aid = dbid
    elif kind == 'song' and dbid:
        d = rpc('AudioLibrary.GetSongDetails', {'songid': dbid, 'properties': ['albumartistid', 'artistid']}).get('songdetails', {})
        aid = (d.get('albumartistid') or d.get('artistid') or [0])[0]
    elif kind == 'album' and dbid:
        aid = (rpc('AudioLibrary.GetAlbumDetails', {'albumid': dbid, 'properties': ['artistid']}).get('albumdetails', {}).get('artistid') or [0])[0]
    if not aid and name:
        a = rpc('AudioLibrary.GetArtists', {'filter': {'field': 'artist', 'operator': 'is', 'value': name.split(' / ')[0]}}).get('artists') or []
        aid = a[0]['artistid'] if a else 0
    nm, thumb, genres = (name or '').split(' / ')[0], '', []
    if aid:
        d = rpc('AudioLibrary.GetArtistDetails', {'artistid': aid, 'properties': ['thumbnail', 'fanart', 'genre']}).get('artistdetails', {})
        nm = d.get('artist') or nm; thumb = d.get('thumbnail') or d.get('fanart') or ''; genres = d.get('genre') or []
        na = rpc('AudioLibrary.GetAlbums', {'filter': {'artistid': aid}, 'limits': {'start': 0, 'end': 1}}).get('limits', {}).get('total', 0)
        ns = rpc('AudioLibrary.GetSongs', {'filter': {'artistid': aid}, 'limits': {'start': 0, 'end': 1}}).get('limits', {}).get('total', 0)
        W.setProperty('bz_am_counts', '%d album%s  \u00b7  %d song%s' % (na, '' if na == 1 else 's', ns, '' if ns == 1 else 's'))
    w = nm.split(' ', 1)
    W.setProperty('bz_am_n1', w[0]); W.setProperty('bz_am_n2', w[1] if len(w) > 1 else '')
    W.setProperty('bz_am_thumb', thumb)
    for i, g in enumerate(genres[:6]):
        W.setProperty('bz_am_g%d' % (i + 1), g)
def ameta(kind, dbid, name):
    # 5.33.236 Rob t1841: 3B on album + disc levels shows the ALBUM (art, split title, artist/year/counts, genre pills)
    W = xbmcgui.Window(10000)
    for k in ['n1','n2','counts','thumb'] + ['g%d' % i for i in range(1,7)]:
        W.clearProperty('bz_am_' + k)
    alb, disc = 0, 0
    if kind == 'album':
        alb = dbid
    elif kind == 'song' and dbid:
        d = rpc('AudioLibrary.GetSongDetails', {'songid': dbid, 'properties': ['albumid', 'disc']}).get('songdetails', {})
        alb, disc = d.get('albumid') or 0, d.get('disc') or 0
    if not alb:
        return meta(kind, dbid, name)
    a = rpc('AudioLibrary.GetAlbumDetails', {'albumid': alb, 'properties': ['title', 'artist', 'year', 'genre', 'thumbnail', 'fanart', 'totaldiscs']}).get('albumdetails', {})
    songs = rpc('AudioLibrary.GetSongs', {'filter': {'albumid': alb}, 'properties': ['disc']}).get('songs') or []
    nd = a.get('totaldiscs') or len(set(x.get('disc') or 1 for x in songs)) or 1
    bits = []
    art = ' / '.join(a.get('artist') or [])
    if art: bits.append(art)
    if a.get('year'): bits.append(str(a['year']))
    if kind == 'song' and nd > 1:
        dn = disc or 1; nt = len([x for x in songs if (x.get('disc') or 1) == dn])
        bits.append('Disc %d of %d' % (dn, nd)); bits.append('%d track%s' % (nt, '' if nt == 1 else 's'))
    else:
        nt = len(songs)
        if nd > 1: bits.append('%d discs' % nd)
        bits.append('%d track%s' % (nt, '' if nt == 1 else 's'))
    W.setProperty('bz_am_counts', '  \u00b7  '.join(bits))
    w = (a.get('title') or '').split(' ', 1)
    W.setProperty('bz_am_n1', w[0]); W.setProperty('bz_am_n2', w[1] if len(w) > 1 else '')
    W.setProperty('bz_am_thumb', a.get('thumbnail') or a.get('fanart') or '')
    for i, g in enumerate((a.get('genre') or [])[:6]):
        W.setProperty('bz_am_g%d' % (i + 1), g)
try:
    if sys.argv[1] == 'meta':
        ameta(sys.argv[2], int(sys.argv[3] or 0), sys.argv[4] if len(sys.argv) > 4 else '')
        sys.exit(0)
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
