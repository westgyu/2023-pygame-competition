import pygame

# 화면 크기 설정
screen_width = 1280
screen_height = 720

# 색상 설정
white = (255, 255, 255)
black = (0, 0, 0)

# 커서 위치
start_cursor_x = screen_width // 2 - 70
start_cursor_y = screen_height - 112
desc_cursor_x = screen_width // 2 - 70
desc_cursor_y = screen_height - 62

# 폰트
pygame.font.init()
Title_font = pygame.font.Font("./font/Cafe24Ohsquare-v2.0/Cafe24Ohsquare-v2.0.otf", 50)
Body_font = pygame.font.Font("./font/S-Core_Dream_OTF/SCDream2.otf", 30)
main_desc_font = pygame.font.Font("./font/S-Core_Dream_OTF/SCDream2.otf", 20)