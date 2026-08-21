# AZ DEV — agency website

Static site. No build step, no dependencies. Upload the contents of this folder to
GitHub Pages (or any static host) with `index.html` at the root.

```
index.html          page structure
styles.css          design tokens + all styling
script.js           i18n dictionary, theme, drawer, project rendering
data/site.json      contact + social links
data/projects.json  the six case studies
assets/brand/       logo mark, favicon, Open Graph cover
assets/projects/    one showcase.svg per project
tools/              Python generators for the project showcases (optional)
```

## Editing content

**Contact details** → `data/site.json`. Email, phone, Instagram and Facebook are read
from here and injected into both the contact card and the footer. Change it once,
it updates everywhere.

**Case studies** → `data/projects.json`. Each project has a `kicker`, `title`,
`description`, `tags` and three `features`, all in `{ "en": ..., "ar": ... }` form.
Add or remove entries freely — the page renders whatever is in the file.

**All other page copy** → the `I18N` object at the top of `script.js`. Every visible
string is keyed by the `data-i18n` attribute on its element, and every key exists in
both `en` and `ar`. If you add a key, add it to both.

## Project visuals

Each showcase lives at `assets/projects/<id>/showcase.svg` and is referenced from
`data/projects.json`. Drop in your own file with the same path and the page picks it
up without any code change. They are drawn on a `1200 × 760` canvas.

To regenerate them, `tools/` contains the Python sources:

```bash
pip install cairosvg          # only needed to preview as PNG
cd tools && python3 p_delivery.py    # writes assets/projects/delivery/showcase.svg
```

`kit.py` holds the shared pieces — device frames with proper clipping, maps, charts,
avatars, star ratings — so all six stay visually consistent.

## Language and theme

Arabic/English toggle in the header, with full RTL layout, plus a dark/light toggle.
Both persist in `localStorage`. Arabic uses Cairo; English uses Space Grotesk for
headings and Inter for body text.

## Before you publish

- Set the real domain in the `<link rel="canonical">` and `og:image` URL in `index.html`.
- The six projects are described as **concept showcases** built in-house. If you replace
  them with real client work, update the `kicker` text so the framing stays accurate.
