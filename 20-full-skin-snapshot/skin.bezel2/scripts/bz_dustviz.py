# 5.33.416 NOBZVIZ: was 5.33.352 DustViz auto-install (Rob t2503): copy bundled visualization.bezel into special://home/addons,
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
def main():   # 5.33.416 NOBZVIZ (Rob): Bezel Viz removed - no install; disable it and unselect it as the music visualisation
    cur = (rpc('Settings.GetSettingValue', {'setting': 'musicplayer.visualisation'}).get('result') or {}).get('value')
    if cur == ID: rpc('Settings.SetSettingValue', {'setting': 'musicplayer.visualisation', 'value': ''})
    rpc('Addons.SetAddonEnabled', {'addonid': ID, 'enabled': False})
    xbmc.executebuiltin('ClearProperty(bz_dustviz_ok,home)'); xbmc.log('BEZEL: Bezel Viz disabled/unselected', xbmc.LOGINFO)
def noautoviz():   # 5.33.409 NOAUTOVIZ (Rob pt2915u): Kodi 'Switch to visualisation on playback' (musicfiles.selectaction) popped stock fullscreen on Music Select; Bezel owns FS opens
    r = rpc('Settings.GetSettingValue', {'setting': 'musicfiles.selectaction'})
    if (r.get('result') or {}).get('value') is not False:
        rpc('Settings.SetSettingValue', {'setting': 'musicfiles.selectaction', 'value': False}); xbmc.log('BEZEL: musicfiles.selectaction forced off', xbmc.LOGINFO)
if __name__ == '__main__':
    try: noautoviz()
    except Exception as e: xbmc.log('BEZEL noautoviz failed %s' % e, xbmc.LOGWARNING)
    main()
