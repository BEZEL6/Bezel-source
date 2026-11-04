"""Ordinal-addressed edits on Kodi XML source text (comments preserved).
Element ordinals match geom.py's _o / _co (document order, comments skipped)."""
import re
from lxml import etree

TAG = re.compile(r'<(/?)([A-Za-z_][\w.-]*)((?:\s+[^\s=>/]+\s*=\s*"[^"]*")*)\s*(/?)>')

def tokens(text):
    out = []
    pos = 0
    com = [(m.start(), m.end()) for m in re.finditer(r'<!--.*?-->', text, re.S)]
    ci = 0
    for m in TAG.finditer(text):
        while ci < len(com) and com[ci][1] <= m.start(): ci += 1
        if ci < len(com) and com[ci][0] <= m.start() < com[ci][1]: continue
        out.append(m)
    return out

def index(text):
    """returns dict tag->[match of start tag], centers list [match]"""
    by = {}; cen = []
    for m in tokens(text):
        if m.group(1): continue
        by.setdefault(m.group(2), []).append(m)
        if re.search(r'\scenter\s*=\s*"', m.group(3) or ''): cen.append(m)
    return by, cen

def check(path):
    text = open(path, encoding='utf-8').read()
    by, cen = index(text)
    t = etree.parse(path, etree.XMLParser(remove_comments=True, huge_tree=True))
    cnt = {}; cc = 0
    for e in t.iter():
        if isinstance(e.tag, str):
            cnt[e.tag] = cnt.get(e.tag, 0) + 1
            if 'center' in e.attrib: cc += 1
    bad = [k for k in cnt if cnt[k] != len(by.get(k, []))]
    return bad, cc == len(cen)

def fmt(v):
    return str(int(v)) if float(v).is_integer() else ('%.2f' % v).rstrip('0').rstrip('.')

def apply(path, edits):
    """edits: list of (kind, ord, op) kind in tag name (value edit of element text) or 'c' (center x).
    op: callable old_str -> new_str"""
    text = open(path, encoding='utf-8').read()
    by, cen = index(text)
    reps = []
    for kind, k, op in edits:
        if kind == 'c':
            m = cen[k]
            a = re.search(r'(\scenter\s*=\s*")([^"]*)(")', m.group(0))
            s0 = m.start() + a.start(2); s1 = m.start() + a.end(2)
            reps.append((s0, s1, op(text[s0:s1])))
        elif '@' in kind:
            tag, attr = kind.split('@')
            m = by[tag][k]
            a = re.search(r'(\s%s\s*=\s*")([^"]*)(")' % attr, m.group(0))
            s0 = m.start() + a.start(2); s1 = m.start() + a.end(2)
            reps.append((s0, s1, op(text[s0:s1])))
        else:
            m = by[kind][k]
            close = text.index('</%s>' % kind, m.end())
            reps.append((m.end(), close, op(text[m.end():close])))
    reps.sort()
    for a, b in zip(reps, reps[1:]):
        if a[1] > b[0]: raise Exception('overlap %s %s' % (a, b))
    for s0, s1, new in reversed(reps):
        text = text[:s0] + new + text[s1:]
    open(path, 'w', encoding='utf-8').write(text)
