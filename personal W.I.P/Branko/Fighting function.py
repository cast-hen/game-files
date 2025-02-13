import pygame
import time

allMovesList = ["punch", "heal", "combo punch", "enrage", "poison", "life steal", "block"]
playerMoves = ["punch", "heal", "combo punch"]

running = True
health = 100
enemy1 = [(0, 0, 255), 100, ["punch", "block"]]
enemy2 = [(255, 0, 255), 500, ["combo punch", "heal", "block"]]


def fight(enemy):
    def draw_scene():
        background = pygame.image.load("fightBackground.jpg")
        background = pygame.transform.scale(background, (1300, 600))
        screen.blit(background, (0, 0))
        healthFont = pygame.font.Font("freesansbold.ttf", 40)
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(200, 250, 100, 200))
        pygame.draw.rect(screen, enemy[0], pygame.Rect(1000, 250, 100, 200))
        healthTextPlayer = healthFont.render(str(playerHealth) + "/" + str(health), True, (255, 255, 255))
        healthTextPlayerRect = healthTextPlayer.get_rect()
        healthTextPlayerRect.center = (250, 200)
        screen.blit(healthTextPlayer, healthTextPlayerRect)
        healthTextEnemy = healthFont.render(str(enemyHealth) + "/" + str(enemy[1]), True, (255, 255, 255))
        healthTextEnemyRect = healthTextEnemy.get_rect()
        healthTextEnemyRect.center = (1050, 200)
        screen.blit(healthTextEnemy, healthTextEnemyRect)
        pygame.display.update()

    playerHealth = health
    enemyHealth = enemy[1]
    fighting = True
    state = "turnPlayer"
    while fighting:
        draw_scene()
        if state == "turnPlayer":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fighting = False
                    return "quit"
        elif state == "turnEnemy":
            pass
        time.sleep(0.1)

    pygame.display.update()


screen = pygame.display.set_mode((1300, 600))
pygame.init()
while running:
    result = "none"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                result = fight(enemy1)
            if event.key == pygame.K_r:
                result = fight(enemy2)
    if result == "quit":
        running = False
    elif result == "win":
        print("yay")
    elif result == "loss":
        print("aw")

    time.sleep(0.1)
pygame.quit()