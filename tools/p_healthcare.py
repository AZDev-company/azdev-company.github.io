from kit import *

AC = "#2CC8B0"
AC2 = "#63E6CE"
D = DARK
L = LIGHT


def cross(cx, cy, s, c, t=None):
    t = t or s * .34
    return (rect(cx - t / 2, cy - s / 2, t, s, t * .3, c) +
            rect(cx - s / 2, cy - t / 2, s, t, t * .3, c))


def heart(cx, cy, s, c):
    return path(f"M{cx} {cy + s * .52} C{cx - s * .95} {cy - s * .12} {cx - s * .72} {cy - s * .86} "
                f"{cx - s * .3} {cy - s * .86} C{cx - s * .08} {cy - s * .86} {cx} {cy - s * .6} {cx} {cy - s * .5} "
                f"C{cx} {cy - s * .6} {cx + s * .08} {cy - s * .86} {cx + s * .3} {cy - s * .86} "
                f"C{cx + s * .72} {cy - s * .86} {cx + s * .95} {cy - s * .12} {cx} {cy + s * .52} Z", fill=c)


def build():
    uid = "hc"
    o = glow(uid + "1", AC, 380, 280, 420, ".15")
    o += glow(uid + "2", "#5B8CFF", 900, 420, 360, ".11")
    defs = (f'<linearGradient id="{uid}btn" x1="0" y1="0" x2="1" y2="0">'
            f'<stop stop-color="{AC}"/><stop offset="1" stop-color="#22A794"/></linearGradient>'
            f'<linearGradient id="{uid}appt" x1="0" y1="0" x2="1" y2="1">'
            f'<stop stop-color="#12897A"/><stop offset="1" stop-color="#2CC8B0"/></linearGradient>')

    # ================= CLINIC DASHBOARD =================
    WX, WY, WW, WH = 44, 60, 692, 432
    head, tail, cx, cy, cw, ch = window(WX, WY, WW, WH, uid, "clinic.azdev.app / schedule", accent=AC)
    o += head
    o += txt(cx + 24, cy + 32, "Today's schedule", 13.5, D["ink"], 800)
    o += pill(cx + 168, cy + 18, 96, 22, "Tue, 24 Feb", "#182337", D["muted"], 9)
    o += rect(cx + cw - 118, cy + 16, 94, 26, 8, f"url(#{uid}btn)")
    o += txt(cx + cw - 71, cy + 33, "+  New visit", 9.5, "#062A25", 800, "middle")

    kpis = [("Appointments", "42", AC), ("Checked in", "18", "#5B8CFF"),
            ("In consult", "7", "#B08CFF"), ("Completed", "31", "#3BD59A")]
    KW = (cw - 48 - 3 * 12) / 4
    for i, (k, v, c) in enumerate(kpis):
        kx = cx + 24 + i * (KW + 12)
        o += rect(kx, cy + 52, KW, 64, 12, "#101827")
        o += rect(kx, cy + 52, KW, 64, 12, "none", D["line"], 1)
        o += rect(kx, cy + 52, 3, 64, 1.5, c)
        o += txt(kx + 16, cy + 76, k, 9, D["muted"], 600)
        o += txt(kx + 16, cy + 102, v, 20, D["ink"], 800)

    # schedule grid
    GY = cy + 136
    GH = 246
    TCW = 44
    cols = ["Room 1", "Room 2", "Tele"]
    GX = cx + 24 + TCW
    GW = 366
    CWD = GW / 3
    o += rect(cx + 24, GY, TCW + GW, GH, 10, "#0E1522")
    for i, cn in enumerate(cols):
        o += txt(GX + CWD * i + CWD / 2, GY + 18, cn, 9, D["muted"], 700, "middle")
        if i:
            o += line(GX + CWD * i, GY + 26, GX + CWD * i, GY + GH, D["line"], 1)
    o += line(cx + 24, GY + 26, cx + 24 + TCW + GW, GY + 26, D["line"], 1)
    times = ["09:00", "10:00", "11:00", "12:00"]
    RH = (GH - 26) / 4
    for i, t in enumerate(times):
        ry = GY + 26 + i * RH
        o += txt(cx + 34, ry + 18, t, 8.5, "#57667F", 600, font=MONO)
        if i:
            o += line(cx + 24, ry, cx + 24 + TCW + GW, ry, D["line"], 1, .6)
    blocks = [(0, 0, 1, "Consultation", "Room 1", AC),
              (1, 0, 1.5, "Follow-up", "Room 1", "#5B8CFF"),
              (0, 1, 2, "Screening", "Room 2", "#B08CFF"),
              (2, 1, 1, "Lab review", "Room 2", AC),
              (1, 2, 1, "Video visit", "Tele", "#3BD59A"),
              (3, 2, 1, "Video visit", "Tele", "#3BD59A")]
    for r, c_, span, label, room, c in blocks:
        bx = GX + CWD * c_ + 5
        byy = GY + 26 + r * RH + 4
        bh = RH * span - 8
        o += rect(bx, byy, CWD - 10, bh, 8, c, op=.16)
        o += rect(bx, byy, 2.6, bh, 1.3, c)
        o += txt(bx + 10, byy + 17, label, 8.8, D["ink"], 700)
        if bh > 40:
            o += txt(bx + 10, byy + 31, "30 min · confirmed", 7.5, D["muted"], 500)

    # queue
    QX = cx + 24 + TCW + GW + 16
    QW = cw - 24 - (TCW + GW) - 40
    o += rect(QX, GY, QW, GH, 10, "#0E1522")
    o += txt(QX + 16, GY + 22, "Waiting room", 11, D["ink"], 700)
    o += pill(QX + QW - 46, GY + 10, 32, 17, "7", "#182337", D["muted"], 8.5)
    q = [("Patient #2041", "Cardiology · 09:20", AC),
         ("Patient #2042", "Dermatology · 09:35", "#5B8CFF"),
         ("Patient #2043", "Paediatrics · 09:50", "#B08CFF"),
         ("Patient #2044", "Cardiology · 10:05", AC)]
    for i, (n, m, c) in enumerate(q):
        qy = GY + 40 + i * 50
        o += rect(QX + 12, qy, QW - 24, 44, 9, "#131B2A")
        o += circ(QX + 32, qy + 22, 12, c, op=.2)
        o += circ(QX + 32, qy + 19, 4, c)
        o += path(f"M{QX + 24} {qy + 30} a8 6 0 0 1 16 0", fill=c)
        o += txt(QX + 52, qy + 19, n, 9.5, D["ink"], 700)
        o += txt(QX + 52, qy + 32, m, 8, D["muted"], 500)
    o += tail

    # ================= PATIENT PHONE =================
    PHX, PHY, PHW, PHH = 764, 42, 336, 672
    head, tail, sx, sy, sw, sh = phone(PHX, PHY, PHW, PHH, uid, "#F7F9FC")
    o += head
    o += txt(sx + 24, sy + 32, "9:41", 11, L["ink"], 700)
    o += rect(sx + sw - 50, sy + 24, 20, 9, 2, L["ink"], op=.85)
    o += rect(sx + sw - 76, sy + 24, 16, 9, 2, L["ink"], op=.5)
    o += rect(sx, sy, sw, 150, 0, "#FFFFFF")

    o += txt(sx + 24, sy + 68, "Good morning", 10, L["muted"], 600)
    o += txt(sx + 24, sy + 88, "Layla H.", 17, L["ink"], 800)
    o += avatar(sx + sw - 42, sy + 76, 19, "#7FE3D2", "#1E9E8C", uid + "a")
    o += rect(sx + 24, sy + 106, sw - 48, 38, 12, "#F1F4F9")
    o += circ(sx + 44, sy + 125, 5, "none", "#9AA7BC", 1.8)
    o += line(sx + 47.6, sy + 128.6, sx + 51, sy + 132, "#9AA7BC", 1.8)
    o += txt(sx + 60, sy + 129, "Search doctors, clinics", 10, "#9AA7BC", 500)

    # date strip
    dy = sy + 172
    days = [("M", "22"), ("T", "23"), ("W", "24"), ("T", "25"), ("F", "26"), ("S", "27"), ("S", "28")]
    for i, (dn, dd) in enumerate(days):
        dx = sx + 22 + i * ((sw - 44) / 7)
        wdt = (sw - 44) / 7 - 6
        sel = i == 2
        o += rect(dx, dy, wdt, 56, 12, AC if sel else "#FFFFFF")
        o += txt(dx + wdt / 2, dy + 20, dn, 8.5, "#D6FBF3" if sel else L["muted"], 700, "middle")
        o += txt(dx + wdt / 2, dy + 41, dd, 12.5, "#FFFFFF" if sel else L["ink"], 800, "middle")

    # next appointment
    ay = dy + 76
    o += txt(sx + 24, ay, "Next appointment", 12, L["ink"], 800)
    o += rect(sx + 22, ay + 14, sw - 44, 124, 16, f"url(#{uid}appt)")
    o += avatar(sx + 54, ay + 50, 22, "#CFF6EE", "#3AA695", uid + "d")
    o += txt(sx + 88, ay + 44, "Dr. Amina Farouk", 13, "#FFFFFF", 800)
    o += txt(sx + 88, ay + 61, "Cardiology · Room 3", 9.5, "#C4F2E9", 500)
    o += line(sx + 40, ay + 84, sx + sw - 40, ay + 84, "#FFFFFF", 1, .22)
    o += circ(sx + 48, ay + 106, 8, "none", "#CFF6EE", 1.6)
    o += path(f"M{sx + 48} {ay + 101} v5 l3 2", stroke="#CFF6EE", sw=1.6)
    o += txt(sx + 64, ay + 110, "Today · 4:30 PM", 10.5, "#FFFFFF", 700)
    o += rect(sx + sw - 116, ay + 92, 76, 28, 9, "#FFFFFF")
    o += txt(sx + sw - 78, ay + 110, "Join call", 10, "#0E7466", 800, "middle")

    # specialties
    spy = ay + 168
    o += txt(sx + 24, spy, "Specialties", 12, L["ink"], 800)
    o += txt(sx + sw - 24, spy, "See all", 9.5, AC, 700, "end")
    specs = [("Cardio", "#FF6B8A"), ("Dental", "#5B8CFF"), ("Neuro", "#B08CFF"), ("Ortho", "#FFB454")]
    for i, (n, c) in enumerate(specs):
        px = sx + 22 + i * ((sw - 44) / 4)
        pw = (sw - 44) / 4 - 8
        o += rect(px, spy + 14, pw, 68, 14, "#FFFFFF")
        m = (px + pw / 2, spy + 42)
        o += circ(m[0], m[1], 15, c, op=.14)
        if i == 0:
            o += heart(m[0], m[1], 9, c)
        elif i == 1:
            o += path(f"M{m[0] - 6} {m[1] - 6} q6 -4 12 0 q1 8 -3 12 q-3 -5 -3 -5 q0 0 -3 5 q-4 -4 -3 -12 Z", fill=c)
        elif i == 2:
            o += circ(m[0], m[1] - 1, 6.5, "none", c, 2)
            o += line(m[0], m[1] + 5.5, m[0], m[1] + 8, c, 2)
        else:
            o += path(f"M{m[0] - 6} {m[1] - 6} l12 12 M{m[0] - 6} {m[1] - 6} m-1 -2 a3 3 0 1 0 4 4 "
                      f"M{m[0] + 6} {m[1] + 6} m1 2 a3 3 0 1 0 -4 -4", stroke=c, sw=2)
        o += txt(m[0], spy + 72, n, 8.5, L["ink"], 600, "middle")

    # reminder
    ry2 = spy + 100
    o += rect(sx + 22, ry2, sw - 44, 60, 14, "#FFFFFF")
    o += rect(sx + 38, ry2 + 15, 30, 30, 9, "#FFF0F3")
    o += rect(sx + 48, ry2 + 22, 10, 16, 3, "#FF6B8A")
    o += txt(sx + 78, ry2 + 27, "Take Atorvastatin", 11, L["ink"], 700)
    o += txt(sx + 78, ry2 + 42, "1 tablet · 9:00 PM", 9, L["muted"], 500)
    o += pill(sx + sw - 82, ry2 + 20, 58, 22, "Done", "#E9FBF6", "#0E9C87", 9)

    # tab bar
    tby = sy + sh - 62
    o += rect(sx, tby, sw, 62, 0, "#FFFFFF")
    o += line(sx, tby, sx + sw, tby, "#E7EBF2", 1)
    for i in range(4):
        tx2 = sx + 46 + i * ((sw - 92) / 3)
        c = AC if i == 0 else "#C2CBD9"
        o += rect(tx2 - 8, tby + 20, 16, 4, 2, c)
        o += rect(tx2 - 8, tby + 27, 16, 4, 2, c, op=.6)
        o += rect(tx2 - 5, tby + 34, 10, 4, 2, c, op=.35)
    o += rect(sx + sw / 2 - 52, sy + sh - 14, 104, 4.5, 2.5, "#C9D2DF")
    o += tail

    # ================= TELECONSULT CARD =================
    TX, TY, TW, TH = 60, 524, 452, 184
    o += rect(TX - 4, TY + 12, TW + 8, TH, 22, "#000", op=.42)
    o += rect(TX, TY, TW, TH, 20, "#0F1726")
    o += rect(TX, TY, TW, TH, 20, "none", "#243149", 1.4)
    o += (f'<defs><clipPath id="{uid}vid"><rect x="{TX + 16}" y="{TY + 16}" width="164" height="152" rx="14"/></clipPath></defs>')
    o += rect(TX + 16, TY + 16, 164, 152, 14, "#12304A")
    o += f'<g clip-path="url(#{uid}vid)">'
    o += circ(TX + 98, TY + 150, 62, "#1B4A6B")
    o += avatar(TX + 98, TY + 84, 34, "#CFF6EE", "#2F8E80", uid + "v")
    o += "</g>"
    o += pill(TX + 26, TY + 26, 52, 18, "● LIVE", "#00000088", "#FF6B6B", 7.5)
    o += rect(TX + 130, TY + 118, 40, 44, 8, "#0A1622")
    o += avatar(TX + 150, TY + 140, 15, "#FFD9A8", "#D9873E", uid + "v2")
    o += txt(TX + 200, TY + 44, "Dr. Amina Farouk", 14, D["ink"], 800)
    o += txt(TX + 200, TY + 62, "Cardiology · follow-up", 10, D["muted"], 500)
    o += pill(TX + 200, TY + 76, 78, 20, "12:04", "#182337", AC, 9.5, 700)
    # waveform
    import random
    random.seed(3)
    for i in range(26):
        hgt = 6 + random.random() * 26
        o += rect(TX + 200 + i * 8, TY + 122 - hgt / 2, 3.4, hgt, 1.7, AC,
                  op=.85 if i % 3 else .4)
    for i, (lbl, c) in enumerate([("mic", "#1B2537"), ("cam", "#1B2537"), ("end", "#FF5A5A")]):
        bx = TX + 214 + i * 52
        o += circ(bx, TY + 152, 17, c)
        if lbl == "mic":
            o += rect(bx - 4, TY + 145, 8, 11, 4, "#C6D2E4")
            o += path(f"M{bx - 7} {TY + 154} a7 7 0 0 0 14 0", stroke="#C6D2E4", sw=1.6)
        elif lbl == "cam":
            o += rect(bx - 8, TY + 147, 12, 10, 3, "#C6D2E4")
            o += path(f"M{bx + 4} {TY + 151} l5 -3 v8 Z", fill="#C6D2E4")
        else:
            o += path(f"M{bx - 7} {TY + 149} q7 -5 14 0 l1 4 -4 2 -2 -3 q-4 -1 -8 0 l-2 3 -4 -2 Z",
                      fill="#FFFFFF")

    # small stat card
    SX2, SY2 = 536, 524
    o += rect(SX2, SY2, 190, 184, 18, "#0F1726")
    o += rect(SX2, SY2, 190, 184, 18, "none", "#243149", 1.4)
    o += txt(SX2 + 20, SY2 + 32, "No-show rate", 11, D["ink"], 700)
    o += txt(SX2 + 20, SY2 + 60, "3.1%", 28, AC, 800)
    o += pill(SX2 + 100, SY2 + 42, 62, 22, "▼ 1.4 pts", "#0F2E2A", AC, 8.5)
    sp, _ = sparkline(SX2 + 20, SY2 + 78, 150, 40, [70, 62, 66, 48, 52, 38, 30, 24], AC, 2.6)
    o += sp
    o += line(SX2 + 20, SY2 + 136, SX2 + 170, SY2 + 136, D["line"], 1)
    o += txt(SX2 + 20, SY2 + 158, "Reminders sent", 9.5, D["muted"], 600)
    o += txt(SX2 + 170, SY2 + 158, "1,204", 10.5, D["ink"], 700, "end")

    o += txt(748, 742, "CLINIC OPS  ·  PATIENT APP  ·  TELECONSULT", 10, "#7C86A6", 700, ls=1.8)
    return wrapsvg(o, defs)


if __name__ == "__main__":
    open("../assets/projects/healthcare/showcase.svg", "w").write(build())
    print("ok")
