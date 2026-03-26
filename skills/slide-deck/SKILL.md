---
name: slide-deck-generator
description: >
  Generate a full visual HTML slide deck from a topic or brief. Use this skill when the user says
  "make a presentation", "create slides", "slide deck", "build a deck about", "presentation on",
  "I need to present", or any variation of wanting a visual presentation generated.
---

# Slide Deck Generator

You create polished, visual HTML slide decks that look professional and are ready to present directly from a browser. These are not bullet-point-on-white slides — they use rich visual components to tell a compelling story.

## Process

### Step 1: Understand the Ask
Confirm:
- What is the topic or subject?
- Who is the audience? (team, client, investors, class)
- How many slides? (default: 8-12)
- Any specific points that must be included?

If the user gives a clear topic, skip questions and start building.

### Step 2: Plan the Narrative
Before writing any HTML, outline the slides:
- What story are you telling?
- What is the hook on slide 1?
- What is the key takeaway?
- Each slide = one idea, one visual

### Step 3: Build the Deck

Generate a single self-contained HTML file. All CSS in `<style>`, all JS in `<script>`. No external dependencies.

**Design System:**
```
Background: #0a0a0a
Primary text: #f5f5f7 (weight 400)
Bold text: #fff (weight 700)
Secondary text: #86868b
Font: -apple-system, BlinkMacSystemFont, 'SF Pro Display', sans-serif
Card background: rgba(255,255,255,0.04)
Card radius: 20px
Accent: #DA7756
```

**Visual Components Available:**
- **Big stat** — large number + label (for impressive data points)
- **Comparison panel** — side-by-side with labels (for before/after, pros/cons)
- **Card grid** — 2x2, 2x3, or 3x3 icon cards (for categories, features)
- **Flow diagram** — step boxes with arrows (for processes, timelines)
- **Code panel** — monospace text block (for technical content, commands)
- **Bullet list** — icon + text rows (for quick facts)
- **Mockup** — fake UI window with content (for showing tool output)
- **Emoji + text** — large emoji + headline (for emotional or simple concepts)

**Slide text rules:**
- 3-10 words per headline. Less is more.
- Use `<strong>` tags to emphasize 1-2 key words per headline
- One visual component per slide
- Subtext (smaller gray text) for context — one sentence max

**Navigation:**
- Arrow keys (left/right) to navigate
- Space bar or click to advance
- F key for fullscreen
- Double-click for fullscreen
- Progress dots at bottom
- Auto-hide cursor after 3 seconds

### Step 4: Save and Open

Save the HTML file and open it in the browser for the user to review.

## Rules

- Every slide must have a visual component. Never just text on black.
- The first slide is always the hook — make it compelling.
- Maximum 15 slides. If you need more, you're not being concise enough.
- Minimum 5 slides. If you need fewer, the topic might not warrant a deck.
- No external dependencies. Everything is inline in one HTML file.
- The deck should work in any modern browser with no setup.
- Think Apple keynote aesthetic — clean, spacious, high contrast, minimal.
