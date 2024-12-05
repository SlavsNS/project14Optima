
# Full Character Game Project

This project combines character catalog and a text-based game.

## Features
1. Fetch character data from API.
2. Save and load character data locally.
3. Play a turn-based game with characters.

## How to Run
1. Install required libraries:
   ```bash
   pip install requests
   ```
2. Run the program:
   ```bash
   python main.py
   ```

## Game Mechanics
- Each character has attributes: health, damage, armor, and resist.
- Players can attack or defend during their turn.
- Damage calculation:
  ```plaintext
  CleanDamage = Damage - Armor
  FinalDamage = CleanDamage * (1 - Resist)
  ```
- The game ends when one character's health reaches zero.

## Files
- `main.py`: Entry point for the application.
- `parser.py`: Handles character data fetching and saving.
- `game.py`: Implements the text-based game.
- `characters.json`: Stores character data.
