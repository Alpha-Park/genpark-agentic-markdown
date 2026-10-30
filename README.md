# genpark-agentic-markdown

![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Dependencies](https://img.shields.io/badge/dependencies-zero-success)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

GenPark Agentic Markdown is a zero-dependency CommonMark AST parsing, interactive widget transformation, and accessibility compliance engine designed for autonomous agent doc generation and markdown artifact rendering.

```mermaid
flowchart TD
    A[Markdown Raw Text] --> B[Recursive Token & AST Parser]
    B --> C[Structural Depth & Density Metric]
    A --> D[Agentic Widget Matcher]
    D --> E[Interactive Alerts, Tabs & Carousels]
    A --> F[Accessibility & Contrast Linter]
    F --> G[WCAG Hierarchy & Alt-Text Audit Score]
```

## Features
- **Recursive AST Tokenizer**: Measures nesting depth, code block integrity, and information density without external markdown libraries.
- **Interactive Agentic Directives**: Transforms `:::alert`, `:::tabs`, and `::::carousel` markup into responsive HTML widgets.
- **Accessibility Linter**: Detects heading level skips, empty image alt tags, and vague hyperlink anchor text.

## Quickstart

```python
from client import GenParkAgenticMarkdown

gam = GenParkAgenticMarkdown()
res = gam.parse_ast_token_density_and_depth("# Hello\n\n```python\npass\n```")
print("Density:", res["structural_density_pct"], "%")
```

## License
MIT
