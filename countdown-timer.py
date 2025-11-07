import pygame

pygame.init()
font = pygame.font.Font(None, 40)
font_big = pygame.font.Font(None, 50)

screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Đồng hồ đếm ngược")

GREY = (200, 200, 200)
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
LIGHT_BLUE = (100, 160, 210)

center = (250, 370)
radius = 120

minutes = 0
seconds = 0

running = True

plus_min_rect = pygame.Rect(80, 60, 60, 60)
minus_min_rect = pygame.Rect(180, 60, 60, 60)
start_rect = pygame.Rect(300, 60, 120, 60)
plus_sec_rect = pygame.Rect(80, 160, 60, 60)
minus_sec_rect = pygame.Rect(180, 160, 60, 60)
reset_rect = pygame.Rect(300, 160, 120, 60)

while running:
    screen.fill(GREY)
    # --- Nút điều khiển ---
    pygame.draw.rect(screen, WHITE, plus_min_rect, border_radius=12)
    pygame.draw.rect(screen, WHITE, minus_min_rect, border_radius=12)
    pygame.draw.rect(screen, LIGHT_BLUE, start_rect, border_radius=12)
    pygame.draw.rect(screen, WHITE, plus_sec_rect, border_radius=12)
    pygame.draw.rect(screen, WHITE, minus_sec_rect, border_radius=12)
    pygame.draw.rect(screen, LIGHT_BLUE, reset_rect, border_radius=12)

    screen.blit(font.render('+', True, BLACK), (100, 70))
    screen.blit(font.render('-', True, BLACK), (200, 70))
    screen.blit(font.render('Start', True, BLACK), (320, 75))
    screen.blit(font.render('+', True, BLACK), (100, 170))
    screen.blit(font.render('-', True, BLACK), (200, 170))
    screen.blit(font.render('Reset', True, BLACK), (315, 175))

    pygame.draw.circle(screen, WHITE, center, radius)
    pygame.draw.circle(screen, BLACK, center, radius, 3)
    pygame.draw.line(screen, BLACK, center, (250, 270), 4)

    time_text = font_big.render(f"{minutes:02d}:{seconds:02d}", True, BLACK)
    screen.blit(time_text, (center[0] - 40, center[1] - 20))

    pygame.draw.rect(screen, BLACK, (50, 520, 400, 50), border_radius=10)
    pygame.draw.rect(screen, WHITE, (60, 530, 380, 30), border_radius=10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if plus_min_rect.collidepoint(event.pos):
                minutes = (minutes + 1) % 60
            elif minus_min_rect.collidepoint(event.pos):
                if minutes >0 :
                    minutes = (minutes - 1) % 60
            elif plus_sec_rect.collidepoint(event.pos):
                seconds = (seconds + 1) % 60
            elif minus_sec_rect.collidepoint(event.pos):
                if seconds == 0:
                    seconds = 59
                else:
                    seconds = (seconds - 1) % 60

    pygame.display.flip()

pygame.quit()
