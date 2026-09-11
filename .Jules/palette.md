## 2026-09-11 - Semantic Forms
**Learning:** Discovered a pattern of using stylized `<div>` elements as labels for inputs in `solpro_ui.html`. While visually identical, this breaks accessibility as screen readers cannot associate the text with the input, and users miss out on an expanded clickable area.
**Action:** Replaced `<div class="lbl">` with semantic `<label class="lbl" for="[id]">` and set CSS to `display: block;` to preserve the layout. Will prioritize semantic HTML tags over divs for form fields.
