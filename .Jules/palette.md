## 2024-09-13 - Semantic HTML for Forms
**Learning:** Stylized `<div>` elements used as labels limit accessibility. Screen readers cannot properly associate them with input fields, and users cannot click them to focus the inputs.
**Action:** Always use semantic `<label>` elements with `for` attributes that correspond to the `id` of the respective input elements to ensure they are accessible.