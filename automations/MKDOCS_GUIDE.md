# FlowRunner Docs — Theme Guide

This guide is for working on the FlowRunner documentation site, which is built with Material for MkDocs. It complements the product theme defined in `THEME_GUIDE.md` (the site/product design system) but is specific to documentation.

The two visual systems share fonts, color tokens, and editorial aesthetic. They diverge in structure: docs have a left navigation rail, a right table of contents, search, and breadcrumbs that are fundamentally part of how documentation works. We don't try to make docs look identical to the product. We aim for **family resemblance**, not pixel sameness.

## Files

```
docs/stylesheets/flowrunner-mkdocs.css   The theme stylesheet
mkdocs.yml                                Site config (palette, fonts, plugins)
MKDOCS_GUIDE.md                          This file
```

The CSS file overrides Material's CSS variables (the `--md-*` family) to use FlowRunner's color palette. It also reskins admonitions, code blocks, tabs, kbd elements, blockquotes, and tables to match the editorial aesthetic.

## Two themes, light is default

Material supports both light and dark schemes natively, and the FlowRunner port handles both.

**Default is light** because long-form technical documentation reads better in light mode. Code block syntax highlighting is clearer, copy-paste contrast is better, and most users expect docs to be light by default.

**Dark is one toggle away.** The header has a sun/moon icon. User preference is saved in localStorage automatically — no custom JavaScript required, Material handles it.

The toggle uses Material's own preference detection: it respects `prefers-color-scheme` on first visit, then remembers the user's manual choice.

## Typography

Three faces, same as the product:

- **Fraunces** for h1, h2, h3 (the serif moments)
- **Inter Tight** for body prose, h5, h6, navigation
- **JetBrains Mono** for code, kbd, uppercase labels, site title, nav section headers, search

The fonts load automatically. Inter Tight and JetBrains Mono come from Material's `theme.font` config in `mkdocs.yml`. Fraunces loads via an `@import` inside the CSS file.

**Headings:**

- `h1` is your page title — serif, 2.4em, tight letter-spacing. Use one per page.
- `h2` is section breaks — serif, 1.65em. Generous top margin.
- `h3` is subsections — serif, 1.25em.
- `h4` is **deliberately different**: mono uppercase, small, muted. It's a label, not a headline. Use it when you want a small categorical marker, not a content break. If `h4` feels too small for your section break, you're probably looking for `h3`.

**Don't try to override the heading styles in individual pages.** The visual rhythm depends on consistency across docs.

## When to use admonitions

Admonitions are reskinned to follow FlowRunner's left-border-color convention:

- `!!! note` and `??? note` (collapsible) — accent color (forest green light / amber dark). Use for important context, definitions, conceptual notes.
- `!!! tip` / `!!! hint` — green. Use for best practices and recommendations.
- `!!! warning` / `!!! caution` / `!!! danger` / `!!! failure` — flag color (rust). Use sparingly, only for genuine warnings.
- `!!! info` / `!!! abstract` / `!!! summary` / `!!! example` — muted gray. Use for asides and supplementary info.

**Rule of thumb: at most two admonitions per page.** Heavy admonition use turns docs into a colored-box obstacle course. Most context belongs in prose.

## Tabs (pymdownx.tabbed)

The reskinned tab style uses the FlowRunner pattern: serif tab labels with a 2px accent bottom-border on the active tab.

Good uses for tabs:

- Multiple code language examples (`=== "Python" ... === "JavaScript" ...`)
- Multiple installation paths (Docker / pip / source)
- Multiple platform-specific instructions (macOS / Windows / Linux)

Bad uses for tabs:

- Hiding content that should be visible by default
- Comparison content (use a table instead)
- More than 4 tabs (becomes visual noise)

## Code blocks

Three small things worth knowing:

**Add a title for context.** Use `python title="example.py"` after the language hint and you get a filename header above the code block. Always do this when the code is meant to live in a specific file the user will create.

