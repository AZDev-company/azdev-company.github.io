"""Shared primitives for building realistic product-showcase SVGs."""

W, H = 1200, 760

# ---- UI palettes -------------------------------------------------
LIGHT = dict(bg="#FFFFFF", sub="#F3F6FA", line="#E6EBF3", ink="#0E1622",
             muted="#7A879C", faint="#EDF1F7")
DARK = dict(bg="#0C121D", sub="#141C2B", line="#212C40", ink="#EDF2FA",
            muted="#7E8CA6", faint="#18212F")

FONT = "Inter, 'Segoe UI', system-ui, -apple-system, sans-serif"
MONO = "'SF Mono', 'Roboto Mono', ui-monospace, monospace"


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def txt(x, y, s, size=12, fill="#0E1622", w=400, anchor="start", ls=0, op=1, font=None):
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    l = f' letter-spacing="{ls}"' if ls else ""
    o = f' opacity="{op}"' if op != 1 else ""
    return (f'<text x="{x}" y="{y}" font-family="{font or FONT}" font-size="{size}" '
            f'font-weight="{w}" fill="{fill}"{a}{l}{o}>{esc(s)}</text>')


def rect(x, y, w, h, rx=0, fill="none", stroke=None, sw=1, op=1, extra=""):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o = f' opacity="{op}"' if op != 1 else ""
    r = f' rx="{rx}"' if rx else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}"{r} fill="{fill}"{s}{o} {extra}/>'


def circ(cx, cy, r, fill="none", stroke=None, sw=1, op=1):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o = f' opacity="{op}"' if op != 1 else ""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{s}{o}/>'


