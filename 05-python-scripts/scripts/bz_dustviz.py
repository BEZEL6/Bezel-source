# 5.33.352 DustViz auto-install (Rob t2503): copy bundled visualization.bezel into special://home/addons,
# enable it and make it the music visualisation. Skin = trigger only; viz draws in Bezel's visualisation rect.
# Bundles: resources/dustviz/android (Shield aarch64 GLES 0.2.0) / linux (desktop) / windows (x64 DX11 0.2.0, 5.33.358).
import os, json, shutil, xbmc, xbmcvfs
ID = 'visualization.bezel'
def rpc(m, p):
    try: return json.loads(xbmc.executeJSONRPC(json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': m, 'params': p})))
    except Exception: return {}
def ver(path):
    try:
        s = open(os.path.join(path, 'addon.xml'), encoding='utf-8').read()
        i = s.index('version="', s.index('<addon')) + 9; return s[i:s.index('"', i)]
    except Exception: return ''
def main():
    cv = xbmc.getCondVisibility
    plat = 'windows' if cv('System.Platform.Windows') else ('android' if cv('System.Platform.Android') else ('linux' if cv('System.Platform.Linux') else ''))
    if not plat:
        xbmc.log('BEZEL dustviz: no bundled binary for this platform - skipped', xbmc.LOGINFO); return
    src = os.path.join(xbmcvfs.translatePath('special://skin/'), 'resources', 'dustviz', plat, ID)
    dst = os.path.join(xbmcvfs.translatePath('special://home/addons/'), ID)
    if not os.path.isdir(src): return
    if ver(dst) != ver(src):
        try:
            if os.path.isdir(dst): shutil.rmtree(dst)
            shutil.copytree(src, dst)
            for f in os.listdir(dst):
                if f.startswith(ID + '.so'): os.chmod(os.path.join(dst, f), 0o755)
            xbmc.log('BEZEL dustviz: installed %s %s' % (plat, ver(src)), xbmc.LOGINFO)
        except Exception as e:
            xbmc.log('BEZEL dustviz: copy failed %s' % e, xbmc.LOGERROR); return
        xbmc.executebuiltin('UpdateLocalAddons'); xbmc.sleep(1500)
    for _ in range(10):
        r = rpc('Addons.SetAddonEnabled', {'addonid': ID, 'enabled': True})
        if r.get('result') == 'OK': break
        xbmc.sleep(500)
    cur = (rpc('Settings.GetSettingValue', {'setting': 'musicplayer.visualisation'}).get('result') or {}).get('value')
    if cur != ID: rpc('Settings.SetSettingValue', {'setting': 'musicplayer.visualisation', 'value': ID})
    xbmc.executebuiltin('SetProperty(bz_dustviz_ok,1,home)')
if __name__ == '__main__': main()
