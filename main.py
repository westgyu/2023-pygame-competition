# 임포트
import pygame
import sys
from settings import * # 설정값 저장 파일: settings.py

###### 초기화 ######
pygame.init() # Pygame 초기화
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 크기 설정

# 화면 타이틀
pygame.display.set_caption("2023 pygame competition") # 제목 설정

# 폰트 설정
Title_font = pygame.font.Font("./font/Cafe24Ohsquare-v2.0/Cafe24Ohsquare-v2.0.otf", 50)
Body_font = pygame.font.Font("./font/S-Core_Dream_OTF/SCDream2.otf", 20)

###### 게임 화면 ######
cursor_x = start_cursor_x
cursor_y = start_cursor_y

while True:
    screen.fill(white)  # 흰색 배경화면
    
    # 타이틀 출력
    text = Title_font.render("2023 Pygmae Competition", True, black)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)
    
    # 게임 시작 출력
    game_start_text = Body_font.render("게임 시작", True, black)
    game_start_rect = game_start_text.get_rect(center=(screen_width // 2, screen_height - 100))
    screen.blit(game_start_text, game_start_rect)
    
    # 게임 설명 출력
    game_desc_text = Body_font.render("게임 설명", True, black)
    game_desc_rect = game_desc_text.get_rect(center=(screen_width // 2, screen_height - 50))
    screen.blit(game_desc_text, game_desc_rect)
    
    # 커서 그리기
    cursor_rect = pygame.Rect(cursor_x, cursor_y, 20, 20) # 초기위치: 게임 시작
    pygame.draw.rect(screen, black, cursor_rect)
    
    pygame.display.update()
    
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:  # 아래 방향키
                if cursor_y == start_cursor_y:  # 커서가 게임 시작에 있을 때
                    cursor_y = desc_cursor_y  # 커서를 게임 설명으로 이동
            elif event.key == pygame.K_UP:  # 위 방향키
                if cursor_y == desc_cursor_y:  # 커서가 게임 설명에 있을 때
                    cursor_y = start_cursor_y  # 커서를 게임 시작으로 이동
            elif event.key == pygame.K_RETURN:  # Enter 키
                if cursor_y == start_cursor_y:  # 커서가 게임 시작에 있을 때
                    print("게임 시작")  # 여기에 게임 시작 로직을 작성하면 됩니다.
                elif cursor_y == desc_cursor_y:  # 커서가 게임 설명에 있을 때
                    print("게임 설명")  # 여기에 게임 설명 로직을 작성하면 됩니다.