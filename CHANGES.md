# Nytel site package (1 Nov 2026), changes versus repo main d6eb66c

Apply with `git apply package.patch` from a clean checkout of main (checked with `git apply --check`). Or copy this folder over the repo. Nothing has been committed or pushed.

## Added
- `fonts/`: six self-hosted IBM Plex woff2 files (Sans 300/400/500/600, Mono 400/500).
- `fonts.css`: the @font-face rules plus size-adjusted fallbacks (CLS went from 0.147 to 0).

## Changed
- `templates/index.html.j2` and the built `index.html`: the Compiler/SOP-IR redesign.
  - An interactive hero: clause 4 (critical monitoring finding) leads, and 4 topic tabs (APG pattern: Escalation / Site activation / Delegation log / Re-consent) switch between the four example clauses.
  - Sections in this order, with no section numbers: What we've built, How it works, Co-founders + Partners, Let's team up.
  - A `#how` nav link, `<main tabindex="-1">` and three font preloads.
  - The `?v=` cache-buster is now `2026-11-01e` (in `templates/index.html.j2`, the built `index.html` and `whitepaper.html`). It is on the og image URL (og:image, twitter:image, JSON-LD image) and also on the CSS links in both pages.
- Hero v2 (copy final and approved by Marketing on 1 Nov 2026): the four example clauses and their rules. Superseded in layout by hero option A below.
- `style.css`: the redesign styles, the `.whitepaper` article styles, the hero v2 layout, and a fix for the capabilities overflow at 861–1100px.
- `chrome.css` (shared with the static whitepaper), versus main d6eb66c: the header comment now says the file is also loaded by the static whitepaper.html; the `--sans` definition was replaced by a comment (fonts.css defines `--sans`/`--mono`; see Fonts and weight below); the `.btn` and `.btn:hover` rules were removed and `.quiet` was dropped from the 44px tap-target selector (round 10, "Let's team up" CTA below). No other rules changed.
- `build.py`: the `_footer.html` output was removed, so it now writes index.html and llms.txt only. It also adds the `noorphan` filter, which joins the last two words of clauses and rule values with a non-breaking space.
- `whitepaper.html`: now static, hand-maintained HTML with no Quarto or Bootstrap.
  - It uses the same header, nav and footer as index.html.
  - Its links are absolute (`/#how` and so on) and the Whitepaper link carries `aria-current="page"`.
  - The "Whitepaper" eyebrow is approved.
- `og-image.png`: a new 1200×630 image showing the hero with the Escalation tab selected, clause 4 (N = 5) and its rule (CONDITION, CHECK, SCHEDULE as the cron chip with its gloss, and ACTION as the chips `draft_notice(study_lead)` and `draft_escalation(next_level)`). It has no connector line.
- `_data/messaging.yaml`: local keys, listed below.

## Later changes (1 Nov 2026, Vadim feedback and Marketing copy)
- **Section numbers removed from the markup.** On the home page, the 01–04 margin column is gone and the `.num`/`.sec` CSS was dropped. Sections now share the hero's left edge and max width, and the spacing between sections is the same everywhere.
  - On the whitepaper, the numbers 1–5 and 4.1 are gone and the `.whitepaper .sn` CSS was dropped.
  - The 01–04 step numbers inside How it works are removed too.
- **Whitepaper copy fixes from Marketing:** all 5 fixes are applied, and "MVP" no longer appears on either page. See `../whitepaper-copyfix-diff.txt`.
- **Fonts and weight:**
  - `chrome.css` no longer redefines `--sans`. Before this, it overrode fonts.css, so the size-adjusted fallback was never used.
  - The webfont families are renamed to 'Nytel Plex Sans' and 'Nytel Plex Mono', so a locally installed IBM Plex is never matched.
  - `url()`s are relative to the CSS file.
  - `font-synthesis: none` is set, and body text uses `-moz-osx-font-smoothing: grayscale`.
  - Whitepaper body text is `var(--muted)` like the home page, and `<strong>` is weight 500.

- **How it works "Line" layout (option A, picked by Vadim, 1 Nov 2026):** the four steps sit as stations on a teal hairline. The human-review safeguard branches off the Agents station at every width (in the markup it sits inside that station, so screen readers hear it right after Agents), and the audit-trail safeguard is a dotted rule under the line. On mobile the line runs vertically.
  - No section or step numbers, and no copy changes: visible text is identical before and after.
  - The old `.steps` and `.aside` CSS was removed and the new `.hiw-a`/`.stations`/`.branch`/`.audit` CSS added. The template's How it works block was swapped.

- **"Let's team up" CTA, "Outlined pair" (picked by Vadim, 1 Nov 2026):** two equal outlined controls, "Email Matthew" and "Book a call", with uppercase Plex Mono labels. A mono line under them shows "Matthew Wamsley · mw@nytel.ai".
  - The hrefs are unchanged.
  - Applies to both `templates/index.html.j2` and the static `whitepaper.html` contact block.
  - `style.css`: the old `.actions`/`.btn`/`.quiet` rules were removed and the `.cta-pair`/`.cta-who` rules added. `chrome.css`: the unused `.btn` rules and the `.quiet` selector were removed.
  - **yaml:** `call_to_action.secondary.label` changed from "or book a call" to "Book a call" (approved by Marketing; merge this key into the knowledge base). `llms.txt` is unaffected.

