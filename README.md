=== File: README.md ===
<!-- Repository Badges -->
<p align="center">
  <a href="https://github.com/GovindTechie/Programming-Collection/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/GovindTechie/Programming-Collection/ci.yml?branch=master" alt="CI Status" />
  </a>
  <a href="https://github.com/GovindTechie/Programming-Collection/releases">
    <img src="https://img.shields.io/github/v/release/GovindTechie/Programming-Collection" alt="Release Version" />
  </a>
  <a href="https://github.com/GovindTechie/Programming-Collection/issues">
    <img src="https://img.shields.io/github/issues/GovindTechie/Programming-Collection" alt="Open Issues" />
  </a>
  <a href="https://github.com/GovindTechie/Programming-Collection/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/GovindTechie/Programming-Collection" alt="License" />
  </a>
</p>

# 📚 Programming‑Collection
Curated examples & mini‑projects in C, C++, Java, JavaScript, and Python—perfect for learners, interview prep, or quick reference.

## 📑 Table of Contents
- [About](#about)
- [Demo](#demo)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [Changelog](#changelog)
- [License](#license)
- [Contact](#contact)

## About
This repo collects small, well‑documented code examples across multiple languages. Each top‑level folder has its own README showing how to run the examples.

## Demo
![Flask Library Management Demo](./assets/flask-demo.gif)

## Getting Started
1. **Clone** the repo:
   ```bash
   git clone https://github.com/GovindTechie/Programming-Collection.git
   cd Programming-Collection
   ```
2. **Install dependencies** (for Flask example):
   ```bash
   pip install -r FlaskLibraryManagement/requirements.txt
   ```

## Usage
Choose any language folder and follow its instructions. For example, to run a C example:
```bash
cd C_Language
gcc linked_list.c -o linked_list && ./linked_list
```

## Folder Structure
- CPP_Language — OOP, templates, STL, file I/O, algorithms
- C_Language — Data structures, pointers, dynamic memory, file handling
- JavaGUI_Application — Swing & JavaFX UIs
- JavaServlet&JDBC — Servlets + JDBC CRUD examples
- Java_Language — Core Java, concurrency, collections, streams
- JavaScript — DOM, ES6+, async/await, mini apps
- Python_Language — pandas, NumPy, matplotlib, web scraping
- FlaskLibraryManagement — RESTful Flask backend + Bootstrap frontend

## Contributing
We welcome contributions! Please read CONTRIBUTING.md and follow these steps:
1. Fork the repo & create a branch (`git checkout -b feature/name`)
2. Add or improve examples, update docs
3. Submit a Pull Request

## Roadmap
- Add Ruby and Go examples
- Dockerize select projects
- Expand AI/ML demos in Python

## Changelog
See CHANGELOG.md for release notes and updates.

## License
MIT © GovindTechie — see LICENSE

## Contact
Maintainer: GovindTechie • Email: khedkargovind60@gmail.com

=== File: C_Language/README.md ===
# C Language Examples

This folder contains small C programs demonstrating:
- Data structures: linked lists, stacks, queues (linked_list.c, stack.c)
- Pointers & memory: malloc_demo.c, pointer_arith.c
- File I/O: file_read_write.c, binary_io.c

## Usage
Compile and run any example:
```bash
gcc linked_list.c -o linked_list && ./linked_list
```

## Programs
| File              | Description                    |
|-------------------|--------------------------------|
| linked_list.c     | Singly & doubly linked lists   |
| stack.c           | Array- and pointer-based stack |
| pointer_arith.c   | Demonstrates pointer arithmetic|
| ...               | ...                            |

=== File: CPP_Language/README.md ===
# C++ Language Examples

- OOP: classes.cpp, inheritance.cpp, polymorphism.cpp
- Templates & STL: vector_demo.cpp, map_usage.cpp
- File I/O: file_streams.cpp

## Usage
```bash
g++ classes.cpp -o classes && ./classes
```

## Programs
| File             | Description          |
|------------------|----------------------|
| inheritance.cpp  | Base & derived demo  |
| vector_demo.cpp  | Vector operations    |
| ...              | ...                  |

=== File: JavaScript/README.md ===
# JavaScript Projects

- DOM & Events: dom_events.html, event_handlers.js
- ES6+: modules_demo.js, async_await.js
- Mini Apps: todo_app/, calculator/

## Usage
Open index.html in your browser or serve via Live Server.

=== File: FlaskLibraryManagement/README.md ===
# Flask Library Management

A simple library system with:
- RESTful Flask backend (app.py, routes.py)
- Bootstrap frontend (templates/, static/)
- SQLite integration

## Setup
```bash
cd FlaskLibraryManagement
pip install -r requirements.txt
flask run
```

Access at http://localhost:5000

=== File: CONTRIBUTING.md ===
# Contributing to Programming‑Collection

Thank you for considering a contribution! Please follow these steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Add or update examples and tests
4. Update relevant README.md
5. Submit a pull request

Please read our Code of Conduct in CODE_OF_CONDUCT.md.

=== File: CODE_OF_CONDUCT.md ===
# Code of Conduct

All participants are expected to uphold this code of conduct to maintain a welcoming community.
* Be respectful and considerate.
* No harassment or discrimination.
* Report issues to the maintainers.

=== File: CHANGELOG.md ===
# Changelog

## [Unreleased]
- Initial restructure and documentation overhaul

## [v0.1.0] - 2025-04-17
- Added root and folder READMEs
- Introduced Table of Contents, Usage & Contributing guides
