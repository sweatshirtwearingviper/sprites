import pygame

# ALWAYS remember pygame.init() at the start
# pygame.display.update() at the end of the while loop

pygame.init()
display = pygame.display.set_mode((600,400))
background = pygame.Surface((600,400))
background.fill((0,0,0))
clock = pygame.time.Clock()

group = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = pygame.image.load('test.png').convert()
sprite.rect = sprite.image.get_rect()
sprite.rect.x = 100
sprite.rect.y = 100
group.add(sprite)

velx = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        velx += 1
            
        
    for sprite in group.sprites():
        sprite.rect.x += velx

 
            
    display.blit(background, (0,0))
    group.draw(display)
    pygame.display.update()
    clock.tick(60)
    