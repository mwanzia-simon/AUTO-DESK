# AutoDesk | Automation Center

AutoDesk is a Python desktop application designed to simplify everyday tasks through automation. Its first implemented feature is a **file organizer** that automatically sorts files into categories based on their file extensions.

The application uses CustomTkinter to provide a graphical user interface, allowing users to select a folder and organize its contents without manually moving files.

## Features

- **Folder Selection:** Choose a folder to organize using a file browser.
- **Automatic File Organization:** Sort supported files into category folders.
- **File Categories:**
  - **Images:** `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`
  - **Documents:** `.pdf`, `.docx`, `.txt`, `.xlsx`, `.js`, `.ts`
  - **Videos:** `.mp4`, `.mkv`, `.mov`
- **Duplicate Protection:** Skip files when a file with the same name already exists in the destination folder.
- **Operation Statistics:** Display the number of moved, skipped, and failed files.
- **Error Handling:** Handle common filesystem errors, including inaccessible folders and failed file operations.
- **Graphical Interface:** A dark-themed interface built with CustomTkinter.

## Tech Stack

- **Python** — Application logic and file operations.
- **CustomTkinter** — Desktop graphical user interface.
- **OS and Shutil modules** — Folder navigation, directory creation, and file movement.

## Project Structure

```text
AutoDesk/
├── main.py
├── automations/
│   ├── __init__.py
│   └── organizer.py
├── tests/
├── requirements.txt
├── .gitignore
└── README.md
```

*Note: The structure above represents the intended project layout. Adjust it to match your actual repository.*

## Getting Started

### Prerequisites

- Python 3.10 or later recommended.
- Git (optional, for cloning the repository).

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mwanzia-simon/AUTO-DESK
   ```

2. Navigate into the project directory:

   ```bash
   cd AUTO-DESK
   ```

3. Create and activate a virtual environment:

   **Windows:**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   If your requirements file does not yet list CustomTkinter, install it with:

   ```bash
   pip install customtkinter
   ```

### Running AutoDesk

Start the application from the project root:

```bash
python main.py
```

Select a folder, click **Organize files**, and review the operation statistics in the results panel.

## How It Works

1. The user selects a folder through the graphical interface.
2. AutoDesk scans the selected folder's immediate contents.
3. Each supported file is identified by its extension.
4. Category folders are created when necessary.
5. Supported files are moved into their respective folders.
6. Files with an existing destination filename are skipped.
7. The application reports the number of moved, skipped, and failed files.

## Current Development Status

**Implemented:** File organization with a CustomTkinter graphical interface.

**Future Improvements:**
- Display individual file operations in a scrollable activity panel.
- Add more automation features.
- Improve error reporting and user feedback.
- Continue improving the interface and overall user experience.

## Purpose

AutoDesk is a hands-on software development project focused on learning Python, desktop application development, file handling, error handling, and automation.

The project will evolve as additional features are designed, implemented, and tested.

## License

No license has been specified yet. A license can be added when the project's distribution terms are decided.
