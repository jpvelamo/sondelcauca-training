# Slide Deck Reference — Session 1

## Technical Spec

- Self-contained HTML file (inline CSS + JS)
- Google Fonts via `<link>` (Space Grotesk, Inter Tight, IBM Plex Mono)
- Navigation: arrow keys, spacebar, click (right half = next, left half = prev), F = fullscreen
- Progress dots at bottom center, slide counter at bottom right
- Logo watermark top-left (low opacity)
- Keyboard hints bottom-left
- **Transition: opacity fade only** (no translateX — causes back-navigation bugs)
- Auto-hide cursor after 3s of inactivity
- Responsive: stack grids on mobile, reduce font sizes

## Slide Navigation JS Pattern

```javascript
// IMPORTANT: simple fade only, no prev/next transforms
function goTo(n) {
  if (n < 0 || n >= total) return;
  slides[current].classList.remove('active');
  current = n;
  slides.forEach(s => s.classList.remove('active'));
  slides[current].classList.add('active');
  updateUI();
}
```

## Visual Components

Each slide MUST have a visual component. Never just text on dark.

| Component | CSS Pattern | Use for |
|-----------|------------|---------|
| Card grid | `.card-grid .g2/.g3/.g4` | Categories, features, comparisons |
| Big stat | `.big-stat` + `.stat-label` | Impressive numbers |
| Flow diagram | `.flow` + `.flow-step` + `.flow-arrow` | Processes, timelines |
| Comparison panel | `.compare` + `.compare-panel` | Side-by-side (before/after, pros/cons) |
| Bullet list | `.bullet-list` + `.bl-icon` | Quick facts, rules |
| Formula | `.formula` + `.formula-part` + `.formula-op` | Component breakdowns |
| Callout | `.callout` | Key insights, tips, examples |
| Probability bars | Inline flex + width% | LLM prediction visual |
| U-curve chart | Inline flex + height% | Lost in the Middle visual |
| FIFO conveyor | Inline flex + strikethrough | Memory deletion visual |
| Section divider | `.slide.divider` | Section transitions with hooks |

## Section Divider Component

The deck is organized into sections. Each section starts with a **divider slide** that gives the audience a mental map of what's coming and hooks their attention with a data point or teaser.

### CSS

```css
.slide.divider { justify-content: center; }
.divider-num { font-family: var(--font-m); font-size: 13px; letter-spacing: 0.15em; text-transform: uppercase; color: var(--green); margin-bottom: 16px; opacity: 0.7; }
.divider-title { font-family: var(--font-h); font-weight: 700; font-size: 56px; letter-spacing: -0.03em; text-align: center; line-height: 1.1; }
.divider-hook { font-size: 18px; color: var(--muted); margin-top: 20px; text-align: center; max-width: 550px; line-height: 1.6; }
.divider-hook strong { color: var(--text); }
.divider-line { width: 60px; height: 3px; background: var(--green); margin-top: 28px; }
```

### HTML Pattern

```html
<div class="slide divider">
  <div class="divider-num">Sección 0N</div>
  <div class="divider-title">Section <span class="accent">Title</span></div>
  <div class="divider-hook">A compelling hook — a stat, a question, or a teaser. <strong>The bold part is the payoff.</strong></div>
  <div class="divider-line"></div>
</div>
```

### Rules for section divider hooks
- Use a **data point, stat, or surprising fact** when possible (e.g., "72% of AI users...")
- Or a **teaser of what they'll learn** (e.g., "5 components and 2 hacks you can apply today")
- The `<strong>` part is the payoff — the reason they should care
- Keep it to 1-2 sentences max
- The divider-line is a short green accent bar that anchors the slide visually

## 18-Slide Narrative Arc (with section dividers)

### INTRO (no divider — starts immediately)

#### Slide 1 — Title
- Big title: workshop name
- Subtitle: "Sesión 1" + topic
- Badges: "100% PRÁCTICO" + "4 SESIONES"
- QR code to student guide (if deployed)

#### Slide 2 — Instructors
- 2 cards side by side with names + roles
- Subtitle: company description

