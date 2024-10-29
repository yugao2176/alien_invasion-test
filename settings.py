class Settings:
    def __init__(self):
        # 屏幕設置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飛船設置
        self.ship_speed_factor = 8
        self.ship_limit = 3

        # 子彈設置
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5

        # 外星人設定
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 50
        self.fleet_direction = 1
        
        # 初始化動態設置
        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        # 擊墜外星人得分
        self.alien_points = 50


