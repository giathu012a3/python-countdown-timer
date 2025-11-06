import pygame

# Khởi tạo pygame
pygame.init()
font = pygame.font.Font(None, 40)
font_big = pygame.font.Font(None, 50)

# Tạo cửa sổ
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Đồng hồ đếm ngược")

# Màu sắc
GREY = (200, 200, 200)
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
BLUE = (70, 130, 180)
LIGHT_BLUE = (100, 160, 210)

# Vị trí trung tâm đồng hồ (hạ xuống)
center = (250, 370)  # trước là 250,300 -> giờ hạ xuống 370
radius = 120

running = True

# ===== Vẽ giao diện =====
while running:
    screen.fill(GREY)

    # --- Nút điều khiển ---
    pygame.draw.rect(screen, WHITE, (80, 60, 60, 60), border_radius=12)
    pygame.draw.rect(screen, WHITE, (180, 60, 60, 60), border_radius=12)
    pygame.draw.rect(screen, LIGHT_BLUE, (300, 60, 120, 60), border_radius=12)
    pygame.draw.rect(screen, WHITE, (80, 160, 60, 60), border_radius=12)
    pygame.draw.rect(screen, WHITE, (180, 160, 60, 60), border_radius=12)
    pygame.draw.rect(screen, LIGHT_BLUE, (300, 160, 120, 60), border_radius=12)

    screen.blit(font.render('+', True, BLACK), (100, 70))
    screen.blit(font.render('-', True, BLACK), (200, 70))
    screen.blit(font.render('Start', True, BLACK), (320, 75))

    screen.blit(font.render('+', True, BLACK), (100, 170))
    screen.blit(font.render('-', True, BLACK), (200, 170))
    screen.blit(font.render('Reset', True, BLACK), (315, 175))

    pygame.draw.circle(screen, WHITE, center, radius)
    pygame.draw.circle(screen, BLACK, center, radius, 3)

    pygame.draw.line(screen, BLACK, center, (250, 270), 4)

    time_text = font_big.render("00:00", True, BLACK)
    screen.blit(time_text, (center[0] - 40, center[1] - 20))

    pygame.draw.rect(screen, BLACK, (50, 520, 400, 50), border_radius=10)
    pygame.draw.rect(screen, WHITE, (60, 530, 380, 30), border_radius=10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
