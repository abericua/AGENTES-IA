## 2024-05-18 - Semantic Form Accessibility
**Learning:** Legacy UI prototypes frequently use generic tags (`<div>`) for form labels which breaks screen reader experiences, but changing them to `<label>` tags natively disrupts block layout flow because labels are inline elements.
**Action:** When updating generic containers to semantic `<label for="...">` tags for accessibility, remember to check and explicitly assign `display: block` in CSS to preserve visual spacing constraints without needing a structural refactor.
