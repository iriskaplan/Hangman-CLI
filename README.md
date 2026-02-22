# Hangman CLI 🎯

A simple command-line implementation of the classic Hangman game written in Python.

## Features

- ASCII hangman visualization
- Input validation
- Word selection from file
- Win/Lose detection
- Clean modular structure

## How to Run

```bash
python main.py
```

You will be prompted to:
1. Enter a file path containing words
2. Enter an index to select a word

Example:

```bash
Enter file path: words.txt
Enter index: 3
```

## Example Words File

The repository includes `words.txt` with sample words.
The file should contain words separated by whitespace.

## Project Structure

```
main.py        # Game logic
words.txt      # Sample word list
```

## Future Improvements

- Random word selection
- Replay option
- Difficulty levels
- Unit tests
- Convert guesses to a set for O(1) lookup