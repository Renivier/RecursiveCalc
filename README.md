# RecursiveCalc

**RecursiveCalc** is a Python-based arithmetic expression evaluator. It parses and calculates mathematical expressions from strings, handling:

- Parentheses recursively
- Operator precedence (PEMDAS)
- Unary minus (e.g., `-3`)
- Implicit multiplication (e.g., `2(3 + 4)`)

---

## Features

- `Tokenize()`: Converts a string into a list of numbers, operators, and parentheses
- `recursive_parser()`: Handles nested parentheses and creates sublists
- `evaluate()`: Evaluates expressions using operator precedence
- `calculate_expression(expr)`: Simple wrapper for evaluating any string expression
- Fully compatible with Discord bots or standalone scripts

---

## Usage

```python
import calculator

expr = "2*(3 + 4) - 5/2"
result = calculator.calculate_expression(expr)
print(result)  # Output: 10.5
```
or you can run standalone
```python calculator.py```
# Discord Bot Integration
It can be directly integrated into a Discord bot:
```python
@bot.command()
async def calculate(ctx, *, expression: str):
    try:
        result = calculator.calculate_expression(expression)
        await ctx.send(f"Result: {result}")
    except Exception as e:
        await ctx.send(f"Error in calculation: {e}")
```

