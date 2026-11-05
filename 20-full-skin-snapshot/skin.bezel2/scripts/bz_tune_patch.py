# BEZEL 2.0 BETA 2.10 (poster hold + hold dust timing added); 2.9: tuner "patch engine". Kodi animation / scroll / fade times cannot be conditional, so the tuner steps for
# row scroll, focus zoom, fanart fade, cascade, flip, album scale, Long sway pause are written into the skin files
# themselves (regex on fixed anchors), then the skin is reloaded. patch() is idempotent and returns True when a file changed.
import os, re, json, math
here = os.path.dirname(os.path.abspath(__file__))
SKIN = os.path.dirname(here)
J = json.load(open(os.path.join(here, 'bz_tune.json'), encoding='utf-8'))   # BEZEL 3.0 fix: Windows default codepage
DEF = {p[0]: p[2] for p in J['P']}
V = J['V']
def val(i, get):
    s = get('Skin.String(bz_at_%s)' % i)
    k = int(s) if s.isdigit() and 1 <= int(s) <= len(V[i]) else DEF[i]
    return V[i][k - 1]
def shift(D):
    # pulse anims: the hold is the leading start==end effect (T0 = D + 10250); move it and every delay by D - D0
    def f(m):
        b = m.group(0)
        t0 = re.search(r'<effect type="\w+" start="([^"]+)" end="\1" center="[^"]*" time="(\d+)"/>|<effect type="fade" start="100" end="100" time="(\d+)"/>', b)
        if not t0: return b
        T0 = int(t0.group(2) or t0.group(3)); D0 = T0 - 10250
        if not 0 <= D0 <= 5000: return b
        dd = D - D0
        b = b.replace('time="%d"/>' % T0, 'time="%d"/>' % (T0 + dd), 1)
        return re.sub(r'delay="(\d+)"', lambda q: 'delay="%d"' % (int(q.group(1)) + dd), b)
    return f
def _bezel(s, g):
    t, tw = val('rowscroll', g), val('rowsoft', g)
    s = re.sub(r'<scrolltime tween="\w+" easing="\w+" bzt="row">\d+</scrolltime>', '<scrolltime tween="%s" easing="out" bzt="row">%d</scrolltime>' % (tw, t), s)
    zt, zs = val('zoomtime', g), val('zoomsize', g)
    s = re.sub(r'(<animation type="Focus" condition="!Container\(61\)\.Scrolling"><effect type="zoom" start="100" end=")\d+(" center="150,225" time=")\d+', r'\g<1>%d\g<2>%d' % (zs, zt), s)
    s = re.sub(r'(<animation type="Unfocus" condition="!Container\(61\)\.Scrolling"><effect type="zoom" start=")\d+(" end="100" center="150,225" time=")\d+', r'\g<1>%d\g<2>%d' % (zs, zt), s)
    s = re.sub(r'(condition="Container\(61\)\.Scrolling \+ Control\.HasFocus\(61\)"><effect type="zoom" start=")\d+(" end=")\d+', r'\g<1>%d\g<2>%d' % (zs, zs), s)
    f = 0 if g('Skin.String(bz_at_fantype)') == '2' else val('fanart', g)   # 5.33.474 FANARTTUNER: Fade type Cut = instant fanart change
    s = re.sub(r'<fadetime>\d+</fadetime>(<!-- BETA 2\.6 item 10)', r'<fadetime>%d</fadetime>\1' % f, s)
    s = re.sub(r'<fadetime>\d+</fadetime>(<!-- BZMMXF)', r'<fadetime>%d</fadetime>\1' % val('mmxfade', g), s)   # t4084 MM-open art crossfade
    cs, cg = val('cascspeed', g), val('cascstag', g)
    def casc(m):   # 4.0.1 O21: delay AND duration scale together from the speed (cascspeed) so spacing stays even at every speed; later rows get up to +35% time and a soft quadratic-out settle (no snap at the end)
        k = int(m.group(2)); sp = 400.0 / cs
        d = int(round((k - 1) * cg / sp)); t = int(round(cs * (1 + 0.35 * (k - 1) / 14.0)))
        return '%s%d" delay="%d" tween="quadratic" easing="out"/><effect type="fade" start="0" end="100" time="%d" delay="%d"' % (m.group(1), t, d, int(round(t * 0.9)), d)
    # 5.33.454 FADEINS (Rob: "I PREFER FADE INS FOR ALL TRANSITIONS"): cascade rows no longer drop in (slide start 0,0 = fade only); anchor accepts both
    s = re.sub(r'(Integer\.IsEqual\(ListItem\.CurrentItem,(\d+)\)"[^>]*><effect type="slide" start="0,(?:-40|0)" end="0,0" time=")\d+" delay="\d+" tween="\w+" easing="out"/><effect type="fade" start="0" end="100" time="\d+" delay="\d+"', casc, s)
    fl = val('flip', g)
    def flip(m):
        x = re.sub(r'time="\d+"', 'time="%d"' % fl, m.group(0))
        return re.sub(r'delay="\d+"', 'delay="%d"' % fl, x)
    s = re.sub(r'<animation type="(?:Hidden|Visible)" condition="!String\.IsEqual\(Window\(Home\)\.Property\(bz_tovideo\),long\)">.*?</animation>', flip, s)
    # 4.0.1 O09: albumscale (Jumbo album scale speed) row is gone with O36; the album zoom keeps its 1200 ms
    s = re.sub(r'<animation type="Conditional" condition="[^"]*bz_sway_pulse[^"]*" reversible="false" pulse="true">.*?</animation>', shift(int(round(val('swaypause', g) * 500))), s, flags=re.S)
    # BETA 2.10: poster hold (pause at the -13 / +13 end points), same scheme as the album hold
    s = re.sub(r'<animation type="Conditional" condition="[^"]*bz_ppulse[^"]*" reversible="false" pulse="true">.*?</animation>', shift(int(round(val('phold', g) * 500))), s, flags=re.S)
    return s
