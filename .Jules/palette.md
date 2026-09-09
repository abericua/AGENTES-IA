## 2026-09-09 - [Semantic Forms]
**Learning:** Found an accessibility issue pattern where inputs used visually styled `<div>` elements instead of `<label>` tags. This prevents screen readers from associating the label with the input field.
**Action:** Always use semantic `<label>` tags with a `for` attribute matching the input's `id`. If a block layout is needed, apply `display: block;` to the label via CSS.
