from kit import *

AC = "#FFB454"
AC2 = "#FFD08A"
D = DARK
L = LIGHT


def scene(x, y, w, h, uid, kind="beach"):
    """A stylised destination photo built from shapes."""
    cid = f"sc{uid}"
    sky = {"beach": ("#3E5F97", "#F0A87E", "#FFD9A8"),
           "city": ("#1E2E52", "#5E4C8A", "#E28FA0"),
           "desert": ("#5C7FB0", "#E8A46B", "#FFDCA8"),
           "mountain": ("#2E4A78", "#7C8FC0", "#F2D3B0")}[kind]
    o = (f'<defs><clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath>'
         f'<linearGradient id="sk{cid}" x1="0" y1="0" x2="0" y2="1">'
         f'<stop stop-color="{sky[0]}"/><stop offset=".62" stop-color="{sky[1]}"/>'
         f'<stop offset="1" stop-color="{sky[2]}"/></linearGradient>'
         f'<linearGradient id="se{cid}" x1="0" y1="0" x2="0" y2="1">'
         f'<stop stop-color="#2E6E96"/><stop offset="1" stop-color="#15486B"/></linearGradient></defs>')
    o += f'<g clip-path="url(#{cid})">'
    o += rect(x, y, w, h, 0, f"url(#sk{cid})")
    sunx, suny = x + w * .70, y + h * .40
    o += circ(sunx, suny, h * .11, "#FFF3D6", op=.95)
    o += circ(sunx, suny, h * .20, "#FFE3AE", op=.22)
    # horizon / sea
    hz = y + h * .58
    o += rect(x, hz, w, y + h - hz, 0, f"url(#se{cid})")
    for i in range(4):
        o += rect(x + w * (.08 + i * .19), hz + h * (.08 + i * .07), w * .13, 2, 1, "#BFE4F2", op=.5)
    o += path(f"M{sunx} {hz} L{sunx - 6} {y + h} L{sunx + 6} {y + h} Z", fill="#FFE9BE", op=.35)
    if kind == "beach":
        # sand
        o += path(f"M{x} {y + h} L{x} {y + h * .86} Q{x + w * .3} {y + h * .78} {x + w} {y + h * .88} "
                  f"L{x + w} {y + h} Z", fill="#F0DDB8")
        # palms
        for px, ps in [(x + w * .16, 1.0), (x + w * .30, .72)]:
            base = y + h * .88
            o += path(f"M{px} {base} q{-3 * ps} {-26 * ps} {2 * ps} {-46 * ps}",
                      stroke="#3A2A1E", sw=3.4 * ps)
            top = base - 46 * ps
            for a in (-1, -.5, .5, 1):
                o += path(f"M{px + 2 * ps} {top} q{16 * a * ps} {-9 * ps} {26 * a * ps} {4 * ps}",
                          stroke="#1F4736", sw=3.6 * ps)
        # resort block
        o += rect(x + w * .52, y + h * .60, w * .30, h * .26, 3, "#F7EEDD", op=.95)
        o += path(f"M{x + w * .50} {y + h * .60} L{x + w * .67} {y + h * .50} L{x + w * .84} {y + h * .60} Z",
                  fill="#C4715A")
        for i in range(4):
            o += rect(x + w * (.55 + i * .065), y + h * .68, w * .035, h * .07, 1, "#5E8FA8")
    elif kind == "desert":
        o += path(f"M{x} {y + h} L{x} {y + h * .74} Q{x + w * .26} {y + h * .60} {x + w * .52} {y + h * .76} "
                  f"Q{x + w * .78} {y + h * .90} {x + w} {y + h * .70} L{x + w} {y + h} Z", fill="#E6C289")
        o += path(f"M{x} {y + h} L{x} {y + h * .88} Q{x + w * .34} {y + h * .74} {x + w * .66} {y + h * .90} "
                  f"Q{x + w * .86} {y + h} {x + w} {y + h * .92} L{x + w} {y + h} Z", fill="#C99C5F")
        o += rect(x + w * .10, y + h * .62, w * .22, h * .20, 2, "#F3E6CE")
        o += path(f"M{x + w * .08} {y + h * .62} L{x + w * .21} {y + h * .53} L{x + w * .34} {y + h * .62} Z",
                  fill="#8C6B4A")
        for i in range(3):
            o += rect(x + w * (.13 + i * .06), y + h * .68, w * .028, h * .06, 1, "#6E93A8")
    else:
        for i, (bw, bh) in enumerate([(.08, .30), (.06, .42), (.09, .24), (.05, .36), (.10, .20)]):
            bx = x + w * (.10 + i * .17)
            o += rect(bx, hz - h * bh, w * bw, h * bh, 2, "#101B2E", op=.9)
            for k in range(3):
                o += rect(bx + w * .012, hz - h * bh + h * .04 + k * h * .06, w * .015, h * .022, .5,
                          "#FFD9A0", op=.75)
    o += "</g>"
    return o


