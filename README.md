# BugAnalyzer


A static code analyzer for Python that detects common bugs and code quality issues using Python's Abstract Syntax Tree (AST). This tool provides a user-friendly Streamlit web interface to paste your Python code, analyze it, and get actionable bug reports and suggestions for improvement.

---

## Features

- **Static Python code analysis using AST**: No code execution, safe for untrusted code.
- **Detects common issues**:
  - Use of variables before assignment
  - Functions missing a return statement
  - Unused function arguments
  - Syntax errors
- **Easy-to-use web interface**: Paste your Python code, analyze, and view results instantly.
- **Actionable bug reports**: Each issue comes with a description, suggested fix, and a confidence score.

---

## Demo

_![image](https://github.com/user-attachments/assets/f9550b95-763a-49aa-8f7d-79cf60fe9a94)
![image](https://github.com/user-attachments/assets/7ddc081e-8feb-4e6b-8e94-9b7208a2397c)



---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/python-ast-bug-finder.git
cd python-ast-bug-finder
```

### 2. Install dependencies

This project requires Python 3.7+ and uses [Streamlit](https://streamlit.io/).


## Usage

### Start the Streamlit app:

```bash
streamlit run app.py
```

### How to use

1. Open the provided Streamlit URL in your browser (usually http://localhost:8501).
2. Paste your Python code into the input area.
3. Optionally, specify a file name (used in the report).
4. Click **Analyze**.
5. View bug reports and suggestions below the form.

---

## Example Output

```
**File**: `example.py`  
**Line Number**: `3`  
**Issue Detected**: Variable 'x' used before assignment.  
**Variable Name**: `x`  
**Suggested Fix**: Assign a value to 'x' before using it.  
**Confidence Score**: `0.95`  
---
```

---

## Project Structure

```
├── app.py                 # Streamlit web interface
├── bug_analyzer.py        # Core Python AST analysis logic
├── README.md              # This file

```

---

## How it Works

- The app uses Python's `ast` module to parse input code and walk its syntax tree.
- It detects:
  - **Variables used before assignment**: Flags variables that are loaded before being assigned.
  - **Functions missing return**: Flags functions that do not contain a return statement.
  - **Unused function arguments**: Flags arguments that are never used inside a function.
  - **Syntax errors**: Catches and reports unparseable code.
- Each issue is reported with:
  - Source file and line number
  - Description of the problem
  - The variable or function involved
  - Suggested fix
  - Confidence score

---

## Limitations

- **Python-only**: Only supports Python code. Other languages will result in a syntax error.
- **AST-based analysis**: Cannot detect all types of bugs (e.g., runtime errors, logical errors, or issues requiring type inference).
- **False positives**: May flag unused arguments in callbacks or functions intentionally left without a return.
- **Not AI-powered**: Uses rule-based static analysis, not machine learning.

---

## Contributing

Contributions are welcome! To add features or improve bug detection, please open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
