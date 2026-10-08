
# Password Analyzer and Generator

A basic Python project with a graphical user interface. It analyzes passwords in real time as you type, evaluates their strength, identifies missing security requirements, and suggests a stronger password.

The application also includes a separate tab for generating customizable passwords and a comfortable dark-themed interface for desktop use.

## Features

- Real-time password analysis with every character typed
- Fully dark-themed interface
- Color-coded password strength indicator
- Five strength levels: Very Weak, Weak, Medium, Strong, and Very Strong
- List of missing requirements to improve password security
- Automatic strong password suggestions
- Password generator supporting 6 to 128 characters
- Customizable options for uppercase letters, lowercase letters, numbers, and special characters
- Option to exclude ambiguous characters such as `I`, `l`, `1`, `O`, `0`, and `o`
- Button to copy generated passwords
- Automated tests for core functionality

## What You Will Practice

- Strings and lists
- Functions
- Conditional statements and loops
- Regular expressions using `re`
- Secure random value generation using `secrets`
- Graphical user interface development with `tkinter`
- Automated testing with `unittest`

> This project uses Python's `secrets` module instead of `random` because `secrets` is more suitable for generating unpredictable and secure passwords.

## How to Run in VS Code

1. Install Python 3 from the official website and enable **Add Python to PATH**.
2. Extract the project folder.
3. Open the `analisador_senhas` folder in Visual Studio Code.
4. Open the integrated terminal through **Terminal > New Terminal**.
5. Run the application:

```bash
python app.py
```

On Windows, if `python` does not work, try:

```bash
py app.py
```

No additional packages are required because the project uses only Python's standard library.

## How to Run Tests

Inside the project directory, run:

```bash
python -m unittest -v
```

Alternatively, on Windows:

```bash
py -m unittest -v
```

If all tests return `ok`, the tested core functionality is working as expected.

## Project Structure

```text
analisador_senhas/
├── app.py
├── password_tools.py
├── test_password_tools.py
├── requirements.txt
└── .gitignore
```

## Technologies Used

- Python
- tkinter
- re
- secrets
- unittest

## Project Purpose

This project was developed to practice Python programming, password validation, secure password generation, graphical interface development, and automated testing.

It also provides hands-on experience with basic password security concepts and secure coding practices.

## Author

Developed by **Emanuel Vítor Fernandes Nascimento**.

[GitHub](https://github.com/emanuelvitorfn7-gif)