def line(x1, y1, x2, y2, stroke, sw=1, op=1, cap="round", dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{sw}" stroke-linecap="{cap}" opacity="{op}"{d}/>')


def path(d, fill="none", stroke=None, sw=1, op=1, cap="round", join="round", dash=None):
    s = f' stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}" stroke-linejoin="{join}"' if stroke else ""
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="{fill}"{s} opacity="{op}"{da}/>'


def bar(x, y, w, h, fill, rx=None, op=1):
    """Skeleton/placeholder line."""
    return rect(x, y, w, h, rx if rx is not None else h / 2, fill, op=op)


def pill(x, y, w, h, label, bg, fg, size=9, weight=700, ls=0.4):
    return (rect(x, y, w, h, h / 2, bg) +
            txt(x + w / 2, y + h / 2 + size * 0.36, label, size, fg, weight, "middle", ls))


def avatar(cx, cy, r, c1, c2, uid):
    """Abstract person silhouette inside a circle — reads as a photo, invents no one."""
    cid = f"av{uid}"
    return (f'<defs><clipPath id="{cid}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>'
            f'<linearGradient id="g{cid}" x1="0" y1="0" x2="0" y2="1">'
            f'<stop stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs>'
            f'<g clip-path="url(#{cid})">'
            + circ(cx, cy, r, f"url(#g{cid})")
            + circ(cx, cy - r * 0.22, r * 0.34, "#ffffff", op=.85)
            + f'<ellipse cx="{cx}" cy="{cy + r * 0.78}" rx="{r * 0.62}" ry="{r * 0.48}" fill="#ffffff" opacity=".85"/>'
            + '</g>')


# ---- Device frames -----------------------------------------------
def phone(x, y, w, h, uid, screen_bg="#FFFFFF", tilt=None, island=True):
    """Returns (frame_open, frame_close, sx, sy, sw, sh) — draw screen content between."""
    rx = w * 0.135
    pad = w * 0.032
    sx, sy = x + pad, y + pad
    sw, sh = w - pad * 2, h - pad * 2
    srx = rx - pad * 0.85
    cid = f"ph{uid}"
    g = f'<g transform="{tilt}">' if tilt else "<g>"
    head = (g
            + f'<defs><clipPath id="{cid}"><rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="{srx}"/></clipPath>'
            + f'<linearGradient id="fr{cid}" x1="0" y1="0" x2="1" y2="1">'
            + f'<stop stop-color="#2E3949"/><stop offset=".45" stop-color="#151D2A"/>'
            + f'<stop offset="1" stop-color="#333F52"/></linearGradient></defs>'
            + f'<rect x="{x - 3}" y="{y + 10}" width="{w + 6}" height="{h}" rx="{rx + 3}" fill="#000" opacity=".38"/>'
            + rect(x, y, w, h, rx, f"url(#fr{cid})")
            + rect(x + 1.2, y + 1.2, w - 2.4, h - 2.4, rx - 1, "none", "#4A5768", 1.2, .5)
            + rect(sx, sy, sw, sh, srx, screen_bg)
            + f'<g clip-path="url(#{cid})">')
    tail = "</g>"
    if island:
        iw, ih = w * 0.30, w * 0.075
        tail += rect(x + w / 2 - iw / 2, y + pad + w * 0.028, iw, ih, ih / 2, "#0A0E16")
    tail += "</g>"
    return head, tail, sx, sy, sw, sh


def window(x, y, w, h, uid, url, bg="#0C121D", bar_bg="#131B29", line_c="#232F44",
           ink="#93A2BB", accent="#5B8CFF"):
    """Browser chrome. Returns (head, tail, cx, cy, cw, ch) for content area."""
    rx, bh = 16, 40
    cid = f"wn{uid}"
    head = (f'<defs><clipPath id="{cid}"><rect x="{x}" y="{y + bh}" width="{w}" height="{h - bh}"/></clipPath>'
            f'<clipPath id="{cid}o"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/></clipPath></defs>'
            + f'<rect x="{x - 4}" y="{y + 14}" width="{w + 8}" height="{h}" rx="{rx + 4}" fill="#000" opacity=".42"/>'
            + f'<g clip-path="url(#{cid}o)">'
            + rect(x, y, w, h, rx, bg)
            + rect(x, y, w, bh, 0, bar_bg)
            + line(x, y + bh, x + w, y + bh, line_c, 1)
            + circ(x + 20, y + bh / 2, 4.5, "#FF5F57") + circ(x + 36, y + bh / 2, 4.5, "#FEBC2E")
            + circ(x + 52, y + bh / 2, 4.5, "#28C840")
            + rect(x + 72, y + 10, min(240, w * 0.32), bh - 20, 10, "#1B2537")
            + circ(x + 86, y + bh / 2, 3.2, accent)
            + txt(x + 96, y + bh / 2 + 3.4, url, 9.5, ink, 500)
            + f'</g><g clip-path="url(#{cid})">')
    tail = f'</g>{rect(x, y, w, h, rx, "none", line_c, 1.4)}'
    return head, tail, x, y + bh, w, h - bh


def laptop(x, y, w, uid, url, **kw):
    """Laptop = window + base. Screen height locked to 16:10."""
    h = round(w * 0.625)
    head, tail, cx, cy, cw, ch = window(x, y, w, h, uid, url, **kw)
    bw = w * 1.20
    bx = x - (bw - w) / 2
    by = y + h
    base = (f'<path d="M{bx} {by + 20} L{bx + bw} {by + 20} L{bx + bw - 34} {by} L{bx + 34} {by} Z" '
            f'fill="#1A2231"/>'
            + f'<path d="M{bx} {by + 20} L{bx + bw} {by + 20} L{bx + bw - 4} {by + 27} L{bx + 4} {by + 27} Z" '
            f'fill="#101724"/>'
            + rect(x + w / 2 - 34, by + 5, 68, 5, 2.5, "#2C384B"))
    return head, tail + base, cx, cy, cw, ch


# ---- Reusable content blocks -------------------------------------
def sparkline(x, y, w, h, pts, stroke, sw=2.5, fill_id=None, op=1):
    n = len(pts)
    lo, hi = min(pts), max(pts)
    rng = (hi - lo) or 1
    coords = [(x + w * i / (n - 1), y + h - (p - lo) / rng * h) for i, p in enumerate(pts)]
    d = f"M{coords[0][0]:.1f} {coords[0][1]:.1f}"
    for i in range(1, n):
        px, py = coords[i - 1]
        cx, cy = coords[i]
        mx = (px + cx) / 2
        d += f" C{mx:.1f} {py:.1f} {mx:.1f} {cy:.1f} {cx:.1f} {cy:.1f}"
    out = ""
    if fill_id:
        out += path(d + f" L{coords[-1][0]:.1f} {y + h} L{coords[0][0]:.1f} {y + h} Z",
                    f"url(#{fill_id})")
    out += path(d, stroke=stroke, sw=sw, op=op)
    return out, coords


def bars(x, y, w, h, vals, fill, gap=0.34, rx=3, hi=None, hi_fill=None):
    n = len(vals)
    bw = w / (n - (1 - gap) * 0 + (n - 1) * gap) if False else w / (n + (n - 1) * gap)
    step = bw * (1 + gap)
    mx = max(vals) or 1
    out = ""
    for i, v in enumerate(vals):
        bh = max(3, h * v / mx)
        f = hi_fill if (hi is not None and i == hi) else fill
        out += rect(x + i * step, y + h - bh, bw, bh, min(rx, bw / 2), f)
    return out


def stars(x, y, n, size, fill, empty="#D8DEE9", total=5):
    out = ""
    for i in range(total):
        cx = x + i * (size * 1.32)
        c = fill if i < n else empty
        pts = []
        import math
        for k in range(10):
            r = size / 2 if k % 2 == 0 else size / 4.6
            a = -math.pi / 2 + k * math.pi / 5
            pts.append(f"{cx + r * math.cos(a):.2f},{y + r * math.sin(a):.2f}")
        out += f'<polygon points="{" ".join(pts)}" fill="{c}"/>'
    return out


def wrapsvg(body, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
            f'role="img" aria-label="Product interface showcase" '
            f'font-family="{FONT}">\n<defs>{defs}</defs>\n{body}\n</svg>\n')


def glow(uid, color, cx, cy, r, op=".30"):
    return (f'<defs><radialGradient id="gl{uid}"><stop stop-color="{color}" stop-opacity="{op}"/>'
            f'<stop offset="1" stop-color="{color}" stop-opacity="0"/></radialGradient></defs>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#gl{uid})"/>')


def caption(title, sub, accent, x=64, y=706):
    return (txt(x, y, title, 17, "#F2F6FC", 800, ls=0.2)
            + txt(x, y + 24, sub, 10.5, "#8494AC", 600, ls=1.5))
