# Asteroids

A classic Asteroids arcade game built with Python and Pygame.

## Quick Start

Get up and running in 30 seconds with uv:

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone, setup, and run
git clone https://github.com/mammykins/asteroids.git
cd asteroids
uv sync
uv run main.py
```

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
- [uv](https://docs.astral.sh/uv/) (recommended) - Fast Python package manager
- Pygame 2.6.1

> **Why uv?** uv is 10-100x faster than pip, automatically manages Python versions and virtual environments, and provides reproducible installs with lock files.

## Installation

### Recommended: Using uv

We **strongly recommend** using [uv](https://docs.astral.sh/uv/) for the best development experience. uv is an extremely fast Python package and project manager written in Rust, offering speeds 10-100x faster than pip.

#### 1. Install uv

**macOS and Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**With pip (alternative):**
```bash
pip install uv
```

#### 2. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/mammykins/asteroids.git
cd asteroids

# Sync dependencies (creates virtual environment automatically)
uv sync
```

That's it! `uv sync` will:
- Create a virtual environment in `.venv` if it doesn't exist
- Install Python 3.13 if not available
- Install all dependencies from `pyproject.toml` and `uv.lock`

### Alternative: Using pip

If you prefer traditional pip:

```bash
# Clone the repository
git clone https://github.com/mammykins/asteroids.git
cd asteroids

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
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

### Using uv for Development

uv makes development workflows faster and more efficient:

```bash
# Run the game
uv run main.py

# Run tests
uv run pytest test_main.py

# Add new dependencies
uv add package-name

# Add development dependencies
uv add --dev pytest ruff

# Update dependencies
uv sync --upgrade

# Run any Python script with uv
uv run python -m pytest
```

### Code Architecture

- Inheritance hierarchy using `CircleShape` base class
- Sprite groups for efficient object management
- Separation of concerns across multiple modules
- Circle-based collision detection

## Testing

Run tests with uv (recommended):

```bash
uv run pytest test_main.py
```

Or with python directly:

```bash
python -m pytest test_main.py
```

## License

This project is open source and available for educational purposes.
