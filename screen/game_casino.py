# 임포트
import pygame
import sys
import random
from env import * # 설정값 저장 파일: env.py
import func as utils # 함수 파일: func.py

res = ['5', '3', '2', '1', '0', '-1', '-2', '-3', '-5'] # 결과값 (배수)
time = 100000 # 시간

# 도박장 - screen_flag = 3
def casino(screen, money, hogamdo):
    global res, time

    # 배경화면
    utils.show_image("img/game_desc/flower-g1457003f2_1920.jpg", screen)

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: # 엔터 눌렀을 때
                time = 0 # time 초기화 -> 다시 도박 시작