def _dust(s, g):
    # 3.1.2: the old BZD lit-hold fades (afin/afout/pfin/pfout) are gone: lit dust now rides the art glare (BezelLitDust)
    # BEZEL 3.1.1: ambient glow cycle: the dust colour is the Glow peak, the fade dips to Ambient (lo = Ambient / peak); peak <= Ambient = steady
    def num(i, d, vals):
        x = g('Skin.String(bz_at_%s)' % i); return vals[int(x) - 1] if x.isdigit() and 1 <= int(x) <= len(vals) else vals[d - 1]
    amb = num('d3amb', 2, [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]); pk = num('d3glow', 2, [10, 20, 30, 40, 45, 50, 60, 70, 80, 90, 100])
    lo = min(100, int(round(100.0 * amb / pk)))
    off = num('d3goff', 3, [i * 1000 for i in range(11)])   # Glow layer offset: 0 .. 10 s between successive layers (far, mid, near, soft dust, spin)
    def glow(m):
        d = off * int(m.group(1)); L = 20000 + 4 * off
        if g('Skin.String(bz_at_breathe)') == '1' or g('Skin.String(bz_at_glow%s)' % m.group(1)) == '1':   # 4.0.1 O12: Breathe off (all or this layer) = steady at Ambient
            return ('<!--BZG:%s--><animation type="Conditional" condition="true" loop="true" reversible="false"><effect type="fade" start="%d" end="%d" time="%d"/></animation>') % (m.group(1), lo, lo, L)   # every layer loops on the same L so the offsets stay locked (layers glow in turn, then rest at Ambient)
        lw = min(lo, 40) if m.group(1) == '4' else lo   # 4.5.2: spin layer always pulses (fades to 40% and back) even when Ambient = Glow made the others steady
        return ('<!--BZG:%s--><animation type="Conditional" condition="true" loop="true" reversible="false"><effect type="fade" start="100" end="100" time="%d"/><effect type="fade" start="%d" end="100" time="10000" delay="%d" tween="sine" easing="inout"/>'
                '<effect type="fade" start="100" end="%d" time="10000" delay="%d" tween="sine" easing="inout"/></animation>') % (m.group(1), L, lw, d, lw, d + 10000)
    s = re.sub(r'<!--BZG:(\d)--><animation [^>]*>.*?</animation>', glow, s, flags=re.S)
    # 4.2.0 O62: flake sparkle removed (no BZS stacks any more)
    return s
def _flip(s, g):
    return re.sub(r'mon\.waitForAbort\([\d.]+\)(: break +# BETA 2\.2 A)', 'mon.waitForAbort(%g)\\1' % (val('flip', g) / 1000.0), s)
