# Installation

This file explains common installation steps. Choose the instructions for the environment you plan to use.

## Option A — Python (recommended)
1. Install Python 3.8+ from https://python.org.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate    # Windows (PowerShell)
   ```
3. Install dependencies (example):
   ```bash
   pip install numpy
   ```
4. Run the app (example for CLI):
   ```bash
   python -m matrix_app.cli --help
   ```

## Option B — JavaScript / Node.js
1. Install Node.js 16+ from https://nodejs.org.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the app (example):
   ```bash
   node cli.js --help
   ```

## Option C — Including as a library
Add the library files to your project and follow the API descriptions in `API.md`.

## Notes
- Replace the example commands above with the actual script names your project uses.
- For CPU-heavy operations, consider using optimized numeric libraries (e.g., NumPy for Python).
