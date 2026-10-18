import pygame

pygame.init()

SCREEN_WIDTH = 500

SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Project Jungle')
background_image = pygame.image.load('Indian Village Cartoon Background  Village Backgrounds  Copyright-Free Cartoon Backgrounds.jpg').convert()
tiger = pygame.image.load('Tiger-removebg-preview.png')
header_text = pygame.font.Font('None', 42)
fact = pygame.font.Font('None', 24)

header_text = header_text.render(
    'Tigers are really powerful jungle animals', 
    True, 
    pygame.color('black')
)
fact = fact.render(
    'Fact: Tigers can easily see in the dark compared to humans!', 
    True, 
    pygame.color('black')
)

header_rect = header_text.get_rect()
header_rect.center = (SCREEN_WIDTH // 2, 40)

fact_rect = fact.get_rect()
fact_rect.center = (SCREEN_WIDTH // 2, 420)
def main_game():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        tiger = pygame.transform.scale(tiger, (100, 100))

        screen.blit(background_image, (0, 0))
        screen.blit(tiger, (200, 200))

        screen.blit(header_text, header_rect)
        screen.blit(fact, fact_rect)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main_game()
        

    
    