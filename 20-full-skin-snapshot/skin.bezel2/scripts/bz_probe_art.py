# 5.33.475 ARTPROBE (Rob, MANAGE ART phase 1): diagnostics only, no visual change.
# Answers what Kodi lets a script do with library art before MANAGE ART is built.
# Run from Tuner > ABOUT / VERSIONS. Results are merged into one file:
#   special://profile/addon_data/skin.bezel2/art_probe.json   (+ BEZEL ARTPROBE lines in kodi.log)
#
#   RunScript(special://skin/scripts/bz_probe_art.py,read)     read-only: art keys, API, NFO files beside the media
#   RunScript(special://skin/scripts/bz_probe_art.py,set)      set a test cover on ONE album (backs up the original first)
#   RunScript(special://skin/scripts/bz_probe_art.py,check)    report that album's art now (run after a Refresh to test persistence)
#   RunScript(special://skin/scripts/bz_probe_art.py,restore)  put the original art back
#   RunScript(special://skin/scripts/bz_probe_art.py,folder)   try to create + delete a tiny temp file in that album's folder
import sys, os, json, time, struct, zlib
from urllib.parse import unquote
import xbmc, xbmcgui, xbmcvfs

DATA = xbmcvfs.translatePath('special://profile/addon_data/skin.bezel2/')
OUT = os.path.join(DATA, 'art_probe.json')
STATE = os.path.join(DATA, 'art_probe_state.json')
TESTPNG = os.path.join(DATA, 'probe_dark.png')


def log(msg):
    xbmc.log('BEZEL ARTPROBE ' + msg, xbmc.LOGWARNING)


def rpc(method, params=None):
    req = {'jsonrpc': '2.0', 'id': 1, 'method': method}
    if params is not None:
        req['params'] = params
    try:
        r = json.loads(xbmc.executeJSONRPC(json.dumps(req)))
    except Exception as e:
        return {'_error': 'exception: %s' % e}
    if 'error' in r:
        return {'_error': r['error']}
    return r.get('result', {})


def bad(res):
    return isinstance(res, dict) and '_error' in res


def kind(u):
    """What an art URL really points at."""
    if not u:
        return 'none'
    inner = u
    if u.startswith('image://'):
        inner = unquote(u[8:].rstrip('/'))
    if inner.startswith('music@'):
        return 'embedded-tag:' + inner[6:]
    if inner.startswith(('http://', 'https://')):
        return 'remote:' + inner
    return 'local:' + inner


def art_kinds(art):
    return {k: kind(v) for k, v in (art or {}).items()}


def load(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}


def save(path, data):
    xbmcvfs.mkdirs(DATA)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=1, ensure_ascii=False, sort_keys=True)


def record(step, data):
    allr = load(OUT)
    data['_when'] = time.strftime('%Y-%m-%d %H:%M:%S')
    allr[step] = data
    save(OUT, allr)
    log('%s done -> %s' % (step, OUT))


def toast(head, msg, ms=6000):
    xbmcgui.Dialog().notification(head, msg, time=ms, sound=False)


def album_art_list(n=60):
    res = rpc('AudioLibrary.GetAlbums', {'properties': ['title', 'displayartist', 'art', 'thumbnail'],
                                         'limits': {'start': 0, 'end': n},
                                         'sort': {'method': 'dateadded', 'order': 'descending'}})
    return [] if bad(res) else res.get('albums', [])


def first_song(albumid):
    res = rpc('AudioLibrary.GetSongs', {'filter': {'albumid': albumid}, 'limits': {'start': 0, 'end': 3},
                                        'properties': ['title', 'file', 'art', 'albumid']})
    return [] if bad(res) else res.get('songs', [])


def split_dir(path):
    sep = '\\' if ('\\' in path and '/' not in path) else '/'
    i = path.rfind(sep)
    return (path[:i + 1], sep) if i >= 0 else ('', sep)


def listing(folder):
    try:
        dirs, files = xbmcvfs.listdir(folder)
    except Exception as e:
        return {'_error': str(e)}
    return {'dirs': sorted(dirs)[:40], 'files': sorted(files)[:80]}


def exists(p):
    try:
        return bool(xbmcvfs.exists(p))
    except Exception:
        return None


