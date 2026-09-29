## 2024-09-13 - Semantic HTML for Forms
**Learning:** Stylized `<div>` elements used as labels limit accessibility. Screen readers cannot properly associate them with input fields, and users cannot click them to focus the inputs.
**Action:** Always use semantic `<label>` elements with `for` attributes that correspond to the `id` of the respective input elements to ensure they are accessible.
## 2024-09-14 - Screen Reader Support for Async Operations
**Learning:** Visual progress bars and dynamic status text changes during asynchronous operations are completely invisible to screen reader users unless properly marked up.
**Action:** Always pair visual progress indicators with `role="progressbar"` and dynamic `aria-valuenow` attributes. For dynamic status text that changes asynchronously, use `aria-live="polite"` to announce updates to screen readers without interrupting the user.