def build():
    uid = "bk"
    o = glow(uid + "1", AC, 240, 320, 400, ".15")
    o += glow(uid + "2", "#5B8CFF", 880, 300, 380, ".11")
    defs = (f'<linearGradient id="{uid}btn" x1="0" y1="0" x2="1" y2="0">'
            f'<stop stop-color="{AC}"/><stop offset="1" stop-color="#FF9A3D"/></linearGradient>')

    # ================= HOTEL DETAIL PHONE =================
    PHX, PHY, PHW, PHH = 56, 46, 336, 672
    head, tail, sx, sy, sw, sh = phone(PHX, PHY, PHW, PHH, uid, "#FFFFFF")
    o += head
    IH = 268
    o += scene(sx, sy, sw, IH, uid + "h", "beach")
    o += txt(sx + 24, sy + 32, "9:41", 11, "#FFFFFF", 700)
    o += rect(sx + sw - 50, sy + 24, 20, 9, 2, "#FFFFFF", op=.9)
    o += circ(sx + 32, sy + 74, 17, "#FFFFFF", op=.92)
    o += path(f"M{sx + 35} {sy + 68} L{sx + 29} {sy + 74} L{sx + 35} {sy + 80}", stroke=L["ink"], sw=2)
    o += circ(sx + sw - 32, sy + 74, 17, "#FFFFFF", op=.92)
    hx, hy = sx + sw - 32, sy + 74
    o += path(f"M{hx} {hy + 5.5} C{hx - 9} {hy - 1} {hx - 7} {hy - 8} {hx - 3} {hy - 8} "
              f"C{hx - 1} {hy - 8} {hx} {hy - 6.5} {hx} {hy - 5.5} "
              f"C{hx} {hy - 6.5} {hx + 1} {hy - 8} {hx + 3} {hy - 8} "
              f"C{hx + 7} {hy - 8} {hx + 9} {hy - 1} {hx} {hy + 5.5} Z",
              fill="none", stroke=L["ink"], sw=1.8)
    o += pill(sx + 24, sy + IH - 84, 96, 22, "GULF ESCAPES", "#00000059", "#FFFFFF", 8, 800, 1.4)
    for i in range(5):
        o += rect(sx + sw / 2 - 26 + i * 12, sy + IH - 48, 8 if i else 16, 4, 2,
                  "#FFFFFF", op=1 if i == 0 else .5)

    # sheet
    BY = sy + IH - 24
    o += path(f"M{sx} {BY + 26} Q{sx} {BY} {sx + 26} {BY} L{sx + sw - 26} {BY} "
              f"Q{sx + sw} {BY} {sx + sw} {BY + 26} L{sx + sw} {sy + sh} L{sx} {sy + sh} Z",
              fill="#FFFFFF")
    ty = BY + 44
    o += txt(sx + 24, ty, "Marina Bay Resort", 20, L["ink"], 800)
    o += circ(sx + 28, ty + 18, 3.4, "none", L["muted"], 1.6)
    o += path(f"M{sx + 28} {ty + 26} c-6 -8 -5 -14 0 -14 c5 0 6 6 0 14 Z", fill=L["muted"])
    o += txt(sx + 40, ty + 24, "Sahl Hasheesh · Hurghada", 10, L["muted"], 500)
    o += stars(sx + 24, ty + 44, 5, 10, "#FFB020")
    o += txt(sx + 92, ty + 47.5, "4.8", 10.5, L["ink"], 800)
    o += txt(sx + 112, ty + 47.5, "· 312 reviews", 10, L["muted"], 500)
    o += pill(sx + sw - 92, ty + 34, 68, 20, "Superhost", "#FFF5E6", "#B87413", 8.5)

    ay = ty + 70
    for i, (n, k) in enumerate([("Wi-Fi", "wifi"), ("Pool", "pool"), ("Breakfast", "food"), ("Spa", "spa")]):
        awd = (sw - 48) / 4
        ax = sx + 24 + i * awd
        o += rect(ax, ay, awd - 8, 56, 12, "#F5F7FB")
        m = (ax + (awd - 8) / 2, ay + 22)
        if k == "wifi":
            for r in (10, 6.5):
                o += path(f"M{m[0] - r} {m[1] + r * .35} a{r} {r} 0 0 1 {2 * r} 0",
                          stroke="#C08432", sw=2)
            o += circ(m[0], m[1] + 6, 2, "#C08432")
        elif k == "pool":
            o += path(f"M{m[0] - 10} {m[1] + 5} q5 -5 10 0 t10 0", stroke="#C08432", sw=2)
            o += path(f"M{m[0] - 10} {m[1] - 2} q5 -5 10 0 t10 0", stroke="#C08432", sw=2)
        elif k == "food":
            o += path(f"M{m[0] - 7} {m[1] - 8} v14 M{m[0] - 7} {m[1] - 8} m-3 0 v6 m6 -6 v6",
                      stroke="#C08432", sw=1.8)
            o += path(f"M{m[0] + 6} {m[1] - 8} v14 M{m[0] + 6} {m[1] - 8} q-4 2 -4 6 h8 q0 -4 -4 -6",
                      stroke="#C08432", sw=1.8)
        else:
            o += path(f"M{m[0]} {m[1] + 7} c-9 -5 -9 -14 0 -16 c9 2 9 11 0 16 Z", fill="#C08432")
        o += txt(m[0], ay + 46, n, 8.5, L["ink"], 600, "middle")

    # dates
    dy = ay + 74
    o += rect(sx + 24, dy, sw - 48, 62, 14, "#FFFFFF")
    o += rect(sx + 24, dy, sw - 48, 62, 14, "none", "#E6EBF3", 1.4)
    o += line(sx + sw / 2 - 12, dy + 12, sx + sw / 2 - 12, dy + 50, "#E6EBF3", 1.2)
    o += txt(sx + 42, dy + 24, "CHECK IN", 8, L["muted"], 800, ls=1.2)
    o += txt(sx + 42, dy + 44, "24 Feb", 13, L["ink"], 700)
    o += txt(sx + sw / 2 + 6, dy + 24, "CHECK OUT", 8, L["muted"], 800, ls=1.2)
    o += txt(sx + sw / 2 + 6, dy + 44, "27 Feb", 13, L["ink"], 700)
    o += pill(sx + sw - 96, dy + 70, 72, 22, "2 guests", "#F1F4F9", L["muted"], 9)
    o += txt(sx + 24, dy + 86, "3 nights · free cancellation", 9.5, "#12A56B", 600)

    # price bar
    by = sy + sh - 84
    o += line(sx + 20, by - 14, sx + sw - 20, by - 14, "#EDF1F7", 1)
    o += txt(sx + 24, by + 20, "EGP 3,450", 19, L["ink"], 800)
    o += txt(sx + 24, by + 38, "per night · EGP 10,350 total", 9.5, L["muted"], 500)
    o += rect(sx + sw - 138, by - 2, 114, 46, 14, f"url(#{uid}btn)")
    o += txt(sx + sw - 81, by + 27, "Reserve", 13, "#3D2606", 800, "middle")
    o += rect(sx + sw / 2 - 52, sy + sh - 16, 104, 4.5, 2.5, "#C9D2DF")
    o += tail

    # ================= SEARCH RESULTS WINDOW =================
    WX, WY, WW, WH = 430, 92, 718, 452
    head, tail, cx, cy, cw, ch = window(WX, WY, WW, WH, uid, "stay.azdev.app / search", accent=AC)
    o += head
    # search bar
    o += rect(cx, cy, cw, 66, 0, "#0E1522")
    o += line(cx, cy + 66, cx + cw, cy + 66, D["line"], 1)
    fields = [("WHERE", "Hurghada, Egypt", 200), ("DATES", "24 – 27 Feb", 140), ("GUESTS", "2 adults", 116)]
    fx = cx + 24
    o += rect(cx + 24, cy + 14, 500, 38, 19, "#182337")
    for i, (k, v, fw) in enumerate(fields):
        o += txt(fx + 20, cy + 30, k, 7.5, D["muted"], 800, ls=1.2)
        o += txt(fx + 20, cy + 44, v, 10, D["ink"], 600)
        if i < 2:
            o += line(fx + fw, cy + 22, fx + fw, cy + 44, "#26334B", 1)
        fx += fw
    o += rect(cx + 496, cy + 20, 26, 26, 13, f"url(#{uid}btn)")
    o += circ(cx + 508, cy + 32, 4.4, "none", "#3D2606", 1.8)
    o += line(cx + 511, cy + 35, cx + 514, cy + 38, "#3D2606", 1.8)
    o += pill(cx + cw - 130, cy + 22, 100, 22, "Filters  ·  3", "#182337", AC, 9)

    # filter rail
    FX2 = cx + 24
    FW2 = 168
    FY2 = cy + 86
    o += rect(FX2, FY2, FW2, ch - 100, 12, "#0E1522")
    o += txt(FX2 + 16, FY2 + 26, "Price / night", 10.5, D["ink"], 700)
    o += bars(FX2 + 16, FY2 + 38, FW2 - 32, 30, [3, 6, 9, 14, 18, 15, 11, 7, 4, 2], "#1E2B42", .2, 2)
    o += rect(FX2 + 16, FY2 + 72, FW2 - 32, 4, 2, "#1E2B42")
    o += rect(FX2 + 42, FY2 + 72, 78, 4, 2, AC)
    o += circ(FX2 + 42, FY2 + 74, 7, AC, "#0E1522", 2)
    o += circ(FX2 + 120, FY2 + 74, 7, AC, "#0E1522", 2)
    o += txt(FX2 + 16, FY2 + 96, "EGP 1,200", 8.5, D["muted"], 600)
    o += txt(FX2 + FW2 - 16, FY2 + 96, "EGP 6,000", 8.5, D["muted"], 600, "end")
    o += line(FX2 + 16, FY2 + 112, FX2 + FW2 - 16, FY2 + 112, D["line"], 1)
    o += txt(FX2 + 16, FY2 + 134, "Guest rating", 10.5, D["ink"], 700)
    for i, (lb, on) in enumerate([("4.5+  Exceptional", True), ("4.0+  Very good", True),
                                  ("3.5+  Good", False)]):
        oy = FY2 + 150 + i * 26
        o += rect(FX2 + 16, oy, 14, 14, 4, AC if on else "none", "#2C3A54" if not on else None, 1.4)
        if on:
            o += path(f"M{FX2 + 20} {oy + 7} l3 3.4 6 -7", stroke="#3D2606", sw=2)
        o += txt(FX2 + 38, oy + 11, lb, 9, D["ink"] if on else D["muted"], 500)
    o += line(FX2 + 16, FY2 + 236, FX2 + FW2 - 16, FY2 + 236, D["line"], 1)
    o += txt(FX2 + 16, FY2 + 258, "Amenities", 10.5, D["ink"], 700)
    for i, lb in enumerate(["Private beach", "Free breakfast"]):
        oy = FY2 + 272 + i * 24
        o += rect(FX2 + 16, oy, 14, 14, 4, "none", "#2C3A54", 1.4)
        o += txt(FX2 + 38, oy + 11, lb, 9, D["muted"], 500)

    # results
    RX2 = FX2 + FW2 + 18
    RW2 = cw - (FW2 + 18) - 48
    o += txt(RX2, FY2 + 14, "218 stays in Hurghada", 11.5, D["ink"], 700)
    o += txt(cx + cw - 24, FY2 + 14, "Sort: Top rated ▾", 9.5, D["muted"], 600, "end")
    res = [("Marina Bay Resort", "Sahl Hasheesh · Sea view", "4.8", "EGP 3,450", "beach", True),
           ("Dune Palace Hotel", "El Gouna · Desert suite", "4.6", "EGP 2,180", "desert", False),
           ("Harbour View Suites", "Downtown · City centre", "4.5", "EGP 1,690", "city", False)]
    for i, (n, sub, rt, pr, kind, sel) in enumerate(res):
        ry = FY2 + 28 + i * 100
        o += rect(RX2, ry, RW2, 92, 12, "#101827")
        o += rect(RX2, ry, RW2, 92, 12, "none", AC if sel else D["line"], 1.4)
        o += (f'<defs><clipPath id="{uid}rc{i}"><rect x="{RX2 + 8}" y="{ry + 8}" width="118" height="76" rx="9"/></clipPath></defs>'
              f'<g clip-path="url(#{uid}rc{i})">')
        o += scene(RX2 + 8, ry + 8, 118, 76, uid + "r" + str(i), kind)
        o += "</g>"
        o += txt(RX2 + 140, ry + 26, n, 12, D["ink"], 700)
        o += txt(RX2 + 140, ry + 42, sub, 9, D["muted"], 500)
        o += stars(RX2 + 140, ry + 58, 5, 7.5, "#FFB020", "#2A3550")
        o += txt(RX2 + 192, ry + 61, rt, 9, D["ink"], 700)
        o += txt(RX2 + 210, ry + 61, "· 312 reviews", 9, D["muted"], 500)
        if sel:
            o += pill(RX2 + 140, ry + 68, 76, 17, "Free cancel", "#132A22", "#3BD59A", 7.5)
        o += txt(RX2 + RW2 - 16, ry + 32, pr, 13, D["ink"], 800, "end")
        o += txt(RX2 + RW2 - 16, ry + 48, "per night", 8.5, D["muted"], 500, "end")
        o += rect(RX2 + RW2 - 84, ry + 58, 68, 24, 8, f"url(#{uid}btn)" if sel else "#1B2537")
        o += txt(RX2 + RW2 - 50, ry + 74, "View" if not sel else "Booked", 9,
                 "#3D2606" if sel else D["ink"], 800, "middle")
    o += tail

    # ================= CONFIRMATION TICKET =================
    TX, TY, TW, TH = 468, 572, 680, 150
    o += rect(TX - 4, TY + 12, TW + 8, TH, 20, "#000", op=.42)
    o += rect(TX, TY, TW, TH, 18, "#0F1726")
    o += rect(TX, TY, TW, TH, 18, "none", "#243149", 1.4)
    o += rect(TX, TY, 5, TH, 2.5, AC)
    # perforation
    o += line(TX + 496, TY + 18, TX + 496, TY + TH - 18, "#243149", 1.4, 1, "round", "5 7")
    o += circ(TX + 496, TY, 9, "#080D16")
    o += circ(TX + 496, TY + TH, 9, "#080D16")

    o += pill(TX + 28, TY + 22, 108, 20, "● BOOKING CONFIRMED", "#132A22", "#3BD59A", 7.5)
    o += txt(TX + 28, TY + 70, "Marina Bay Resort", 17, D["ink"], 800)
    o += txt(TX + 28, TY + 90, "Deluxe sea-view room · 2 adults", 10, D["muted"], 500)
    cols = [("CHECK IN", "Tue 24 Feb"), ("CHECK OUT", "Fri 27 Feb"), ("REF", "AZ-4821-HRG")]
    for i, (k, v) in enumerate(cols):
        kx = TX + 28 + i * 152
        o += txt(kx, TY + 116, k, 7.5, D["muted"], 800, ls=1.2)
        o += txt(kx, TY + 132, v, 10.5, D["ink"], 700, font=MONO if i == 2 else None)
    # qr-ish
    import random
    random.seed(21)
    QX, QY = TX + 556, TY + 30
    o += rect(QX - 8, QY - 8, 76, 76, 10, "#FFFFFF")
    for r in range(7):
        for c in range(7):
            if random.random() > .45:
                o += rect(QX + c * 8.6, QY + r * 8.6, 7.2, 7.2, 1.4, "#0F1726")
    o += rect(QX - 4, QY - 4, 22, 22, 4, "#FFFFFF")
    o += rect(QX - 2, QY - 2, 18, 18, 3, "none", "#0F1726", 3)
    o += txt(TX + 588, TY + 128, "Scan at reception", 9, D["muted"], 600, "middle")

    o += txt(1148, 66, "SEARCH  ·  STAY DETAIL  ·  CONFIRMATION", 10, "#7C86A6", 700, "end", 1.8)
    return wrapsvg(o, defs)


if __name__ == "__main__":
    open("../assets/projects/booking/showcase.svg", "w").write(build())
    print("ok")
