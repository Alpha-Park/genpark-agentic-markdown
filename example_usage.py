# -*- coding: utf-8 -*-
import json
from client import GenParkAgenticMarkdown

gam = GenParkAgenticMarkdown()

doc = """# Agentic Operating System

> [!NOTE] Background context on neural agents.

Here is a link to the [Agent Documentation](https://alphapark.io/docs).
Here is an image: ![Agent Diagram](https://alphapark.io/diagram.png)

:::alert[tip]
Use zero-dependency algorithms for maximum latency performance.
:::

::::carousel
Slide 1: Overview
<!-- slide -->
Slide 2: Implementation Details
::::

```python
def agent_loop():
    pass
```
"""

# 1. AST Parsing & Density
ast_res = gam.parse_ast_token_density_and_depth(doc)
print(f"AST Density: {ast_res['structural_density_pct']}% | Max Depth={ast_res['max_ast_depth']} | RichDoc={ast_res['is_rich_document']}")
print(f"Elements: {ast_res['element_counts']}")

# 2. Interactive Widget Transformation
widgets = gam.transform_interactive_agentic_widgets(doc)
print()
print(f"Widgets Transformed: {widgets['total_widgets_transformed']} ({widgets['widget_breakdown']})")
for w in widgets["widgets"]:
    print(f"  {w['widget_type']}: {w['rendered_html'][:80]}...")

# 3. Accessibility & Structure Audit
audit = gam.audit_accessibility_and_contrast(doc)
print()
print(f"Accessibility Score: {audit['accessibility_score']}/100 ({audit['rating']}) | Violations={audit['violation_count']}")
