# 임포트
import pygame
import sys
# from env import * # 설정값 저장 파일: env.py
from func import * # 함수 파일: func.py

# 게임 설명 함수
def game_start(screen):
    show_image("img/game_desc/flower-g1457003f2_1920.jpg", screen)

    # 타이틀 출력
    show_text("Game START", Title_font, black, screen, screen_width // 2, screen_height // 2)

    pygame.display.update()

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()