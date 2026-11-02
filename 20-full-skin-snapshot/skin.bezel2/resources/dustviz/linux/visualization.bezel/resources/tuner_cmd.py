# Bezel Viz live in-viz tuner: key -> command bridge (Kodi gives visualisation addons no input).
# Usage from a keymap:  RunScript(special://home/addons/visualization.bezel/resources/tuner_cmd.py,<cmd>)
#   cmd: toggle | open | close | up | down | left | right | reset
# Appends "<seq> <cmd>" to special://temp/bezelviz_cmd.txt; the engine polls it ~10x/s.
# While open, the arrow/OK/Back keymap (zzz_bezelviz_tuner_open.xml) is installed into userdata/keymaps and keymaps
# reloaded; on close it is removed, so normal Bezel visualisation keys are untouched when the menu is shut.
import sys, os, time, xbmc, xbmcvfs
cmd = (sys.argv[1] if len(sys.argv) > 1 else 'toggle').strip().lower()
tmp = xbmcvfs.translatePath('special://temp/')
cmdf = os.path.join(tmp, 'bezelviz_cmd.txt'); statef = os.path.join(tmp, 'bezelviz_state.txt')
here = os.path.dirname(os.path.abspath(__file__))
km_src = os.path.join(here, 'keymaps', 'bezelviz_tuner_open.xml')
km_dst = os.path.join(xbmcvfs.translatePath('special://userdata/keymaps/'), 'zzz_bezelviz_tuner_open.xml')
def is_open():
    try:
        return 'open 1' in open(statef).read()
    except Exception:
        return False
lines = []
try:
    lines = open(cmdf).read().splitlines()[-50:]
except Exception:
    pass
seq = int(time.time() * 1000)
try:
    last = int(lines[-1].split()[0]) if lines else 0
    seq = max(seq, last + 1)
except Exception:
    pass
was_open = is_open()
lines.append('%d %s' % (seq, cmd))
with open(cmdf, 'w') as f:
    f.write('\n'.join(lines) + '\n')
will_open = {'toggle': not was_open, 'open': True, 'close': False}.get(cmd, was_open)
if will_open != os.path.exists(km_dst):
    try:
        if will_open:
            os.makedirs(os.path.dirname(km_dst), exist_ok=True)
            open(km_dst, 'w').write(open(km_src).read())
        elif os.path.exists(km_dst):
            os.remove(km_dst)
        xbmc.executebuiltin('Action(reloadkeymaps)')
    except Exception as e:
        xbmc.log('BezelViz tuner keymap swap failed: %s' % e, xbmc.LOGWARNING)
