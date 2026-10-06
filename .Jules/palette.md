## 2024-09-13 - Semantic HTML for Forms
**Learning:** Stylized `<div>` elements used as labels limit accessibility. Screen readers cannot properly associate them with input fields, and users cannot click them to focus the inputs.
**Action:** Always use semantic `<label>` elements with `for` attributes that correspond to the `id` of the respective input elements to ensure they are accessible.
## 2024-10-01 - ARIA roles for dynamic custom UI feedback
**Learning:** For dynamic progress indicators (`#pg`) and real-time chat updates (`#chat`), visually indicating state change isn't enough for screen readers. They need explicit roles and `aria-live` attributes to notify users when content changes dynamically without explicit focus changes.
**Action:** Always add `role="progressbar"`, `aria-valuenow`, `aria-valuemin`, and `aria-valuemax` to custom progress components and ensure `aria-valuenow` updates dynamically. Use `aria-live="polite"` for status indicators and `role="log"` for chat/console output elements.

## 2024-10-24 - Focus States with Custom Cursors
**Learning:** When using a custom cursor design (`cursor: none`), users lose the default visual feedback of mouse interactions. For users relying on keyboard navigation, the lack of an explicit focus state means they cannot tell which element is currently active, severely harming accessibility.
**Action:** Explicit `:focus-visible` styles must be manually added to all interactive elements (e.g., buttons, inputs, textareas) whenever a custom cursor is used to maintain keyboard navigation accessibility.
