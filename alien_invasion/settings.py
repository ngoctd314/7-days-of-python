class Settings:
    def __init__(self):
        self.step = 1
        self.speed = 3
        self.screen_width = self.step * 1200
        self.screen_height = self.step * 800
        self.bg_color = (230, 230, 230)

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
