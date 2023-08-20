# 임포트
import pygame
import sys
import threading
from env import * # 설정값 저장 파일: env.py
import func as utils  # 게임 기능 함수 파일: func.py

###### 초기화 ######
utils.init() # Pygame 초기화
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 화면 크기 설정
utils.varfile("w", loc_screen_flag, 1) # 1: 시작 화면, 2: 메인 게임화면(판매/배달) 3: 농장, 4: 상점, 5: 도박장, 6: 메뉴(다른 화면 이동)
utils.varfile("w", loc_money, 100000) # 돈 (초기값: 100,000)
utils.varfile("w", loc_hogamdo, 0) # 호감도
mouse_pos = [0, 0] # 마우스 위치

###### 게임 화면 ######
while True:
    screen_flag = int(utils.varfile("r", loc_screen_flag, 0)) # screen_flag 변수 업데이트
    money = int(utils.varfile("r", loc_money, 0)) # 돈 업데이트
    hogamdo = int(utils.varfile("r", loc_hogamdo, 0)) # 호감도 업데이트
    # 마우스 위치 설정
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pos[0] = mouse_x
    mouse_pos[1] = mouse_y

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
                        utils.varfile("w", loc_screen_flag, 2) # 게임 시작 화면으로 이동
    utils.switch_screen(screen, screen_flag, money, hogamdo) # screen_flag 변수에 따라 화면 전환