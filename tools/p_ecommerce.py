from kit import *

AC = "#8B7CFF"
AC2 = "#B4A6FF"
INK = "#0E1622"


def headphones(cx, cy, s, c1, c2, uid):
    """Stylised over-ear headphones — reads instantly as a real product."""
    d = f'<linearGradient id="hp{uid}" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>'
    o = f"<defs>{d}</defs>"
    o += path(f"M{cx - s * .74} {cy + s * .12} A{s * .76} {s * .82} 0 0 1 {cx + s * .74} {cy + s * .12}",
              stroke=f"url(#hp{uid})", sw=s * .19, cap="round")
    o += path(f"M{cx - s * .70} {cy + s * .06} A{s * .70} {s * .76} 0 0 1 {cx + s * .70} {cy + s * .06}",
              stroke="#FFFFFF", sw=s * .05, op=.22, cap="round")
    for sgn in (-1, 1):
        ex = cx + sgn * s * .74
        o += rect(ex - s * .21, cy + s * .04, s * .42, s * .62, s * .17, f"url(#hp{uid})")
        o += rect(ex - s * .13, cy + s * .13, s * .26, s * .44, s * .12, "#0E1622", op=.55)
        o += rect(ex - s * .07, cy + s * .19, s * .14, s * .3, s * .07, "#FFFFFF", op=.10)
    return o


def prod_glyph(kind, cx, cy, s, c1, c2, uid):
    o = f'<defs><linearGradient id="pg{uid}" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs>'
    if kind == "watch":
        o += rect(cx - s * .16, cy - s * .62, s * .32, s * .32, s * .1, c1, op=.55)
        o += rect(cx - s * .16, cy + s * .3, s * .32, s * .32, s * .1, c1, op=.55)
        o += rect(cx - s * .34, cy - s * .38, s * .68, s * .76, s * .22, f"url(#pg{uid})")
        o += rect(cx - s * .24, cy - s * .28, s * .48, s * .56, s * .15, "#0E1622", op=.5)
        o += line(cx, cy, cx, cy - s * .16, "#FFFFFF", 2.4)
        o += line(cx, cy, cx + s * .12, cy + s * .04, "#FFFFFF", 2.4)
    elif kind == "sneaker":
        o += path(f"M{cx - s * .62} {cy + s * .3} L{cx - s * .58} {cy - s * .02} "
                  f"Q{cx - s * .3} {cy - s * .1} {cx - s * .1} {cy - s * .3} "
                  f"Q{cx + s * .1} {cy - s * .46} {cx + s * .26} {cy - s * .2} "
                  f"Q{cx + s * .38} {cy} {cx + s * .62} {cy + s * .1} "
                  f"L{cx + s * .62} {cy + s * .3} Z", fill=f"url(#pg{uid})")
        o += rect(cx - s * .64, cy + s * .26, s * 1.28, s * .13, s * .06, "#FFFFFF", op=.85)
        for i in range(3):
            o += line(cx - s * .18 + i * s * .13, cy - s * .12 - i * s * .04,
                      cx - s * .04 + i * s * .13, cy - s * .02 - i * s * .04, "#FFFFFF", 2.2, .8)
    elif kind == "bag":
        o += path(f"M{cx - s * .48} {cy - s * .22} L{cx + s * .48} {cy - s * .22} "
                  f"L{cx + s * .38} {cy + s * .52} L{cx - s * .38} {cy + s * .52} Z", fill=f"url(#pg{uid})")
        o += path(f"M{cx - s * .24} {cy - s * .22} a{s * .24} {s * .3} 0 0 1 {s * .48} 0",
                  stroke=f"url(#pg{uid})", sw=s * .09)
        o += rect(cx - s * .1, cy + s * .04, s * .2, s * .12, s * .04, "#FFFFFF", op=.6)
    elif kind == "cam":
        o += rect(cx - s * .54, cy - s * .3, s * 1.08, s * .74, s * .14, f"url(#pg{uid})")
        o += rect(cx - s * .2, cy - s * .44, s * .3, s * .16, s * .05, f"url(#pg{uid})")
        o += circ(cx + s * .06, cy + s * .06, s * .24, "#0E1622", op=.55)
        o += circ(cx + s * .06, cy + s * .06, s * .14, "#FFFFFF", op=.28)
        o += circ(cx - s * .34, cy - s * .14, s * .05, "#FFFFFF", op=.7)
    else:  # speaker
        o += rect(cx - s * .34, cy - s * .52, s * .68, s * 1.04, s * .3, f"url(#pg{uid})")
        o += circ(cx, cy - s * .18, s * .17, "#0E1622", op=.5)
        o += circ(cx, cy + s * .24, s * .1, "#0E1622", op=.5)
    return o


