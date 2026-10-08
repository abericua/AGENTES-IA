## 2024-09-13 - Semantic HTML for Forms
**Learning:** Stylized `<div>` elements used as labels limit accessibility. Screen readers cannot properly associate them with input fields, and users cannot click them to focus the inputs.
**Action:** Always use semantic `<label>` elements with `for` attributes that correspond to the `id` of the respective input elements to ensure they are accessible.
## 2024-10-01 - ARIA roles for dynamic custom UI feedback
**Learning:** For dynamic progress indicators (`#pg`) and real-time chat updates (`#chat`), visually indicating state change isn't enough for screen readers. They need explicit roles and `aria-live` attributes to notify users when content changes dynamically without explicit focus changes.
**Action:** Always add `role="progressbar"`, `aria-valuenow`, `aria-valuemin`, and `aria-valuemax` to custom progress components and ensure `aria-valuenow` updates dynamically. Use `aria-live="polite"` for status indicators and `role="log"` for chat/console output elements.
## 2024-10-08 - Keyboard accessibility with custom cursors
**Learning:** The use of `cursor: none` with custom DOM-based cursors can override or obscure native focus behaviors for keyboard-only users, as they may rely on native focus outlines that sometimes get disrupted or aren't distinct enough against custom backgrounds.
**Action:** Always provide explicit `:focus-visible` styles with prominent outlines (`outline`, `outline-offset`) on interactive elements (`button`, `input`, `textarea`) in apps using custom cursors to ensure keyboard navigation remains clearly visible.
