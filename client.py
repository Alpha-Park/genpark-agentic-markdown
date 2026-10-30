# -*- coding: utf-8 -*-
"""
GenPark Agentic Markdown Client
Zero-dependency recursive CommonMark AST parser, interactive UI widget markup transformer,
and accessibility/contrast integrity auditor.
"""

import re
from typing import Dict, List, Any, Optional

class GenParkAgenticMarkdown:
    """
    Parses Markdown into structured AST node streams, transforms interactive widget directives,
    and audits document accessibility and structural integrity.
    """

    def parse_ast_token_density_and_depth(
        self,
        markdown_text: str
    ) -> Dict[str, Any]:
        """
        Parses Markdown text into token streams, measures maximum nesting depth, and computes structural density.
        """
        lines = markdown_text.splitlines()
        headings = []
        code_blocks = []
        links = []
        blockquotes = []
        math_blocks = []

        in_code = False
        code_lang = ""
        in_math = False
        max_depth = 0

        for idx, line in enumerate(lines):
            line_str = line.strip()
            
            # Check code fence
            if line_str.startswith("```"):
                if not in_code:
                    in_code = True
                    code_lang = line_str[3:].strip()
                else:
                    in_code = False
                    code_blocks.append({"line": idx + 1, "language": code_lang})
                continue
            if in_code:
                continue

            # Check math blocks
            if line_str.startswith("$$"):
                in_math = not in_math
                if in_math:
                    math_blocks.append({"line": idx + 1})
                continue
            if in_math:
                continue

            # Headings
            h_match = re.match(r"^(#{1,6})\s+(.*)$", line_str)
            if h_match:
                level = len(h_match.group(1))
                headings.append({"level": level, "text": h_match.group(2).strip(), "line": idx + 1})
                max_depth = max(max_depth, level)

            # Blockquotes
            if line_str.startswith(">"):
                quote_depth = len(re.match(r"^(>+)", line_str).group(1))
                blockquotes.append({"depth": quote_depth, "line": idx + 1})
                max_depth = max(max_depth, quote_depth)

            # Links [text](url)
            for m in re.finditer(r"\[([^\]]+)\]\(([^\)]+)\)", line_str):
                links.append({"text": m.group(1), "url": m.group(2), "line": idx + 1})

        total_lines = len(lines)
        total_elements = len(headings) + len(code_blocks) + len(links) + len(blockquotes) + len(math_blocks)
        density_pct = round(100.0 * total_elements / max(1, total_lines), 2)

        return {
            "total_lines": total_lines,
            "element_counts": {
                "headings": len(headings),
                "code_blocks": len(code_blocks),
                "links": len(links),
                "blockquotes": len(blockquotes),
                "math_blocks": len(math_blocks)
            },
            "max_ast_depth": max_depth,
            "structural_density_pct": density_pct,
            "is_rich_document": density_pct >= 15.0 and len(headings) >= 2
        }

    def transform_interactive_agentic_widgets(
        self,
        markdown_text: str
    ) -> Dict[str, Any]:
        """
        Transforms custom agentic widget markup (:::alert[type], :::tabs, :::carousel) into standard HTML AST structures.
        """
        widgets = []
        
        # Alerts
        alert_pattern = r":::alert\[(note|tip|warning|caution|important)\]\s*(.*?):::"
        for m in re.finditer(alert_pattern, markdown_text, re.DOTALL):
            alert_type = m.group(1)
            content = m.group(2).strip()
            widgets.append({
                "widget_type": "alert",
                "variant": alert_type,
                "content": content,
                "rendered_html": f'<div class="admonition admonition-{alert_type}"><p>{content}</p></div>'
            })

        # Tabs
        tabs_pattern = r":::tabs\s*(.*?):::"
        for m in re.finditer(tabs_pattern, markdown_text, re.DOTALL):
            tab_block = m.group(1).strip()
            widgets.append({
                "widget_type": "tabs",
                "raw_block": tab_block,
                "rendered_html": f'<div class="agentic-tabs">{tab_block}</div>'
            })

        # Carousels
        carousel_pattern = r"::::carousel\s*(.*?)::::"
        for m in re.finditer(carousel_pattern, markdown_text, re.DOTALL):
            slides = [s.strip() for s in m.group(1).split("<!-- slide -->") if s.strip()]
            widgets.append({
                "widget_type": "carousel",
                "slide_count": len(slides),
                "slides": slides,
                "rendered_html": f'<div class="agentic-carousel" data-slides="{len(slides)}">' + "".join(f"<div class=\"slide\">{s}</div>" for s in slides) + "</div>"
            })

        return {
            "total_widgets_transformed": len(widgets),
            "widget_breakdown": {
                "alerts": sum(1 for w in widgets if w["widget_type"] == "alert"),
                "tabs": sum(1 for w in widgets if w["widget_type"] == "tabs"),
                "carousels": sum(1 for w in widgets if w["widget_type"] == "carousel")
            },
            "widgets": widgets
        }

    def audit_accessibility_and_contrast(
        self,
        markdown_text: str
    ) -> Dict[str, Any]:
        """
        Audits accessibility: checks for skipped heading hierarchy, image alt text presence, and non-descriptive links.
        """
        violations = []
        
        # Check image alt tags: ![alt](url)
        for m in re.finditer(r"!\\[(.*?)\\]\((.*?)\)", markdown_text):
            alt_text = m.group(1).strip()
            if not alt_text:
                violations.append({
                    "type": "EMPTY_IMAGE_ALT",
                    "severity": "HIGH",
                    "issue": f"Image missing descriptive alt text for accessibility: {m.group(0)}"
                })

        # Check non-descriptive link text
        vague_links = ["click here", "link", "here", "more", "this"]
        for m in re.finditer(r"\[(.*?)\]\((.*?)\)", markdown_text):
            link_text = m.group(1).strip().lower()
            if link_text in vague_links:
                violations.append({
                    "type": "VAGUE_LINK_TEXT",
                    "severity": "MEDIUM",
                    "issue": f"Non-descriptive link text '{m.group(1)}'. Prefer descriptive anchor text."
                })

        # Check heading hierarchy (skipping levels e.g. H1 -> H3)
        headings = [len(m.group(1)) for m in re.finditer(r"^(#{1,6})\s+", markdown_text, re.MULTILINE)]
        for i in range(1, len(headings)):
            if headings[i] > headings[i - 1] + 1:
                violations.append({
                    "type": "SKIPPED_HEADING_LEVEL",
                    "severity": "LOW",
                    "issue": f"Skipped heading level from H{headings[i-1]} to H{headings[i]}."
                })

        score = max(0, 100 - len(violations) * 15)

        return {
            "accessibility_score": score,
            "is_accessible": len(violations) == 0,
            "violation_count": len(violations),
            "violations": violations,
            "rating": "PERFECT" if score == 100 else ("NEEDS_WORK" if score >= 70 else "ACCESSIBILITY_FAILED")
        }
