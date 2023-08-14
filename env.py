import pygame

# 화면 플래그 설정
screen_flag = 1 # 1: 시작 화면, 2: 메인 게임화면(판매/배달) 3: 농장, 4: 상점, 5: 도박장, 6: 메뉴(다른 화면 이동)

# 화면 크기 설정
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# 색상 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 커서 위치
START_Y = SCREEN_HEIGHT // 2 + 180

# 앞으로 모든 위치는 [x, y] 형태로 표현

# 메인 화면
# 게임 시작 버튼
MAIN_BUTTON_START = [560, 520]
MAIN_BUTTON_END = [720, 550]

# 폰트
pygame.font.init()
TITLE_FONT = pygame.font.Font("./font/Cafe24Ohsquare-v2.0/Cafe24Ohsquare-v2.0.otf", 50)
BODY_FONT = pygame.font.Font("./font/S-Core_Dream_OTF/SCDream2.otf", 30)