- **Hero option A (approved by Vadim via Kate, 1 Nov 2026):** clause 4 (critical monitoring finding) leads. APG topic tabs in the order Escalation / Site activation / Delegation log / Re-consent switch the example. The clause is on the left and the rule is on the right.
  - N is one live number input in the clause line (default 5, range 1–30, aria-label "N, configurable, in business days"). It is clamped to 1–30 on every input event. The CHECK row shows a read-only mirror of N: plain text, not focusable and with no input semantics, kept in sync.
  - ACTION values are command chips with the same teal tint as the cron chip, one per `; `-separated part of the action (`hero_local.action_chips`). They have no visible gloss. Each chip carries its verbatim yaml action text as `.sr-only` text. Chips never wrap inside a call; they wrap to the next line as whole chips.
  - **No `title` on any chip (action chips and the cron chip).** A `title` plus identical `.sr-only` text can be read twice, and the visible clause already explains the chips to sighted users. The action chips keep their `.sr-only` verbatim text; the cron chip's visible gloss is enough.
  - **"N business days" (approved by Vadim via Kate, 1 Nov 2026):** the clause 4 line, `check_lead` and `n_label` now say "business days". `hero.examples[3].check` is now "unresolved > {N} business days" (round 12). It is not rendered anywhere: CHECK uses `check_lead`, and llms.txt does not include the hero.
  - **N stays with "business days":** in the template's `ntext` macro, N (the clause chip or the CHECK mirror) and the word after it are joined by a non-breaking space inside a `.n-keep` no-wrap span. The CHECK text also goes through `noorphan`, so "N business days" stays on one line everywhere. An nbsp alone was not enough, because browsers still break after the inline-block N chip. The yaml copy is unchanged.
  - At 1100px and below, every rule row stacks its label above its value, so values get the full panel width.
  - The rule panel has a faint teal tint fading left to right, tabular numerals and a right inset. No text was added.
  - Tap targets: the tabs are at least 44px tall. The N chip stays 32×32 visually, and a padded `<label>` around it gives a 44×44 tap area.
  - Clause 4's rule: CHECK "finding unresolved > {N} business days", SCHEDULE as the cron chip `0 7 * * 1-5` (teal-tinted). The visible gloss "07:00, Monday to Friday" sits beside it and wraps under the chip when it does not fit. ACTION is shown as chips (above). The other three clauses' rule text is verbatim from the yaml.
  - The connector line between the clause and the rule panel was removed (no SVG, CSS or JS). The human-review note is not in the hero; it stays in How it works only. There are no buttons or numbering in the hero.
  - All panels share one grid cell, so the hero height is constant across tabs: the stage is 233px at 1280 and 420px at 390. The hero bottom is 689px at 1280×800.
  - Reduced motion: no animations. Without it, the highlight and rule rows animate in on a tab switch.
  - `style.css`: removed the dead hero CSS (`.specimen`, `.doc`, `.clauses`, `.clause-tab`, `.ci`, `.ct`, `.link`/`.ln-*`, `.rule`, `.tok`/`.t1–3`, `.param`, the global `blockquote p` and `mark` rules, the `grow`/`draw`/`pop` keyframes and the mid-width specimen rules). Added the `.hx*`/`.n-in` rules. The desktop `.hero`/`.hero-top` spacing is kept.
  - `templates/index.html.j2`: the hero figure was replaced, the `param` macro removed, and the old tab, measure and elbow-link JS was replaced by the N-sync and tabs JS.
  - **yaml:** new `hero_local` keys; see the merge list below. `hero.params` was removed because nothing reads it any more. `llms.txt` is byte-identical.

## Removed
- The Quarto pipeline: `whitepaper.qmd`, `nytel.scss`, `_header.html`, `_header-meta.html`, `_footer.html` and `templates/_footer.html.j2`. The package contains no `whitepaper_files/`.

## Unchanged on purpose
- `overview.html` (the redirect to /), CNAME, robots.txt, sitemap.xml and the icons.

## llms.txt
- `build.py` regenerates `llms.txt` from `_data/messaging.yaml` (`templates/llms.txt.j2`). Versus main it has co-founder credentials from the yaml, Slack and location removed, the new whitepaper title, and partner links. The hero changes do not affect it; it is byte-identical before and after hero A.

