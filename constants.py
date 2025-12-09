SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE_SECONDS = 0.8  # in seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300  # degrees per second
PLAYER_SPEED = 200  # pixels per second
LINE_WIDTH = 2
SHOT_RADIUS = 5
PLAYER_SHOOT_SPEED = 500  # pixels per second
PLAYER_SHOOT_COOLDOWN_SECONDS = 0.3  # in seconds
SHOT_PLAYER_IMMUNITY_SECONDS = 0.2  # time before shot can hit the player who fired it

# Scoring
SCORE_SURVIVAL_PER_SECOND = 10  # points per second for staying alive
SCORE_ASTEROID_DESTROYED = 100  # points for destroying an asteroid
SCORE_SURVIVAL_BONUS = 500  # bonus points every 10 seconds
SCORE_SURVIVAL_BONUS_INTERVAL = 10  # seconds between survival bonuses

# Cthulhu Boss
CTHULHU_SPAWN_TIME = 30.0  # seconds before Cthulhu appears
CTHULHU_RADIUS = 80  # collision radius
CTHULHU_SPEED = 100  # pixels per second
CTHULHU_TENTACLE_COOLDOWN = 5.0  # seconds between tentacle whip attacks
CTHULHU_TENTACLE_WIDTH = 20  # visual thickness of tentacle whip
CTHULHU_TENTACLE_DURATION = 1.0  # how long tentacle whip stays active
CTHULHU_COLOR = (0, 255, 100)  # greenish eldritch color
TENTACLE_COLOR = (255, 0, 100)  # reddish danger color
CTHULHU_WARNING_TIME = 25.0  # seconds before warning appears