# 3.0.2 slide-menu freeze fix: Kodi resets only the FIRST Hidden animation of a control when it is shown again
# (CGUIControl::QueueAnimation looks the reverse animation up without conditions). With 7 conditional Hidden
# animations, any non-default close step (Mid / High / Extreme) stayed applied after the first close, so the
# reopened slide menu sat off-screen (invisible) while holding the focus. So the menu / dim / music-control
# animations are now ONE unconditional Visible + ONE Hidden animation, with the times written here.
SPK0 = 7000
SPKF = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.25, 1.4, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3]
TOPEN = [450, 360, 300, 257, 225, 200, 180, 164, 144, 129, 120, 103, 90, 80, 72, 65, 60]
# BEZEL 3.1: the menu drops from the block top (~0.4 s open / 0.35 s close at 1x)
# 4.0.1 O23/O24: 17 steps 0.4x .. 3x (step 7 = 1x = default, as before)
MOPEN = [1000, 800, 667, 571, 500, 444, 400, 364, 320, 286, 267, 229, 200, 178, 160, 145, 133]
MCLOSE = [875, 700, 583, 500, 438, 389, 350, 318, 280, 250, 233, 200, 175, 156, 140, 127, 117]
TCLOSE = {'menuclose': [375, 300, 250, 214, 188, 167, 150, 136, 120, 107, 100, 86, 75, 67, 60, 55, 50], 'mctrl': [375, 300, 250, 214, 188, 167, 150, 136, 120, 107, 100, 86, 75, 67, 60, 55, 50]}
def _step(i, get, n=7, d=1):
    s = get('Skin.String(bz_at_%s)' % i)
    return int(s) if s.isdigit() and 1 <= int(s) <= n else d
def _tuner(s, g):
    o = MOPEN[_step('menuopen', g, 17, 7) - 1]; c = MCLOSE[_step('menuclose', g, 17, 7) - 1]
    m = _step('mctrl', g, 17, 7); mo = TOPEN[m - 1]; mc = TCLOSE['mctrl'][m - 1]
    body = {'BezelATMenuAnim': '<animation type="Visible"><effect type="fade" start="0" end="100" time="%d" tween="sine" easing="out"/></animation>'
                               '<animation type="Hidden"><effect type="fade" start="100" end="0" time="%d" tween="sine" easing="in"/></animation>' % (o, c),   # 4.7.2 Rob: no slide / no pop
            'BezelATViewAnim': '<animation type="Visible"><effect type="fade" start="0" end="100" time="%d" tween="sine" easing="out"/></animation>'
                               '<animation type="Hidden"><effect type="fade" start="100" end="0" time="%d" tween="sine" easing="in"/></animation>' % (max(o,180), max(c,150)),   # 4.7.2 Rob: crossfade, no slide   # 4.0.1 O35: view options = Main menu speed
            'BezelATDimAnim': '<animation effect="fade" start="0" end="100" time="%d" tween="cubic" easing="out">Visible</animation>'
                              '<animation effect="fade" start="100" end="0" time="%d" tween="cubic" easing="in">Hidden</animation>' % (o, c),
            'BezelATMctrlAnim': '<animation effect="fade" start="0" end="100" time="%d" tween="sine" easing="out">Visible</animation>'
                                '<animation effect="fade" start="100" end="0" time="%d" tween="sine" easing="in">Hidden</animation>' % (mo, mc)}
    for k, b in body.items():
        s = re.sub(r'(<include name="%s">).*?(</include>)' % k, lambda x: x.group(1) + b + x.group(2), s, count=1, flags=re.S)
    return s

