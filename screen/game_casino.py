# 임포트
import pygame
import sys
import threading
import random
from env import * # 설정값 저장 파일: env.py
import func as utils # 함수 파일: func.py

thr_flag = 0 # 쓰레드 실행 여부
mouse_pos = [0, 0] # 마우스 위치 [x, y]
menu_check_stop_event = threading.Event() # 쓰레드 종료 이벤트
res = ['5', '3', '2', '1', '0', '-1', '-2', '-3', '-5'] # 결과값 (배수)
time = 100000 # 시간

# 도박장 - screen_flag = 3
def casino(screen, money, hogamdo):
    global res, time, mouse_pos, thr_flag
    utils.show_image("img/game_desc/flower-g1457003f2_1920.jpg", screen) # 배경 출력
    # 마우스 위치 설정
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pos[0] = mouse_x
    mouse_pos[1] = mouse_y

    screen_flag = int(utils.varfile("r", loc_screen_flag, 0)) # screen_flag 변수 업데이트
    menu_distance = utils.varfile("r", loc_menu_distance, 0) # menu_distance(마우스가 원 위에 있는지 탐지) 변수 업데이트
    arrow_l_distance = utils.varfile("r", loc_arrow_l, 0) # arrow_l_distance 변수 업데이트
    arrow_r_distance = utils.varfile("r", loc_arrow_r, 0) # arrow_r_distance 변수 업데이트

    if menu_distance != '': # menu_distance에 값이 있다면
        menu_distance = float(menu_distance) # float로 형변환
    if arrow_l_distance != '': # menu_distance에 값이 있다면
        arrow_l_distance = float(arrow_l_distance) # float로 형변환
    if arrow_r_distance != '': # menu_distance에 값이 있다면
        arrow_r_distance = float(arrow_r_distance) # float로 형변환
    
    menu_check = threading.Thread(target=utils.default_ui, args=(screen, mouse_pos, menu_check_stop_event, 1)) # UI 쓰레드
    if thr_flag == 0: # 한 번도 실행이 안 됐다면
        thr_flag = 1
        menu_check_stop_event.clear() # 이벤트 초기화
        menu_check.start() # 실행

    # 타이틀 출력
    utils.show_text("CASINO", TITLE_FONT, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    pygame.display.update() # 화면 먼저 업데이트

    while time <= 5: # 5초동안
        # 도박 확률에 따라 시간 조절
        res_text = utils.show_text(res[time], BODY_FONT, BLACK, screen, SCREEN_WIDTH // 2 , START_Y // 2 - 100) # 값 출력
        pygame.display.update(res_text)
        pygame.time.delay(500)
        pygame.draw.rect(screen, WHITE, res_text) # 값 지우기
        pygame.display.update(res_text)
        pygame.time.delay(500)
        time += 1
    
    if time == 6: # 5초가 지나면
        # 결과값 반영
        money *= int(res[time-1])
        utils.varfile("w", loc_money, money) # 돈 저장
        time += 100000 # 다시 여기 못 오게 만들기

    # 이벤트 처리
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
                if isinstance(arrow_l_distance, float) and arrow_l_distance <= MENU_BUTTON[2]: # 마우스가 원 위에 있을 때
                    utils.varfile("w", loc_screen_flag, 3) # 농장 이동
                    menu_check_stop_event.set()
                    thr_flag = 0
                if isinstance(arrow_r_distance, float) and arrow_r_distance <= MENU_BUTTON[2]: # 마우스가 원 위에 있을 때
                    utils.varfile("w", loc_screen_flag, 4) # 상점 이동
                    menu_check_stop_event.set()
                    thr_flag = 0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: # 엔터 눌렀을 때
                time = 0 # time 초기화 -> 다시 도박 시작
    
    return screen_flag