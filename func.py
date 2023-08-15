# 임포트
import pygame
import sys
from env import * # 설정값 저장 파일: env.py

import screen.game_start as gs # 게임 실행 파일: screen\game_start.py
import screen.game_farm as gf # 게임 실행 파일: screen\game_farm.py
import screen.game_market as gmarket # 게임 실행 파일: screen\game_market.py
import screen.game_casino as gc # 게임 실행 파일: screen\game_casino.py
import screen.game_menu as gmenu # 게임 실행 파일: screen\game_menu.py

def init():
    pygame.init() # Pygame 초기화
    pygame.display.set_caption("2023 Pygame Competition") # 제목 설정

def show_text(text, font, color, screen, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)
    return text_rect

# 이미지 로드
def load_image(image_path):
    try:
        image = pygame.image.load(image_path)
        return image
    except pygame.error as e:
        print("이미지를 불러오는 데 실패했습니다:", str(e))
        sys.exit()

# 이미지 띄우기 함수
def show_image(image_path, screen):
    image = load_image(image_path)
    image_rect = image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(image, image_rect)

# 함숫값 바꾸는 함수(파일로) -> 연동 불가능한 함수들 한정
def varfile(mode, loc, data):
    if mode == "w":
        f = open(loc, 'w')
        f.write(str(data))
        f.close()
    elif mode == "r":
        f = open(loc, "r")
        res = f.read()
        f.close()
        return res

# 화면 바꾸는 함수
def switch_screen(screen, flag):
    if flag == 2: # 메인 게임화면(판매/배달)
        gs.start(screen) # 게임 시작 함수 호출
    elif flag == 3: # 농장 화면
        gf.farm(screen) # 농장 화면 함수 호출
    elif flag == 4: # 상점 화면
        gmarket.market(screen) # 상점 화면 함수 호출
    elif flag == 5: # 도박장 화면
        gc.casino(screen) # 도박장 화면 함수 호출
    elif flag == 6: # 메뉴 화면
        gmenu.menu(screen) # 메뉴 화면 함수 호출

# 버튼 띄우기 함수
def default_ui(screen, mouse_pos, event):
    global screen_flag
    pygame.draw.circle(screen, BLACK, (MENU_BUTTON[0], MENU_BUTTON[1]), MENU_BUTTON[2]) # 원 그리기
    while not event.is_set():
        # 마우스가 원 위에 있는지 여부 확인
        distance = ((MENU_BUTTON[0] - mouse_pos[0]) ** 2 + (MENU_BUTTON[1] - mouse_pos[1]) ** 2) ** 0.5
        varfile("w", "data/menu.distance", distance) # 값 저장

        # 마우스가 원 위에 있는 경우
        if distance <= MENU_BUTTON[2]:
            circle = pygame.draw.circle(screen, (255, 0, 0), (MENU_BUTTON[0], MENU_BUTTON[1]), MENU_BUTTON[2]) # 빨간색으로 변경
        else: # 아니라면
            circle = pygame.draw.circle(screen, BLACK, (MENU_BUTTON[0], MENU_BUTTON[1]), MENU_BUTTON[2]) # 원래대로

        # 화면 업데이트
        pygame.display.update(circle)