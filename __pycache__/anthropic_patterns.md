# Anthropic Code Patterns and Structures

This document catalogs observed patterns in Anthropic's code, specifically their chat display system.

## Message Structure
- **Format**: `(role, text)` tuple structure
- **Roles**:
  - user
  - assistant
  - system
- **Role Display**:
  - U (User): #007AFF
  - A (Assistant): #FF9500
  - S (System): #4CD964

## Content Blocks
### Code Blocks
```
<code>...</code>
```
- Formatter: PythonLexer
- Style: Pygments friendly theme

### Standard Output
```
<stdout>...</stdout>
```
- Background: #f0f0f0
- Font: Courier New, monospace

### Error Output
```
<stderr>...</stderr>
```
- Background: #fff0f0
- Color: #d00000
- Border: #ffd0d0

## Display Elements
### Chat Container
- Max Width: 750px
- Font Family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif

### Message Formatting
- Padding Left: 40px
- Margin Bottom: 24px
- Line Height: 1.6

### Avatar Design
- Size: 24px
- Border Radius: 12px
- Colors:
  - User: #007AFF
  - Assistant: #FF9500
  - System: #4CD964

## Code Formatting
### Syntax Highlighting
- System: Pygments
- Theme: Friendly

### Color Scheme
- Keywords: #007020 (bold)
- Strings: #4070a0
- Comments: #60a0b0 (italic)
- Functions: #06287e
- Variables: #bb60d5
- Numbers: #40a070
- Class Names: #0e84b5 (bold)
- Decorators: #555555 (bold)

---
*Note: This is a living document that will be updated as we analyze more of Anthropic's code patterns.*