#### Slide 3 — Program Overview
- 4 cards showing all sessions, S1 highlighted with accent border
- S4 = "Proyecto Final" (not Claude Cowork)

#### Slide 4 — Rules
- Bullet list with emoji icons
- DO NOT include confidentiality bullet
- Include: cameras on, mute, ask anytime, corporate account, experiment

---

### SECTION 01 — Cómo funciona la IA

#### Slide 5 — Section Divider
- Title: "Cómo funciona **la IA**"
- Hook: Data point about AI literacy + teaser of the 4 concepts coming

#### Slide 6 — What is an LLM
- Word blocks from client's domain + animated mystery word
- Probability bars (3 options with %)
- Insight: "doesn't know — learned that after those words, X appears Y% of the time"
- JS: mystery word cycles through alternatives every 2s

#### Slide 7 — Memory: "La IA te conoce — más o menos"
- **Keynote-style visual, minimal text.** Narrative: the AI remembers things about you across conversations, but imperfectly — like taking notes in class.
- Left: "notebook" visual with green checkmarks (what it saves: role, language preference) and red crosses with strikethrough (what it loses: specific data, past conversations)
- Arrow pointing right
- Right: two stacked cards for the two memory levels:
  - 🌐 **Memoria global** — persists between chats (name, role, language)
  - 💬 **Memoria de conversación** — lives within the chat, rich but temporary
- Callout: "Si un dato es clave, inclúyelo en el prompt."
- **This slide introduces the concept of memory. The next slide deep-dives into the conversation-level memory problems.**

#### Slide 8 — Memory temporal (Lost in the Middle + FIFO)
- Two cards side by side:
  - Left: U-curve chart (7 bars, high-low-high) with labels Inicio✅ Medio❌ Final✅ — "Perdidos en el medio"
  - Right: FIFO conveyor belt (old messages crossed out, scissors, new messages) — "lo viejo se borra"
- Two callout tips at bottom: "Lo importante va en los extremos" + "Chat nuevo para cada tema"

#### Slide 9 — Hallucinations
- 4 mitigation strategy cards (2x2): give real data, ask for sources, use Deep Research, verify critical info
- Callout: "Use AI to generate, not to decide"

---

### SECTION 02 — Prompt Engineering

#### Slide 10 — Section Divider
- Title: "Prompt **Engineering**"
- Hook: Teaser about 5 components + 2 hacks that transform results

#### Slide 11 — Prompt Engineering Formula
- Formula: Rol + Propósito + Contexto + Restricciones + Output = Buen prompt
- Two callout tips: dictation + "hazme preguntas" hack

#### Slide 12 — Context Engineering
- Side-by-side: bad prompt vs good prompt
- Bad: short vague prompt + 4 red ✗ marks
- Good: full contextual prompt with green-highlighted components + 4 green ✓ marks
- **Placed after Prompt Engineering formula as an applied example of what good context looks like in practice.**

---

### SECTION 03 — Gemini

#### Slide 13 — Section Divider
- Title: "**Gemini**"
- Hook: "3 models, 4 superpowers" + teaser about the AI team inside Google Workspace

#### Slide 14 — Gemini Models
- 3 cards: Flash / Thinking / Pro (Pro highlighted with accent border)
- Flash: fastest, simple tasks
- Thinking: Flash+Pro mix, reasons before answering
- Pro: frontier model, most powerful
- Callout: "80% Flash/Thinking, Pro for demanding"

#### Slide 15 — Deep Research
- Description: "Like hiring an expert researcher"
- 3 cards: navigates web, report with sources, ready to use
- Callout with example

#### Slide 16 — Canvas
- Description: "Your AI designer"
- 4 cards: infographics, presentations, podcasts, websites

#### Slide 17 — Connectors + Scheduled Actions
- Description explaining both concepts
- Two comparison panels: Connectors (5 apps) / Scheduled Actions (3 example prompts)

---

### CLOSING (no divider)

#### Slide 18 — Closing
- "Hora de practicar"
- CTA box with Gemini URL
- Topic tags at bottom