def _hold(s, g):
    # 4.7.1 B11: Dust 2.0 fade hold. After the fade-out the layer stays out for H ms (fixed 2 s since t3943u; still re-applied when Fade speed changes).
    # far / spin fade out first: the fade-in delay = T + H; mid fades in first: a neutral 100->100 effect stretches the loop to 2T + H.
    for L in 'fms':
        H = 2000   # t3943u: Fade hold Tuner rows deleted -> fixed 2 s (old default)
        def f(m):
            b = m.group(0)
            b = re.sub(r'<effect type="fade" start="100" end="100" time="\d+"/>', '', b)
            e = re.findall(r'<effect type="fade" start="(\d+)" end="(\d+)" time="(\d+)"(?: delay="\d+")?[^>]*/>', b)
            if len(e) != 2: return b
            T = int(e[0][2])
            if int(e[0][1]) < int(e[0][0]):
                return re.sub(r'(<effect type="fade" start="\d+" end="\d+" time="\d+") delay="\d+"', r'\g<1> delay="%d"' % (T + H), b, count=1)
            b = re.sub(r'(<effect type="fade" start="\d+" end="\d+" time="\d+") delay="\d+"', r'\g<1> delay="%d"' % T, b, count=1)
            if H: b = b.replace('reversible="false">', 'reversible="false"><effect type="fade" start="100" end="100" time="%d"/>' % (2 * T + H), 1)
            return b
        s = re.sub(r'<animation type="Conditional" condition="[^"]*bz_at_d20%sfade\)[^"]*" loop="true" reversible="false">.*?</animation>' % L, f, s)
    return s
def _dusth(s, g): return _hold(_dust(s, g), g)
def _bezelh(s, g): return _hold(_bezel(s, g), g)
def _rows(s, g):   # 5.33.7 fork7: shared list row-scroll anim on every BEZEL list outside Includes_Bezel (same bzt="row" anchor)
    t, tw = val('rowscroll', g), val('rowsoft', g)
    return re.sub(r'<scrolltime tween="\w+" easing="\w+" bzt="row">\d+</scrolltime>', '<scrolltime tween="%s" easing="out" bzt="row">%d</scrolltime>' % (tw, t), s)
FILES = (('xml/Includes_Tuner.xml', _tuner), ('xml/Includes_Bezel.xml', _bezelh), ('xml/Custom_1114_Dust.xml', _dusth), ('xml/Includes_Dust3.xml', _dust))   # 5.33.8: _rows unhooked (Rob: bar+anim only, no scroll)   # BEZEL 3.0: bz_flip reads the flip time live; dust lives in the dust dialog
def _check(n):
    # 3.0.2: a patch result is only accepted when it is well-formed XML with the expected root
    import xml.etree.ElementTree as ET
    try: r = ET.fromstring(n.encode('utf-8'))
    except Exception as e: raise ValueError('XML parse error: %s' % e)
    if r.tag not in ('window', 'includes'): raise ValueError('unexpected root <%s>' % r.tag)
def _write(p, n):
    # BEZEL 3.0 fix: write a temp file then swap it in, retrying (Windows / Android can briefly hold the file while Kodi reloads the skin)
    import time
    t = p + '.bztmp'; err = None
    for _ in range(5):
        try:
            with open(t, 'w', encoding='utf-8', newline='') as f: f.write(n)
            _check(open(t, encoding='utf-8').read())   # 3.0.2: the file on disk must parse before it is swapped in
            os.replace(t, p); return
        except ValueError:
            err = None; break
        except Exception as e:
            err = e; time.sleep(0.3)
    try: os.remove(t)
    except Exception: pass
    if err is None: raise ValueError('patched %s did not parse as XML; original kept' % os.path.basename(p))
    raise err   # BEZEL 3.0 fix: never fall back to an in-place write (a failed in-place write left a cut-off Custom_1114_Dust.xml)
def patch(get):
    ch = False
    for rel, fn in FILES:
        p = os.path.join(SKIN, rel)
        try:
            s = open(p, encoding='utf-8').read(); n = fn(s, get)
            if n != s and n.rstrip().endswith('</window>' if (rel.startswith('xml/Custom') or rel == 'xml/FileManager.xml') else '</includes>'):   # BEZEL 3.0: only whole files are written
                _check(n); _write(p, n); ch = True   # 3.0.2: parse-check in memory, then again on the temp file
        except Exception as e:
            try:
                import xbmc, xbmcgui, traceback; xbmc.log('BEZEL tuner patch %s failed: %r\n%s' % (rel, e, traceback.format_exc()), xbmc.LOGERROR)
                xbmcgui.Dialog().notification('BEZEL tuner', 'Could not apply to %s (see log)' % os.path.basename(rel), xbmcgui.NOTIFICATION_ERROR, 4000)   # BEZEL 3.0 patch-error toast
            except Exception: pass
    return ch
