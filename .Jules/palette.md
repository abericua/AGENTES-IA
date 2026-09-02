## 2024-06-25 - Semantic Labels vs Stylized Divs
**Learning:** This app heavily relies on stylized `<div>` elements (`<div class="lbl">`) for form field labels rather than semantic HTML (`<label>`). This breaks screen reader association and creates smaller click targets for users.
**Action:** Always prefer semantic HTML tags like `<label>` with `for` attributes for inputs when adding form elements, even if relying on existing design system utility classes.
