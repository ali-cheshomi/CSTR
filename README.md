# CSTR

 A lightweight Python class for adding **ANSI colors and background colors to strings** using a simple and readable syntax.

 Instead of writing ANSI escape sequences manually, you can use short color codes such as `^r^`, `^g^`, `^b^`, etc.

 ## ✨ Features

 - 🎨 Easy colored text syntax
- 🖌️ Support for background colors
- 📝 Automatically provides the raw/uncolored text
- 💻 Uses standard ANSI escape sequences
- 🐍 Pure Python — no external dependencies
- 🔄 `CSTR` behaves like a normal Python `str`

 ## 📁 Project Structure

```
CSTR/
│
├── CSTR.py
├── __main__.py
└── README.md
```

 > `__pycache__` is generated automatically by Python and does not need to be included in the repository.

 ## 🚀 Installation

 No external package is required.

 Clone the repository:

```
git clone https://github.com/ali-cheshomi/CSTR.git
cd REPOSITORY
```

 Then simply import `cstr`:

```
from CSTR import cstr
```

 ## 📖 Usage

 ### Basic Example

```
from CSTR import cstr

text = cstr("^r^Hello ^g^World!")

print(text)
```

 The `^color^` syntax is replaced with the corresponding ANSI color code.

 ### Example

```
from CSTR import cstr

text1 = "this is a test1 for color"

text2 = cstr("^r^this ^g^is a test2 ^b^for^y^ color")

print(text1)
print(text2)
```

 The second string will be displayed with multiple colors in a terminal that supports ANSI escape sequences.

 ## 🎨 Color Codes

 ### Text Colors

 | Code | Color |
| --- | --- |
| `^r^` | 🔴 Red |
| `^g^` | 🟢 Green |
| `^b^` | 🔵 Blue |
| `^c^` | 🩵 Cyan |
| `^y^` | 🟡 Yellow |
| `^w^` | Reset |
| `^k^` | Gray |
| `^t^` | Transparent/hidden |

 ### Background Colors

 | Code | Background |
| --- | --- |
| `^R^` | 🔴 Red |
| `^G^` | 🟢 Green |
| `^B^` | 🔵 Blue |
| `^C^` | 🩵 Cyan |
| `^Y^` | 🟡 Yellow |
| `^W^` | ⚪ White |
| `^D^` | ⚫ Black |
| `^Rs^` | Reset |

 ## 🔄 Raw Text

 `cstr` stores both the colored version and the raw version of the text.

 For example:

```
from CSTR import cstr

text = cstr("^r^Hello ^g^World")

print(text)
```

 The raw text can be accessed using:

```
print(text._RawText)
```

 Output:

```
Hello World
```

 While:

```
print(text._ColoredText)
```

 contains the ANSI escape sequences used for terminal coloring.

 ## 📄 Writing Colored Text to a File

 You can also write the colored string to a file:

```
from CSTR import cstr

text = cstr("^r^Hello ^g^World")

with open("test.txt", "w") as f:
    f.write(text)
```

 Keep in mind that the file will contain ANSI escape sequences rather than visually colored text. The colors will only be rendered by applications that interpret ANSI escape codes.

 ## 🧩 How It Works

 The `cstr` class inherits from Python's built-in `str`:

```
class cstr(str):
```

 When a `cstr` object is created, the class:

 1. Detects color markers such as `^r^` and `^g^`.
2. Removes these markers to create the raw string.
3. Replaces the markers with ANSI escape sequences.
4. Stores both versions of the string.
5. Returns the raw version as the underlying `str` value.
6. Displays the colored version when converted to `str` or printed.

 For example:

```
^r^Hello ^g^World
```

 becomes conceptually:

```
Hello World
```

 for the raw text, while the terminal version contains ANSI escape sequences for red and green.

 ## 🖥️ Terminal Compatibility

 `CSTR` relies on ANSI escape sequences.

 Most modern Linux and macOS terminals support them. Windows Terminal and modern Windows consoles also generally support ANSI/VT sequences.

 If the terminal does not support ANSI colors, you may see escape sequences instead of colors.

 ## ⚠️ Notes

 - `^` is used as the color-marker character.
- Color codes are case-sensitive.
- ANSI support depends on the terminal or application.
- `__pycache__` should normally be excluded from Git.
- For a clean repository, add it to `.gitignore`.

 Example `.gitignore`:

```
__pycache__/
*.pyc
```

 ## 🛠️ Requirements

 - Python 3.x
- No external dependencies

 ## 📜 License

license file [here](https://github.com/ali-cheshomi/CSTR/blob/main/LICENSE)

```
Please make sure your changes are compatible with the project's
[Apache License 2.0]
```

 If this project is intended to be open source, adding a `LICENSE` file to the repository is recommended.

 ## ⭐ Contributing

 Contributions, improvements, and bug reports are welcome.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Open a Pull Request.

---

 Made with ❤️ and Python 🐍
