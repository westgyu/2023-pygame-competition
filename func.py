# 임포트
import pygame
import sys
from env import * # 설정값 저장 파일: env.py

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
    image_rect = image.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(image, image_rect)