# 임포트
import pygame
import sys
from env import * # 설정값 저장 파일: env.py
from func import * # 게임 기능 함수 파일: func.py
from screen.game_start import * # 게임 실행 파일: screen\game_start.py

###### 초기화 ######
init() # Pygame 초기화
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 화면 크기 설정

# 플래그 설정
screen_flag = 1 # 1: 메인 화면, 2: 게임 설명 화면, 3: 게임 시작 화면

###### 게임 화면 ######
while True:
    # 마우스 위치 설정
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if screen_flag == 1: # 메인 화면 일 때
        screen.fill(WHITE)  # 흰색 배경화면
        
        # 출력
        show_text("2023 Pygame Competition", TITLE_FONT, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2) # 타이틀 출력
        show_text("[ 게임 시작 ]", BODY_FONT, BLACK, screen, SCREEN_WIDTH // 2 , START_Y) # 게임 시작 출력

        pygame.display.update() # 화면 업데이트
    
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN: # 마우스 눌렀을 때
                if event.button == 1: # 마우스 왼쪽 버튼 눌렀을 때
                    if mouse_x >= 560 and mouse_x <= 720 and mouse_y >= 520 and mouse_y <= 550: # 마우스가 게임 시작 위치에 있을 때
                        screen_flag = 2 # 게임 시작 화면으로 이동
                    else:
                        screen_flag = 1 # 메인 화면으로 이동

    elif screen_flag == 2: # 게임 시작을 눌렀을 때
        game_start(screen) # 게임 시작 함수 호출