# HTML & CSS Fundamentals for MCQ Tests

While often considered basic, HTML and CSS can have tricky MCQ questions. Focus on core concepts, specificity, and layout mechanisms.

## Probable MCQ Topics & Previous Year Style Questions

### HTML Core Concepts
1.  **Semantic HTML**:
    *   *Question:* Why use semantic tags like `<article>`, `<section>`, `<nav>` instead of `<div>`?
    *   *Answer:* For accessibility (screen readers) and SEO (Search Engine Optimization).
2.  **`head` vs `body` tags**:
    *   *Question:* Which tag is used to include external CSS?
    *   *Answer:* `<link rel="stylesheet" href="...">` inside the `<head>`.
    *   *Question:* Where does `<meta>` tag go and what is it used for?
    *   *Answer:* Inside `<head>`, used for character set, viewport settings, SEO descriptions.
3.  **Attributes**:
    *   *Question:* Difference between `id` and `class`?
    *   *Answer:* `id` must be unique per page; `class` can be used on multiple elements.
    *   *Question:* What is the `alt` attribute in an `<img>` tag?
    *   *Answer:* Alternative text displayed if the image fails to load, and used by screen readers.
4.  **Forms**:
    *   *Question:* Difference between GET and POST methods in an HTML `<form>`?
    *   *Answer:* GET appends data to the URL (visible, length limit), POST sends data in the HTTP body (secure for passwords, no length limit).

### CSS Core Concepts
1.  **The Box Model (Very Important!)**:
    *   *Question:* What comprises the CSS Box Model?
    *   *Answer:* Content, Padding, Border, Margin (from inside to outside).
    *   *Question:* What does `box-sizing: border-box;` do?
    *   *Answer:* It includes padding and border in the element's total width and height. (Without it, adding padding makes the element wider).
2.  **CSS Specificity (Calculation MCQs are common)**:
    *   Hierarchy: Inline style > ID > Class/Pseudo-class/Attribute > Element/Tag.
    *   *Question:* If an element has `#myId` (color: red) and `.myClass` (color: blue), what color will it be?
    *   *Answer:* Red, because ID has higher specificity.
    *   *Question:* What does `!important` do?
    *   *Answer:* Overrides all other specificity rules (should be used sparingly).
3.  **Positioning**:
    *   *Question:* What is the default position of an HTML element?
    *   *Answer:* `position: static;`
    *   *Question:* Difference between `absolute` and `relative`?
    *   *Answer:* `relative` positions an element relative to its normal position. `absolute` positions an element relative to its closest *positioned* ancestor (an ancestor with position other than static).
    *   *Question:* Difference between `fixed` and `sticky`?
    *   *Answer:* `fixed` is relative to the viewport (window). `sticky` toggles between relative and fixed depending on scroll position.
4.  **Display Properties**:
    *   *Question:* Difference between `display: none;` and `visibility: hidden;`?
    *   *Answer:* `display: none` removes the element from the document layout flow entirely (takes up no space). `visibility: hidden` makes it invisible but it still takes up space.
    *   *Question:* Difference between `inline` and `block` elements?
    *   *Answer:* `block` takes up full width (e.g., `<div>`, `<p>`). `inline` takes up only necessary width and doesn't start a new line (e.g., `<span>`, `<a>`). `inline-block` is like inline but allows setting width and height.
5.  **Units**:
    *   *Question:* Difference between `em` and `rem`?
    *   *Answer:* `em` is relative to the font-size of its direct parent. `rem` is relative to the font-size of the root element (`<html>`).

### Layouts
*   **Flexbox**: Know properties like `justify-content` (main axis alignment) and `align-items` (cross axis alignment).
*   **Grid**: Understand it is a 2D layout system (rows and columns) compared to Flexbox's 1D system.
