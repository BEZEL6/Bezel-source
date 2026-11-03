# 5.33.229 Add Source strip keyboard: append one char from a vbar to the open Kodi keyboard (DialogKeyboard edit 312).
# RunScript(special://skin/scripts/bz_kb.py,<bar a|n|s>,<index>)
import sys, json, xbmc
BARS = {'a': 'abcdefghijklmnopqrstuvwxyz', 'n': '0123456789', 's': '/:._-@\\!#$%&+=?'}
try:
    bar, idx = sys.argv[1], int(sys.argv[2])
    ch = BARS[bar][idx]
    if bar == 'a' and xbmc.getCondVisibility('!String.IsEmpty(Window(Home).Property(bz_kbcaps))'):
        ch = ch.upper()
    cur = xbmc.getInfoLabel('Control.GetLabel(312).index(1)')
    xbmc.executeJSONRPC(json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': 'Input.SendText', 'params': {'text': cur + ch, 'done': False}}))
except Exception as e:
    xbmc.log('bz_kb: %s' % e, xbmc.LOGWARNING)
