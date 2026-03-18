---
marp: true
theme: rmt-light-blue
headingDivider: [2, 3]
paginate: true
header: 'Refined Marp Theme User Guide'
footer: 'Refined Marp Theme User Guide'
---

## How to Use Refined Marp Theme

#### Feature Overview

Refined Marp Theme is a feature-rich custom theme for Marp, designed specifically for presentations with support for multiple page types and block styles.

Supports multiple color schemes with both light and dark modes

- Light mode uses a white background with theme colors, suitable for bright environments and daytime presentations.
- Dark mode uses a dark gray background with theme colors, suitable for low-light environments and nighttime presentations.

#### Usage Guide

1. Add YAML configuration at the top of your Markdown file
2. Use H2 for chapter titles and H3 for content page titles, with Marp's headingDivider: [2, 3] configuration for automatic pagination—no manual page breaks needed
3. Use `<!-- _class: -->` to specify page styles
4. Use block class names to create special content layouts
5. Choose an appropriate theme, such as rmt-light-blue or rmt-dark-blue

**Enjoy your presentation!**

## 01

<!-- _class: chapter-2 -->

#### Cover Page Styles

Refined Marp Theme provides 6 cover page styles for different presentation scenarios.

## cover-1 Brand Identity Cover

<!-- _class: cover-1 -->

#### Professional Presentation Theme System

Author · Design Department · January 2026

## cover-2 Left Decorated Cover

<!-- _class: cover-2 -->

#### Minimalist Design Modern Aesthetics

Zhang San · Tech Team · 2026-01-30

## cover-3 Bottom Gradient Cover

<!-- _class: cover-3 -->

#### Clear Information Hierarchy Design

Li Si · R&D Department · 2026

## cover-4 Floating Card Cover

<!-- _class: cover-4 -->

#### Elegant and Concise Visual Experience

Product Team · Marketing Department · Q1 2026

## cover-5 Split Column Cover

<!-- _class: cover-5 -->

#### Vibrant Presentation Style

Design Department · Creative Center · January 2026

## cover-6 Top Gradient Cover

<!-- _class: cover-6 -->

#### Professional Business Presentation Style

Data Analytics Team · Operations Department · January 2026

## 02

<!-- _class: chapter-2 -->

#### Table of Contents Styles

Refined Marp Theme provides 6 table of contents styles, supporting both ordered and unordered lists, with support for in-page anchors and external links.

## menu-1 Standard List Menu

<!-- _class: menu-1 -->

