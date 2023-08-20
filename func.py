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

def show_text(text, font, color, screen, x, y, align="center"):
    text_surface = font.render(text, True, color)
    if align == "center":
        text_rect = text_surface.get_rect(center=(x, y))
    elif align == "left":
        text_rect = text_surface.get_rect(topleft=(x, y))
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
def switch_screen(screen, flag, money, hogamdo):
    if flag == 2: # 메인 게임화면(판매/배달)
        gs.start(screen) # 게임 시작 함수 호출
    elif flag == 3: # 농장 화면
        gf.farm(screen) # 농장 화면 함수 호출
    elif flag == 4: # 상점 화면
        gmarket.market(screen) # 상점 화면 함수 호출
    elif flag == 5: # 도박장 화면
        gc.casino(screen, money, hogamdo) # 도박장 화면 함수 호출
    elif flag == 6: # 메뉴 화면
        gmenu.menu(screen) # 메뉴 화면 함수 호출

# 버튼 띄우기 함수(메뉴)
def default_ui(screen, mouse_pos, event, pos):
    # pos : 0 - 좌측 하단(game_start), 1 - 우측 상단과 오른쪽, 왼쪽(나머지)
    global screen_flag

    if pos == 0:
        button = MENU_BUTTON
    elif pos == 1:
        button = EXIT_BUTTON
    
    pygame.draw.circle(screen, BLACK, (button[0], button[1]), button[2]) # 원 그리기
    
    if pos == 1:
        pygame.draw.circle(screen, BLACK, (LEFT_BUTTON[0], LEFT_BUTTON[1]), LEFT_BUTTON[2]) # 왼쪽 화살표 그리기
        pygame.draw.circle(screen, BLACK, (RIGHT_BUTTON[0], RIGHT_BUTTON[1]), RIGHT_BUTTON[2]) # 왼쪽 화살표 그리기
    else:
        pygame.display.update()
    
    while not event.is_set():
        money = varfile("r", loc_money, 0) # arrow_l_distance 변수 업데이트
        hogamdo = varfile("r", loc_hogamdo, 0) # arrow_r_distance 변수 업데이트

        # 마우스가 원 위에 있는지 여부 확인
        distance = ((button[0] - mouse_pos[0]) ** 2 + (button[1] - mouse_pos[1]) ** 2) ** 0.5
        arrow_l_distance = ((LEFT_BUTTON[0] - mouse_pos[0]) ** 2 + (LEFT_BUTTON[1] - mouse_pos[1]) ** 2) ** 0.5
        arrow_r_distance = ((RIGHT_BUTTON[0] - mouse_pos[0]) ** 2 + (RIGHT_BUTTON[1] - mouse_pos[1]) ** 2) ** 0.5


        varfile("w", loc_menu_distance, distance) # 값 저장
        if pos == 1:
            varfile("w", loc_arrow_l, arrow_l_distance) # 값 저장
            varfile("w", loc_arrow_r, arrow_r_distance) # 값 저장


        # 마우스가 원 위에 있는 경우
        if distance <= MENU_BUTTON[2]:
            circle = pygame.draw.circle(screen, RED, (button[0], button[1]), button[2]) # 빨간색으로 변경
        else: # 아니라면
            circle = pygame.draw.circle(screen, BLACK, (button[0], button[1]), button[2]) # 원래대로
        if pos == 1: # 화살표 마우스 위치 확인
            if arrow_l_distance <= LEFT_BUTTON[2]: # 왼쪽 화살표
                arrow_l = pygame.draw.circle(screen, RED, (LEFT_BUTTON[0], LEFT_BUTTON[1]), LEFT_BUTTON[2]) # 빨간색으로 변경
            else:
                arrow_l = pygame.draw.circle(screen, BLACK, (LEFT_BUTTON[0], LEFT_BUTTON[1]), LEFT_BUTTON[2]) # 원래대로

            if arrow_r_distance <= RIGHT_BUTTON[2]: # 오른쪽 화살표
                arrow_r = pygame.draw.circle(screen, RED, (RIGHT_BUTTON[0], RIGHT_BUTTON[1]), RIGHT_BUTTON[2]) # 빨간색으로 변경
            else:
                arrow_r = pygame.draw.circle(screen, BLACK, (RIGHT_BUTTON[0], RIGHT_BUTTON[1]), RIGHT_BUTTON[2]) # 원래대로

        # 화면 업데이트
        pygame.display.update(circle)
        if pos == 1:
            pygame.display.update(arrow_l)
            pygame.display.update(arrow_r)
        
        # 재화 출력
        show_text(f"돈: {money}", BODY_FONT, BLACK, screen, 15, SCREEN_HEIGHT // 7, "left")
        show_text(f"호감도: {hogamdo}", BODY_FONT, BLACK, screen, 15, SCREEN_HEIGHT // 7 + 40, "left")