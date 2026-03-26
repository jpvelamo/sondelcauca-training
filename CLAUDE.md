# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A skill-driven generator for Session 1 of Kyto's AI & Automation workshops. Given a client profile, it produces three deliverables: an 18-slide HTML presentation, an interactive student guide (scrollable HTML website with copyable prompts), and 3-5 synthetic demo data files — all contextualized to the client's industry.

## Architecture

The repo is a **skill chain**, not a traditional app. There is no build step, package manager, or test suite.

- `SKILL.md` (root) — Master orchestrator. Defines the end-to-end process: discovery → demo data → slides → guide → deploy. References all other files.
- `reference-slides.md` — Spec for the 18-slide deck: narrative arc, section dividers, visual components (card grids, U-curves, FIFO conveyor, probability bars), CSS patterns, and JS navigation.
- `reference-guide.md` — Spec for the student guide: 7 sections, CSS component library (exercises, copy buttons, download cards, rating dots), JS patterns (tabs, clipboard API).
- `reference-brand.md` — Default Kyto brand tokens (CSS variables). Overridden per-client.
- `skills/slide-deck/SKILL.md` — Sub-skill for generic slide deck generation (design system, navigation, visual components).
- `skills/frontend-design/SKILL.md` — Sub-skill for UI quality (anti-AI-slop aesthetics, typography, motion, spatial composition).

**How they compose**: The master `SKILL.md` drives the process. It calls `reference-slides.md` + `skills/slide-deck/SKILL.md` when building the deck, and `reference-guide.md` + `skills/frontend-design/SKILL.md` when building the guide. Brand tokens from `reference-brand.md` apply to both.

## Common Commands

```bash
# Deploy guide to Vercel (after generating assets into deploy/)
npx vercel --prod --yes

# Sanity check: find leftover placeholders or old client names
grep -r "CLIENT_NAME\|PLACEHOLDER\|Melonn" "Work files/"

# Generate demo data (Python, uses csv + random with seed)
python generate_data.py
```

## Output Files

All deliverables go to `Work files/` (or `deploy/` for Vercel):
- `presentacion-s1.html` — Self-contained slide deck (inline CSS/JS, Google Fonts via link)
- `guia-s1.html` — Self-contained student guide (same pattern)
- `*.csv` / `*.txt` — Demo data files referenced by guide exercises via relative paths

## Key Technical Constraints

- All HTML deliverables are **single-file, self-contained** (inline CSS + JS, no external deps except Google Fonts)
- Slide navigation uses **opacity fade only** — no translateX (causes back-navigation bugs)
- Copy buttons use `data-text` attribute for the full prompt, not the visible abbreviated text
- Download links in the guide use **relative paths** (files must be co-located)
- Kyto brand: `border-radius: 0px` everywhere (sharp corners), pill shape only for CTA buttons

---

> **Template below**: Copy this repo to bootstrap a new S1 workshop. Placeholders get filled during initialization.

## Initialization Protocol

At the start of the FIRST conversation in this project, run this discovery flow before doing anything else. Do NOT skip steps. Do NOT start generating assets until all steps are complete.

### Step 0: Read the Skill

Read `SKILL.md` and all its reference files (`reference-slides.md`, `reference-guide.md`, `reference-brand.md`). These contain the proven structure, narrative arc, visual components, and exercise design patterns. Everything you generate must follow these specs.

### Step 1: Discovery — Ask the User

Ask ALL of the following in a single message. Do not split across multiple turns. Wait for the user to answer everything before proceeding.