# ---------------------------------------------------------------- read
def do_read():
    R = {}
    R['kodi'] = {'build': xbmc.getInfoLabel('System.BuildVersion'), 'os': xbmc.getInfoLabel('System.OSVersionInfo')}

    intro = rpc('JSONRPC.Introspect', {'getdescriptions': False, 'getmetadata': False, 'filterbytransport': False})
    names = sorted((intro.get('methods') or {}).keys()) if not bad(intro) else []
    keys = ('Art', 'Export', 'Clean', 'Scan', 'Refresh', 'GetAvailable', 'SetAlbumDetails', 'SetArtistDetails',
            'SetSongDetails', 'SetMovieDetails', 'SetTVShowDetails', 'SetEpisodeDetails', 'SetMovieSetDetails')
    R['api_methods'] = [n for n in names if any(k in n for k in keys)] if names else {'_error': intro}

    sett = {}
    for s in ('musiclibrary.artistsfolder', 'musiclibrary.preferonlinealbumart', 'musiclibrary.albumsscraper',
              'musiclibrary.artistsscraper', 'musiclibrary.downloadinfo', 'musiclibrary.useoriginaldate'):
        v = rpc('Settings.GetSettingValue', {'setting': s})
        sett[s] = v if bad(v) else v.get('value')
    R['settings'] = sett

    albums = album_art_list(60)
    R['album_count_sampled'] = len(albums)
    samples = []
    for a in albums[:5]:
        samples.append({'albumid': a.get('albumid'), 'title': a.get('title'), 'artist': a.get('displayartist'),
                        'art_keys': sorted((a.get('art') or {}).keys()), 'art_kinds': art_kinds(a.get('art')),
                        'thumbnail': kind(a.get('thumbnail'))})
    R['albums'] = samples

    # a song's view of its album art, a local-files listing, and the NFO files beside the media
    for a in albums:
        songs = first_song(a.get('albumid'))
        if not songs:
            continue
        s = songs[0]
        folder, sep = split_dir(s.get('file', ''))
        parent, _ = split_dir(folder[:-1]) if folder.endswith(sep) else ('', sep)
        R['song_view'] = {'album': a.get('title'), 'song': s.get('title'), 'file': s.get('file'),
                          'song_art_keys': sorted((s.get('art') or {}).keys()), 'song_art_kinds': art_kinds(s.get('art'))}
        R['folders'] = {'album_folder': folder, 'album_listing': listing(folder),
                        'album_nfo': exists(folder + 'album.nfo'), 'artist_nfo_in_album_folder': exists(folder + 'artist.nfo'),
                        'artist_nfo_in_parent': exists(parent + 'artist.nfo') if parent else None,
                        'parent_folder': parent, 'parent_listing': listing(parent) if parent else None}
        break

    ar = rpc('AudioLibrary.GetArtists', {'properties': ['art', 'thumbnail'], 'limits': {'start': 0, 'end': 3}})
    R['artists'] = [] if bad(ar) else [{'artist': x.get('artist'), 'art_keys': sorted((x.get('art') or {}).keys()),
                                        'art_kinds': art_kinds(x.get('art'))} for x in ar.get('artists', [])]

    pl = rpc('Player.GetActivePlayers')
    R['player_active'] = pl
    if not bad(pl) and any(p.get('type') == 'audio' for p in pl):
        pid = [p['playerid'] for p in pl if p.get('type') == 'audio'][0]
        it = rpc('Player.GetItem', {'playerid': pid, 'properties': ['title', 'album', 'albumid', 'art', 'thumbnail', 'file']})
        item = it.get('item', {}) if not bad(it) else {}
        R['player_item'] = {'title': item.get('title'), 'album': item.get('album'), 'albumid': item.get('albumid'),
                            'art_keys': sorted((item.get('art') or {}).keys()), 'art_kinds': art_kinds(item.get('art'))}
        R['player_labels'] = {k: xbmc.getInfoLabel(k) for k in ('Player.Art(thumb)', 'Player.Art(album.thumb)',
                                                                'Player.Art(artist.thumb)', 'MusicPlayer.Cover')}
    else:
        R['player_item'] = 'nothing playing: start a song first and run READ again to see the player view'

    record('read', R)
    toast('BEZEL art probe: read', 'Saved to addon_data/skin.bezel2/art_probe.json')


# ---------------------------------------------------------------- set / check / restore
def make_png(path, size=300):
    """Dark navy square with a bright frame, so it is obvious on screen. Pure python, no extras."""
    rows = []
    for y in range(size):
        row = bytearray([0])
        for x in range(size):
            edge = min(x, y, size - 1 - x, size - 1 - y)
            if edge < 14:
                row += bytes((59, 130, 246))
            elif abs(x - y) < 6:
                row += bytes((30, 41, 59))
            else:
                row += bytes((12, 18, 32))
        rows.append(bytes(row))
    raw = b''.join(rows)

    def chunk(t, d):
        c = struct.pack('>I', len(d)) + t + d
        return c + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
    png = b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 2, 0, 0, 0)) \
        + chunk(b'IDAT', zlib.compress(raw, 9)) + chunk(b'IEND', b'')
    xbmcvfs.mkdirs(DATA)
    with open(path, 'wb') as f:
        f.write(png)


def album_now(albumid):
    res = rpc('AudioLibrary.GetAlbumDetails', {'albumid': albumid, 'properties': ['title', 'displayartist', 'art', 'thumbnail']})
    return res if bad(res) else res.get('albumdetails', {})


