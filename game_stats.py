class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.highest_score = 0

    def reset_stats(self):
        # 殘機數設定
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
