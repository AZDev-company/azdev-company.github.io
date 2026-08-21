from kit import *
import math

AC = "#39D98A"
AC2 = "#7BF0BC"
RED = "#FF6B6B"


def donut(cx, cy, r, tw, segs, uid):
    o = circ(cx, cy, r, "none", "#1B2536", tw)
    a0 = -math.pi / 2
    total = sum(v for v, _ in segs)
    for i, (v, c) in enumerate(segs):
        a1 = a0 + 2 * math.pi * v / total
        large = 1 if (a1 - a0) > math.pi else 0
        x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
        x1, y1 = cx + r * math.cos(a1 - .04), cy + r * math.sin(a1 - .04)
        o += path(f"M{x0:.2f} {y0:.2f} A{r} {r} 0 {large} 1 {x1:.2f} {y1:.2f}",
                  stroke=c, sw=tw, cap="round")
        a0 = a1
    return o


def build():
    uid = "fn"
    o = glow(uid + "1", AC, 640, 300, 440, ".16")
    o += glow(uid + "2", "#5B8CFF", 180, 420, 340, ".12")
    defs = (f'<linearGradient id="{uid}btn" x1="0" y1="0" x2="1" y2="0">'
            f'<stop stop-color="{AC}"/><stop offset="1" stop-color="#2FC9A0"/></linearGradient>'
            f'<linearGradient id="{uid}card" x1="0" y1="0" x2="1" y2="1">'
            f'<stop stop-color="#0F3B33"/><stop offset=".5" stop-color="#14795E"/>'
            f'<stop offset="1" stop-color="#2FD69B"/></linearGradient>'
            f'<linearGradient id="{uid}card2" x1="0" y1="0" x2="1" y2="1">'
            f'<stop stop-color="#1B2440"/><stop offset="1" stop-color="#38507F"/></linearGradient>'
            f'<linearGradient id="{uid}fill" x1="0" y1="0" x2="0" y2="1">'
            f'<stop stop-color="{AC}" stop-opacity=".34"/><stop offset="1" stop-color="{AC}" stop-opacity="0"/></linearGradient>')
    D = DARK

    # ================= ANALYTICS WINDOW =================
    WX, WY, WW, WH = 36, 116, 462, 474
    head, tail, cx, cy, cw, ch = window(WX, WY, WW, WH, uid, "wallet.azdev.app / insights", accent=AC)
    o += head
    o += txt(cx + 24, cy + 32, "Spending overview", 13.5, D["ink"], 800)
    o += pill(cx + cw - 106, cy + 18, 82, 22, "This month", "#182337", D["muted"], 9)

    # donut + legend
    dcx, dcy = cx + 92, cy + 128
    segs = [(42, AC), (24, "#5B8CFF"), (18, "#B08CFF"), (16, "#FFB454")]
    o += donut(dcx, dcy, 50, 15, segs, uid)
    o += txt(dcx, dcy - 2, "EGP", 8.5, D["muted"], 700, "middle", 1)
    o += txt(dcx, dcy + 17, "18,240", 17, D["ink"], 800, "middle")
    legend = [("Groceries", "42%", AC), ("Transport", "24%", "#5B8CFF"),
              ("Subscriptions", "18%", "#B08CFF"), ("Dining", "16%", "#FFB454")]
    for i, (n, p, c) in enumerate(legend):
        ly = cy + 82 + i * 32
        o += circ(cx + 186, ly, 4.5, c)
        o += txt(cx + 200, ly + 4, n, 10.5, D["ink"], 600)
        o += txt(cx + cw - 24, ly + 4, p, 10.5, D["muted"], 700, "end")

    # monthly bars
    by = cy + 214
    o += line(cx + 24, by - 12, cx + cw - 24, by - 12, D["line"], 1)
    o += txt(cx + 24, by + 12, "Monthly net flow", 11.5, D["ink"], 700)
    o += txt(cx + cw - 24, by + 12, "+18.4%", 11, AC, 800, "end")
    vals = [46, 58, 41, 70, 63, 94]
    BW2 = cw - 48
    o += bars(cx + 24, by + 28, BW2, 76, vals, "#1F2C42", hi=5, hi_fill=AC)
    _bw = BW2 / (6 + 5 * 0.34)
    for i, m in enumerate(["Apr", "May", "Jun", "Jul", "Aug", "Sep"]):
        o += txt(cx + 24 + i * _bw * 1.34 + _bw / 2, by + 120, m, 8.5, D["muted"], 600, "middle")

    # sparkline balance
    sy2 = by + 130
    o += rect(cx + 24, sy2, cw - 48, 84, 12, "#101827")
    o += rect(cx + 24, sy2, cw - 48, 84, 12, "none", D["line"], 1)
    o += txt(cx + 40, sy2 + 24, "Balance trend", 10, D["muted"], 600)
    o += txt(cx + 40, sy2 + 46, "EGP 128,450", 16, D["ink"], 800)
    sp, _ = sparkline(cx + 40, sy2 + 50, cw - 88, 26, [30, 38, 33, 48, 44, 60, 55, 72, 80],
                      AC, 2.6, f"{uid}fill")
    o += sp
    o += tail

    # ================= WALLET PHONE =================
    PHX, PHY, PHW, PHH = 528, 40, 344, 684
    head, tail, sx, sy, sw, sh = phone(PHX, PHY, PHW, PHH, uid, "#080D16")
    o += head
    o += txt(sx + 26, sy + 34, "9:41", 11, "#E7EEF9", 700)
    o += rect(sx + sw - 52, sy + 26, 20, 9, 2, "#E7EEF9", op=.85)
    o += rect(sx + sw - 78, sy + 26, 16, 9, 2, "#E7EEF9", op=.5)

    # header
    hy = sy + 74
    o += avatar(sx + 42, hy + 4, 19, "#4FE3A8", "#1E8F6C", uid + "a")
    o += txt(sx + 72, hy, "Good evening", 9.5, "#7E8CA6", 600)
    o += txt(sx + 72, hy + 17, "Nour A.", 13, "#EDF2FA", 800)
    o += circ(sx + sw - 44, hy + 2, 17, "#141C2B")
    o += path(f"M{sx + sw - 50} {hy + 6} a6 6 0 0 1 12 0 v3 h-12 Z", fill="#8FA0BC")
    o += circ(sx + sw - 37, hy - 6, 4, AC)

    # balance
    byy = sy + 138
    o += txt(sx + 26, byy, "TOTAL BALANCE", 8.5, "#7E8CA6", 800, ls=1.6)
    o += txt(sx + 26, byy + 32, "EGP 128,450", 29, "#FFFFFF", 800)
    o += txt(sx + 234, byy + 32, ".20", 15, "#7E8CA6", 700)
    o += pill(sx + 26, byy + 44, 96, 22, "▲  +8.4% MTD", "#12331F", AC, 8.5)

    # card
    cyy = byy + 82
    o += rect(sx + 40, cyy - 8, sw - 80, 26, 12, f"url(#{uid}card2)", op=.7)
    o += (f'<defs><clipPath id="{uid}pc"><rect x="{sx + 26}" y="{cyy}" width="{sw - 52}" height="138" rx="18"/></clipPath></defs>')
    o += rect(sx + 26, cyy, sw - 52, 138, 18, f"url(#{uid}card)")
    o += (f'<g clip-path="url(#{uid}pc)">' + circ(sx + sw - 56, cyy + 46, 62, "#FFFFFF", op=.07)
          + circ(sx + sw - 96, cyy + 118, 44, "#FFFFFF", op=.05) + '</g>')
    o += txt(sx + 48, cyy + 32, "AZ PAY", 10.5, "#CFF7E6", 800, ls=1.8)
    o += rect(sx + 48, cyy + 48, 34, 25, 5, "#F5D585")
    o += line(sx + 48, cyy + 60, sx + 82, cyy + 60, "#C9A85C", 1.4)
    o += line(sx + 65, cyy + 48, sx + 65, cyy + 73, "#C9A85C", 1.4)
    o += txt(sx + 48, cyy + 98, "••••    ••••    ••••    4821", 15, "#FFFFFF", 700, ls=.8)
    o += txt(sx + 48, cyy + 122, "NOUR ABDELAZIZ", 9, "#BFEFDA", 700, ls=1.2)
    o += txt(sx + sw - 48, cyy + 122, "09/29", 9, "#BFEFDA", 700, "end", 1.2)
    o += txt(sx + sw - 48, cyy + 36, "VISA", 13, "#FFFFFF", 800, "end", 1.4)

    # quick actions
    ay = cyy + 166
    acts = [("Send", "send"), ("Request", "req"), ("Top up", "top"), ("Bills", "bill")]
    for i, (n, k) in enumerate(acts):
        ax = sx + 40 + i * ((sw - 80) / 3)
        o += circ(ax, ay, 22, "#121B29")
        o += circ(ax, ay, 22, "none", "#1E293C", 1)
        if k == "send":
            o += path(f"M{ax - 7} {ay + 6} L{ax + 7} {ay - 7} M{ax + 7} {ay - 7} L{ax + 1} {ay - 7} "
                      f"M{ax + 7} {ay - 7} L{ax + 7} {ay - 1}", stroke=AC, sw=2)
        elif k == "req":
            o += path(f"M{ax + 7} {ay - 6} L{ax - 7} {ay + 7} M{ax - 7} {ay + 7} L{ax - 1} {ay + 7} "
                      f"M{ax - 7} {ay + 7} L{ax - 7} {ay + 1}", stroke=AC, sw=2)
        elif k == "top":
            o += path(f"M{ax} {ay - 7} V{ay + 7} M{ax - 7} {ay} H{ax + 7}", stroke=AC, sw=2)
        else:
            o += rect(ax - 6, ay - 7.5, 12, 15, 2, "none", AC, 1.8)
            o += line(ax - 3, ay - 3, ax + 3, ay - 3, AC, 1.6)
            o += line(ax - 3, ay + 1, ax + 3, ay + 1, AC, 1.6)
        o += txt(ax, ay + 36, n, 9, "#8FA0BC", 600, "middle")

    # activity
    ly = ay + 58
    o += txt(sx + 26, ly, "Recent activity", 12, "#EDF2FA", 700)
    o += txt(sx + sw - 26, ly, "See all", 9.5, AC, 700, "end")
    tx = [("Carrefour", "Groceries · Today", "− 640.00", "#FF9F4D", "#FF6B6B"),
          ("Salary", "Deposit · 1 Feb", "+ 24,000.00", "#39D98A", "#2FC9A0"),
          ("Uber", "Transport · 31 Jan", "− 118.50", "#7EA0FF", "#5B8CFF")]
    for i, (n, m, amt, c1, c2) in enumerate(tx):
        ry = ly + 16 + i * 47
        o += rect(sx + 26, ry, 36, 36, 11, "#131C2B")
        o += circ(sx + 44, ry + 18, 9, c1, op=.9)
        o += txt(sx + 72, ry + 15, n, 11, "#EDF2FA", 700)
        o += txt(sx + 72, ry + 30, m, 9, "#7E8CA6", 500)
        o += txt(sx + sw - 26, ry + 22, amt, 11, AC if amt[0] == "+" else "#E2E8F4", 700, "end")

    # tab bar
    tby = sy + sh - 62
    o += rect(sx, tby, sw, 62, 0, "#0B121D")
    o += line(sx, tby, sx + sw, tby, "#18202F", 1)
    for i in range(4):
        tx2 = sx + 46 + i * ((sw - 92) / 3)
        c = AC if i == 0 else "#3C4A61"
        o += rect(tx2 - 8, tby + 20, 16, 4, 2, c)
        o += rect(tx2 - 8, tby + 27, 16, 4, 2, c, op=.6)
        o += rect(tx2 - 5, tby + 34, 10, 4, 2, c, op=.35)
    o += rect(sx + sw / 2 - 52, sy + sh - 14, 104, 4.5, 2.5, "#25314A")
    o += tail

    # ================= RIGHT CARDS =================
    RX, RW2 = 906, 262
    # virtual card
    o += rect(RX - 4, 154, RW2 + 8, 158, 20, "#000", op=.4)
    o += (f'<defs><clipPath id="{uid}vc"><rect x="{RX}" y="142" width="{RW2}" height="158" rx="18"/></clipPath></defs>')
    o += rect(RX, 142, RW2, 158, 18, f"url(#{uid}card2)")
    o += f'<g clip-path="url(#{uid}vc)">' + circ(RX + RW2 - 40, 180, 60, "#FFFFFF", op=.06) + '</g>' 
    o += pill(RX + 20, 162, 78, 20, "VIRTUAL", "#FFFFFF1F", "#CBD8EE", 8, 800, 1.2)
    o += txt(RX + 20, 238, "••••  ••••  ••••  9034", 13, "#FFFFFF", 700, ls=.6)
    o += txt(RX + 20, 268, "FROZEN", 9, "#8FA0BC", 800, ls=1.4)
    o += rect(RX + RW2 - 74, 254, 54, 22, 11, "#2C3A57")
    o += circ(RX + RW2 - 60, 265, 8, "#8FA0BC")

    # security card
    o += rect(RX, 330, RW2, 128, 16, "#0F1726")
    o += rect(RX, 330, RW2, 128, 16, "none", "#243149", 1.4)
    o += circ(RX + 42, 372, 18, "#12331F")
    o += path(f"M{RX + 42} {372 - 9} l9 4 v6 c0 6 -4 9 -9 11 c-5 -2 -9 -5 -9 -11 v-6 Z", fill=AC)
    o += txt(RX + 72, 368, "3-D Secure", 12, D["ink"], 700)
    o += txt(RX + 72, 383, "Every payment verified", 9.5, D["muted"], 500)
    o += line(RX + 20, 400, RX + RW2 - 20, 400, D["line"], 1)
    o += txt(RX + 20, 424, "Limits used", 9.5, D["muted"], 600)
    o += txt(RX + RW2 - 20, 424, "62%", 9.5, D["ink"], 700, "end")
    o += rect(RX + 20, 432, RW2 - 40, 7, 3.5, "#1B2536")
    o += rect(RX + 20, 432, (RW2 - 40) * .62, 7, 3.5, AC)

    # transfer card
    o += rect(RX, 488, RW2, 156, 16, "#0F1726")
    o += rect(RX, 488, RW2, 156, 16, "none", "#243149", 1.4)
    o += txt(RX + 20, 516, "Send again", 12, D["ink"], 700)
    for i, (n, c1, c2) in enumerate([("Mona", "#FFB775", "#F0873A"),
                                     ("Tarek", "#8FB6FF", "#4C7BE8"),
                                     ("Rana", "#9CE7C8", "#33B387")]):
        ax2 = RX + 46 + i * 62
        o += avatar(ax2, 560, 20, c1, c2, uid + "s" + str(i))
        o += txt(ax2, 596, n, 9, D["muted"], 600, "middle")
    o += rect(RX + 20, 608, RW2 - 40, 20, 10, "#182337")
    o += txt(RX + RW2 / 2, 622, "Instant · 0 fees", 9, AC, 700, "middle")

    o += txt(40, 46, "SPEND INSIGHTS  ·  WALLET  ·  CARD CONTROLS", 10, "#7C86A6", 700, ls=1.8)
    return wrapsvg(o, defs)


if __name__ == "__main__":
    open("../assets/projects/fintech/showcase.svg", "w").write(build())
    print("ok")
