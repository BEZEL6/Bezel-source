# fork.3: BEZEL MM debug helpers. RunScript(special://skin/scripts/bz_dbg.py,dump) logs MM state once (LOGWARNING).
import sys, xbmc, xbmcgui
P = ('bz_nav', 'bz_mmwarm', 'bz_xfade', 'bz_mmpick', 'bz_mmlock', 'bz_mmpos', 'bz_mmlive', 'bz_navroot', 'bz_mmstart')
def dump():
    h = xbmcgui.Window(10000)
    s = ' '.join('%s=%s' % (p, h.getProperty(p) or '-') for p in P)
    s += ' win=%s ctl=%s path=%s row=%s' % (xbmc.getInfoLabel('System.CurrentWindow'), xbmc.getInfoLabel('System.CurrentControlId'),
         xbmc.getInfoLabel('Container.FolderPath'), xbmc.getInfoLabel('Container(6996).ListItem.Label'))
    xbmc.log('BEZEL DBGMM dump ' + s, xbmc.LOGWARNING)
    xbmcgui.Dialog().notification('BEZEL MM state', 'Written to kodi.log', time=1500, sound=False)
if __name__ == '__main__' and (sys.argv[1:] or ['dump'])[0] == 'dump': dump()