def build():
    uid = "ec"
    o = glow(uid + "1", AC, 240, 330, 400, ".17")
    o += glow(uid + "2", "#4DD6FF", 900, 250, 380, ".10")
    defs = (f'<linearGradient id="{uid}btn" x1="0" y1="0" x2="1" y2="0">'
            f'<stop stop-color="{AC}"/><stop offset="1" stop-color="#6F5CFF"/></linearGradient>'
            f'<linearGradient id="{uid}hero" x1="0" y1="0" x2="1" y2="1">'
            f'<stop stop-color="#241E52"/><stop offset="1" stop-color="#3A2E7A"/></linearGradient>'
            f'<linearGradient id="{uid}pimg" x1="0" y1="0" x2="1" y2="1">'
            f'<stop stop-color="#F0EDFF"/><stop offset="1" stop-color="#E2DCFF"/></linearGradient>')

    # ================= PHONE — product detail =================
    PHX, PHY, PHW, PHH = 62, 58, 336, 662
    head, tail, sx, sy, sw, sh = phone(PHX, PHY, PHW, PHH, uid, "#FFFFFF")
    o += head
    L = LIGHT
    o += txt(sx + 24, sy + 32, "9:41", 11, L["ink"], 700)
    o += rect(sx + sw - 50, sy + 24, 20, 9, 2, L["ink"], op=.85)
    o += rect(sx + sw - 76, sy + 24, 16, 9, 2, L["ink"], op=.55)

    # product image panel
    IH = 290
    o += rect(sx, sy + 44, sw, IH, 0, f"url(#{uid}pimg)")
    o += circ(sx + sw / 2, sy + 44 + IH / 2 + 6, 104, "#FFFFFF", op=.55)
    o += headphones(sx + sw / 2, sy + 44 + IH / 2, 118, "#5B4BD8", "#9C8CFF", uid)
    # header controls
    o += circ(sx + 32, sy + 74, 17, "#FFFFFF", op=.9)
    o += path(f"M{sx + 35} {sy + 68} L{sx + 29} {sy + 74} L{sx + 35} {sy + 80}", stroke=L["ink"], sw=2)
    o += circ(sx + sw - 32, sy + 74, 17, "#FFFFFF", op=.9)
    hx, hy = sx + sw - 32, sy + 74
    o += path(f"M{hx} {hy + 5.5} C{hx - 9} {hy - 1} {hx - 7} {hy - 8} {hx - 3} {hy - 8} "
              f"C{hx - 1} {hy - 8} {hx} {hy - 6.5} {hx} {hy - 5.5} "
              f"C{hx} {hy - 6.5} {hx + 1} {hy - 8} {hx + 3} {hy - 8} "
              f"C{hx + 7} {hy - 8} {hx + 9} {hy - 1} {hx} {hy + 5.5} Z", fill="#FF5A7A")
    # dots
    for i in range(4):
        o += circ(sx + sw / 2 - 21 + i * 14, sy + 44 + IH - 22, 3.4 if i else 4,
                  AC if i == 0 else "#C7BEEC")

    # info
    iy = sy + 44 + IH + 30
    o += txt(sx + 24, iy, "AZ AUDIO", 8.5, AC, 800, ls=1.6)
    o += txt(sx + 24, iy + 24, "Studio Pro Wireless", 20, L["ink"], 800)
    o += stars(sx + 24, iy + 44, 5, 10, "#FFB020")
    o += txt(sx + 92, iy + 47.5, "4.8", 10, L["ink"], 700)
    o += txt(sx + 112, iy + 47.5, "· 212 reviews", 10, L["muted"], 500)
    o += txt(sx + 24, iy + 78, "EGP 4,290", 24, L["ink"], 800)
    o += txt(sx + 176, iy + 78, "5,100", 12, L["muted"], 600)
    o += line(sx + 174, iy + 74, sx + 213, iy + 74, L["muted"], 1.4)
    o += pill(sx + 228, iy + 60, 60, 22, "−16%", "#E9FBF2", "#12A56B", 9.5)

    # colour swatches
    cyy = iy + 106
    o += txt(sx + 24, cyy, "Colour", 10, L["muted"], 600)
    for i, c in enumerate(["#5B4BD8", "#111827", "#E9E4FF"]):
        cx2 = sx + 82 + i * 34
        if i == 0:
            o += circ(cx2, cyy - 4, 14, "none", AC, 1.8)
        o += circ(cx2, cyy - 4, 9.5, c, "#FFFFFF" if c == "#E9E4FF" else None, 1)
    o += pill(sx + sw - 100, cyy - 17, 76, 24, "In stock", "#E9FBF2", "#12A56B", 9)

    # delivery note
    o += rect(sx + 20, cyy + 20, sw - 40, 44, 12, "#F5F4FF")
    o += circ(sx + 44, cyy + 42, 12, "#FFFFFF")
    o += rect(sx + 38, cyy + 38, 12, 8, 2, AC)
    o += txt(sx + 66, cyy + 38, "Free delivery", 10.5, L["ink"], 700)
    o += txt(sx + 66, cyy + 52, "Arrives Tue, 24 Feb", 9, L["muted"], 500)

    # add to cart
    by = sy + sh - 80
    o += rect(sx + 20, by, 52, 52, 15, "#F1EFFF")
    kx2, ky2 = sx + 46, by + 26
    o += path(f"M{kx2 - 9} {ky2 - 7} h4 l2.6 13 h11.4", stroke=AC, sw=2)
    o += path(f"M{kx2 - 3} {ky2 - 4} h13 l-1.8 7.6 h-10", stroke=AC, sw=2)
    o += circ(kx2 - 2, ky2 + 9, 2, AC) + circ(kx2 + 7, ky2 + 9, 2, AC)
    o += rect(sx + 82, by, sw - 102, 52, 15, f"url(#{uid}btn)")
    o += txt(sx + 82 + (sw - 102) / 2, by + 32, "Add to cart", 13.5, "#FFFFFF", 800, "middle")
    o += rect(sx + sw / 2 - 52, sy + sh - 16, 104, 4.5, 2.5, "#C9D2DF")
    o += tail

    # ================= STOREFRONT WINDOW =================
    WX, WY, WW, WH = 434, 96, 714, 452
    head, tail, cx, cy, cw, ch = window(WX, WY, WW, WH, uid, "shop.azdev.app / new-arrivals", accent=AC)
    o += head
    D = DARK
    # site nav
    o += rect(cx, cy, cw, 46, 0, "#0E1522")
    o += line(cx, cy + 46, cx + cw, cy + 46, D["line"], 1)
    o += rect(cx + 24, cy + 15, 16, 16, 5, f"url(#{uid}btn)")
    o += txt(cx + 46, cy + 28, "AZ Store", 12, D["ink"], 800)
    for i, m in enumerate(["New", "Audio", "Wearables", "Sale"]):
        o += txt(cx + 128 + i * 66, cy + 28, m, 10, AC if i == 0 else D["muted"], 700 if i == 0 else 500)
    o += rect(cx + cw - 214, cy + 12, 120, 22, 11, "#182337")
    o += circ(cx + cw - 200, cy + 23, 3.6, "none", "#4B5B76", 1.5)
    o += txt(cx + cw - 190, cy + 26.5, "Search", 8.5, "#4B5B76", 500)
    o += circ(cx + cw - 58, cy + 23, 12, "#182337")
    kx, ky = cx + cw - 58, cy + 23
    o += path(f"M{kx - 7} {ky - 5.5} h3 l1.9 9.5 h8.4", stroke=D["ink"], sw=1.5)
    o += path(f"M{kx - 2.4} {ky - 3} h9.6 l-1.3 5.6 h-7.4", stroke=D["ink"], sw=1.5)
    o += circ(kx - 1.4, ky + 6.4, 1.4, D["ink"]) + circ(kx + 5, ky + 6.4, 1.4, D["ink"])
    o += circ(cx + cw - 34, cy + 17, 8, AC)
    o += txt(cx + cw - 34, cy + 20.5, "3", 8.5, "#FFFFFF", 800, "middle")

    # hero band
    HY = cy + 62
    o += rect(cx + 22, HY, cw - 44, 138, 16, f"url(#{uid}hero)")
    o += circ(cx + cw - 150, HY + 70, 78, "#FFFFFF", op=.06)
    o += pill(cx + 46, HY + 24, 90, 20, "NEW SEASON", "#FFFFFF22", "#D6CEFF", 8, 800, 1.2)
    o += txt(cx + 46, HY + 74, "Sound, redesigned.", 26, "#FFFFFF", 800)
    o += txt(cx + 46, HY + 96, "Up to 30% off the Studio range this week.", 11, "#BBB2E8", 500)
    o += rect(cx + 46, HY + 108, 108, 30, 9, "#FFFFFF")
    o += txt(cx + 100, HY + 128, "Shop now", 10.5, "#2B2160", 800, "middle")
    o += headphones(cx + cw - 152, HY + 66, 76, "#8C7BFF", "#D6CEFF", uid + "h")

    # grid header
    GY = HY + 158
    o += txt(cx + 24, GY, "Trending now", 13, D["ink"], 700)
    o += txt(cx + cw - 24, GY, "View all →", 10, AC, 700, "end")

    cards = [("sneaker", "Runner Lite", "EGP 2,150", 5, "#5B4BD8", "#9C8CFF"),
             ("watch", "Pulse Watch 2", "EGP 3,600", 4, "#2B7FFF", "#7FB4FF"),
             ("cam", "Field Cam M1", "EGP 8,900", 5, "#00A98F", "#5FE0C6"),
             ("bag", "Daily Tote", "EGP 980", 4, "#FF7A4D", "#FFB08C")]
    CW2 = (cw - 48 - 3 * 16) / 4
    for i, (k, name, price, rt, c1, c2) in enumerate(cards):
        px = cx + 24 + i * (CW2 + 16)
        py = GY + 16
        o += rect(px, py, CW2, 138, 12, "#101827")
        o += rect(px, py, CW2, 138, 12, "none", D["line"], 1)
        o += rect(px + 1, py + 1, CW2 - 2, 82, 11, "#161F30")
        o += prod_glyph(k, px + CW2 / 2, py + 42, 52, c1, c2, uid + str(i))
        o += txt(px + 12, py + 102, name, 10, D["ink"], 700)
        o += txt(px + 12, py + 122, price, 11, AC, 800)
        o += stars(px + CW2 - 44, py + 118, rt, 6.4, "#FFB020", "#2A3550")
        if i == 2:
            o += pill(px + CW2 - 46, py + 9, 38, 17, "NEW", AC, "#FFFFFF", 7.5)
    o += tail

    # ---- floating cart / checkout card ----
    FX, FY, FW, FH = 700, 526, 430, 188
    o += rect(FX - 4, FY + 12, FW + 8, FH, 20, "#000000", op=.42)
    o += rect(FX, FY, FW, FH, 18, "#0F1726")
    o += rect(FX, FY, FW, FH, 18, "none", "#243149", 1.4)
    o += txt(FX + 24, FY + 32, "Your cart", 13, D["ink"], 800)
    o += pill(FX + 92, FY + 20, 40, 17, "3", "#1B2537", D["muted"], 8.5)
    o += txt(FX + FW - 24, FY + 32, "Secure checkout", 9.5, "#3BD59A", 700, "end")
    litems = [("Studio Pro Wireless", "Midnight · 1", "EGP 4,290", "#5B4BD8", "#9C8CFF", "speaker"),
              ("Runner Lite", "Size 42 · 1", "EGP 2,150", "#2B7FFF", "#7FB4FF", "sneaker")]
    for i, (n, v, pr, c1, c2, k) in enumerate(litems):
        ly = FY + 48 + i * 48
        o += rect(FX + 22, ly, 38, 38, 10, "#182337")
        o += prod_glyph(k, FX + 41, ly + 19, 24, c1, c2, uid + "f" + str(i))
        o += txt(FX + 70, ly + 16, n, 10.5, D["ink"], 700)
        o += txt(FX + 70, ly + 30, v, 9, D["muted"], 500)
        o += txt(FX + FW - 24, ly + 24, pr, 10.5, D["ink"], 700, "end")
    o += line(FX + 22, FY + 148, FX + FW - 22, FY + 148, D["line"], 1)
    o += txt(FX + 22, FY + 172, "Total", 10, D["muted"], 600)
    o += txt(FX + 62, FY + 173, "EGP 6,440", 14, D["ink"], 800)
    o += rect(FX + FW - 154, FY + 155, 132, 32, 10, f"url(#{uid}btn)")
    o += txt(FX + FW - 88, FY + 175.5, "Checkout →", 11, "#FFFFFF", 800, "middle")

    # small label
    o += txt(438, 720, "STOREFRONT  ·  PRODUCT DETAIL  ·  MERCHANDISING", 10, "#7C86A6", 700, ls=1.8)
    return wrapsvg(o, defs)


if __name__ == "__main__":
    open("../assets/projects/ecommerce/showcase.svg", "w").write(build())
    print("ok")
