## 2024-09-13 - Semantic HTML for Forms
**Learning:** Stylized `<div>` elements used as labels limit accessibility. Screen readers cannot properly associate them with input fields, and users cannot click them to focus the inputs.
**Action:** Always use semantic `<label>` elements with `for` attributes that correspond to the `id` of the respective input elements to ensure they are accessible.
## 2024-10-01 - ARIA roles for dynamic custom UI feedback
**Learning:** For dynamic progress indicators (`#pg`) and real-time chat updates (`#chat`), visually indicating state change isn't enough for screen readers. They need explicit roles and `aria-live` attributes to notify users when content changes dynamically without explicit focus changes.
**Action:** Always add `role="progressbar"`, `aria-valuenow`, `aria-valuemin`, and `aria-valuemax` to custom progress components and ensure `aria-valuenow` updates dynamically. Use `aria-live="polite"` for status indicators and `role="log"` for chat/console output elements.
## YYYY-MM-DD - Custom Cursors and Keyboard Focus
**Learning:** When a UI implements a custom cursor (e.g., `cursor: none`), keyboard users lack a visual frame of reference because they don't use the mouse. Without explicit `:focus-visible` styles on interactive elements, they have no visual way to know which element is currently focused.
**Action:** Always add explicit `:focus-visible` styles (like a clear `outline`) to all interactive elements (buttons, inputs) in custom cursor UIs to maintain keyboard navigation accessibility.
