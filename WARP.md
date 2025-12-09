# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

Asteroids is a classic arcade game built with Python 3.13+ and Pygame 2.6.1. The game features a player-controlled spaceship navigating through an asteroid field with collision detection, shooting mechanics, and a scoring system.

## Development Commands

### Setup
```bash
# Install dependencies (recommended)
uv sync

# Alternative using pip
pip install pygame==2.6.1
```

### Running the Game
```bash
# Run the game
uv run main.py

# Alternative without uv
python main.py
```

### Testing
```bash
# Run all tests
python -m pytest test_main.py

# Run specific test class
python -m pytest test_main.py::TestGameLoop

# Run with verbose output
python -m pytest test_main.py -v
```

## Code Architecture

### Inheritance Hierarchy

The codebase uses an object-oriented design centered around a `CircleShape` base class:

- **CircleShape** (circleshape.py): Base class for all circular game objects
  - Inherits from `pygame.sprite.Sprite`
  - Provides core functionality: position, velocity, radius, collision detection, and screen wrapping
  - Must be subclassed; `draw()` and `update()` methods are meant to be overridden
  
- **Player** (player.py): Extends CircleShape
  - Triangle-shaped spaceship with rotation mechanics
  - Handles keyboard input (WASD + SPACE)
  - Manages shooting cooldown
  
- **Asteroid** (asteroid.py): Extends CircleShape
  - Implements `split()` method for breaking into smaller asteroids
  - Recursively creates two smaller asteroids when hit (until reaching minimum radius)
  
- **Shot** (shot.py): Extends CircleShape
  - Projectiles fired by the player
  - Has player immunity timer to prevent instant self-collision

### Sprite Group Architecture

The game uses pygame sprite groups for efficient collision detection and updates:

- **updatable**: Contains all objects that need `update(dt)` called each frame
- **drawable**: Contains all objects that need `draw(screen)` called each frame
- **asteroids**: Subset for collision detection with player and shots
- **shots**: Subset for collision detection with asteroids and player

Objects are automatically added to groups via the class-level `containers` attribute pattern:
```python
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
```

### Screen Wrapping

All CircleShape objects support screen wrapping via `wrap_position()`. When an object moves off one edge, it reappears on the opposite edge, creating a "flat world" toroidal topology.

### Game Loop Structure (main.py)

1. Initialize pygame and create sprite groups
2. Create player, asteroid field, and score objects
3. Game loop:
   - Process quit events
   - Log state (for debugging)
   - Update score and all updatable objects
   - Check collisions (player vs asteroids, shots vs asteroids, shots vs player)
   - Draw everything to screen
   - Maintain 60 FPS with delta time (`dt`)

### Collision Detection

Collision detection is **manual and circle-based**, not using pygame's built-in sprite collision:
- Implemented in `CircleShape.collides_with()` using distance formula
- Two objects collide when `distance < (radius1 + radius2)`
- Checked explicitly in the game loop for each collision pair

### Logging System (logger.py)

Provides two logging mechanisms for debugging and analysis:
- **log_state()**: Captures snapshots of all game objects once per second for the first 16 seconds → `game_state.jsonl`
- **log_event()**: Records discrete events (asteroid hits, splits, player hits) → `game_events.jsonl`

Both use JSONL format (newline-delimited JSON) with timestamps and frame numbers.

### Configuration (constants.py)

All game parameters are centralized in constants.py:
- Screen dimensions
- Player speed, turn speed, shoot cooldown
- Asteroid spawn rate, sizes
- Scoring parameters

When adjusting game balance or behavior, modify constants rather than hardcoding values.

## File Organization

- **main.py**: Entry point, game loop, collision detection
- **circleshape.py**: Base class for all game objects
- **player.py**, **asteroid.py**, **shot.py**: Game object classes
- **asteroidfield.py**: Spawns asteroids at regular intervals
- **score.py**: Tracks score, survival time, level, and renders HUD
- **logger.py**: Game state and event logging for debugging
- **constants.py**: All game configuration parameters
- **test_main.py**: Unit tests for game loop mechanics
- **pyproject.toml**: Project metadata and dependencies (uv-managed)
