## 2024-09-13 - Semantic HTML for Forms
**Learning:** Stylized `<div>` elements used as labels limit accessibility. Screen readers cannot properly associate them with input fields, and users cannot click them to focus the inputs.
**Action:** Always use semantic `<label>` elements with `for` attributes that correspond to the `id` of the respective input elements to ensure they are accessible.
## 2024-10-01 - ARIA roles for dynamic custom UI feedback
**Learning:** For dynamic progress indicators (`#pg`) and real-time chat updates (`#chat`), visually indicating state change isn't enough for screen readers. They need explicit roles and `aria-live` attributes to notify users when content changes dynamically without explicit focus changes.
**Action:** Always add `role="progressbar"`, `aria-valuenow`, `aria-valuemin`, and `aria-valuemax` to custom progress components and ensure `aria-valuenow` updates dynamically. Use `aria-live="polite"` for status indicators and `role="log"` for chat/console output elements.
## 2024-11-20 - Custom Cursor Keyboard Accessibility
**Learning:** The frontend UI uses a custom cursor design (`cursor: none`), which makes explicit `:focus-visible` styles crucial for maintaining keyboard navigation accessibility. Without default browser outlines or explicit styles, users navigating via keyboard cannot see which element has focus.
**Action:** Always add manual `:focus-visible` styles (e.g. `outline`, `outline-offset`, or `box-shadow`) to all interactive elements (`button`, `input`, `textarea`, `a`) when implementing custom cursors or disabling default pointer events.
