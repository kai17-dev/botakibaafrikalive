# Font Update Plan

## Task
- **Headings** → `'Lemon Milk', Arial, sans-serif`
- **Body text** → `'Avernire Medium', Arial, sans-serif`

## Steps

### Step 1: Add @font-face declarations to all pages
Add font-face blocks for both custom fonts (assuming font files in `/public/fonts/`).

### Step 2: Update font-family in all 10 pages
| File | Body current | Headings current | Action |
|------|-------------|------------------|--------|
| `src/pages/index.astro` | 'Lemon Milk' | 'Lemon Milk' | Body→Avernire Medium, Headings keep Lemon Milk |
| `src/pages/disciplines.html` | 'Helvetica Neue' | inherited | Body→Avernire Medium, add Lemon Milk to headings |
| `src/pages/about.html` | 'Helvetica Neue' | inherited | Body→Avernire Medium, add Lemon Milk to headings |
| `src/pages/abouT.astro` | 'Helvetica Neue' | inherited | Body→Avernire Medium, add Lemon Milk to headings |
| `src/pages/crafts.html` | 'Helvetica Neue' | inherited | Body→Avernire Medium, add Lemon Milk to headings |
| `src/pages/literature.html` | 'Helvetica Neue' | inherited | Body→Avernire Medium, add Lemon Milk to headings |
| `src/pages/music.html` | 'Helvetica Neue' | inherited | Body→Avernire Medium, add Lemon Milk to headings |
| `src/pages/visualArts.html` | 'Helvetica Neue' | inherited | Body→Avernire Medium, add Lemon Milk to headings |
| `src/pages/bloG.html` | 'Helvetica Neue' | inherited | Body→Avernire Medium, add Lemon Milk to headings |
| `src/layouts/Layout.astro` | none set | none set | Add Avernire Medium to body, Lemon Milk to headings |

### Step 3: Verify changes
- [x] index.astro
- [x] disciplines.html
- [x] about.html
- [x] abouT.astro
- [x] crafts.html
- [x] literature.html
- [x] music.html
- [x] visualArts.html
- [x] bloG.html
- [x] Layout.astro

