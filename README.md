# AutoDesk 

**Your Personal Automation Center**

AutoDesk is a Python desktop application designed to simplify repetitive computer tasks through a clean, user-friendly graphical interface. It brings useful file management and automation tools together in one place.

The project is being built as a hands-on exploration of Python, desktop GUI development, and practical automation.

##  Features

* **File Organizer** — Automatically sort files into categorized folders based on file type.
* **Folder Analyzer** — Analyze folders to view file counts, file types, and total storage usage.
* **Batch File Renamer** — Rename multiple files using customizable prefixes and numbering.
* **Visual Dashboard** — Access automation tools through a modern desktop interface.
* **Task History** — Track completed automation tasks and their results.

> Features are planned for implementation as development progresses.

##  Tech Stack

* **Python** — Core application logic and automation.
* **CustomTkinter** — Modern graphical user interface.
* **pathlib** — Filesystem navigation and path management.
* **shutil** — File operations and organization.
* **unittest / pytest** — Testing and reliability.

##  Project Structure

```text
AutoDesk/
├── main.py
├── automations/
│   ├── organizer.py
│   ├── analyzer.py
│   └── renamer.py
├── tests/
├── requirements.txt
├── .gitignore
└── README.md
```

*The structure may evolve as the project grows.*

##  Getting Started

### Prerequisites

* Python 3.11 or newer
* Git

### 1. Clone the repository

```bash
git clone https://github.com/mwanzia-simon/AUTO-DESK
cd AUTO-DESK
```

### 2. Create a virtual environment

**Windows:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install customtkinter
```

### 4. Run the application

```bash
python main.py
```

##  Project Goals

* Build a functional desktop automation dashboard.
* Practice modular Python development.
* Learn graphical user interface design.
* Implement safe and reliable filesystem operations.
* Improve error handling, testing, and code organization.

##  Safety

AutoDesk interacts with files on your computer. Always test file operations using sample folders first. Preview changes before applying them, handle duplicate filenames safely, and avoid modifying important files without confirmation.

##  Roadmap

* [ ] Create the main dashboard and navigation.
* [ ] Implement the file organizer.
* [ ] Add folder analysis and storage statistics.
* [ ] Implement batch file renaming with previews.
* [ ] Add task history and progress indicators.
* [ ] Improve error handling and automated tests.
* [ ] Package the application for desktop use.

##  Contributing

Suggestions, bug reports, and improvements are welcome. Feel free to fork the repository and experiment with new automation features.

##  License

This project is currently a learning project. A license can be added when the distribution terms are decided.
