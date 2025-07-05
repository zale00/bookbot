# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
BookBot is a Python text analysis tool that analyzes text files to provide word counts and character frequency statistics. It's structured as a beginner project for Boot.dev.

## Commands

### Running the Application
```bash
python3 main.py
```

## Code Architecture

### Module Structure
- `main.py`: Entry point and file I/O operations
- `stats.py`: Statistical analysis functions (word counting, character frequency)

### Data Flow
1. Text file is read via `get_book_text()`
2. Word count calculated with `get_num_words()`
3. Character frequencies calculated with `get_char_count()` (case-insensitive)
4. Results sorted by frequency using `sort_char_count()`
5. Formatted report printed (alphabetical characters only)

### Key Functions
- `get_num_words(text)`: Splits text on whitespace to count words
- `get_char_count(text)`: Returns dictionary of character frequencies (lowercase)
- `sort_char_count(char_count_dict)`: Converts to sorted list of dictionaries by count

## Important Notes
- Uses only Python standard library (no external dependencies)
- Text files are stored in `books/` directory (gitignored)
- Character analysis filters to alphabetical characters only in output
- All character counting is case-insensitive

## Development Workflow
- Always commit and push changes after each task is complete