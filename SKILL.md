---
name: workshop-s1-generator
description: >
  Use when the user says "create workshop materials", "build session 1", "generate training content",
  "new client workshop", "replicate the Melonn workshop", or any variation of creating AI & Automation
  training content for a new client. Generates a complete Session 1 package: slide deck, student guide,
  and demo data files — all contextualized for the client's industry and audience.
argument-hint: [client website URL or company name]
disable-model-invocation: true
---

# Workshop Session 1 Generator

Creates a complete, deploy-ready Session 1 training package for AI & Automation workshops. The output replicates the proven Kyto × Melonn workflow: a visual slide deck, an interactive student guide with copyable prompts, and realistic demo data files for hands-on exercises.

## Reference Files

- [reference-slides.md](reference-slides.md) — Slide structure, narrative arc, and content spec for the 14-slide deck
- [reference-guide.md](reference-guide.md) — Student guide structure, exercise design patterns, and CSS component library
- [reference-brand.md](reference-brand.md) — Default Kyto brand tokens (override with client brand if provided)
- [skills/slide-deck/SKILL.md](skills/slide-deck/SKILL.md) — Slide deck generation skill (visual components, navigation, design system)
- [skills/frontend-design/SKILL.md](skills/frontend-design/SKILL.md) — Frontend design skill (UI quality, aesthetics, no AI slop)

## Process

### Step 1: Discovery

If the user provides a website URL, scrape it to extract:
- Company name, industry, and business model
- Countries of operation
- Products/services
- Visual brand (colors, fonts, logo) — check CSS variables, meta tags, and stylesheets

Then ask the user these questions using AskUserQuestion (one round):

**Round 1: Client & Audience**
1. Confirm: Is this the correct company? [show what you scraped]
2. How many attendees and from which areas? (Ops, Finance, Sales, HR, Tech, etc.)
3. What is their AI experience level? (Never used / Basic / Intermediate / Advanced)
4. Do you have a pre-course survey CSV? If so, share it.

**Round 2: Content & Brand**
1. Instructor names and roles for the intro slide
2. Number of total sessions in the program and what each covers (default: 4)
3. Brand: use Kyto brand, client brand (from website scrape), or custom? If custom, provide brand JSON.
4. Any specific exercises, use cases, or pain points to prioritize?

**Round 3: Logistics**
1. Where should output files go? (default: `Work files/`)
2. Deploy to Vercel? If yes, project name.
3. Any specific companies/prospects to use in the Deep Research exercise?

### Step 2: Generate Demo Data

Create 3-5 synthetic data files using Python (csv module, random with seed). The files must be **tailored to the client's industry and operations** — not every client is a logistics company. The goal is to create data that:
- Feels real to the attendees (uses their terminology, their KPIs, their pain points)
- Has embedded anomalies and patterns for Gemini to discover during exercises
- Is complex enough to show value but not so large that it overwhelms

**Discovery determines the files.** Based on what you learned about the client in Step 1, design the data files. Here are archetypes by industry:

#### Logistics / 3PL / Supply Chain
- Shipment performance data (200 rows): carriers, cities, SLA, delivery times, incidents
- Customer claims/complaints (80 rows): types, severity, amounts, resolution status
- Sales pipeline (30 rows): prospects, stages, contract values
- Operational notes (text): weekly narrative with KPIs, incidents, recommendations

#### Retail / E-commerce
- Sales transactions (200 rows): products, channels, revenue, margins, returns
- Customer feedback/reviews (80 rows): ratings, categories, sentiment, product issues
- Inventory levels (100 rows): SKUs, stock, reorder points, days of supply
- Supplier performance notes (text): delivery reliability, quality issues, negotiations

#### Financial Services / Fintech
- Transaction ledger (200 rows): accounts, amounts, categories, dates, status, anomalies
- Customer support tickets (80 rows): issue types, resolution time, escalations, SLA compliance
- Portfolio/pipeline (30 rows): clients, products, AUM/revenue, risk rating
- Compliance review notes (text): findings, risk assessments, action items

#### SaaS / Technology
- Usage metrics (200 rows): accounts, feature usage, logins, churn signals, MRR
- Support tickets (80 rows): severity, feature area, resolution time, CSAT
- Sales pipeline (30 rows): leads, deal size, stage, win probability
- Product release notes (text): bugs, feature requests, sprint outcomes, customer feedback

#### Healthcare / Pharma
- Patient flow data (200 rows): appointments, wait times, no-shows, procedures, departments
- Quality incidents (80 rows): type, severity, department, resolution, root cause
- Vendor/supplier tracking (30 rows): products, lead times, costs, compliance status
- Clinical operations notes (text): weekly KPIs, staffing, equipment, patient satisfaction

#### Professional Services / Consulting
- Project tracking (200 rows): clients, hours billed, budget vs actual, milestones, overruns
- Client satisfaction surveys (80 rows): project, NPS, comments, follow-up status
- Business development pipeline (30 rows): prospects, proposal stage, deal value
- Account review notes (text): delivery quality, margin analysis, upsell opportunities

#### Custom / Other
If the client doesn't fit these archetypes, design files based on:
1. Their **core operational data** — what do they measure daily?
2. Their **customer/stakeholder interactions** — complaints, feedback, requests
3. Their **sales/growth pipeline** — prospects, deals, conversions
4. Their **narrative reporting** — weekly notes, review docs, operational summaries