def do_set():
    st = load(STATE)
    if st.get('albumid') and st.get('orig_art') is not None:
        toast('BEZEL art probe: set', 'A test is already active. Run RESTORE first.')
        return
    albums = [a for a in album_art_list(60) if (a.get('art') or {}).get('thumb')]
    if not albums:
        toast('BEZEL art probe: set', 'No album with a cover found.')
        return
    a = albums[0]
    st = {'albumid': a['albumid'], 'title': a.get('title'), 'artist': a.get('displayartist'),
          'orig_art': a.get('art'), 'set_at': time.strftime('%Y-%m-%d %H:%M:%S')}
    save(STATE, st)   # backup BEFORE touching anything
    make_png(TESTPNG)
    new = 'special://profile/addon_data/skin.bezel2/probe_dark.png'
    res = rpc('AudioLibrary.SetAlbumDetails', {'albumid': a['albumid'], 'art': {'thumb': new}})
    after = album_now(a['albumid'])
    songs = first_song(a['albumid'])
    R = {'album': {'id': a['albumid'], 'title': a.get('title'), 'artist': a.get('displayartist')},
         'original_art': a.get('art'), 'set_result': res, 'album_art_after': (after or {}).get('art'),
         'album_art_kinds_after': art_kinds((after or {}).get('art')),
         'song_art_keys_after': sorted(((songs[0].get('art') if songs else {}) or {}).keys()),
         'song_art_kinds_after': art_kinds(songs[0].get('art')) if songs else None}
    record('set', R)
    toast('BEZEL art probe: set', 'Test cover on "%s". Look at it in every section, then RESTORE.' % a.get('title'), 9000)


def do_check():
    st = load(STATE)
    if not st.get('albumid'):
        toast('BEZEL art probe: check', 'No test active. Run SET first.')
        return
    now = album_now(st['albumid'])
    art = (now or {}).get('art')
    songs = first_song(st['albumid'])
    still = bool(art) and 'probe_dark' in (art.get('thumb') or '')
    R = {'album': {'id': st['albumid'], 'title': st.get('title')}, 'test_cover_still_set': still,
         'art_now': art, 'art_kinds_now': art_kinds(art), 'original_art': st.get('orig_art'),
         'song_art_kinds_now': art_kinds(songs[0].get('art')) if songs else None}
    record('check', R)
    toast('BEZEL art probe: check', 'Test cover %s on "%s".' % ('STILL SET' if still else 'GONE (changed back)', st.get('title')), 8000)


def do_restore():
    st = load(STATE)
    if not st.get('albumid') or st.get('orig_art') is None:
        toast('BEZEL art probe: restore', 'Nothing to restore.')
        return
    res = rpc('AudioLibrary.SetAlbumDetails', {'albumid': st['albumid'], 'art': st['orig_art']})
    now = album_now(st['albumid'])
    same = ((now or {}).get('art') or {}) == st['orig_art']
    R = {'album': {'id': st['albumid'], 'title': st.get('title')}, 'restore_result': res,
         'art_now': (now or {}).get('art'), 'matches_original': same}
    record('restore', R)
    if same:
        try:
            os.remove(STATE)
        except Exception:
            pass
    toast('BEZEL art probe: restore', ('Original cover back on "%s".' if same else 'Could not fully restore "%s". Send me art_probe.json.') % st.get('title'), 8000)


# ---------------------------------------------------------------- folder write test
def do_folder():
    st = load(STATE)
    albumid = st.get('albumid')
    if not albumid:
        albums = [a for a in album_art_list(20)]
        albumid = albums[0]['albumid'] if albums else None
    songs = first_song(albumid) if albumid else []
    if not songs:
        toast('BEZEL art probe: folder', 'No album folder found.')
        return
    folder, _ = split_dir(songs[0].get('file', ''))
    tmp = folder + '.bezel_probe_tmp'
    R = {'folder': folder, 'created': False, 'deleted': False}
    try:
        f = xbmcvfs.File(tmp, 'w')
        R['created'] = bool(f.write('bezel probe'))
        f.close()
    except Exception as e:
        R['create_error'] = str(e)
    if exists(tmp):
        R['deleted'] = bool(xbmcvfs.delete(tmp))
    R['left_behind'] = bool(exists(tmp))
    record('folder', R)
    toast('BEZEL art probe: folder', 'Writable: %s' % ('YES' if R['created'] and R['deleted'] else 'NO (see art_probe.json)'), 6000)


if __name__ == '__main__':
    mode = (sys.argv[1:] or ['read'])[0]
    try:
        {'read': do_read, 'set': do_set, 'check': do_check, 'restore': do_restore, 'folder': do_folder}.get(mode, do_read)()
    except Exception as e:
        log('ERROR in %s: %s' % (mode, e))
        toast('BEZEL art probe', 'Error: %s' % e, 8000)
