## 2024-09-13 - Semantic HTML for Forms
**Learning:** Stylized `<div>` elements used as labels limit accessibility. Screen readers cannot properly associate them with input fields, and users cannot click them to focus the inputs.
**Action:** Always use semantic `<label>` elements with `for` attributes that correspond to the `id` of the respective input elements to ensure they are accessible.
## 2024-10-01 - ARIA roles for dynamic custom UI feedback
**Learning:** For dynamic progress indicators (`#pg`) and real-time chat updates (`#chat`), visually indicating state change isn't enough for screen readers. They need explicit roles and `aria-live` attributes to notify users when content changes dynamically without explicit focus changes.
**Action:** Always add `role="progressbar"`, `aria-valuenow`, `aria-valuemin`, and `aria-valuemax` to custom progress components and ensure `aria-valuenow` updates dynamically. Use `aria-live="polite"` for status indicators and `role="log"` for chat/console output elements.

## 2024-03-01 - Keyboard Accessibility with Custom Cursors
**Learning:** When a UI utilizes a custom cursor design via CSS (`cursor: none`), it often visually de-emphasizes native browser focus states, making keyboard navigation difficult or impossible for users who rely on it.
**Action:** Always explicitly define `:focus-visible` styles with sufficient contrast (e.g., using an outline) for all interactive elements (`button`, `input`, `textarea`, `a`) in projects employing custom cursors to ensure they remain accessible to keyboard users.
