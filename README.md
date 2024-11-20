# mini Test Case Adder
You can use this program to quickly add test cases related to questions in the tc (test cases) folder. You can also test these test cases using [mini-judge](https://github.com/ctrl-alt-Defeat-icpc/mini-judge).

`tca.py` is a Python program designed to simplify the process of adding test cases for competitive programming problems. It helps you quickly organize and create test case folders and files, streamlining the workflow for problem-solving.

---

## Features

- **Quick Test Case Setup**: Automatically generate folders and files for test cases.
- **Customizable Naming**: Flexible options for naming and organizing test cases.
- **Easy-to-Use Switches**: Various switches to control behavior and add specific features.

---

## Installation

1. Ensure you have Python 3 installed on your system.
2. Clone or download this repository:
   ```bash
   git clone https://github.com/ctrl-alt-Defeat-icpc/mini-tca.git
   cd mini-tca
   ```
3. Run the program:
    ```bash
    python3 tca.py <switch>
    ```

## Usage
Here's how you can use `tca.py`:
| switch | description |
|---|---|
| `+` | Create a series of folders for test cases. |
| `.` | Create test cases for all problems |
| `<name>` | Create test cases for a specific problem |

<details><summary><strong>How About domjudge.py file?</strong></summary><br>

This is probably the simplest executable you'll ever see. Just copy the files in the format `samples-x.zip`, where `x` is the **name of problem**, into the `tc` folder, and then run the `domjudge.py` [file](./tc/domjudge.py).

This program will extract the **zip files**, give the folder a shortened name, and then delete the zip file.
</details>

## Contribution
This project is licensed under the [MIT License](./LICENSE), so feel free to use and modify it as you like. I believe in the power of collaboration, and I'm always excited to see others improve or expand this project.

Got ideas or suggestions? Found a bug? Open an issue or send a pull request. Let's make this tool better together! 🚀