## yaml keys to merge into the knowledge-base master
Every copy difference between `_data/messaging.yaml` and main's copy, all approved on 1 Nov 2026.
- `call_to_action.secondary.label`: "or book a call" → "Book a call".
- `capabilities.items[1].detail`, `[2].detail` and `[3].detail` (new): the one-liners.
- `capabilities.mvp_agents.items[0..3].detail_short` (new): the one-line cuts.
- `capabilities.mockup_groups` (new): the headings Compliance & SOPs, Protocols & EDC and Trial operations agents, with their rows.
- `partners.items[1].long`: a straight apostrophe → curly (Investigators’). `partners.items[1].url` (new): https://poeticphase1.org.
- `hero.source_label`, `hero.rule_labels` and `hero.examples[0..3]` (line, condition, check, action), all new. `hero.examples[3].line` ends "…escalated if unresolved after {N} business days." `hero.examples[3].check` is "unresolved > {N} business days". The clauses are illustrative examples. In the yaml, `{N}` marks the configurable parameter.
- `hero_local` (new; merge under `hero:`):
  - `n_default: 5`
  - `n_label: 'N, configurable, in business days'`
  - `topics: [Site activation, Delegation log, Re-consent, Escalation]`
  - `check_lead: 'finding unresolved > {N} business days'`
  - `schedule_label: SCHEDULE`
  - `schedule_cron: '0 7 * * 1-5'`
  - `schedule_cron_gloss: '07:00, Monday to Friday'`
  - `action_chips` (in hero.examples order): `[hold(site), draft_missing_items(owner)]`, `[flag(reg_coord, pi)]`, `[flag(re_consent), draft_notice(pi, coord)]`, `[draft_notice(study_lead), draft_escalation(next_level)]`
- Not copy, so do not merge: `mockup_direction`.

## Master patch (`../master-messaging.patch`)
A unified diff of knowledge-base `marketing/messaging.yaml` (base: `../master/messaging.yaml.orig`; result: `../master/messaging.yaml`). Not committed or pushed. It applies cleanly (`patch --dry-run`, `git apply --check`), and a script confirmed every merged value is identical to `_data/messaging.yaml`. Each new key carries a real source field, with no `# source:` comments (round 12): `detail_short` is merged into each MVP agent's existing `source` ("…; detail_short: Approved by Vadim Sokolov, 1 Nov 2026 (one-line cut of detail, words cut only)"). There are also `capabilities.mockup_groups_source` (the file's existing `*_source` sibling pattern), `hero.source` (source_label, rule_labels), a `source` on each `hero.examples[]` item, and `hero_local.source` (every key in it). Parsed copy values are unchanged apart from `examples[3].check`. `build.py --sync` strips all of these.
- **Fixed in `build.py` (round 13):** `strip_internal` used to drop every key containing "source", which also removed the copy key `hero.source_label` and broke the build after `--sync`. It now drops only keys that are exactly `source` or end in `_source` (plus the existing INTERNAL_KEYS). Checked on a scratch copy: `build.py --sync ../master/messaging.yaml` succeeds, and the built index.html and llms.txt are byte-identical to this package. The synced `_data` matches this package's `_data` in every value except the local, unused `mockup_direction`; the other differences are comments and formatting. Keys:
- `capabilities.items[1..3].detail`
- `capabilities.mvp_agents.items[0..3].detail_short`
- `capabilities.mockup_groups`
- `partners.items[1].long` (curly apostrophe, Investigators’) and `partners.items[1].url` (https://poeticphase1.org), with its source note
- `call_to_action.secondary.label`: "Book a call"
- `hero.source_label`, `hero.rule_labels`, `hero.examples[0..3]` (`examples[3].line` and `examples[3].check` say "{N} business days")
- `hero_local.n_default`, `n_label` ("N, configurable, in business days"), `topics`, `check_lead` ("finding unresolved > {N} business days"), `schedule_label`, `schedule_cron`, `schedule_cron_gloss`, `action_chips` (top-level `hero_local`, as the site reads it)
- Left out: `mockup_direction`, `hero.params`, `hero_local.schedule_daily`.

## Deploy notes
1. Run `python3 build.py`, which writes index.html and llms.txt. It is StrictUndefined, so the yaml must include the hero and hero_local keys above.
2. Push to main, and GitHub Pages serves it. There is no build step on Pages and Quarto is no longer needed.

## Verification (local server)
- **axe:** 0 violations (wcag2a/aa, 21aa, 22aa, best-practice) on index in all four hero tab states and after an N change, at 1280 and 390, and on the whitepaper at 1280 and 390.
- **Overflow:** none at 1280, 1024, 768 and 390; scrollWidth equals the viewport.
- **Keyboard (hero A):** tabs use a roving tabindex, Left/Right wrap, Home/End work, and selection follows focus. Tab moves on to the single N input; Up/Down step N and clamp at 1 and 30. The CHECK mirror is not in the tab order.
- **Whitepaper:** pixel-identical full-page screenshots before and after hero A, at 1280 and 390.
- **Lighthouse (measured before hero A; not re-run):** 100/100/100/100 on both pages, mobile and desktop. CLS is 0; LCP is 1.2 s on mobile and 0.3 s on desktop.
- **Links and assets:** all internal links and anchors resolve, every asset returns 200, and the fonts load.
- **overview.html** redirects to /.
- **Remnants:** a grep for quarto or bootstrap finds nothing.
