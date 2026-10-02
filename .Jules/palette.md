## 2024-09-13 - Semantic HTML for Forms
**Learning:** Stylized `<div>` elements used as labels limit accessibility. Screen readers cannot properly associate them with input fields, and users cannot click them to focus the inputs.
**Action:** Always use semantic `<label>` elements with `for` attributes that correspond to the `id` of the respective input elements to ensure they are accessible.
## 2024-10-01 - ARIA roles for dynamic custom UI feedback
**Learning:** For dynamic progress indicators (`#pg`) and real-time chat updates (`#chat`), visually indicating state change isn't enough for screen readers. They need explicit roles and `aria-live` attributes to notify users when content changes dynamically without explicit focus changes.
**Action:** Always add `role="progressbar"`, `aria-valuenow`, `aria-valuemin`, and `aria-valuemax` to custom progress components and ensure `aria-valuenow` updates dynamically. Use `aria-live="polite"` for status indicators and `role="log"` for chat/console output elements.
## 2026-10-02 - Keyboard Focus States for Custom Buttons
**Learning:** Interactive elements like `.btn-sm` and `.btn-run` lacked `:focus-visible` styles, meaning keyboard users (who rely on the Tab key for navigation) would not see a clear indicator of which element was focused.
**Action:** Always add `:focus-visible` pseudo-class styles with clear visual feedback (like a distinct outline or `box-shadow`) to all interactive elements, matching or adapting their hover styles.
