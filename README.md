# Tic Tac Toe

A graphical Tic-Tac-Toe game built with Pygame, featuring an AI opponent using the Minimax algorithm with alpha-beta pruning.

## Features

- Play as X or O against an AI opponent.
- Interactive graphical interface using Pygame.
- AI uses Minimax algorithm with alpha-beta pruning for optimal play.
- AI never loses — it either wins or forces a draw.
- Responsive gameplay with clear visual feedback.
- Restart the game anytime after it ends.

## AI Features

- **Minimax Algorithm:** Explores all possible future moves to select the one that maximizes the AI's chance of winning while minimizing the opponent’s chances.
- **Alpha-Beta Pruning:** Enhances Minimax by eliminating branches in the game tree that won’t affect the final decision, improving efficiency.
- **Optimal Play:** The AI never loses—it will either win or force a draw.
- **Turn-aware:** The AI adapts its moves based on whether it plays as X or O, always choosing the best possible action for its turn.

## Requirements

- Python 3.x
- Pygame

## Installation

```bash
pip install -r requirements.txt
```

## Usage
Run the game with:

```bash
python runner.py
```

## Authors
CS50 & Sandrin Muramutsa

