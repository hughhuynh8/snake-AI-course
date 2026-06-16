# Project GEMINI: Snake Game Suite

This project provides two distinct implementations of the classic Snake game, catering to different terminal and environment capabilities.

## Project Overview

- **Core Purpose**: A lightweight, zero-dependency Snake game suite for Python.
- **Main Technologies**: Python 3.x, `turtle` (for GUI), and `curses` (for CLI).
- **Architecture**: Single-file procedural game loops for both versions.

## Building and Running

### Prerequisites
- Python 3.10 or higher.
- (Optional) `tkinter` for the graphical version.

### Execution Commands

- **Terminal Version (Recommended)**: Use this if you are in a remote SSH session or lack a window manager.
  ```bash
  python3 snake_cli.py
  ```
- **Graphical Version**: Opens a window on your desktop.
  ```bash
  python3 snake.py
  ```

### Testing
- No formal testing framework is currently implemented. Verification is done through manual gameplay.
- **TODO**: Implement basic unit tests for movement logic and collision detection.

## Development Conventions

- **Dependencies**: Prioritize using the Python Standard Library to ensure maximum portability.
- **Environment**: A local `venv` directory is used for experimentation, but the core game files must remain dependency-free.
- **Coding Style**:
  - Use descriptive variable names (e.g., `snake_head`, `food_pos`).
  - Maintain a clear separation between game state updates and rendering.
  - Keyboard event handling should support both WASD and Arrow keys where possible.

## Key Files

- `snake.py`: Graphical implementation using the `turtle` module.
- `snake_cli.py`: Terminal implementation using the `curses` module.
- `README.md`: Basic user-facing instructions.
- `venv/`: Local virtual environment (ignored by Git/Gemini if configured).
