from kit import *

AC = "#FF7A18"
AC2 = "#FFA martial"
AC2 = "#FFAA4D"


def road_grid(x, y, w, h, road, minor, uid):
    """Abstract city grid: blocks, roads, a river."""
    o = rect(x, y, w, h, 0, "#0B1420")
    # blocks
    import random
    random.seed(7)
    bx = x
    cols = [0.16, 0.13, 0.19, 0.15, 0.22, 0.15]
    rows = [0.21, 0.17, 0.24, 0.19, 0.19]
    ys = y
    for rh in rows:
        bx = x
        for cw in cols:
            o += rect(bx + 5, ys + 5, w * cw - 10, h * rh - 10, 4, "#111C2C")
            bx += w * cw
        ys += h * rh
    # roads
    bx = x
    for cw in cols[:-1]:
        bx += w * cw
        o += line(bx, y, bx, y + h, road, 3.5, .9, "butt")
    ys = y
    for rh in rows[:-1]:
        ys += h * rh
        o += line(x, ys, x + w, ys, road, 3.5, .9, "butt")
    # river
    o += path(f"M{x} {y + h * .74} C{x + w * .28} {y + h * .60} {x + w * .42} {y + h * .92} "
              f"{x + w * .68} {y + h * .74} S{x + w * .9} {y + h * .5} {x + w} {y + h * .56}",
              stroke="#12314F", sw=15, op=.95, cap="butt")
    # green patch
    o += rect(x + w * .06, y + h * .10, w * .17, h * .19, 5, "#12281F")
    return o


