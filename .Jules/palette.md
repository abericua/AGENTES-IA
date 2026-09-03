## 2026-09-03 - Semantic Labels with Custom CSS
**Learning:** When replacing stylized `<div>` elements with semantic `<label>` elements for form accessibility in custom UIs, you often need to explicitly set `display: block` to prevent layout shifts, as `<label>` elements are inline by default, unlike `<div>` elements.
**Action:** When updating existing UI components to be more semantic, always check the display property of the original element to maintain layout fidelity.
