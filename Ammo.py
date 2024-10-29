import time

class Ammo:
    def __init__(self, bullet_max=10, bullet_amount=10, reload_time=1000):
        
        self.bullet_max = bullet_max
        self.bullet_amount = bullet_amount
        self.reload_time = reload_time
        self.last_reload_time = time.time() * 1000  

    def update(self):
        
        current_time = time.time() * 1000  
        if current_time - self.last_reload_time >= self.reload_time:
            if self.bullet_amount < self.bullet_max:
                self.bullet_amount += 1
                self.last_reload_time = current_time  
        return self

    def fire(self):
        
        if self.bullet_amount > 0:
            self.bullet_amount -= 1
        return self
