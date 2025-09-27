import constants
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    #Create game groups here
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (updatable, drawable, asteroid_group)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shot_group)

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0, 0, 0))  # screen with black

        updatable.update(dt)  # update all sprites in the updatable group
        for sprite in drawable:
            sprite.draw(screen)  # draw each sprite in the drawable group

        # Check for collisions
        for asteroid in asteroid_group:
            if player.check_collision(asteroid):
                # Handle collision
                print("Game Over!")
                running = False

        for asteroid in asteroid_group:
            for shot in shot_group:
                if shot.check_collision(asteroid):
                    asteroid.split()
                    shot.kill()
                    break # Exit the inner loop to avoid checking other shots for this asteroid

        pygame.display.flip()  # update the full display Surface to the screen
        dt = clock.tick(60) / 1000  # Limit to 60 frames per second -> returns milliseconds since last frame
        


    pygame.quit()


if __name__ == "__main__":
    main()
