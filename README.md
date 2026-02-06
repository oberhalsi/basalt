# Basalt

> **Learn the Stack.**

A minimalist stack-oriented programming language designed to teach the fundamentals of stack-based computing. No parentheses. No indentation. No noise — just the pure mechanics of a stack.

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)

## What is Basalt?

Basalt strips programming down to its **raw fundamentals**. Every operation is an explicit manipulation of a single data structure — the stack. There are no hidden abstractions, no syntactic sugar hiding complexity. What you see is exactly what the interpreter executes.

Written in **Python 3** with a custom-built Lexer and Parser, Basalt is fully open source. You can read every line of the interpreter and trace exactly how your code is processed — from raw text to executed output.

## Features

- **Stack-Oriented**: All computation flows through a single stack. Push values, apply operations, read results — no variable declarations needed.
- **Zero Noise**: No parentheses, no indentation, no semicolons. Basalt's syntax is intentionally stripped bare so you focus on the stack.
- **Fully Transparent**: The entire interpreter is open source. Trace how the lexer tokenizes input, how the parser builds structure, and how each instruction executes.
- **Learn by Doing**: Basalt is purpose-built for learning. Master stack manipulation, understand how real low-level systems work, build from the ground up.

## Quick Start

### Prerequisites

- Python 3.x installed on your system

### Installation

1. Clone this repository:
```bash
git clone https://github.com/oberhalsi/basalt.git
cd basalt
```

2. Quickly run your first program:
```bash
python main.py tests/math.b
```

3. Or if you have completed the full installation:
```bash
basalt yourfile.b
```

### Your First Program

Create a file called `hello.b`:

```basalt
# Push two numbers and add them
7 42 + print

# Output: 49
```

Run it:
```bash
python main.py hello.b
```

## Project Structure

```
basalt/
├── src/
│   ├── lexer.py         # Tokenization
│   ├── parser.py        # AST generation
│   └── interpreter.py   # Execution engine
├── tests/
│   ├── math.b           # Basic arithmetic examples
│   └── factorial.b      # Recursion example
├── docs/                # Documentation
├── main.py              # Entry point
└── README.md
```

## Documentation

For more detailed documentation, check out the `/docs` folder or visit our [website](https://basaltt.vercel.app/).

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
6. Validate Changes: Run `test_basalt` to ensure all core mechanics and stack operations remain intact.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by Forth, PostScript, and other stack-based languages
- Built as an educational tool to demystify how programming languages work
- Thanks to everyone who believed in this project

---

**Learn more at [basaltt.vercel.app](https://basaltt.vercel.app/)**

---

**Oberhalsi** ([@Oberhalsi](https://github.com/oberhalsi)) & **Alexander Wondwossen** ([@alxgraphy](https://github.com/alxgraphy))  
Made with ❤️ from two kids who had an idea in Toronto, Canada 🇨🇦
