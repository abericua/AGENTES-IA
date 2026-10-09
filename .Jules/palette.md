## 2024-09-13 - Semantic HTML for Forms
**Learning:** Stylized `<div>` elements used as labels limit accessibility. Screen readers cannot properly associate them with input fields, and users cannot click them to focus the inputs.
**Action:** Always use semantic `<label>` elements with `for` attributes that correspond to the `id` of the respective input elements to ensure they are accessible.
## 2024-10-01 - ARIA roles for dynamic custom UI feedback
**Learning:** For dynamic progress indicators (`#pg`) and real-time chat updates (`#chat`), visually indicating state change isn't enough for screen readers. They need explicit roles and `aria-live` attributes to notify users when content changes dynamically without explicit focus changes.
**Action:** Always add `role="progressbar"`, `aria-valuenow`, `aria-valuemin`, and `aria-valuemax` to custom progress components and ensure `aria-valuenow` updates dynamically. Use `aria-live="polite"` for status indicators and `role="log"` for chat/console output elements.
## 2024-10-24 - Focus states with custom cursors
**Learning:** When using `cursor: none` to implement a custom cursor across an entire application, default browser focus rings might not be prominent enough or might conflict with the intended visual design. This makes it difficult for keyboard users to determine which element currently has focus.
**Action:** Always provide explicit, high-contrast `:focus-visible` styles (e.g., using `box-shadow` or `outline` with accent colors) for all interactive elements like buttons and inputs to ensure keyboard navigation remains accessible.
