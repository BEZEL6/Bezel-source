# v0.1.18: focus the first real album when entering an artist's album strip (list 62).
# Waits until the folder has finished loading, skips '..' and 'All albums' whether present or not,
# retries until the focus really sits on an album, and runs once per folder so a remembered position is kept on return.
import xbmc, xbmcgui
home = xbmcgui.Window(10000)
ALL = xbmc.getLocalizedString(15102)
def lab(i): return xbmc.getInfoLabel('Container(62).ListItemAbsolute(%d).Label' % i)
path = xbmc.getInfoLabel('Container.FolderPath')
if path.startswith('musicdb://artists/') and path not in home.getProperty('bz_fa_seen').split('|') and home.getProperty('bz_fa_busy') != '1':
    home.setProperty('bz_fa_busy', '1')
    try:
        mon = xbmc.Monitor()
        # wait (max ~6 s) for loading to finish and the item count to settle
        last, stable = -1, 0
        for _ in range(60):
            if mon.waitForAbort(0.1) or xbmc.getInfoLabel('Container.FolderPath') != path: break
            if xbmc.getCondVisibility('Container.IsUpdating'): stable = 0; continue
            n = xbmc.getInfoLabel('Container(62).NumAllItems') or xbmc.getInfoLabel('Container(62).NumItems')
            stable = stable + 1 if n == last else 0; last = n
            if stable >= 3 and lab(0): break
        if xbmc.getInfoLabel('Container.FolderPath') == path:
            idx = 0
            while idx < 3 and lab(idx) in ('..', ALL): idx += 1
            if lab(idx):
                for _ in range(10):   # retry until the focus really is on a real album
                    cur = xbmc.getInfoLabel('Container(62).ListItem.Label')
                    if cur and cur not in ('..', ALL): break
                    xbmc.executebuiltin('SetFocus(62,%d,absolute)' % idx)
                    if mon.waitForAbort(0.15): break
            home.setProperty('bz_fa_seen', '|'.join(([path] + home.getProperty('bz_fa_seen').split('|'))[:200]))
            home.setProperty('bz_fa_done', path)
    finally:
        home.clearProperty('bz_fa_busy')
