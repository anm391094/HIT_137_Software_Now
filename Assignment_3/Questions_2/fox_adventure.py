"""
S125 HIT137 SOFTWARE NOW
Group Assignment 3 - Question 2
Group - CAS/DAN 10

"""

import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
WIDTH, HEIGHT = 1079, 400
# WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fox's Adventure")

# Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Load images for player, enemies, projectiles, collectibles, hearts, and background
def load_image(image_path, size=None):
    image = pygame.image.load(image_path)
    if size:
        image = pygame.transform.scale(image, size)
    return image

# Load images
fox_img = load_image('icons/fox.png', (100, 100))
hunter_img = load_image('icons/hunter.png', (100, 100))
berry_img = load_image('icons/berry.png', (40, 40))
feather_img = load_image('icons/feather.png', (50, 50))
projectile_img = load_image('icons/projectile.png', (10, 5))

# Heart image (For lives)
heart_img = load_image('icons/heart.png', (30, 30))

# Background image
background_img = load_image('icons/background.jpg', (WIDTH, HEIGHT))

# Font for text
font = pygame.font.SysFont("arial", 24)

# Clock
clock = pygame.time.Clock()

# --- CLASSES ---

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = fox_img
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = HEIGHT - 150
        self.vel_y = 0
        self.speed = 5
        self.jump_power = 15
        self.health = 100
        self.lives = 3
        self.score = 0
        self.on_ground = False

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = -self.jump_power

    def shoot(self):
        projectile = Projectile(self.rect.right, self.rect.centery)
        projectiles.add(projectile)

    def apply_gravity(self):
        self.vel_y += 0.8
        self.rect.y += self.vel_y
        if self.rect.bottom >= HEIGHT - 50:
            self.rect.bottom = HEIGHT - 50
            self.vel_y = 0
            self.on_ground = True
        else:
            self.on_ground = False

    def update(self):
        self.handle_keys()
        self.apply_gravity()

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            if self.lives > 0:
                self.lives -= 1
                self.health = 100
            else:
                game_over()

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = projectile_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10
        self.damage = 25

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > WIDTH:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, health=50):
        super().__init__()
        self.image = hunter_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = random.randint(1, 3)
        self.health = health

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            player.score += 100
            self.kill()


class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y, kind="berry"):
        super().__init__()
        if kind == "berry":
            self.image = berry_img
            self.effect = "health"
        else:
            self.image = feather_img
            self.effect = "life"
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def apply_effect(self, player):
        if self.effect == "health":
            player.health = min(player.health + 30, 100)
        elif self.effect == "life":
            player.lives += 1


# --- FUNCTIONS ---

def draw_health_bar(x, y, health, max_health=100):
    ratio = health / max_health
    pygame.draw.rect(screen, RED, (x, y, 100, 10))
    pygame.draw.rect(screen, GREEN, (x, y, 100 * ratio, 10))

def draw_lives(x, y, lives):
    for i in range(lives):
        screen.blit(heart_img, (x + i * 35, y))

def spawn_enemy(level):
    x = random.randint(WIDTH + 50, WIDTH + 300)
    y = HEIGHT - 100
    if level == 3:
        enemy = Enemy(x, y, health=100)
    else:
        enemy = Enemy(x, y)
    enemies.add(enemy)

def spawn_collectible():
    x = random.randint(WIDTH + 50, WIDTH + 300)
    y = random.randint(100, HEIGHT - 100)
    kind = random.choice(["berry", "feather"])
    item = Collectible(x, y, kind)
    collectibles.add(item)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    surface.blit(textobj, (x, y))

def game_over():
    screen.fill(BLACK)
    draw_text("Game Over", font, RED, screen, WIDTH // 2 - 80, HEIGHT // 2 - 50)
    draw_text("Press R to Restart", font, WHITE, screen, WIDTH // 2 - 100, HEIGHT // 2)
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    player.health = 100
                    player.lives = 3
                    main()

# --- GROUPS ---

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

projectiles = pygame.sprite.Group()
enemies = pygame.sprite.Group()
collectibles = pygame.sprite.Group()

# --- MAIN GAME LOOP ---

def main():
    global paused  # Referencing global paused variable

    level = 1
    enemy_timer = 0
    collectible_timer = 0

    running = True
    while running:
        clock.tick(FPS)
        
        # Blit the background image to the screen
        screen.blit(background_img, (0, 0))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    player.shoot()
                if event.key == pygame.K_ESCAPE:  # Toggle pause state
                    paused = not paused

        if paused:
            # Display the pause screen
            screen.fill(BLACK)
            draw_text("PAUSED", font, WHITE, screen, WIDTH // 2 - 60, HEIGHT // 2 - 50)
            draw_text("Press ESC to Resume", font, WHITE, screen, WIDTH // 2 - 100, HEIGHT // 2)
            pygame.display.update()
            continue  # Skip the game updates and wait for ESC to resume

        # Update the game only when not paused
        player_group.update()
        projectiles.update()
        enemies.update()
        collectibles.update()

        # Spawning enemies
        enemy_timer += 1
        if enemy_timer > 90:
            spawn_enemy(level)
            enemy_timer = 0

        # Spawning collectibles
        collectible_timer += 1
        if collectible_timer > 300:
            spawn_collectible()
            collectible_timer = 0

        # Collision detection
        for proj in projectiles:
            hits = pygame.sprite.spritecollide(proj, enemies, False)
            for enemy in hits:
                enemy.take_damage(proj.damage)
                proj.kill()

        player_hits = pygame.sprite.spritecollide(player, enemies, True)
        for enemy in player_hits:
            player.take_damage(20)

        collected = pygame.sprite.spritecollide(player, collectibles, True)
        for item in collected:
            item.apply_effect(player)
            player.score += 50

        # Level progression
        if player.score > 1000 and level == 1:
            level = 2
        if player.score > 2500 and level == 2:
            level = 3

        # Draw everything
        player_group.draw(screen)
        projectiles.draw(screen)
        enemies.draw(screen)
        collectibles.draw(screen)

        draw_health_bar(10, 10, player.health)
        draw_lives(10, 40, player.lives)
        draw_text(f"Score: {player.score}", font, BLACK, screen, 10, 70)
        draw_text(f"Level: {level}", font, BLACK, screen, 10, 100)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    paused = False
    main()
