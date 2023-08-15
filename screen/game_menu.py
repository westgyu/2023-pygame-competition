# 임포트
import pygame
import sys
import threading
from env import * # 설정값 저장 파일: env.py
import func as utils # 함수 파일: func.py

thr_flag = 0 # 쓰레드 실행 여부
menu_check_stop_event = threading.Event() # 쓰레드 종료 이벤트
mouse_pos = [0, 0] # 마우스 위치 [x, y]

# 메인 게임화면(판매/배달) - screen_flag = 2
def menu(screen):
    global mouse_pos, thr_flag
    utils.show_image("img/game_desc/flower-g1457003f2_1920.jpg", screen) # 배경 출력
    # 마우스 위치 설정
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pos[0] = mouse_x
    mouse_pos[1] = mouse_y

    screen_flag = int(utils.varfile("r", loc_screen_flag, 0)) # screen_flag 변수 업데이트
    menu_distance = utils.varfile("r", loc_menu_distance, 0) # menu_distance(마우스가 원 위에 있는지 탐지) 변수 업데이트
    if menu_distance != '': # menu_distance에 값이 있다면
        menu_distance = float(menu_distance) # float로 형변환

    menu_check = threading.Thread(target=utils.default_ui, args=(screen, mouse_pos, menu_check_stop_event)) # UI 쓰레드
    if thr_flag == 0: # 한 번도 실행이 안 됐다면
        thr_flag = 1
        menu_check_stop_event.clear() # 이벤트 초기화
        menu_check.start() # 실행
        
    utils.show_text("MENU", TITLE_FONT, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2) # 타이틀 출력
    pygame.display.update() # 화면 업데이트

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN: # 마우스 눌렀을 때
                if event.button == 1: # 마우스 왼쪽 버튼 눌렀을 때
                    if isinstance(menu_distance, float) and menu_distance <= MENU_BUTTON[2]: # 마우스가 원 위에 있을 때
                        utils.varfile("w", loc_screen_flag, 2) # 메인 게임화면(판매/배달) 으로 이동
                        menu_check_stop_event.set()
                        thr_flag = 0
    
    return screen_flag # screen_flag 반환 -> main.py에서 변수 값 업데이트 -> 업데이트 된 값에 따라 화면 바뀜