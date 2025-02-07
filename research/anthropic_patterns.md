# Anthropic Code Patterns and Structures

## Display System
### Message Structure
- **Format**: `(role, text)` tuple structure
- **Roles**: user, assistant, system
- **Role Display**: U (#007AFF), A (#FF9500), S (#4CD964)

### Content Blocks
```
<code>...</code>
<stdout>...</stdout>
<stderr>...</stderr>
```

### Display Elements
- Chat container: 750px max-width
- System font stack: -apple-system, BlinkMacSystemFont, etc.
- Avatar system: 24px circular indicators

## Code Execution System
### Output Structure
```python
@dataclass(frozen=True)
class CodeOutput:
    stdout: str
    stderr: str
    returncode: int = 0
```

### Execution Environment
- **Default Modules**: 
  - scikit-learn
  - gym
  - torchvision
  - pillow
- **Pattern**: ML/AI focused environment

### Execution Patterns
- Asynchronous execution
- Result caching
- Immutable outputs
- Controlled module access

### Integration Points
- stdout/stderr mapping to display blocks
- Return code handling
- Async chat interaction flow

## Formatting System
### Code Highlighting
- System: Pygments
- Theme: Friendly
- Language: Python-focused

### Color Scheme
- Keywords: #007020 (bold)
- Strings: #4070a0
- Comments: #60a0b0 (italic)
- Functions: #06287e
- Variables: #bb60d5

## Security Patterns
- Immutable data structures
- Controlled module access
- Sandboxed execution
- Structured error handling

## Utility Patterns
### Async Caching
- **Structure**: Decorator-based cache
- **Features**:
  - Concurrent access control
  - Exception caching
  - Exponential backoff
  - Process deduplication

### Type System
- **Generic Parameters**: ParamSpec, TypeVar
- **Return Types**: Coroutine specifications
- **Type Safety**: Extensive hinting

### Data Serialization
- **JSON Encoding**: Custom dataclass handling
- **Recursive Processing**: Nested structure support
- **Type Preservation**: Structured serialization

### Error Management
- **Cache Strategy**: Result/Exception tuples
- **Propagation**: Consistent error handling
- **Type Safety**: Error type preservation

## Training Data Patterns
### JSON Structure
- **Core Fields**:
  - prompt: Scenario text
  - corrects/incorrects: Answer options
  - text_correct/incorrect: Full conversations

### Response Format
- Triple bracket delimiters [[[...]]]
- Letter-based options (A), (B)
- Space-prefixed identifiers

### Quality Markers
- Comprehensive information
- Ethical considerations
- Legal implications
- Clear warnings
- Detailed explanations

### Conversation Structure
- Double newline separation
- Role-based formatting
- Context preservation

*Note: These patterns inform both training and response generation.*

## Processing Flow
1. Code input → Async execution
2. Output capture → Immutable structure
3. Format application → Display blocks
4. Role-based styling → Final display

*Note: This is a living document that captures Anthropic's code patterns for reference and replication.*