def build():
    uid = "dl"
    o = glow(uid + "1", AC, 420, 300, 430, ".16")
    o += glow(uid + "2", "#5B8CFF", 930, 380, 380, ".14")

    defs = (f'<linearGradient id="{uid}btn" x1="0" y1="0" x2="1" y2="0">'
            f'<stop stop-color="{AC}"/><stop offset="1" stop-color="{AC2}"/></linearGradient>'
            f'<linearGradient id="{uid}rt" x1="0" y1="0" x2="1" y2="1">'
            f'<stop stop-color="{AC}"/><stop offset="1" stop-color="#FFC46B"/></linearGradient>')

    # ================= DISPATCH CONSOLE =================
    WX, WY, WW, WH = 52, 74, 716, 472
    head, tail, cx, cy, cw, ch = window(WX, WY, WW, WH, uid, "dispatch.azdev.app / live-map", accent=AC)
    o += head
    D = DARK

    # left rail
    RW = 58
    o += rect(cx, cy, RW, ch, 0, "#0A1017")
    o += rect(cx + RW - 1, cy, 1, ch, 0, D["line"])
    o += rect(cx + 15, cy + 20, 28, 28, 9, f"url(#{uid}btn)")
    o += txt(cx + 29, cy + 38, "AZ", 10.5, "#121A26", 800, "middle")
    icons = [(True, "M4 10 L12 3 L20 10 L20 19 L4 19 Z"), (False, None), (False, None), (False, None), (False, None)]
    for i in range(5):
        iy = cy + 74 + i * 44
        if i == 0:
            o += rect(cx + 13, iy - 8, 32, 32, 10, AC, op=.16)
            o += rect(cx, iy - 8, 2.5, 32, 0, AC)
        c = AC if i == 0 else "#3B4A63"
        o += rect(cx + 22, iy, 14, 3, 1.5, c)
        o += rect(cx + 22, iy + 6, 14, 3, 1.5, c, op=.55)
        o += rect(cx + 22, iy + 12, 9, 3, 1.5, c, op=.35)

    # ---- MAP ----
    MX, MY, MW, MH = cx + RW, cy, 380, ch
    o += road_grid(MX, MY, MW, MH, "#1C2A3E", "#16202F", uid)

    # route
    rt = (f"M{MX + 62} {MY + 322} C{MX + 96} {MY + 268} {MX + 92} {MY + 236} {MX + 138} {MY + 214} "
          f"S{MX + 196} {MY + 200} {MX + 224} {MY + 152} "
          f"S{MX + 268} {MY + 96} {MX + 318} {MY + 88}")
    o += path(rt, stroke=AC, sw=11, op=.18)
    o += path(rt, stroke=f"url(#{uid}rt)", sw=4)
    o += path(rt, stroke="#FFFFFF", sw=1.6, op=.45, dash="1 9")

    # origin
    o += circ(MX + 62, MY + 322, 11, AC, op=.22)
    o += circ(MX + 62, MY + 322, 5.5, "#0B1420", AC, 3)
    # destination pin
    px, py = MX + 318, MY + 88
    o += path(f"M{px} {py + 6} C{px - 15} {py - 12} {px - 12} {py - 30} {px} {py - 30} "
              f"C{px + 12} {py - 30} {px + 15} {py - 12} {px} {py + 6} Z", fill="#FFFFFF")
    o += circ(px, py - 18, 5.2, "#0B1420")
    # courier marker
    kx, ky = MX + 216, MY + 168
    o += circ(kx, ky, 22, AC, op=.14)
    o += circ(kx, ky, 14, AC, op=.28)
    o += circ(kx, ky, 9, f"url(#{uid}btn)", "#0B1420", 2.5)
    o += path(f"M{kx - 3.2} {ky - 3.6} L{kx + 3.6} {ky} L{kx - 3.2} {ky + 3.6} Z", fill="#121A26")

    # other vehicles
    for vx, vy in [(MX + 96, MY + 118), (MX + 300, MY + 258), (MX + 158, MY + 344), (MX + 336, MY + 186)]:
        o += circ(vx, vy, 7, "#5B8CFF", op=.22)
        o += circ(vx, vy, 3.4, "#5B8CFF")

    # eta floating chip
    o += rect(MX + 16, MY + 16, 186, 54, 12, "#0D1725", op=.94)
    o += rect(MX + 16, MY + 16, 186, 54, 12, "none", "#23324A", 1)
    o += circ(MX + 34, MY + 34, 3.5, "#3BD59A")
    o += txt(MX + 44, MY + 37.5, "LIVE FLEET", 8, "#3BD59A", 800, ls=1.3)
    o += txt(MX + 28, MY + 60, "94", 19, "#FFFFFF", 800)
    o += txt(MX + 60, MY + 60, "on route", 10, D["muted"], 600)
    o += txt(MX + 124, MY + 60, "6", 19, AC, 800)
    o += txt(MX + 140, MY + 60, "delayed", 10, D["muted"], 600)

    # scale bar
    o += line(MX + 20, MY + MH - 20, MX + 74, MY + MH - 20, "#5B6B85", 2)
    o += txt(MX + 80, MY + MH - 16.5, "500 m", 8, "#5B6B85", 600)

    # ---- ORDERS PANEL ----
    PX = MX + MW
    PW = cw - RW - MW
    o += rect(PX, cy, PW, ch, 0, D["bg"])
    o += line(PX, cy, PX, cy + ch, D["line"], 1)
    o += txt(PX + 20, cy + 30, "Active orders", 12.5, D["ink"], 700)
    o += pill(PX + 122, cy + 18, 40, 17, "128", "#1B2537", D["muted"], 8.5)
    # search
    o += rect(PX + 20, cy + 44, PW - 76, 28, 8, "#111A28")
    o += circ(PX + 34, cy + 58, 4.2, "none", "#4B5B76", 1.6)
    o += line(PX + 37, cy + 61, PX + 40, cy + 64, "#4B5B76", 1.6)
    o += txt(PX + 47, cy + 61.5, "Search order or driver", 8.8, "#4B5B76", 500)

    rows = [("#4821", "Downtown · 3 items", "On the way", AC, "12 min"),
            ("#4820", "Al Nakheel · 1 item", "Picked up", "#5B8CFF", "18 min"),
            ("#4819", "Corniche · 5 items", "Preparing", "#B08CFF", "26 min"),
            ("#4818", "Sea View · 2 items", "Delivered", "#3BD59A", "done"),
            ("#4817", "Old Town · 4 items", "Delivered", "#3BD59A", "done")]
    ry = cy + 86
    for i, (oid, place, st, c, eta) in enumerate(rows):
        h = 62
        if i == 0:
            o += rect(PX + 12, ry, PW - 36, h - 8, 10, AC, op=.09)
            o += rect(PX + 12, ry, 2.5, h - 8, 1.2, AC)
        o += circ(PX + 32, ry + 26, 13, "#182233")
        o += rect(PX + 27, ry + 21, 10, 8, 1.5, c, op=.85)
        o += txt(PX + 54, ry + 22, oid, 10.5, D["ink"], 700, font=MONO)
        o += txt(PX + 54, ry + 37, place, 8.8, D["muted"], 500)
        o += pill(PX + 54, ry + 43, len(st) * 5.2 + 16, 15, st, "#182233", c, 8)
        o += txt(PX + PW - 26, ry + 28, eta, 9, D["ink"] if eta != "done" else D["muted"], 700, "end")
        if i < len(rows) - 1:
            o += line(PX + 20, ry + h - 4, PX + PW - 24, ry + h - 4, D["line"], 1, .7)
        ry += h
    o += tail

    # ================= CUSTOMER PHONE =================
    PHX, PHY, PHW, PHH = 780, 62, 330, 648
    head, tail, sx, sy, sw, sh = phone(PHX, PHY, PHW, PHH, uid, "#FFFFFF")
    o += head
    L = LIGHT
    # status bar
    o += txt(sx + 24, sy + 32, "9:41", 11, L["ink"], 700)
    o += rect(sx + sw - 52, sy + 24, 20, 9, 2, L["ink"], op=.85)
    o += rect(sx + sw - 78, sy + 24, 16, 9, 2, L["ink"], op=.55)

    # map top
    MPH = 258
    o += rect(sx, sy, sw, MPH, 0, "#E7EDF5")
    for i in range(6):
        o += line(sx, sy + 40 + i * 42, sx + sw, sy + 40 + i * 42, "#FFFFFF", 7, 1, "butt")
    for i in range(5):
        o += line(sx + 26 + i * 62, sy, sx + 26 + i * 62, sy + MPH, "#FFFFFF", 7, 1, "butt")
    o += rect(sx + 34, sy + 96, 52, 40, 5, "#DCEBDF")
    o += rect(sx + 176, sy + 158, 66, 46, 5, "#DCEBDF")
    o += path(f"M{sx} {sy + 214} C{sx + 70} {sy + 200} {sx + 130} {sy + 240} {sx + sw} {sy + 208}",
              stroke="#CFE0F5", sw=18, cap="butt")
    # route on phone
    prt = (f"M{sx + 54} {sy + 224} C{sx + 76} {sy + 186} {sx + 84} {sy + 168} {sx + 128} {sy + 150} "
           f"S{sx + 178} {sy + 128} {sx + 206} {sy + 86}")
    o += path(prt, stroke=AC, sw=10, op=.2)
    o += path(prt, stroke=AC, sw=4.2)
    o += circ(sx + 54, sy + 224, 6, "#FFFFFF", AC, 3)
    dx, dy = sx + 206, sy + 86
    o += path(f"M{dx} {dy + 5} C{dx - 13} {dy - 10} {dx - 10} {dy - 26} {dx} {dy - 26} "
              f"C{dx + 10} {dy - 26} {dx + 13} {dy - 10} {dx} {dy + 5} Z", fill=AC)
    o += circ(dx, dy - 15, 4.4, "#FFFFFF")
    # courier bubble
    bx2, by2 = sx + 132, sy + 152
    o += circ(bx2, by2, 17, AC, op=.16)
    o += circ(bx2, by2, 11.5, "#FFFFFF")
    o += circ(bx2, by2, 9, AC)
    o += path(f"M{bx2 - 3} {by2 - 3.4} L{bx2 + 3.4} {by2} L{bx2 - 3} {by2 + 3.4} Z", fill="#FFFFFF")
    # back button
    o += circ(sx + 30, sy + 66, 16, "#FFFFFF")
    o += path(f"M{sx + 33} {sy + 60} L{sx + 27} {sy + 66} L{sx + 33} {sy + 72}",
              stroke=L["ink"], sw=2)

    # bottom sheet
    BY = sy + MPH - 22
    o += rect(sx, BY, sw, sh - MPH + 22, 0, "#FFFFFF")
    o += path(f"M{sx} {BY + 24} Q{sx} {BY} {sx + 24} {BY} L{sx + sw - 24} {BY} "
              f"Q{sx + sw} {BY} {sx + sw} {BY + 24} L{sx + sw} {BY + 40} L{sx} {BY + 40} Z",
              fill="#FFFFFF")
    o += rect(sx + sw / 2 - 18, BY + 10, 36, 4, 2, "#D5DCE7")

    ty = BY + 46
    o += txt(sx + 24, ty, "Arriving in 12 min", 20, L["ink"], 800)
    o += txt(sx + 24, ty + 22, "Order #4821  ·  3 items  ·  EGP 240", 10, L["muted"], 500)

    # stepper
    sty = ty + 52
    labels = ["Placed", "Prepared", "On the way", "Delivered"]
    for i in range(4):
        px2 = sx + 34 + i * ((sw - 68) / 3)
        done = i <= 2
        if i < 3:
            nx = sx + 34 + (i + 1) * ((sw - 68) / 3)
            o += line(px2 + 10, sty, nx - 10, sty, AC if i <= 1 else "#E3E8F0", 3)
        o += circ(px2, sty, 9, AC if done else "#EDF1F7")
        if i <= 1:
            o += path(f"M{px2 - 3.4} {sty} L{px2 - 0.8} {sty + 2.8} L{px2 + 3.8} {sty - 3}",
                      stroke="#FFFFFF", sw=2)
        elif i == 2:
            o += circ(px2, sty, 3.4, "#FFFFFF")
        o += txt(px2, sty + 24, labels[i], 8, AC if done else L["muted"], 700, "middle")

    # courier card
    cy2 = sty + 42
    o += rect(sx + 20, cy2, sw - 40, 74, 16, "#F5F7FB")
    o += avatar(sx + 52, cy2 + 37, 21, "#FFB775", "#F0873A", uid + "c")
    o += txt(sx + 84, cy2 + 30, "Kareem  ·  Courier", 12, L["ink"], 700)
    o += stars(sx + 84, cy2 + 46, 5, 8.4, "#FFB020")
    o += txt(sx + 142, cy2 + 49, "4.9", 9.5, L["muted"], 700)
    for k, ix in enumerate([sw - 88, sw - 48]):
        o += circ(sx + ix, cy2 + 37, 17, "#FFFFFF")
        if k == 0:
            o += path(f"M{sx + ix - 6} {cy2 + 31} q0 -3 3 -3 l3 3 -2 3 q2 4 5 6 l3 -2 3 3 q0 3 -3 3 "
                      f"q-12 0 -12 -13 Z", fill=AC)
        else:
            o += rect(sx + ix - 7, cy2 + 30, 14, 10, 3, AC)
            o += path(f"M{sx + ix - 3} {cy2 + 40} l0 4 4 -4 Z", fill=AC)

    # order detail rows
    dyr = cy2 + 92
    o += line(sx + 20, dyr - 12, sx + sw - 20, dyr - 12, "#EDF1F7", 1)
    details = [("pin", "Delivery address", "14 Al Nasr St. · Apt 3, Floor 2"),
               ("bag", "Order", "2× Chicken bowl · 1× Iced latte")]
    for i, (ic, k, v) in enumerate(details):
        ry2 = dyr + i * 42
        o += rect(sx + 20, ry2, 32, 32, 10, "#FFF3E8")
        m = (sx + 36, ry2 + 16)
        if ic == "pin":
            o += path(f"M{m[0]} {m[1] + 7} C{m[0] - 8} {m[1] - 2} {m[0] - 6} {m[1] - 10} {m[0]} {m[1] - 10} "
                      f"C{m[0] + 6} {m[1] - 10} {m[0] + 8} {m[1] - 2} {m[0]} {m[1] + 7} Z", fill=AC)
            o += circ(m[0], m[1] - 4, 2.4, "#FFF3E8")
        elif ic == "bag":
            o += path(f"M{m[0] - 7} {m[1] - 3} L{m[0] + 7} {m[1] - 3} L{m[0] + 5.5} {m[1] + 8} "
                      f"L{m[0] - 5.5} {m[1] + 8} Z", fill=AC)
            o += path(f"M{m[0] - 3.6} {m[1] - 3} a3.6 4.6 0 0 1 7.2 0", stroke=AC, sw=1.8)
        else:
            o += rect(m[0] - 8, m[1] - 5, 16, 11, 2.5, AC)
            o += circ(m[0], m[1] + .5, 2.6, "#FFF3E8")
        o += txt(sx + 62, ry2 + 13, k, 9, L["muted"], 600, ls=.3)
        o += txt(sx + 62, ry2 + 27, v, 10.5, L["ink"], 600)

    # CTA anchored to the bottom of the screen
    by3 = sy + sh - 78
    o += rect(sx + 20, by3, sw - 40, 50, 15, f"url(#{uid}btn)")
    o += txt(sx + sw / 2, by3 + 31, "Track live", 13.5, "#22160A", 800, "middle")
    o += rect(sx + sw / 2 - 52, sy + sh - 16, 104, 4.5, 2.5, "#C9D2DF")
    o += tail

    o += caption("Delivery ecosystem", "DISPATCH CONSOLE  ·  CUSTOMER APP  ·  COURIER ROUTING", AC, 48, 700)
    return wrapsvg(o, defs)


if __name__ == "__main__":
    open("../assets/projects/delivery/showcase.svg", "w").write(build())
    print("ok")
