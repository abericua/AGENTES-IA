## 2026-09-07 - Semantic HTML for Form Labels
**Learning:** Found a pattern of using `<div>` elements styled as labels instead of semantic `<label>` elements, breaking screen reader association with inputs.
**Action:** Replaced `<div>` with `<label for="...">` and ensured the CSS class has `display: block;` to preserve layout without introducing new classes or dependencies.
