import pygame
from game import Game



            #initatilisation de pygame
pygame.init()
#laisser ouverte la fenetre et dimensionné dant tuple 400x600
screen = pygame.display.set_mode((1080,720))
title =pygame.display.set_caption('Sab game')

Background = pygame.image.load('PygameAssets-main/bg.jpg')
#charger class game
game =Game()


                ##condition d'ouverture##
#initialisation de la variable game_on
game_on=True
#condition 
#tant que game_on est True 
#création event quitter au clique sur la croix

while game_on:
    screen.blit(Background,(0,-200))
    screen.blit(game.player.image,game.player.rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on=False
            pygame.quit()
#si touche est lachée
        elif event.type ==pygame.KEYDOWN:
#récuperer touche utiliser
            if event.key == pygame.K_RIGHT:
                game.player.move_right()
            elif event.key == pygame.K_LEFT:
                game.player.move_left()
#mise a jour de la fenetre
    pygame.display.update()
