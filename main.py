# 임포트
import pygame
import sys
from env import * # 설정값 저장 파일: env.py
import func as utils  # 게임 기능 함수 파일: func.py
import screen.game_start as gs # 게임 실행 파일: screen\game_start.py
import screen.game_farm as gf # 게임 실행 파일: screen\game_farm.py
import screen.game_market as gmarket # 게임 실행 파일: screen\game_market.py
import screen.game_casino as gc # 게임 실행 파일: screen\game_casino.py
import screen.game_menu as gmenu # 게임 실행 파일: screen\game_menu.py

###### 초기화 ######
utils.init() # Pygame 초기화
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 화면 크기 설정

###### 게임 화면 ######
while True:
    # 마우스 위치 설정
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if screen_flag == 1: # 메인 화면 일 때
        screen.fill(WHITE)  # 흰색 배경화면
        
        # 출력
        utils.show_text("2023 Pygame Competition", TITLE_FONT, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2) # 타이틀 출력
        utils.show_text("[ 게임 시작 ]", BODY_FONT, BLACK, screen, SCREEN_WIDTH // 2 , START_Y) # 게임 시작 출력

        pygame.display.update() # 화면 업데이트
    
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN: # 마우스 눌렀을 때
                if event.button == 1: # 마우스 왼쪽 버튼 눌렀을 때
                    if mouse_x >= MAIN_BUTTON_START[0] and mouse_x <= MAIN_BUTTON_END[0] and mouse_y >= MAIN_BUTTON_START[1] and mouse_y <= MAIN_BUTTON_END[1]: # 마우스가 게임 시작 위치에 있을 때
                        screen_flag = 2 # 게임 시작 화면으로 이동

    elif screen_flag == 2: # 메인 게임화면(판매/배달)
        gs.start(screen) # 게임 시작 함수 호출
    elif screen_flag == 3: # 농장 화면
        gf.farm(screen) # 농장 화면 함수 호출
    elif screen_flag == 4: # 상점 화면
        gmarket.market(screen) # 상점 화면 함수 호출
    elif screen_flag == 5: # 도박장 화면
        gc.casino(screen) # 도박장 화면 함수 호출
    elif screen_flag == 6: # 메뉴 화면
        gmenu.menu(screen) # 메뉴 화면 함수 호출