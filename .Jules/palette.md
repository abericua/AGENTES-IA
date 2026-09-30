## 2024-09-13 - Semantic HTML for Forms
**Learning:** Stylized `<div>` elements used as labels limit accessibility. Screen readers cannot properly associate them with input fields, and users cannot click them to focus the inputs.
**Action:** Always use semantic `<label>` elements with `for` attributes that correspond to the `id` of the respective input elements to ensure they are accessible.
## 2024-11-20 - Form Accessibility During Async Operations
**Learning:** Leaving form fields active during long asynchronous operations can cause user confusion and unexpected states if users try to modify their input.
**Action:** Always disable inputs, textareas, and associated buttons when a process begins and visually indicate this disabled state using `opacity` and `pointer-events: none`. Re-enable them when the process completes or fails.
