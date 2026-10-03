## 2024-09-13 - Semantic HTML for Forms
**Learning:** Stylized `<div>` elements used as labels limit accessibility. Screen readers cannot properly associate them with input fields, and users cannot click them to focus the inputs.
**Action:** Always use semantic `<label>` elements with `for` attributes that correspond to the `id` of the respective input elements to ensure they are accessible.
## 2024-10-01 - ARIA roles for dynamic custom UI feedback
**Learning:** For dynamic progress indicators (`#pg`) and real-time chat updates (`#chat`), visually indicating state change isn't enough for screen readers. They need explicit roles and `aria-live` attributes to notify users when content changes dynamically without explicit focus changes.
**Action:** Always add `role="progressbar"`, `aria-valuenow`, `aria-valuemin`, and `aria-valuemax` to custom progress components and ensure `aria-valuenow` updates dynamically. Use `aria-live="polite"` for status indicators and `role="log"` for chat/console output elements.
## 2024-10-03 - Explicit Focus Styles for Custom Cursors
**Learning:** When using a custom cursor via `cursor: none`, the browser's default keyboard focus outlines might not be sufficient or visually consistent, which can cause keyboard navigation users to lose track of the current focus.
**Action:** Always explicitly define `:focus-visible` styles with a clear outline (e.g., `outline: 2px solid var(--acc); outline-offset: 2px;`) for all interactive elements like `button`, `input`, and `textarea`.