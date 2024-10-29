import pygame.font

class Button:
    def __init__(self, screen, msg):
        # 初始化
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 設置按鈕尺寸及字體
        self.width, self.height = 200, 50
        self.button_color = (255, 0, 50)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # 創建rect並置中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 渲染成圖像
        self.prep_msg(msg)

    def prep_msg(self, msg):
        # 渲染成圖像並設定位於按鈕中央
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 在螢幕上畫出按鈕
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
