# Brand Reference — Default (Kyto)

Override these tokens with the client's brand when provided.

## Design Tokens

```css
:root {
  --bg: #0A0A0C;
  --bg-card: #111111;
  --bg-card-hover: #171717;
  --border: rgba(255,255,255,0.07);
  --border-accent: rgba(68,243,152,0.4);
  --text: #F5F3EF;
  --muted: #86868b;
  --accent: #44F398;
  --accent-glow: rgba(68,243,152,0.12);
  --accent-dim: rgba(68,243,152,0.3);
  --error: #f87171;
  --font-heading: 'Space Grotesk', sans-serif;
  --font-body: 'Inter Tight', sans-serif;
  --font-mono: 'IBM Plex Mono', monospace;
}
```

## Rules

- Border radius: **0px everywhere** (sharp corners)
- Logo text: `kyto<span style="color:var(--accent)">×</span>[client]`
- Buttons: pill shape for CTA (`border-radius: 9999px`), sharp for secondary
- Google Fonts: load via `<link>` tag, no external JS
- Accent color used for: highlights, borders on active elements, callout borders, progress indicators
- Error color (#f87171) used for: bad examples, crossed-out elements, warning states

## Brand JSON Structure (when client provides)

```json
{
  "colors": {
    "primary": "#44F398",
    "background": "#0A0A0C",
    "text": "#F5F3EF"
  },
  "fonts": {
    "heading": "Space Grotesk",
    "body": "Inter Tight",
    "mono": "IBM Plex Mono"
  },
  "images": {
    "logo": "url-or-text"
  },
  "borderRadius": "0px"
}
```
