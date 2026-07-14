# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project status

This repository is currently empty aside from a Python 3.14 virtualenv (`.venv`). No source files, test framework, or package manifest exist yet — this is a TDD kata starting from scratch.

## Environment

- Python 3.14.3, virtualenv at `.venv` (created with `virtualenv`, only `pip` installed so far).
- Activate on Windows: `.venv\Scripts\activate` (PowerShell: `.venv\Scripts\Activate.ps1`).
- No test framework is installed yet. If using `pytest`, install it first: `.venv\Scripts\pip install pytest`, then run with `.venv\Scripts\pytest`. Plain `unittest` (stdlib) works with no install: `.venv\Scripts\python -m unittest discover`.

## The task: Bowling Game Kata

Implement a `Game` class that scores one game of American ten-pin bowling, built test-first (TDD). Per the kata, do not implement:
- validation that rolls/pins are legal,
- validation of roll/frame counts,
- mid-frame score queries.

### Required API

- `roll(pins: int) -> None` — called once per ball thrown; `pins` is the number of pins knocked down.
- `score() -> int` — returns the total score for the completed game.

### Scoring rules

- A game has 10 frames; each (frames 1-9) allows up to two rolls to knock down 10 pins.
- **Spare** (10 pins across two rolls): frame score = 10 + pins from the *next one roll*.
- **Strike** (10 pins on the first roll): frame ends after one roll; frame score = 10 + pins from the *next two rolls*.
- **10th frame**: if a spare or strike is rolled, one or two bonus rolls are awarded to complete the frame (max 3 rolls total in the 10th frame).

### TDD approach

Since this kata is explicitly a TDD exercise, prefer the standard kata cadence when implementing: write one failing test for the smallest next increment (e.g. gutter game, all ones, one spare, one strike, perfect game), make it pass with the simplest code, then refactor, repeating until the full rule set above is covered.