**Annotations work.** With `content.code.annotate` enabled, you can drop `# (1)` in the code and follow with a numbered list for inline explanations. Better than alternating prose and code blocks for walkthroughs.

**Copy button is automatic.** Don't add manual "click to copy" instructions; Material adds the copy button to every code block via the `content.code.copy` feature.

## Mermaid diagrams

Mermaid renders via `pymdownx.superfences`. Diagrams will inherit the theme colors but may need tweaks for complex flows. If you write a Mermaid diagram and it looks wrong in dark mode, set explicit colors using Mermaid's `%%{init: ...}%%` directive at the top.

For most flowcharts and sequence diagrams, the default rendering looks fine in both themes.

## Page structure conventions

This section is **specifically for Claude Code working on doc pages**.

**Every page starts with an h1 and a lede paragraph.** The lede is one to three sentences, plain prose, no formatting tricks. It tells the reader what this page is about and whether they should keep reading. Don't bury the lede behind admonitions, tables of contents, or "in this guide" lists.

**Sections use h2.** Each h2 represents a substantive section. If you have more than 6 h2s on one page, the page should be split.

**Avoid deep nesting.** Going h3 → h4 → h5 means the content is too granular for one page. Consider breaking into multiple pages.

**Code examples come with context.** Don't drop a code block without first explaining what it does. The pattern is: one paragraph of prose, then the code block, then optionally one paragraph of "here's what this means."

**Tables for reference, prose for narrative.** A configuration option table is appropriate. A "step 1, step 2, step 3" sequence in a table is not — that's a numbered list.

**Use mono inline code for these things** (with single backticks): file paths (`/etc/flowrunner/config.yml`), variable names (`api_key`), command-line tools (`kubectl`), configuration keys (`worker.concurrency`), short literal values (`true`, `"production"`).

**Use blockquotes for verbatim quotes from external sources or user testimonials.** Not for emphasis. If you want emphasis, write better prose.

## What to avoid

**No emoji in headings or body prose.** Twemoji is loaded for unicode emoji that appear in user content, but headings, callouts, and prose should stay typography-only. Emoji rabbit-holes the tone away from "serious tool."

**No hero images or cartoon illustrations.** If a concept needs visualization, use a Mermaid diagram, a Material icon (which is just an SVG), or a screenshot of the actual product.

**No abandoned drafts.** If you're not sure about a page, leave it out of the nav (in `mkdocs.yml`) until it's ready. Half-finished pages in the published site are worse than absent pages.

**No mixed-case section titles in nav.** Use Title Case consistently or sentence case consistently. The Material navigation looks bad when "Getting Started" sits next to "advanced topics".

## Site config notes for Claude Code

When you're working on `mkdocs.yml`:

- **Don't remove the social plugin.** It generates Open Graph cards for sharing on Slack, X, LinkedIn. The cards are styled to match FlowRunner branding (forest green background, cream text).
- **Don't disable the search plugin.** Material search is fast, offline-capable, and free. It's the single most important docs feature.
- **Don't add Google Analytics.** If analytics are needed, use a privacy-respecting alternative and add it via `extra` config, not via inline scripts.

## Visual reference

The product demo at `ji_demo.html` is the visual reference for the FlowRunner aesthetic. The colors, typography, and editorial restraint that you see in the demo are what we're trying to evoke in docs — within the constraints of Material's structure.

If you're ever unsure whether a docs element looks right, open the demo in the same theme (light or dark) and compare. If your docs element feels louder, more colorful, or busier than the demo, dial it back.

## Family resemblance, not pixel sameness

Docs will always have a left nav rail, a right ToC, a search bar, and breadcrumbs. Product UI doesn't. That's correct. The goal isn't to strip Material's information architecture to make docs look like the product. The goal is that anyone visiting both flowrunner.ai and the docs site immediately recognizes them as the same brand — same fonts, same color story, same restraint. The structure underneath each one is appropriate to its purpose.
