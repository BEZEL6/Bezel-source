# 4.4.0 O87: crash-report access from the Tuner (view / copy latest kodi_crashlog, kodi.log tail, log uploader)
import os, glob, shutil, xbmc, xbmcgui, xbmcvfs
def T(p): return xbmcvfs.translatePath(p)
def crashlogs():
    d=[os.path.expanduser('~'), T('special://home'), T('special://temp'), T('special://home/..'), '/tmp']
    f=set()
    for x in d:
        for p in glob.glob(os.path.join(x,'kodi_crashlog*.log'))+glob.glob(os.path.join(x,'kodi_stacktrace*.log')): f.add(os.path.realpath(p))
    return sorted(f,key=os.path.getmtime,reverse=True)
def tail(p,n=60000):
    try:
        with open(p,'rb') as h:
            h.seek(0,2); s=h.tell(); h.seek(max(0,s-n)); return h.read().decode('utf-8','replace')
    except Exception as e: return 'Could not read %s: %s'%(p,e)
c=crashlogs(); log=T('special://logpath/kodi.log'); old=T('special://logpath/kodi.old.log')
opts=[];acts=[]
if c: opts.append('View latest crash log (%s)'%os.path.basename(c[0])); acts.append('crash')
else: opts.append('No crash log found'); acts.append('none')
opts+=['View kodi.log (end)','View kodi.old.log (previous run)']; acts+=['log','old']
if c: opts.append('Copy latest crash log to Kodi home'); acts.append('copy')
up=xbmc.getCondVisibility('System.HasAddon(script.kodi.loguploader)')
if up: opts.append('Upload logs (Kodi Logfile Uploader)'); acts.append('up')
i=xbmcgui.Dialog().select('BEZEL crash report',opts)
if i>=0:
    a=acts[i]
    if a=='crash': xbmcgui.Dialog().textviewer(c[0],tail(c[0]))
    elif a=='log': xbmcgui.Dialog().textviewer('kodi.log',tail(log))
    elif a=='old': xbmcgui.Dialog().textviewer('kodi.old.log',tail(old) if os.path.exists(old) else 'No previous log.')
    elif a=='copy':
        dst=os.path.join(T('special://home'),'bezel_crashlog_latest.log')
        try: shutil.copy2(c[0],dst); xbmcgui.Dialog().ok('BEZEL crash report','Copied to[CR]'+dst)
        except Exception as e: xbmcgui.Dialog().ok('BEZEL crash report','Copy failed: %s'%e)
    elif a=='up': xbmc.executebuiltin('RunScript(script.kodi.loguploader)')
    else: xbmcgui.Dialog().ok('BEZEL crash report','No kodi_crashlog file found. kodi.log and kodi.old.log are still available here.')