1. [Introduction and Overview](#introduction)
2. [Key Concepts and Methodology](#key-concepts)
3. [Analysis and Findings](#analysis)
4. [Recommendations](#recommendations)
5. [Implementation Strategy](#implementation)
6. [Conclusion and Next Steps](#conclusion)

## menu-2 Numbered Card Menu

<!-- _class: menu-2 -->

1. [Getting Started](#getting-started)
   Foundation and setup

2. [Core Concepts](#core-concepts)
   Understanding the basics

3. [Advanced Topics](#advanced-topics)
   Deep dive techniques

4. [Best Practices](#best-practices)
   Industry standards

## menu-3 Column List Menu

<!-- _class: menu-3 -->

- [Welcome & Introduction](#welcome)
- [Product Overview](#product-overview)
- [Live Demo](#demo)
- [Q&A Session](#qa)

## menu-4 Ordered List Menu

<!-- _class: menu-4 -->

1. [Explore](#explore)
   Discover possibilities

2. [Learn](#learn)
   Build new skills

3. [Apply](#apply)
   Put knowledge to work

4. [Grow](#grow)
   Achieve results

## menu-5 Simple List Menu

<!-- _class: menu-5 -->

1. Chapter 1: The Beginning
2. Chapter 2: The Process
3. Chapter 3: The Result

## menu-6 Icon List Menu

<!-- _class: menu-6 -->

- [💡Ideas](#ideas)
  Generate creative concepts

- [🎯Strategy](#strategy)
  Plan your approach

- [⚡Execute](#execute)
  Implement with speed

- [🏆Achieve](#achieve)
  Reach your goals

## 03

<!-- _class: chapter-2 -->

#### Chapter Page Styles

Refined Marp Theme provides 3 chapter page styles with vertically centered content.

## 01

<!-- _class: chapter-1 -->

#### Centered Large Number

## 02

<!-- _class: chapter-2 -->

#### Split Column Chapter

Understanding the fundamentals

## 03

<!-- _class: chapter-3 -->

#### Centered Card Focus

## 04

<!-- _class: chapter-2 -->

#### Ending Page Styles

Refined Marp Theme provides 3 ending page styles.

## ending-1 Gradient Background Thank You

<!-- _class: ending-1 -->

#### Thank You

Questions & Discussion

email@example.com

www.example.com

## ending-2 Centered Card Contact

<!-- _class: ending-2 -->

#### Let's Connect

hello@company.com

@company LinkedIn

## ending-3 Minimalist Logo Style

<!-- _class: ending-3 -->

#### Your Company

Thank you for your attention

contact@example.com

www.example.com

## 05

<!-- _class: chapter-2 -->

#### Text Element Styles

Refined Marp Theme supports a complete heading hierarchy system and text styles.

### Paragraph and Text Styles

This is the first paragraph using body font size. The design system adopts clear and readable typography standards.

This is the second paragraph. Paragraph spacing is set to --rmt-spacing-md, ensuring clear content hierarchy.

This is **bold text** for emphasizing important content.

This is _italic text_ for indicating specific meaning.

This is `inline code`.

This is an external link example: [Marp Official Website](https://marp.app). Click the link to navigate to the corresponding page. Supports both in-page anchors and external links.

### Font Size Examples

<span style="font-size: var(--rmt-font-size-body-sm)">This text uses the small body font size (1.25rem). Suitable for compact layouts and supplementary information.</span>

This text uses the standard body font size (1.5rem). The default size for regular paragraph content.

<span style="font-size: var(--rmt-font-size-body-lg)">This text uses the large body font size (1.75rem). Ideal for emphasis and improved readability in presentations.</span>

### Image Styles

Supports both local and online images with automatic rounded corners.

![Sample Image](https://preview.qiantucdn.com/58pic/ali_magnify/Kx/Q6/he/r5/2igqm38fe0s7twpun5cbajkh4oxdyzvl_PIC2018.jpg!qt_h320)

## 06

<!-- _class: chapter-2 -->

#### Callout Styles

Refined Marp Theme supports 8 callout styles.

### All Callout Types

<!-- _class: col-33-33-33 -->

<div>

<div class="callout-tip">

**Tip**
This is a tip callout with green color scheme and lightbulb icon. Used for sharing tips, best practices, and useful suggestions.

</div>

<div class="callout-warning">

**Warning**
This is a warning callout with orange color scheme and triangle icon. Used to remind users of important matters requiring attention.

</div>

<div class="callout-danger">

**Danger**
This is a danger callout with red color scheme and circle icon. Used to indicate dangerous operations, errors, or serious warnings.

</div>

</div>

<div>
<div class="callout-info">

**Info**
This is an info callout with cyan color scheme and info icon. Used to provide supplementary information, explanations, and helpful hints.

</div>

<div class="callout-success">

**Success**
This is a success callout with green color scheme and checkmark icon. Used to indicate successful operations, completion, or passed status.

</div>

<div class="callout-cite">

**Quote**
This is a cite callout with gray color scheme and quote icon. Used for citing literature, quotes, or others' opinions.

</div>
</div>

<div>
<div class="callout-example">

**Example**
This is an example callout with purple color scheme and flask icon. Used to provide example code, sample data, and example explanations.

</div>

<div class="callout-todo">

**Todo**
This is a todo callout with yellow color scheme and tasks icon. Used to mark pending tasks and reminders.

</div>
</div>

## 07

<!-- _class: chapter-2 -->

#### Table Styles

Refined Marp Theme provides 3 table styles.

### table-1 Simple Border Table

| Feature           | Description            | Status |
| ----------------- | ---------------------- | ------ |
| Border Style      | Clean 1px border       | ✓      |
| Shadow Effect     | Subtle soft shadow     | ✓      |
| Rounded Corners   | 12px rounded corners   | ✓      |
| Header Background | Theme color background | ✓      |

### table-2 Card Floating Table

<!-- _class: table-2 -->

| Component | Description              | Status      |
| --------- | ------------------------ | ----------- |
| Card      | Card container component | Completed   |
| Button    | Button component         | Completed   |
| Badge     | Badge component          | Completed   |
| Modal     | Modal component          | In Progress |
| Toast     | Toast component          | Planned     |

### table-3 Classic Striped Table

<!-- _class: table-3 -->

| No. | Task Name                 | Priority | Owner     | Progress |
| --- | ------------------------- | -------- | --------- | -------- |
| 1   | Implement callout styles  | High     | Zhang San | 100%     |
| 2   | Implement table styles    | Medium   | Li Si     | 100%     |
| 3   | Implement grid layouts    | Low      | Wang Wu   | 80%      |
| 4   | Documentation improvement | Medium   | Qian Qi   | 40%      |

## 08

<!-- _class: chapter-2 -->

#### Quote Blocks and Full-Width Blocks

Use quote blocks to highlight important points and professional terminology. Use full-width blocks for important notes, summaries, or conclusions.

### Quote Styles

##### Single Line Quote

> This is a single-line quote. Quotes use background color, double quote decoration, and italic text to stand out, suitable for emphasizing important points or quoting others.

##### Multi-Line Quote

> This is the first paragraph of a multi-line quote, which can contain multiple paragraphs.
>
> This is the second paragraph. Multiple paragraphs are merged within the same quote block, maintaining visual consistency.

##### Nested Quote

> This is the first-level quote for expressing main points.
>
> > This is the second-level quote for citing others' opinions or supplementary explanations.

### Full-Width Block Example

Main content

<footer class="full-bar">

**Important Note**: Full-width blocks use theme color background, suitable for important notes, summaries, or conclusions.

**Other Notes**: Markdown bold syntax can be used to emphasize important content.

</footer>

## 09

<!-- _class: chapter-2 -->

#### List Layouts

Use single or multi-column layouts to display list content, supporting various unordered and ordered list styles.

### Unordered Lists

**ul-style-1 Large Dot Style**

<div class="ul-style-1">

- First item: Uses large dot symbols
- Second item: Dots use theme color
- Third item: Suitable for general list scenarios

</div>

**ul-style-2 Square Style**

<div class="ul-style-2">

- First item: Uses square symbols
- Second item: Squares use theme color
- Third item: Suitable for emphasizing key content

</div>

**ul-style-3 Arrow Style**

<div class="ul-style-3">

- Step 1: Open terminal
- Step 2: Run command
- Step 3: View results

</div>

### Ordered Lists

**ol-style-1 Theme Color Number Style**

<div class="ol-style-1">

1. Step 1: Initialize project
2. Step 2: Write code
3. Step 3: Test and verify

</div>

**ol-style-2 Square Background Number Style**

<div class="ol-style-2">

1. Step 1: Initialize project
2. Step 2: Write code
3. Step 3: Test and verify

</div>

**ol-style-3 Circle Background Number Style**

<div class="ol-style-3">

1. Step 1: Initialize project
2. Step 2: Write code
3. Step 3: Test and verify

</div>

### Two-Column Unordered List

**Dot Style**

<div class="cols-2 ul-style-1">

- First item: Uses large dot symbols
- Second item: Dots use theme color
- Third item: Suitable for general list scenarios
- Fourth item: Automatic line wrapping
- Fifth item: Maintains visual balance
- Sixth item: Evenly distributed in two columns

</div>

**Square Symbol**

<div class="cols-2 ul-style-2">

- First item: Uses square symbols
- Second item: Squares use theme color
- Third item: Suitable for general list scenarios
- Fourth item: Automatic line wrapping
- Fifth item: Maintains visual balance
- Sixth item: Evenly distributed in two columns

</div>

**Arrow Symbol**

<div class="cols-2 ul-style-3">

- First item: Uses arrow symbols
- Second item: Arrows use theme color
- Third item: Suitable for general list scenarios
- Fourth item: Automatic line wrapping
- Fifth item: Maintains visual balance
- Sixth item: Evenly distributed in two columns

</div>

### Three-Column Ordered List

**Theme Color Number Style**

<div class="cols-3 ol-style-1">

1. Step 1: Initialize project
2. Step 2: Write code
3. Step 3: Test and verify
4. Step 4: Code review
5. Step 5: Merge and release
6. Step 6: Monitor and feedback

</div>

**Square Background Number Style**

<div class="cols-3 ol-style-2">

1. Step 1: Initialize project
2. Step 2: Write code
3. Step 3: Test and verify
4. Step 4: Code review
5. Step 5: Merge and release
6. Step 6: Monitor and feedback

</div>

**Circle Background Number Style**

<div class="cols-3 ol-style-3">

1. Step 1: Initialize project
2. Step 2: Write code
3. Step 3: Test and verify
4. Step 4: Code review
5. Step 5: Merge and release
6. Step 6: Monitor and feedback

</div>

## 10

<!-- _class: chapter-2 -->

#### Column Layouts

Refined Marp Theme provides a flexible column layout system, supporting horizontal, vertical, and matrix layouts.

### Horizontal Layout: col-50-50 Two Equal Columns

<!-- _class: col-50-50 -->
<div>

#### Left Column Content

This is the text content of the left column. col-50-50 splits the page horizontally into two equal columns, each occupying **50%** width.

- Left column item 1
- Left column item 2
- Left column item 3

</div>

<div>

#### Right Column Content

This is the text content of the right column. Each column uses H4 headings as column separators, with headings automatically applying the theme color.

- Right column item 1
- Right column item 2
- Right column item 3

</div>

### Horizontal Layout: col-60-40 Left 60 Right 40

<!-- _class: col-60-40 -->

<div>

#### Main Content Area (60%)

This is the main content area occupying 60% width. Suitable for displaying main content, with the left column being wider to accommodate more text.

The col-60-40 layout is often used when emphasizing left-side content, such as combining main introductions with supplementary notes.

</div>

<div>

#### Secondary Content Area (40%)

This is the secondary content area occupying 40% width. Suitable for placing supplementary notes, images, or auxiliary information.

The right column is narrower, suitable for placing key points, notes, or quoted content.

</div>

### Horizontal Layout: col-40-60 Left 40 Right 60

<!-- _class: col-40-60 -->

<div>

#### Left Content (40%)

This is the left content occupying 40% width. Suitable for placing navigation, indexes, or auxiliary information.

The narrow-left, wide-right layout is suitable for scenarios where main content is displayed on the right.

</div>

<div>

#### Right Content (60%)

This is the right content area occupying 60% width. The right side is wider, suitable for placing main text content, detailed explanations, or code examples.

col-40-60 is the reverse layout of col-60-40, used to emphasize right-side content.

</div>

### Horizontal Layout: col-40-60 Left 40 Right 60 (No Headings)

<!-- _class: col-40-60 -->

<div>

Intelligent platforms provide infrastructure management and programmable API functionality composability through automated infrastructure. They integrate compute, storage, and network assets with part or all of the application software stack to create specialized workload architectures. Intelligent platform vendors also include application affinity, management tools, operating systems, and virtualization components purchased and/or used as services.

Intelligent platform solutions differ from integrated systems or hyper-converged infrastructure (HCI) solutions that require purchasing separate software stacks bound to hardware. As part of the shift to consumption-based infrastructure delivery, pricing strategies for entire integrated software stack solutions vary widely. Intelligent platforms also integrate applications and business logic into bundles and partnerships.

Intelligent Platform Benefits:

- Provide workload performance or application manageability across hardware, reducing operational costs and improving IT agility through automation and resource pooling.
- Automation and machine learning for the full stack above integrated systems, hardware management, and software programmability.
- They run proprietary workloads independently, rarely competing with each other when the software stack sets hardware options.

</div>

<div>

![](https://copyright.bdstatic.com/vcg/creative/4ed59bf32ca806f4f159f0b6d45558c7.jpg)

</div>

### Horizontal Layout: col-30-70 Left 30 Right 70

<!-- _class: col-30-70 -->

<div>

#### Left Side (30%)

- Point 1
- Point 2
- Point 3

</div>

<div>

#### Right Main Content (70%)

This is the right main content area occupying 70% width. The col-30-70 layout reserves most space for the right side, suitable for scenarios with short headings or indexes on the left and detailed content on the right.

This layout is common in technical documentation, where the left side can be terms or concepts and the right side contains detailed explanations.

</div>

### Horizontal Layout: col-70-30 Left 70 Right 30

<!-- _class: col-70-30 -->

<div>

#### Left Main Content (70%)

This is the left main content area occupying 70% width. The col-70-30 layout reserves most space for the left side, suitable for placing main text content, detailed explanations, or code.

The left side is the main content, while the right side can contain related links, notes, or auxiliary information.

</div>

<div>

#### Right Side (30%)

- Note 1
- Note 2
- Note 3

</div>

### Horizontal Layout: col-33-33-33 Three Equal Columns

<!-- _class: col-33-33-33 -->

<div>

#### First Column

This is the content of the first column. The three-equal-column layout splits the page horizontally into three equal columns, each occupying approximately 33.33% width.

Suitable for displaying three parallel concepts, steps, or categories.

</div>

<div>

#### Second Column

This is the content of the second column. Each column uses H4 headings as separators, with headings automatically applying the theme color.

- Item A
- Item B
- Item C

</div>

<div>

#### Third Column

This is the content of the third column. The three-column layout is suitable for displaying parallel content, such as three features or three steps.

Each column has equal width, creating a visually balanced appearance.

</div>

### Horizontal Layout: col-25-25-25-25 Four Equal Columns

<!-- _class: col-25-25-25-25 -->

<div>

#### First Column

The four-equal-column layout splits the page horizontally into four equal columns.

</div>

<div>

#### Second Column

Each column occupies 25% width.

</div>

<div>

#### Third Column

Suitable for displaying four parallel concepts or categories.

</div>

<div>

#### Fourth Column

Note: Four-column layout has limited space, so use concise text.

</div>

### Vertical Layout: row-50-50 Two Equal Rows

<!-- _class: row-50-50 -->

<div>

#### Top Half Content

This is the content of the top half. row-50-50 splits the page vertically into two equal rows, each occupying 50% height.

Vertical layouts are suitable for top-bottom content structures, such as image above text, question above answer, etc.

</div>

<div>

#### Bottom Half Content

This is the content of the bottom half. Each row uses H4 headings as separators.

Vertical layouts in presentations can be used to display time series, cause-effect relationships, etc.

</div>

### Vertical Layout: row-60-40 Top 60 Bottom 40

<!-- _class: row-60-40 -->

<div>

#### Top Half (60%)

This is the top half content occupying 60% height. The row-60-40 layout reserves most vertical space for the top half.

Suitable for scenarios with main content above and auxiliary content below.

</div>

<div>

#### Bottom Half (40%)

This is the bottom half content occupying 40% height. The bottom half is shorter, suitable for placing summaries, conclusions, or notes.

The tall-top, short-bottom layout emphasizes top-half content.

</div>

### Vertical Layout: row-40-60 Top 40 Bottom 60

<!-- _class: row-40-60 -->

<div>

#### Top Half (40%)

This is the top half content occupying 40% height.

The top half is shorter, suitable for placing introductions, questions, or background information.

</div>

<div>

#### Bottom Half (60%)

This is the bottom half content occupying 60% height. The row-40-60 layout reserves most vertical space for the bottom half.

Suitable for question-above-answer, cause-above-effect scenarios.

</div>

### Vertical Layout: row-33-33-33 Three Equal Rows

<!-- _class: row-33-33-33 -->

<div>

#### First Row

This is the content of the first row. row-33-33-33 splits the page vertically into three equal rows.

Suitable for displaying three steps, three stages, or three levels of content.

</div>

<div>

#### Second Row

This is the content of the second row. Three-row vertical layouts are suitable for displaying progressive relationships or time sequences.

- Step 1
- Step 2
- Step 3

</div>

<div>

#### Third Row

This is the content of the third row. Each row has equal height, creating a visually balanced appearance.

Vertical layouts are very effective for displaying processes, stages, etc.

</div>

### grid-2-2 Matrix Layout (2 Columns 2 Rows)

<!-- _class: grid-2-2 -->

<div>

#### Top-Left Cell

This is the content of row 1, column 1. grid-2-2 creates a 2x2 matrix layout.

Matrix layouts fill content in left-to-right, top-to-bottom order.

</div>

<div>

#### Top-Right Cell

This is the content of row 1, column 2.

Each cell uses H4 headings as separators.

</div>

<div>

#### Bottom-Left Cell

This is the content of row 2, column 1.

Matrix layouts are suitable for displaying four parallel concepts or categories.

</div>

<div>

#### Bottom-Right Cell

This is the content of row 2, column 2.

The 2x2 matrix is an efficient way to organize content.

</div>

### grid-3-2 Matrix Layout (3 Columns 2 Rows)

<!-- _class: grid-3-2 -->

<div>

#### First Column

grid-3-2 creates a 3-column, 2-row matrix layout.

Suitable for displaying six related content items.

</div>

<div>

#### Second Column

Each cell is of equal size.

Arrangement order: left to right, top to bottom.

</div>

<div>

#### Third Column

Matrix layouts display multiple content items in limited space.

Very suitable for displaying features, advantages, etc.

</div>

<div>

#### Fourth Item

This is the content of row 2, column 1.

Each cell is an independent content block.

</div>

<div>

#### Fifth Item

This is the content of row 2, column 2.

Hover effects include borders, shadows, and位移。

</div>

<div>

#### Sixth Item

This is the content of row 2, column 3.

Matrix layouts make content organization clearer and more orderly.

</div>

### grid-3-3 Matrix Layout (3 Columns 3 Rows)

<!-- _class: grid-3-3 -->

<div>

#### 1

This is the first cell.

</div>

<div>

#### 2

Second cell.

</div>

<div>

#### 3

Third cell.

</div>

<div>

#### 4

Fourth cell.

</div>

<div>

#### 5

Fifth cell.

</div>

<div>

#### 6

Sixth cell.

</div>

<div>

#### 7

Seventh cell.

</div>

<div>

#### 8

Eighth cell.

</div>

<div>

#### 9

Ninth cell. grid-3-3 is suitable for displaying nine related content items.

</div>

### grid-4-2 Matrix Layout (4 Columns 2 Rows)

<!-- _class: grid-4-2 -->

<div>

#### First Column

grid-4-2 creates a 4-column, 2-row matrix layout.

Suitable for displaying eight related content items.

</div>

<div>

#### Second Column

Each cell is of equal size.

Arrangement order: left to right, top to bottom.

</div>

<div>

#### Third Column

Matrix layouts display multiple content items in limited space.

Very suitable for displaying features, advantages, etc.

</div>

<div>

#### Fourth Item

Each cell is an independent content block.

</div>

<div>

#### Fifth Item

Hover effects include borders, shadows, and位移。

</div>

<div>

#### Sixth Item

Matrix layouts make content organization clearer and more orderly.

</div>

<div>

#### Seventh Item

Matrix layouts make content organization clearer and more orderly.

</div>

<div>

#### Eighth Item

Matrix layouts make content organization clearer and more orderly.

</div>

### Column Style Effects (Highlight Column Effect)

<!-- _class: col-50-50 -->

<div>

#### Normal Column

This is a normal column using default styles.

Hover effects include borders, shadows, and slight upward movement.

</div>

<div class="highlight">

#### Highlighted Column

This is a **highlighted column** implemented using the `highlight` class.

Highlighted columns use _light theme color background_ with automatically adapted text color.

</div>

## 11

<!-- _class: chapter-2 -->

#### Code Highlighting Styles

Refined Marp Theme integrates highlight.js for professional code syntax highlighting, supporting multiple programming languages.

### Java Code Example

```java
public class HelloWorld {
    public static void main(String[] args) {
        // Print Hello World
        System.out.println("Hello, World!");

        // Variable declaration
        int count = 10;
        String message = "Welcome to Java";

        // Loop example
        for (int i = 0; i < count; i++) {
            System.out.println("Count: " + i);
        }
    }
}
```

### Python Code Example

```python
# Python code highlighting example
def greet(name):
    """Greet the user"""
    return f"Hello, {name}!"

# List comprehension
numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]

# Class definition
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"I'm {self.name}, {self.age} years old.")
```

### JavaScript Code Example

```javascript
// JavaScript code highlighting example
const users = [
  { id: 1, name: 'Alice', age: 25 },
  { id: 2, name: 'Bob', age: 30 },
  { id: 3, name: 'Charlie', age: 35 },
]

// Arrow function
const filterUsers = (users, minAge) => {
  return users.filter(user => user.age >= minAge)
}
```

### TypeScript Code Example

```typescript
// TypeScript code highlighting example
interface User {
  id: number
  name: string
  email: string
  age?: number // Optional property
}

class UserService {
  private users: User[] = []

  addUser(user: User): void {
    this.users.push(user)
  }

  findUserById(id: number): User | undefined {
    return this.users.find(user => user.id === id)
  }
}
```

### Go Code Example

```go
package main

import "fmt"

// User struct
type User struct {
    Name string
    Age  int
}

// Method
func (u *User) Greet() string {
    return fmt.Sprintf("Hello, %s!", u.Name)
}

func main() {
    // Create user
    user := User{Name: "Alice", Age: 25}

    // Call method
    message := user.Greet()
    fmt.Println(message)
}
```
