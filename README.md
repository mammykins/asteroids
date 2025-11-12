# Asteroids

A classic Asteroids arcade game built with Python and Pygame.

## Description

This is a modern implementation of the classic Asteroids arcade game where you pilot a spaceship through an asteroid field. Shoot asteroids to break them into smaller pieces and survive as long as possible!

### Features

- Classic arcade gameplay with smooth 60 FPS performance
- Player spaceship with rotation and movement controls
- Asteroid spawning system with randomized trajectories
- Collision detection between player, asteroids, and shots
- Asteroid splitting mechanics (large asteroids break into smaller ones)
- Built-in game state and event logging system for analysis

## Requirements

- Python 3.13 or higher
- Pygame 2.6.1

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd Asteroids
```

2. Install dependencies using uv (recommended) or pip:

```bash
# Using uv
uv sync

# Or using pip
pip install pygame==2.6.1
```

## How to Play

Run the game:

```bash
uv run main.py
```

### Controls

- **W** - Move forward
- **S** - Move backward
- **A** - Rotate left
- **D** - Rotate right
- **SPACE** - Shoot

Avoid colliding with asteroids while shooting them to break them apart. Large asteroids split into smaller ones when hit. The game ends when your ship collides with an asteroid.

## Game Configuration

You can adjust game parameters in `constants.py`:

- **Screen resolution**: 1280x720 pixels
- **Asteroid spawn rate**: 0.8 seconds
- **Player speed**: 200 pixels/second
- **Player turn speed**: 300 degrees/second
- **Shot cooldown**: 0.3 seconds

## Project Structure

```
.
├── main.py              # Main game loop and initialization
├── player.py            # Player ship class with controls
├── asteroid.py          # Asteroid class with splitting logic
├── asteroidfield.py     # Asteroid spawning system
├── shot.py              # Projectile class
├── circleshape.py       # Base class for circular game objects
├── constants.py         # Game configuration constants
├── logger.py            # Game state and event logging
├── test_main.py         # Tests
└── pyproject.toml       # Project dependencies
```

## Logging

The game includes a logging system that captures:

- **Game state** (`game_state.jsonl`): Snapshots of all game objects every second for the first 16 seconds
- **Game events** (`game_events.jsonl`): Records events like asteroid hits and splits

These logs are useful for debugging and analyzing gameplay.

## Development

- Inheritance hierarchy using `CircleShape` base class
- Sprite groups for efficient object management
- Separation of concerns across multiple modules
- Circle-based collision detection

## Testing

Run tests with:

```bash
python -m pytest test_main.py
```

## License

This project is open source and available for educational purposes.
