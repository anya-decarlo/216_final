"""
Dictionary of Anthropic code patterns and structures observed in their chat display system.
"""

ANTHROPIC_PATTERNS = {
    "message_structure": {
        "format": "(role, text)",
        "roles": ["user", "assistant", "system"],
        "role_display": {
            "user": "U",
            "assistant": "A",
            "system": "S"
        }
    },
    
    "content_blocks": {
        "code": {
            "pattern": "<code>...</code>",
            "formatter": "PythonLexer",
            "styling": "pygments friendly"
        },
        "stdout": {
            "pattern": "<stdout>...</stdout>",
            "styling": "background-color: #f0f0f0"
        },
        "stderr": {
            "pattern": "<stderr>...</stderr>",
            "styling": "background-color: #fff0f0"
        }
    },
    
    "display_elements": {
        "chat_container": {
            "max_width": "750px",
            "font_family": "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
        },
        "message": {
            "padding_left": "40px",
            "margin_bottom": "24px",
            "line_height": "1.6"
        },
        "avatar": {
            "size": "24px",
            "colors": {
                "user": "#007AFF",
                "assistant": "#FF9500",
                "system": "#4CD964"
            }
        }
    },
    
    "code_formatting": {
        "syntax_highlighting": "pygments",
        "style": "friendly",
        "elements": {
            "keywords": {"color": "#007020", "weight": "bold"},
            "strings": {"color": "#4070a0"},
            "comments": {"color": "#60a0b0", "style": "italic"},
            "functions": {"color": "#06287e"}
        }
    }
}

# Additional patterns can be added as we analyze more files