**Client & Audience**
1. Company name and website URL (I'll scrape it for brand, industry, and business context)
2. How many attendees and from which areas? (Ops, Finance, Sales, HR, Tech, Customer Service, etc.)
3. AI experience level of attendees — never used / basic / intermediate / advanced
4. Do you have a pre-course survey CSV? If yes, share it. If not, what are their top 3 pain points?

**Content & Program**
5. Instructor names and roles for the intro slide
6. Number of sessions and what each covers (default: 4 — IA+Prompting+Gemini, Google AI Ecosystem, n8n Automation, Claude Code+Agents)
7. Any specific exercises, use cases, or pain points to prioritize?
8. Any real company/prospect/competitor to use in the Deep Research exercise?

**Brand & Logistics**
9. Brand: Kyto brand (default), client brand (I'll extract from website), or custom JSON?
10. Deploy student guide to Vercel? If yes, project name.
11. Any specific companies or prospect names to use in demo data?

### Step 2: Scrape & Confirm

If a website URL was provided:
1. Scrape it to extract: company name, industry, business model, countries, products/services
2. Extract visual brand: colors, fonts, logo from CSS/meta tags
3. Present a summary to the user and ask them to confirm or correct

### Step 3: Fill the Project Context

Once the user confirms, fill in ALL the placeholders in this file (the sections below) and rewrite this CLAUDE.md with the real values. Remove the initialization protocol section — it's no longer needed after first run.

Then proceed to Step 4.

### Step 4: Generate Assets

Follow the process in `SKILL.md`:
1. Generate demo data files (tailored to the client's industry)
2. Build slide deck (`presentacion-s1.html`) — 18 slides per `reference-slides.md`
3. Build student guide (`guia-s1.html`) — per `reference-guide.md`
4. Deploy if requested
5. Commit if requested

---

## What This Repository Is

Workshop materials for **Son del Cauca** — a 4-session AI & Automation training delivered by Kyto for Son del Cauca, a Colombian agribusiness company specializing in citrus commercialization (Tahiti lime, Valencia orange), reforested wood (Melina, Teca), and African oil palm, operating in Antioquia and Córdoba, Colombia. The repo contains presentations, student guides, and demo data files.

## Project Structure

```
S1 - Son del Cauca/
├── SKILL.md                    # Master orchestrator skill (do not modify)
├── reference-slides.md         # Slide deck spec (do not modify)
├── reference-guide.md          # Student guide spec (do not modify)
├── reference-brand.md          # Brand tokens (do not modify)
├── skills/                     # Sub-skills (do not modify)
│   ├── slide-deck/SKILL.md
│   └── frontend-design/SKILL.md
├── data/                       # Input data (survey, branding, scrape)
├── output/                     # Deliverables (active work)
│   ├── presentacion-s1.html
│   ├── guia-s1.html
│   └── *.csv / *.txt
└── deploy/                     # Vercel deploy folder
```

## Client Profile

- **Company**: Son del Cauca
- **Industry**: Agroindustria — comercialización de cítricos, madera reforestada, palma africana
- **Business model**: Producción propia + aliados (pequeños/medianos productores), empaque con tecnología de punta, exportación
- **Countries**: Colombia (Antioquia, Córdoba)
- **Products/Services**: Limón Tahití (850ha, 20k ton/año), Naranja Valencia (350ha, 12k ton/año), Madera Melina/Teca, Palma africana

## Audience Profile

- **Attendees**: 15 people
- **Areas**: Finanzas/Contabilidad (5), Operaciones (4), Dirección (2), Ventas (1), RRHH (1), Agronomía (1), Admin (1)
- **AI experience**: Básico/principiante (1 avanzado)
- **Key pain points**: Digitación de facturas, informes para junta directiva desde múltiples fuentes, análisis de datos operativos, registro de labores de campo, redacción de correos, informes en Excel
- **Survey data**: Yes — `data/SON DEL CAUCA - Encuesta curso IA y Automatizaciones_Submissions_2026-03-26.csv`

## Program Plan

| Session | Topic | Status |
|---------|-------|--------|
| S1 | IA + Prompting + Gemini | In progress |
| S2 | Google AI Ecosystem | Placeholder |
| S3 | Make (formerly Integromat) Automation | Placeholder |
| S4 | Proyecto Final | Placeholder |

## Instructors

- Kawa — Co-founder, Kyto
- JP — Co-founder, Kyto

## Brand

- **Source**: Kyto
- **Primary color**: #44F398 (green)
- **Background**: #0A0A0C (dark)
- **Fonts**: Space Grotesk / Inter Tight / IBM Plex Mono
- **Border radius**: 0px (sharp corners)
- **Logo**: kyto×sondelcauca

## Demo Data Design

Files tailored to Son del Cauca's citrus agribusiness operations:

| File | Description | Rows | Purpose |
|------|-------------|------|---------|
| operaciones-fincas.csv | Producción semanal por finca/lote: toneladas, rendimiento, calidad, lluvia, incidencias | ~200 | Primary dataset for analysis exercises |
| reclamos-calidad.csv | Reclamos de clientes: fruta, calibre, destino, severidad, resolución | ~80 | Secondary dataset (quality complaints) |
| pipeline-exportacion.csv | Prospectos de exportación: país, fruta, volumen, etapa, valor | ~30 | Pipeline for Deep Research exercises |
| notas-operativas.txt | Resumen semanal del Dir. Operativo: KPIs, incidencias, clima, recomendaciones | 4 weeks | Narrative notes for Canvas report exercise |

## Key Decisions

- **Two deliverables per session**: slide deck (for presenting) + student guide (scrollable website with exercises)
- **Demo data**: Synthetic but realistic, contextualized for Son del Cauca's citrus operations
- **Exercises**: Non-trivial, grounded in real Son del Cauca workflows (cosechas, calidad, exportación)
- **Deep Research target**: Frudelca (https://www.frudelca.com/) — competitor in Colombian citrus

## Guardrails

- **Never** include confidential client data — all data must be synthetic
- **Always** verify Son del Cauca / Frudelca entity names are consistent across guide + CSV + slides
- **Always** use correct model names: Gemini 3.1 Pro, Claude 4.6 Opus/Sonnet, ChatGPT 5.4
- **Always** present models as Flash < Thinking < Pro (80% of tasks = Flash/Thinking)
- **Never** claim one model has a larger context window — all leaders are at ~1M tokens
- **Never** use border-radius > 0px unless client brand requires it
- **Always** test slide navigation forward AND backward before delivering
- **Always** run sanity check: grep for placeholder text, old client names, inconsistent session descriptions
