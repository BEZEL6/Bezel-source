# BEZEL t4876: Delete BEZEL settings under a black screen; Estuary bounce then back to skin.bezel2 with no visible flash.
# RunScript(special://skin/scripts/bz_wipe.py)
import json, os, sys, xbmc, xbmcgui, xbmcvfs

TMP = 'special://temp/'
BLACK_TMP = TMP + 'bz_wipe_black.png'
SELF_TMP = TMP + 'bz_wipe.py'


def _rpc(method, params=None, rid=1):
    q = {'jsonrpc': '2.0', 'id': rid, 'method': method}
    if params is not None:
        q['params'] = params
    return json.loads(xbmc.executeJSONRPC(json.dumps(q)))


def _skin():
    try:
        return (_rpc('Settings.GetSettingValue', {'setting': 'lookandfeel.skin'}).get('result') or {}).get('value') or ''
    except Exception:
        return ''


def _set_skin(skin_id):
    return _rpc('Settings.SetSettingValue', {'setting': 'lookandfeel.skin', 'value': skin_id})


def _delete_addon_data():
    base = xbmcvfs.translatePath('special://profile/addon_data/skin.bezel2/')
    deleted = []
    if not (base and xbmcvfs.exists(base)):
        return deleted
    try:
        dirs, files = xbmcvfs.listdir(base)
    except Exception as e:
        xbmc.log('BEZEL wipe listdir: %s' % e, xbmc.LOGWARNING)
        return deleted
    for f in files:
        path = base + f
        try:
            if xbmcvfs.delete(path):
                deleted.append(f)
        except Exception as e:
            xbmc.log('BEZEL wipe delete %s: %s' % (f, e), xbmc.LOGWARNING)
    for d in dirs:
        try:
            xbmcvfs.rmdir(base + d)
        except Exception:
            pass
    return deleted


class Blackout(xbmcgui.WindowDialog):
    def __init__(self, texture):
        xbmcgui.WindowDialog.__init__(self)
        # Oversized black cover; works at 1080 / 1440 / 2160 without a resolution probe.
        self._bg = xbmcgui.ControlImage(0, 0, 3840, 2160, texture)
        self.addControl(self._bg)


def _ensure_temp_runner():
    """Copy this script + black texture to special://temp so the wipe can outlive a skin unload."""
    import shutil
    here = os.path.abspath(__file__)
    dest = xbmcvfs.translatePath(SELF_TMP)
    if os.path.normcase(here) == os.path.normcase(dest):
        return False
    try:
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copyfile(here, dest)
    except Exception as e:
        xbmc.log('BEZEL wipe temp copy failed: %s' % e, xbmc.LOGERROR)
        return False
    if not xbmcvfs.exists(BLACK_TMP):
        bdest = xbmcvfs.translatePath(BLACK_TMP)
        copied = False
        for src in (
            xbmcvfs.translatePath('special://skin/media/colors/black.png'),
            os.path.normpath(os.path.join(os.path.dirname(here), '..', 'media', 'colors', 'black.png')),
        ):
            try:
                if src and os.path.isfile(src):
                    shutil.copyfile(src, bdest); copied = True; break
            except Exception:
                pass
        if not copied:
            try:
                xbmcvfs.copy('special://skin/media/colors/black.png', BLACK_TMP)
            except Exception:
                pass
    xbmc.executebuiltin('RunScript(%s,run)' % SELF_TMP)
    return True


def main():
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    if 'run' not in args:
        if _ensure_temp_runner():
            return
        # already somehow local without run flag — continue
    tex = BLACK_TMP if xbmcvfs.exists(BLACK_TMP) else 'colors/black.png'
    black = Blackout(tex)
    black.show()
    xbmc.sleep(120)
    msg = (
        'Delete all BEZEL skin settings on this device?[CR][CR]'
        'Removes settings.xml, Tuner exports, and bezel_cw playlist helpers under userdata/addon_data/skin.bezel2/, '
        'then reloads BEZEL clean.[CR][CR]'
        'The screen stays black while that happens. This cannot be undone.'
    )
    if not xbmcgui.Dialog().yesno('Delete BEZEL settings', msg, yeslabel='Delete', nolabel='Cancel'):
        black.close()
        return
    # Keep black up for the whole bounce.
    deleted = _delete_addon_data()
    xbmc.log('BEZEL wipe: deleted=%s' % deleted, xbmc.LOGINFO)
    # Estuary then immediately BEZEL — no intentional sleep between, so Estuary should not paint.
    try:
        _set_skin('skin.estuary')
    except Exception as e:
        xbmc.log('BEZEL wipe estuary: %s' % e, xbmc.LOGWARNING)
    try:
        _set_skin('skin.bezel2')
    except Exception as e:
        xbmc.log('BEZEL wipe bezel2: %s' % e, xbmc.LOGWARNING)
    try:
        xbmc.executebuiltin('ReloadSkin()')
    except Exception:
        pass
    # Wait until BEZEL is the active skin and the busy dialogs are gone.
    ready = False
    for i in range(80):
        xbmc.sleep(250)
        try:
            # Re-show black if skin reload destroyed the dialog (best-effort).
            if not black:
                pass
        except Exception:
            pass
        cur = _skin()
        busy = xbmc.getCondVisibility(
            'Window.IsActive(busydialog) | Window.IsActive(busydialognocancel) | Window.IsActive(startup)'
        )
        if cur == 'skin.bezel2' and not busy:
            # one extra beat so Home/underlay can settle
            xbmc.sleep(400)
            if _skin() == 'skin.bezel2' and not xbmc.getCondVisibility(
                'Window.IsActive(busydialog) | Window.IsActive(busydialognocancel)'
            ):
                ready = True
                break
        # If the first WindowDialog died across the skin bounce, put a fresh one up once BEZEL is back.
        if cur == 'skin.bezel2' and i in (2, 8, 16):
            try:
                black.close()
            except Exception:
                pass
            try:
                tex2 = BLACK_TMP if xbmcvfs.exists(BLACK_TMP) else 'colors/black.png'
                black = Blackout(tex2)
                black.show()
            except Exception as e:
                xbmc.log('BEZEL wipe re-black: %s' % e, xbmc.LOGWARNING)
    try:
        black.close()
    except Exception:
        pass
    xbmc.log('BEZEL wipe: done ready=%s skin=%s' % (ready, _skin()), xbmc.LOGINFO)
    if ready:
        xbmcgui.Dialog().notification('BEZEL', 'Settings deleted — BEZEL reloaded', xbmcgui.NOTIFICATION_INFO, 2500)
    else:
        xbmcgui.Dialog().notification('BEZEL', 'Settings deleted', xbmcgui.NOTIFICATION_INFO, 2500)


if __name__ == '__main__':
    main()
