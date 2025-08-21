 🧠 KUSP - Mini C Compiler

**KUSP** (Kritarth Uddhav Shashank Pragyan) is a custom-built mini C compiler developed in Python using the PLY (Python Lex-Yacc) library. It performs lexical analysis, parsing, semantic checks, intermediate code generation, and execution through a virtual machine. It also features a modern Graphical User Interface (GUI) for ease of interaction.

---

## 🚀 Features

- ✅ Lexical Analysis using `ply.lex`
- ✅ Parsing and Syntax Analysis using `ply.yacc`
- ✅ Semantic Analysis (undeclared variables, invalid assignments)
- ✅ Intermediate Code Generation
- ✅ Virtual Machine Execution of Intermediate Code
- ✅ Modern GUI using `Tkinter`
- ✅ Built-in Runtime Emulator (Run button)
- ✅ Color-coded Dracula Theme
- ✅ Line-by-line Output & Error Reporting
- ✅ Clear Output with Line Counter Reset
- ✅ Modular code for future extensions

---

## 🔧 Technologies Used

- **Python 3.12**
- **PLY (Python Lex-Yacc) Version: 3.11**
- **Tkinter** – for the GUI
- **Custom VM** – to execute intermediate code
- **Dracula Theme** – for stylish UI

---

## 📁 Project Structure

KUSP/
├── lexer.py # Handles tokenization
├── parser.py # Contains parsing logic & semantic checks
├── vm.py # Virtual machine to run intermediate code
├── gui.py # GUI frontend with code editor
├── yest.c # Sample C program to test the compiler
├── README.md # Project documentation

---

## 🧪 Supported C Features

- Basic types: `int`, `char`
- Arithmetic: `+`, `-`, `*`, `/`
- Relational: `==`, `!=`, `<`, `<=`, `>`, `>=`
- Logical: `&&`, `||`
- Control Flow: `if`, `else`, `while`
- Input/Output: `printf`, `scanf`
- Return statements
- Character constants like `'x'`

---

## 🖥️ How to Run

### 🔹 1. Install Requirements

in bash:

pip install ply
🔹 2. Run the GUI
       python gui.py
🔹 3. Compile and Execute a C Program
Write or paste C code into the GUI.

Click "Run" to analyze, compile, and execute the code.

View output and any errors in the output panel.

📸 Screenshots
![image](https://github.com/user-attachments/assets/4ae8e290-867d-446e-8153-249945305bfd)


🙌 Credits
Developed by Kritarth Uddhav Shashank Pragyan as a semester project for Compiler Design using Python.
