import pygame.font

class Scoreboard:
    def __init__(self, ai_settings, screen, stats):
        # 初始化記分板的屬性
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        # 字體設定
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # 準備圖像
        self.prep_score()
        self.prep_highest_score()  # 確保最高分數圖像被準備

    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        # 將分數渲染成圖像
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        # 將分數的圖像放在螢幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = 0

    def prep_highest_score(self):
        # round用於四捨五入，-1表示四捨五入在十位數
        rounded_highest_score = int(round(self.stats.highest_score, -1))
        highest_score_str = "{:,}".format(rounded_highest_score)
        # 將最高分數渲染成圖像
        self.highest_score_image = self.font.render(highest_score_str, True, self.text_color, self.ai_settings.bg_color)
        # 將最高分數的圖像放在一般得分下方
        self.highest_score_rect = self.highest_score_image.get_rect()
        self.highest_score_rect.right = self.screen_rect.right - 20
        self.highest_score_rect.bottom = self.screen_rect.bottom - 20

    def show_score(self):
        # 在螢幕上畫記分板
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highest_score_image, self.highest_score_rect)


