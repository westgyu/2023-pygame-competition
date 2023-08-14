# 임포트
import pygame
import sys
from env import * # 설정값 저장 파일: env.py
import func as utils # 함수 파일: func.py

# 사점 - screen_flag = 4
def market(screen):
    utils.show_image("img/game_desc/flower-g1457003f2_1920.jpg", screen)

    # 타이틀 출력
    utils.show_text("MARKET", TITLE_FONT, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    pygame.display.update()

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()