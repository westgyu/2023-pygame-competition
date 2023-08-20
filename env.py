import pygame

# 화면 크기 설정
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# 색상 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 커서 위치
START_Y = SCREEN_HEIGHT // 2 + 180

##############################################

# 앞으로 모든 위치는 [x, y] 형태로 표현

# 메인 화면
# 게임 시작 버튼
MAIN_BUTTON_START = [560, 520]
MAIN_BUTTON_END = [720, 550]

# 메뉴 이동 버튼
MENU_BUTTON = [40, SCREEN_HEIGHT-40, 30] # [x, y, r]
EXIT_BUTTON = [1240, SCREEN_HEIGHT-680, 30]
LEFT_BUTTON = [40, (SCREEN_HEIGHT//2)+15, 30]
RIGHT_BUTTON = [1240, (SCREEN_HEIGHT//2)+15, 30]


##############################################

# 파일 위치
loc_screen_flag = "data/screen.flag"
loc_menu_distance = "data/menu.distance"
loc_arrow_l = "data/arrow_l.distance"
loc_arrow_r = "data/arrow_r.distance"
loc_money = 'data/money'
loc_hogamdo = "data/hogamdo"

# 폰트
pygame.font.init()
TITLE_FONT = pygame.font.Font("./font/Cafe24Ohsquare-v2.0/Cafe24Ohsquare-v2.0.otf", 50)
BODY_FONT = pygame.font.Font("./font/S-Core_Dream_OTF/SCDream2.otf", 30)

##############################################