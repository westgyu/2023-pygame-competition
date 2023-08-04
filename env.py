import pygame

# 화면 크기 설정
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# 색상 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 커서 위치
START_Y = SCREEN_HEIGHT // 2 + 180

# 폰트
pygame.font.init()
TITLE_FONT = pygame.font.Font("./font/Cafe24Ohsquare-v2.0/Cafe24Ohsquare-v2.0.otf", 50)
BODY_FONT = pygame.font.Font("./font/S-Core_Dream_OTF/SCDream2.otf", 30)