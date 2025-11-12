# Asteroids

A classic Asteroids arcade game built with Python and Pygame.

## Features

- Classic arcade-style gameplay
- Smooth vector graphics
- Asteroid collision detection
- Score tracking
- Progressive difficulty

## Prerequisites

- Python 3.8 or higher
- [uv](https://docs.astral.sh/uv/) (recommended) or pip for package management

## Installation

### Recommended: Using uv

We recommend using [uv](https://docs.astral.sh/uv/) for the best development experience. uv is an extremely fast Python package installer and resolver, written in Rust.

#### Install uv

**macOS and Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**With pip:**
```bash
pip install uv
```

#### Setup the project with uv

1. Clone the repository:
   ```bash
   git clone https://github.com/mammykins/asteroids.git
   cd asteroids
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -r requirements.txt
   ```

   Or in a single command:
   ```bash
   uv pip install -r requirements.txt
   ```

### Alternative: Using pip

If you prefer to use pip:

1. Clone the repository:
   ```bash
   git clone https://github.com/mammykins/asteroids.git
   cd asteroids
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Game

Once you have installed the dependencies, run the game with:

```bash
python main.py
```

### Game Controls

- **Arrow Keys** or **WASD**: Rotate and thrust the ship
- **Spacebar**: Fire
- **ESC**: Quit game

## Development

### Using uv for Development

uv makes development faster and more efficient:

```bash
# Install development dependencies
uv pip install -r requirements-dev.txt

# Run tests
uv run pytest

# Run linter
uv run ruff check .

# Format code
uv run ruff format .
```

### Project Structure

```
asteroids/
├── main.py              # Game entry point
├── requirements.txt     # Production dependencies
├── requirements-dev.txt # Development dependencies
├── README.md           # This file
└── src/                # Game source code
    ├── game.py         # Main game loop
    ├── player.py       # Player ship class
    ├── asteroid.py     # Asteroid class
    └── utils.py        # Utility functions
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Classic Atari Asteroids game for inspiration
- Pygame community for excellent documentation and support
