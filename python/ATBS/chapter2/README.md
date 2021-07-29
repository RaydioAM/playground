# Flow Control

**Flow Control** - How a program decides which Python instructions to execute under which conditions.

## Boolean Values
**Boolean** - A data type with only two values: `True` or `False`.
- Booleans are not treated as strings.
- Must start with a capital `T` or `F`.

## Comparison Operators
**Comparison Operator** (also called Relational Operators) - Compares two values and evaluates down to a single Boolean value.

### Comparisons
| Operator | Meaning |
|---|---|
| == | Equal to |
| != | Not equal to |
| < | Less than |
| > | Greater than |
| <= | Less than or equal to |
| >= | Greater than or equal to|

_Note: an integer or floating-point value will always be unequal to a string value._

## Boolean Operators
Operators that are used to compare Boolean values:
- `and`
- `or`
- `not`

### Binary Boolean Operators
`and` and `or` are _binary_ operators because they always take two Boolean values.
- `and` - Evaluates to `True` if both Boolean values are `True`
- `or` - Evalueates to `True` if _either_ of the Boolean values are `True`

### The not Operator
Unlike Boolean operators, the `not` operator only operates on one Boolean value, making it a _unary_ operator. The `not` operator evaluates to the opposite Boolean value.

### Mixing Boolean and Comparison Operators
As comparison operators evaluate to Boolean values, comparison operators can be mixed with Boolean operators.

```python
>>> (4 < 5) and (5 < 6)
True
```

## Elements of Flow Control
Flow control statements start with the _condition_ and are followed by a block of code called the _clause_.

### Conditions
Conditions are a more specific name for _expressions_ that evaluate down to a Boolean value. Flow control statements decide what to do based on whether the condition is `True` or `False`.