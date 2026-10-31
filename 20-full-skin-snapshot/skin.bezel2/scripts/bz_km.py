# 5.33.194 keymap quarantine (option one): when the user leaves skin.bezel2, remove ALL BEZEL profile keymaps so they never
# affect another skin. Profile paths only (never special://skin/...) so this still works after the skin switch.
import xbmc, xbmcgui, xbmcvfs
FILES = ('special://profile/keymaps/zz_bezel2_np_tab.xml',
         'special://profile/keymaps/zz_bezel2_dtap.xml',
         'special://profile/keymaps/zz_bezel2_noctx.xml')
SKIN = 'skin.bezel2'
def on_bezel():
    try: return xbmc.getSkinDir() == SKIN
    except Exception: return True   # unknown -> assume still Bezel (never strip keymaps by mistake)
def leave():
    gone = []
    for p in FILES:
        try:
            if xbmcvfs.exists(p) and xbmcvfs.delete(p): gone.append(p.rsplit('/', 1)[-1])
        except Exception as e:
            xbmc.log('BEZEL keymap leave: delete %s failed: %r' % (p, e), xbmc.LOGWARNING)
    try: xbmcgui.Window(10000).clearProperty('bz_km_loaded')
    except Exception: pass
    if gone:
        xbmc.executebuiltin('Action(reloadkeymaps)')
        xbmc.log('BEZEL keymap leave: removed %s (skin now %s)' % (', '.join(gone), xbmc.getSkinDir()), xbmc.LOGINFO)
    else:
        xbmc.log('BEZEL keymap leave: nothing to remove', xbmc.LOGINFO)
    return gone
