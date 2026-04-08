# How to Change Colors in Paperclip

## Where Colors Live

All colors are defined in one primary file:

**`ui/src/index.css`**
- Uses Tailwind CSS v4 with `@theme inline` directive (no separate `tailwind.config.js`)
- Colors are CSS custom properties in **OKLCH color space**
- Light mode under `:root { }`, dark mode under `.dark { }`

Supporting files:
- `ui/src/lib/status-colors.ts` — status/priority badge colors
- `ui/src/lib/color-contrast.ts` — accessibility contrast utilities
- `ui/src/lib/worktree-branding.ts` — runtime branding via HTML meta tags

---

## How to Change Colors

### 1. Global Theme Colors (`ui/src/index.css`)

Edit CSS custom properties in `:root` (light mode) or `.dark` (dark mode):

```css
:root {
  --background: oklch(1 0 0);               /* page background */
  --foreground: oklch(0.145 0 0);           /* primary text */
  --primary: oklch(0.205 0 0);              /* buttons, links */
  --primary-foreground: oklch(0.985 0 0);   /* text on primary */
  --secondary: oklch(0.97 0 0);             /* secondary actions */
  --accent: oklch(0.97 0 0);                /* highlights */
  --destructive: oklch(0.577 0.245 27.325); /* error/delete (red) */
  --border: oklch(0.922 0 0);               /* borders */
  --ring: oklch(0.708 0 0);                 /* focus rings */
  --muted: oklch(0.97 0 0);                 /* muted backgrounds */
  --muted-foreground: oklch(0.556 0 0);     /* muted text */
}
```

**OKLCH format:** `oklch(lightness chroma hue)`
- Lightness: 0 = black, 1 = white
- Chroma: 0 = gray, higher = more saturated
- Hue: 0–360 (0/360 = red, 120 = green, 240 = blue)

Example — make primary blue:
```css
--primary: oklch(0.5 0.2 240);
```

### 2. Status & Priority Colors (`ui/src/lib/status-colors.ts`)

Edit the Tailwind class strings in the status/priority maps:

```ts
// Change "todo" from blue to indigo
todo: { icon: "text-indigo-600 dark:text-indigo-400", ... }
```

Statuses: `backlog`, `todo`, `in_progress`, `in_review`, `done`, `cancelled`, `blocked`  
Priorities: `critical`, `high`, `medium`, `low`

### 3. Chart / Data Visualization Colors (`ui/src/index.css`)

Edit `--chart-1` through `--chart-5` in both `:root` and `.dark`.

### 4. Sidebar Colors (`ui/src/index.css`)

Edit the `--sidebar-*` variables.

### 5. Runtime Branding (Worktrees)

Colors can be injected at runtime via HTML `<meta>` tags, handled by `worktree-branding.ts`. No CSS edits needed — just set the meta tag on the page.

---

## Tips

- Always update both `:root` and `.dark` blocks to keep dark mode consistent.
- Components (`button.tsx`, `badge.tsx`, etc.) use Tailwind utilities like `bg-primary` and `text-foreground` — changing the CSS variables propagates everywhere automatically.
- Use an online OKLCH color picker to find values for your target color.

## Verification

```bash
cd ui && npm run dev
```

Open the app and visually check light + dark mode. Verify buttons, badges, borders, and status indicators reflect the new colors.
