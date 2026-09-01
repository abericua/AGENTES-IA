## 2026-09-01 - Semantic Form Labels Replace Divs
**Learning:** Found a pattern where non-semantic `div.lbl` elements were used visually as form labels without being linked to the inputs.
**Action:** Always prefer `<label for="...">` over `<div>` for accessibility purposes and improved UX, such as allowing screen readers to associate text with inputs, as well as providing click-to-focus on the label.
