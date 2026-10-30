# -*- coding: utf-8 -*-
"""
GenPark Agentic Markdown FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import GenParkAgenticMarkdown

mcp = FastMCP("genpark-agentic-markdown")
md = GenParkAgenticMarkdown()

@mcp.tool()
def parse_ast_token_density_and_depth(markdown_text: str) -> str:
    """
    Parses Markdown text into token streams, measures maximum nesting depth, and computes structural density.
    """
    res = md.parse_ast_token_density_and_depth(markdown_text)
    return json.dumps(res, indent=2)

@mcp.tool()
def transform_interactive_agentic_widgets(markdown_text: str) -> str:
    """
    Transforms custom agentic widget markup (alerts, tabs, carousels) into HTML structures.
    """
    res = md.transform_interactive_agentic_widgets(markdown_text)
    return json.dumps(res, indent=2)

@mcp.tool()
def audit_accessibility_and_contrast(markdown_text: str) -> str:
    """
    Audits accessibility: checks for skipped heading hierarchy, image alt text, and non-descriptive links.
    """
    res = md.audit_accessibility_and_contrast(markdown_text)
    return json.dumps(res, indent=2)

def main():
    print("Testing Agentic Markdown:")
    doc = "# Title\n\n:::alert[note] Note text :::"
    print(transform_interactive_agentic_widgets(doc))

if __name__ == "__main__":
    main()
