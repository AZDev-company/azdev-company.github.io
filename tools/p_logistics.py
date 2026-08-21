from kit import *
import random

AC = "#5B8CFF"
AC2 = "#8FB4FF"
D = DARK


def fleet_map(x, y, w, h, uid):
    o = rect(x, y, w, h, 10, "#0A1220")
    o += f'<defs><clipPath id="{uid}fm"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10"/></clipPath></defs>'
    o += f'<g clip-path="url(#{uid}fm)">'
    random.seed(11)
    for i in range(9):
        bx = x + 10 + (i % 5) * (w / 5)
        byy = y + 12 + (i // 5) * (h / 2.2)
        o += rect(bx, byy, w / 5 - 24, h / 2.2 - 30, 5, "#101A2A")
    for i in range(1, 5):
        o += line(x + w * i / 5, y, x + w * i / 5, y + h, "#182437", 2.6, 1, "butt")
    for i in range(1, 3):
        o += line(x, y + h * i / 3, x + w, y + h * i / 3, "#182437", 2.6, 1, "butt")
    # highway
    o += path(f"M{x} {y + h * .82} C{x + w * .24} {y + h * .70} {x + w * .34} {y + h * .34} "
              f"{x + w * .56} {y + h * .32} S{x + w * .84} {y + h * .48} {x + w} {y + h * .22}",
              stroke="#22314B", sw=9, cap="butt")
    # geofence
    o += circ(x + w * .62, y + h * .40, 74, AC, op=.06)
    o += circ(x + w * .62, y + h * .40, 74, "none", AC, 1.4, .35)
    o += path(f"", stroke=None)
    # active route
    rt = (f"M{x + w * .12} {y + h * .76} C{x + w * .26} {y + h * .60} {x + w * .30} {y + h * .44} "
          f"{x + w * .48} {y + h * .38} S{x + w * .70} {y + h * .40} {x + w * .82} {y + h * .20}")
    o += path(rt, stroke=AC, sw=9, op=.16)
    o += path(rt, stroke=AC, sw=3.2)
    o += path(rt, stroke="#FFFFFF", sw=1.4, op=.4, dash="1 8")
    # vehicles
    veh = [(.12, .76, AC), (.34, .50, AC), (.48, .38, "#3BD59A"), (.66, .40, AC),
           (.82, .20, "#FFB454"), (.24, .28, "#3BD59A"), (.72, .70, "#FF6B6B"), (.90, .60, AC)]
    for fx, fy, c in veh:
        vx, vy = x + w * fx, y + h * fy
        o += circ(vx, vy, 13, c, op=.14)
        o += rect(vx - 7, vy - 5, 14, 10, 3, c)
        o += rect(vx - 2, vy - 8, 9, 6, 2, c, op=.75)
    o += "</g>"
    return o


def build():
    uid = "lg"
    o = glow(uid + "1", AC, 460, 320, 470, ".16")
    o += glow(uid + "2", "#39D98A", 980, 500, 330, ".10")
    defs = (f'<linearGradient id="{uid}btn" x1="0" y1="0" x2="1" y2="0">'
            f'<stop stop-color="{AC}"/><stop offset="1" stop-color="#4A6FE8"/></linearGradient>'
            f'<linearGradient id="{uid}fill" x1="0" y1="0" x2="0" y2="1">'
            f'<stop stop-color="{AC}" stop-opacity=".32"/><stop offset="1" stop-color="{AC}" stop-opacity="0"/></linearGradient>')

    # ================= OPS DASHBOARD =================
    WX, WY, WW, WH = 36, 46, 880, 616
    head, tail, cx, cy, cw, ch = window(WX, WY, WW, WH, uid, "fleet.azdev.app / operations", accent=AC)
    o += head

    # toolbar
    o += rect(cx, cy, cw, 54, 0, "#0E1522")
    o += line(cx, cy + 54, cx + cw, cy + 54, D["line"], 1)
    o += txt(cx + 24, cy + 33, "Fleet operations", 14, D["ink"], 800)
    o += pill(cx + 168, cy + 18, 92, 22, "Eastern region", "#182337", D["muted"], 9)
    o += pill(cx + 270, cy + 18, 76, 22, "Live · 24h", "#132A22", "#3BD59A", 9)
    o += rect(cx + cw - 232, cy + 15, 118, 26, 8, "#182337")
    o += circ(cx + cw - 216, cy + 28, 3.6, "none", "#4B5B76", 1.5)
    o += txt(cx + cw - 206, cy + 31.5, "Search vehicle", 9, "#4B5B76", 500)
    o += rect(cx + cw - 104, cy + 15, 80, 26, 8, f"url(#{uid}btn)")
    o += txt(cx + cw - 64, cy + 32, "Dispatch", 9.5, "#FFFFFF", 800, "middle")

    # KPI row
    kpis = [("Active vehicles", "128", "+6 today", AC, [40, 46, 42, 55, 60, 58, 68]),
            ("On route", "94", "73% of fleet", "#3BD59A", [30, 44, 38, 52, 48, 62, 66]),
            ("Delayed", "6", "−2 vs yesterday", "#FFB454", [60, 52, 55, 40, 36, 30, 24]),
            ("Delivered today", "1,204", "+18.4%", "#B08CFF", [20, 34, 40, 48, 56, 70, 88])]
    KW = (cw - 48 - 3 * 14) / 4
    for i, (k, v, sub, c, sp) in enumerate(kpis):
        kx = cx + 24 + i * (KW + 14)
        ky = cy + 70
        o += rect(kx, ky, KW, 90, 13, "#101827")
        o += rect(kx, ky, KW, 90, 13, "none", D["line"], 1)
        o += txt(kx + 16, ky + 24, k, 9.5, D["muted"], 600)
        o += txt(kx + 16, ky + 54, v, 24, D["ink"], 800)
        o += txt(kx + 16, ky + 74, sub, 8.5, c, 700)
        s2, _ = sparkline(kx + KW - 84, ky + 44, 66, 28, sp, c, 2.2)
        o += s2

    # map + vehicle list
    MY = cy + 178
    MH = 246
    o += fleet_map(cx + 24, MY, 520, MH, uid)
    o += rect(cx + 40, MY + 16, 158, 46, 10, "#0C1524", op=.95)
    o += rect(cx + 40, MY + 16, 158, 46, 10, "none", "#22314B", 1)
    o += circ(cx + 56, MY + 32, 3.4, "#3BD59A")
    o += txt(cx + 66, MY + 35.5, "LIVE TELEMETRY", 8, "#3BD59A", 800, ls=1.2)
    o += txt(cx + 52, MY + 55, "Updated 3s ago  ·  128 units", 8.5, D["muted"], 600)
    for i, (lb, c) in enumerate([("On route", AC), ("Idle", "#3BD59A"), ("Delayed", "#FF6B6B")]):
        lx = cx + 40 + i * 84
        o += circ(lx + 6, MY + MH - 22, 4, c)
        o += txt(lx + 16, MY + MH - 18.5, lb, 8.5, "#93A2BB", 600)

    LX = cx + 560
    LW = cw - 560 - 24
    o += rect(LX, MY, LW, MH, 10, "#0E1522")
    o += txt(LX + 16, MY + 24, "Live vehicles", 11.5, D["ink"], 700)
    o += txt(LX + LW - 16, MY + 24, "Sort: ETA", 9, D["muted"], 600, "end")
    vehicles = [("TRK-1042", "Route 12 · Dammam", "On route", AC, "24 min"),
                ("VAN-0871", "Route 04 · Jubail", "Loading", "#3BD59A", "—"),
                ("TRK-1188", "Route 19 · Qatif", "Delayed", "#FF6B6B", "+16 min"),
                ("VAN-0932", "Route 07 · Khobar", "On route", AC, "38 min"),
                ("TRK-1301", "Route 22 · Dhahran", "On route", AC, "52 min")]
    for i, (pl, rte, st, c, eta) in enumerate(vehicles):
        vy = MY + 38 + i * 42
        if i == 0:
            o += rect(LX + 10, vy, LW - 20, 38, 9, AC, op=.10)
        o += rect(LX + 20, vy + 12, 16, 12, 3, c, op=.85)
        o += rect(LX + 26, vy + 8, 10, 6, 2, c, op=.5)
        o += txt(LX + 46, vy + 16, pl, 9.5, D["ink"], 700, font=MONO)
        o += txt(LX + 46, vy + 29, rte, 8, D["muted"], 500)
        o += txt(LX + LW - 18, vy + 16, eta, 9, D["ink"] if eta != "—" else D["muted"], 700, "end")
        o += pill(LX + LW - 18 - len(st) * 5.0 - 14, vy + 21, len(st) * 5.0 + 14, 14, st, "#182337", c, 7.5)

    # shipments table
    TY2 = MY + MH + 20
    o += txt(cx + 24, TY2 + 4, "Shipments needing attention", 11.5, D["ink"], 700)
    o += pill(cx + 232, TY2 - 8, 66, 17, "4 flagged", "#2A2113", "#FFB454", 8)
    hdr = ["WAYBILL", "CUSTOMER", "ROUTE", "WINDOW", "STATUS"]
    colx = [cx + 24, cx + 156, cx + 316, cx + 486, cx + 660]
    o += rect(cx + 24, TY2 + 16, cw - 48, 26, 6, "#101827")
    for i, hh in enumerate(hdr):
        o += txt(colx[i] + 10, TY2 + 33, hh, 8, D["muted"], 800, ls=1.1)
    rows = [("AZ-88231", "Gulf Foods Co.", "Dammam → Jubail", "09:00 – 11:00", "Delayed", "#FF6B6B"),
            ("AZ-88240", "Nahda Retail", "Qatif → Khobar", "10:30 – 12:30", "On route", AC),
            ("AZ-88255", "Marina Hotels", "Dhahran → Dammam", "12:00 – 14:00", "Loading", "#3BD59A")]
    for i, (wb, cst, rte, win, st, c) in enumerate(rows):
        ry = TY2 + 48 + i * 34
        if i % 2 == 0:
            o += rect(cx + 24, ry - 12, cw - 48, 30, 6, "#0F1726")
        o += txt(colx[0] + 10, ry + 8, wb, 9.5, D["ink"], 700, font=MONO)
        o += txt(colx[1] + 10, ry + 8, cst, 9.5, D["ink"], 600)
        o += txt(colx[2] + 10, ry + 8, rte, 9.5, D["muted"], 500)
        o += txt(colx[3] + 10, ry + 8, win, 9.5, D["muted"], 500, font=MONO)
        o += pill(colx[4] + 10, ry - 3, len(st) * 5.2 + 16, 17, st, "#182337", c, 8)
    o += tail

    # ================= DRIVER PHONE =================
    PHX, PHY, PHW, PHH = 936, 196, 240, 506
    head, tail, sx, sy, sw, sh = phone(PHX, PHY, PHW, PHH, uid, "#080D16")
    o += head
    o += txt(sx + 18, sy + 26, "9:41", 9, "#E7EEF9", 700)
    o += rect(sx + sw - 40, sy + 19, 16, 7, 2, "#E7EEF9", op=.8)

    o += rect(sx, sy + 38, sw, 34, 0, "#0E1522")
    o += txt(sx + 18, sy + 60, "Route 12", 12, "#EDF2FA", 800)
    o += pill(sx + sw - 84, sy + 47, 66, 18, "Stop 4 of 9", "#16243D", AC, 8)

    # mini map
    MPY = sy + 72
    o += fleet_map(sx, MPY, sw, 150, uid + "p")
    o += rect(sx + 12, MPY + 12, 96, 30, 8, "#0C1524", op=.94)
    o += txt(sx + 22, MPY + 32, "2.4 km · 8 min", 8.5, "#CBD8EE", 700)

    # next stop
    ny = MPY + 166
    o += txt(sx + 18, ny, "NEXT STOP", 8, "#7E8CA6", 800, ls=1.5)
    o += txt(sx + 18, ny + 22, "Gulf Foods Co.", 13.5, "#EDF2FA", 800)
    o += txt(sx + 18, ny + 39, "Warehouse 7, Industrial City 2", 9, "#7E8CA6", 500)
    o += rect(sx + 18, ny + 52, sw - 36, 44, 11, "#101827")
    o += txt(sx + 30, ny + 71, "Window", 8.5, "#7E8CA6", 600)
    o += txt(sx + 30, ny + 87, "09:00 – 11:00", 10, "#EDF2FA", 700, font=MONO)
    o += pill(sx + sw - 84, ny + 64, 60, 20, "3 pallets", "#16243D", AC, 8)

    by = ny + 112
    o += rect(sx + 18, by, sw - 36, 44, 12, f"url(#{uid}btn)")
    o += path(f"M{sx + 62} {by + 16} l14 6 -6 2 -2 6 Z", fill="#FFFFFF")
    o += txt(sx + sw / 2 + 14, by + 27, "Navigate", 11.5, "#FFFFFF", 800, "middle")
    o += rect(sx + 18, by + 54, sw - 36, 40, 12, "#101827")
    o += rect(sx + 18, by + 54, sw - 36, 40, 12, "none", "#20293C", 1)
    o += rect(sx + 40, by + 66, 16, 16, 3, "none", AC, 1.8)
    o += line(sx + 44, by + 66, sx + 44, by + 82, AC, 1.8)
    o += line(sx + 51, by + 66, sx + 51, by + 82, AC, 1.8)
    o += txt(sx + sw / 2 + 12, by + 79, "Scan waybill", 10.5, "#CBD8EE", 700, "middle")
    o += rect(sx + sw / 2 - 40, sy + sh - 14, 80, 4, 2, "#25314A")
    o += tail

    o += txt(40, 706, "DISPATCH  ·  TELEMETRY  ·  DRIVER APP", 10, "#7C86A6", 700, ls=1.8)
    return wrapsvg(o, defs)


if __name__ == "__main__":
    open("../assets/projects/logistics/showcase.svg", "w").write(build())
    print("ok")
