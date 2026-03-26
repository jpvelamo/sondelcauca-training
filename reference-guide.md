# Student Guide Reference — Session 1

## Technical Spec

- Self-contained HTML (inline CSS + JS, Google Fonts via link)
- Scrollable single-page website with tab bar for sessions
- Session 1 = full content; Sessions 2-4 = placeholders with lock icon
- Responsive (mobile-friendly)
- All CSS uses brand tokens via CSS variables

## CSS Component Library

All components use 0px border-radius (Kyto brand). Use these class names consistently:

### Layout
- `.container` — max-width 880px centered
- `nav` — sticky top, blur backdrop
- `.tab-bar` — sticky below nav, session tabs
- `.session-panel` / `.session-panel.active` — show/hide sessions
- `section` — 60px padding, border-top between sections

### Hero
- `.hero` — centered with radial gradient background glow
- `.hero-eyebrow` — flex with badges
- `.hero h1` — clamp(30px, 5vw, 52px)
- `.hero-sub` — muted subtitle
- `.hero-date` — mono uppercase date line

### Cards & Content
- `.badge` / `.badge-muted` — mono uppercase tags
- `.outcomes` / `.outcomes-grid` / `.outcome-card` — strip with icon + text cards
- `.cta-link` — pill-shaped green button
- `.section-header` / `.section-number` / `.section-title` / `.section-desc`
- `.table-wrap` / `table` — bordered responsive table
- `.tip-box` / `.tip-label` — green left-border callout
- `.hack-box` / `.hack-label` — accent left-border quote box
- `.gem-grid` / `.gem-card` / `.gem-area` / `.gem-name` / `.gem-desc` — feature cards
- `.formula-box` / `.formula` / `.part` / `.eq` — horizontal formula

### Exercises
- `.exercise-card` — bordered card with hover effect
- `.exercise-header` / `.exercise-num` / `.exercise-title`
- `.exercise-body` — content area
- `.exercise-prompt` — dark background italic text block with copy button
- `.prompt-inner` — padded text inside prompt (leaves room for copy button)
- `.example-block` — accent background example within prompt
- `.copy-btn` — absolute positioned top-right, with `data-text` attribute for full prompt text
- `.tool-tag` — accent tag showing which Gemini feature to use
- `.download-grid` / `.download-card` / `.dl-icon` / `.dl-name` — file download cards
- `.iteration-list` / `.iteration-item` / `.iter-num` — numbered follow-up prompts
- `.step-list` / `.step-num` — numbered instruction steps

### Interactive
- `.rating-row` / `.rating-dots` — 1-5 rating circles
- `.yesno` — yes/no button pair

## Section Structure

### 01 — Conceptos Clave
Content (no exercises):
- ¿Qué es un LLM? — Prediction explanation
- Memoria de la IA — Two levels: (1) Memoria global (persists between chats: name, role, preferences — like taking notes in class, saves what it considers important but much is lost), (2) Memoria de conversación (ventana de contexto, lives within a single chat, rich but temporary)
- Tokens y ventana de contexto — Table comparing Gemini 3.1 Pro, Claude 4.6 Opus/Sonnet, ChatGPT 5.4 (all 1M tokens) + two problems: Lost in the Middle + FIFO
- Alucinaciones — Table with 5 mitigation strategies (dale datos reales, pide fuentes, usa Deep Research, verifica lo crítico, pide que diga "no sé")
- Ingeniería de contexto — Explanation + bad vs good prompt comparison

### 02 — Prompt Engineering
Content + 5 exercises:
- 5 components table (Rol, Propósito, Contexto, Restricciones, Output)
- Pro tip: DICTA no escribas
- El Hack (copyable)
- 4 types table (Zero Shot, Few Shot, Chain of Thought, Role Playing)
- EJ 1.1: Zero Shot — generic industry question
- EJ 1.2: Few Shot — classify operational incidents with example format
- EJ 1.3: Chain of Thought — step-by-step SLA analysis
- EJ 1.4: Role Playing — VP of Ops scenario
- EJ 1.5: Your own prompt + El Hack

### 03 — Gemini Models
Content (no exercises):
- 3 gem-cards: Flash (fast), Thinking (Flash+Pro mix), Pro (frontier, highlighted)
- Tip: 80% Flash/Thinking, Pro for demanding

### 04 — Deep Research
2 exercises — adapt to the client's business:
- EJ 4.1: **Research exercise** — Investigate a real prospect, competitor, or entity relevant to the client. Include downloadable pipeline/prospect CSV if applicable. Always include anti-hallucination tip ("open at least 2 sources to verify").
  - Logistics: Sales research on a prospect brand
  - Retail: Competitor analysis of a similar brand
  - Finance: Research a regulatory change or market trend
  - SaaS: Research a potential integration partner or competitor
  - Healthcare: Research a treatment protocol or supplier
- EJ 4.2: **Industry intelligence** — Broader research on trends, competitive landscape, or market opportunities in the client's sector

### 05 — Data Analysis
2 exercises with iteration prompts — use the demo data files from Step 2:
- EJ 5.1: **Primary dataset analysis** — The largest CSV (~200 rows). Ask Gemini for anomalies, patterns, trends, and top 3 critical findings. Include 3 iteration prompts: (1) visualization request, (2) draft a communication based on findings, (3) projection or what-if analysis.
- EJ 5.2: **Secondary dataset analysis** — The complaints/tickets/feedback CSV (~80 rows). Ask for distribution by type, worst performers, correlations, and action plan. Include 1 iteration prompt: draft a stakeholder communication.

### 06 — Canvas
2 exercises — adapt to the client's output needs:
- EJ 6.1: **Report from narrative notes** — Use the operational notes TXT file. Generate a formal report (SLA report, quarterly review, compliance summary, project status — whatever fits the client). Include 2 iterations: add comparative data, translate executive summary.
- EJ 6.2: **Infographic** — Visualize a core process or workflow from the client's business (fulfillment flow, patient journey, sales funnel, product lifecycle, etc.)

### 07 — Connectors + Scheduled Actions
2 exercises — these are universal regardless of industry:
- EJ 7.1: Cross-app queries (Drive, Gmail, Calendar) — contextualize the example queries to the client's daily work
- EJ 7.2: Scheduled actions (2 example prompts relevant to their roles + tip to start simple)

## Exercise Design Rules

1. Every copy-btn has `data-text` with the COMPLETE prompt (not abbreviated)
2. Prompts are contextualized to the client's business — never generic
3. Include iteration prompts for data analysis exercises (show the power of follow-up)
4. Download links use relative paths (files in same folder)
5. Deep Research exercises include anti-hallucination tips
6. The visible prompt-inner text can be abbreviated, but data-text is always the full prompt

## JavaScript Patterns

```javascript
// Tab switching
document.querySelectorAll('.tab').forEach(tab => {
  tab.addEventListener('click', () => {
    const s = tab.dataset.session;
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.session-panel').forEach(p => p.classList.remove('active'));
    tab.classList.add('active');
    document.querySelector(`.session-panel[data-session="${s}"]`).classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
});

// Copy buttons — clipboard API with execCommand fallback
// Rating dots — toggle style on click
// Yes/No buttons — toggle active state
```

## Placeholder Pattern (Sessions 2-4)

```html
<div class="session-panel" data-session="N">
  <div class="coming-soon">
    <div class="cs-icon">🔒</div>
    <h2><span class="gradient-text">[Session Title]</span></h2>
    <p>[Brief description of session content]</p>
    <p style="...">Se habilitará antes de la sesión N</p>
  </div>
</div>
```