**Rules for all demo data:**
- Use the client's language (Spanish/English as appropriate)
- Include real-sounding entity names (companies, products, people) relevant to their market
- Build in 2-3 clear anomalies or patterns that Gemini can discover (a bad performer, a trend, a correlation)
- ~80% of data should look "normal", ~20% should have interesting issues to analyze
- Include enough columns to enable multi-dimensional analysis (cross-tab by category, time, geography, etc.)
- Text files (operational notes) should be 4 weeks of narrative with specific numbers, dates, and actionable recommendations

### Step 3: Build Slide Deck

Generate `presentacion-s1.html` following [reference-slides.md](reference-slides.md).

Apply the brand from Step 1. Use the slide-deck skill for visual components and navigation.

**18 slides organized in sections.** Each section starts with a divider slide that hooks the audience with a data point or teaser. See [reference-slides.md](reference-slides.md) for the full CSS pattern and HTML template for dividers.

**INTRO** (no divider)
1. Title — Workshop name + session + QR to student guide
2. Instructors — Names and roles
3. Program overview — All sessions as cards, S1 highlighted
4. Rules — Workshop rules (no confidentiality bullet)

**SECCIÓN 01 — Cómo funciona la IA**
5. ⬛ Section divider — Hook with stat about AI literacy
6. What is an LLM — Word prediction analogy with animated mystery word + probability bars
7. Memory: "La IA te conoce" — Keynote-style visual: notebook analogy (what it saves vs loses) + two memory levels (global 🌐 vs conversation 💬). Introduces the concept before diving into problems.
8. Memory temporal — Two problems: Lost in the Middle (U-curve) + FIFO (conveyor belt). Deep-dive into conversation-level memory limitations.
9. Hallucinations — 4 mitigation strategies as cards

**SECCIÓN 02 — Prompt Engineering**
10. ⬛ Section divider — Hook about 5 components + 2 hacks
11. Prompt Engineering — 5-component formula + pro tips (dictation + "hazme preguntas" hack)
12. Context Engineering — Bad vs good prompt comparison with checklists. Placed after the formula as an applied example.

**SECCIÓN 03 — Gemini**
13. ⬛ Section divider — Hook: "3 models, 4 superpowers"
14. Gemini models — Flash / Thinking / Pro hierarchy (80% Flash+Thinking, Pro for demanding)
15. Deep Research — "Like hiring an expert researcher" + 3 capability cards
16. Canvas — 4 capabilities (infographics, presentations, podcasts, websites)
17. Connectors + Scheduled Actions — Two-panel comparison with descriptions

**CIERRE** (no divider)
18. Closing — CTA to open Gemini + guide + topic tags

**Technical requirements:**
- Self-contained HTML (inline CSS + JS, Google Fonts via link)
- Arrow key + click navigation, F for fullscreen
- Progress dots + counter
- Fade transition (no translateX — causes back-navigation bugs)
- Mystery word animation cycling through industry-relevant words
- Responsive (works on mobile)

### Step 4: Build Student Guide

Generate `guia-s1.html` following [reference-guide.md](reference-guide.md).

Apply the brand from Step 1. Use frontend-design skill for UI quality.

**Structure:**
- Nav (logo + "GUÍA DEL ESTUDIANTE") + Tab bar (S1 active, S2-S4 placeholders)
- Hero + Outcomes strip + CTA to Gemini
- Section 01: Conceptos Clave (LLM, tokens, hallucinations table, context engineering, Lost in the Middle)
- Section 02: Prompt Engineering (5 components table, El Hack, 4 types table, 5 exercises)
- Section 03: Gemini Models (Flash / Thinking / Pro cards)
- Section 04: Deep Research (2 exercises with downloadable pipeline CSV)
- Section 05: Data Analysis (2 exercises with downloadable CSVs, iteration prompts)
- Section 06: Canvas (2 exercises: SLA report from notes, infographic)
- Section 07: Connectors + Scheduled Actions (cross-app queries, scheduled action examples)
- Session 2-4 placeholders with lock icon
- Footer

**Exercise design rules:**
- Every exercise has a `data-text` attribute on the copy button with the FULL prompt
- Prompts must be non-trivial — contextualized for the client's business
- Include iteration prompts (follow-ups) for data analysis exercises
- Download links point to relative paths (same folder)
- Include anti-hallucination tips in Deep Research exercises

**Technical requirements:**
- Self-contained HTML (inline CSS + JS, Google Fonts via link)
- Tab switching, clipboard API with fallback, rating dots, yes/no buttons
- All CSS classes from [reference-guide.md](reference-guide.md) component library
- Responsive
- Sharp corners (border-radius: 0px) per Kyto brand

### Step 5: Deploy

If the user requested Vercel deployment:
1. Create a `deploy/` folder
2. Copy guide as `index.html` + all demo data files
3. Link to existing Vercel project or create new
4. Deploy with `npx vercel --prod --yes`
5. Return the production URL

### Step 6: Push to Git

If the user requests:
1. Stage all new files (exclude desktop.ini, .pptx)
2. Commit with descriptive message
3. Push to specified remote

## Guardrails

- **Never** include confidential client data in demo files — all data must be synthetic
- **Always** verify Onda de Mar / prospect company names are consistent across guide + CSV + script
- **Always** use the correct model names: Gemini 3.1 Pro, Claude 4.6 Opus/Sonnet, ChatGPT 5.4
- **Always** present models as Flash < Thinking < Pro (Pro is frontier, 80% of tasks = Flash/Thinking)
- **Never** claim one model has a larger context window than others — all leaders are at ~1M tokens
- **Never** use border-radius > 0px (Kyto brand = sharp corners)
- **Always** test navigation forward AND backward before delivering the slide deck
- **Always** run a sanity check: grep for old company names, old model names, inconsistent S4 descriptions
