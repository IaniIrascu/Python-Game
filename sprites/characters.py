import pygame as pg

class Entity(pg.sprite.Sprite):
    def __init__(self, frames, position, group, turned):
        super().__init__(group)
        self.wait = 0
        self.idx = 0
        self.frames = frames
        self.speed = 600
        self.image = self.frames['down'][self.idx]
        self.rect = self.image.get_rect(center = position)
        self.behind = self.rect.centery
        self.direction = pg.math.Vector2(0, 0)
        self.turned = turned
        self.order = 3
        self.hitbox = self.rect.inflate(-self.rect.width / 2, -self.rect.height / 2)
    
    def change(self):
        self.wait += 1
        if self.wait == 5:
            self.wait = 0
            self.idx += 1
        self.idx = self.idx % len(self.frames[self.get_direction()])
        self.image = self.frames[self.get_direction()][self.idx]
    
    def get_direction(self):
        return f"{self.turned}{'' if self.direction else '_idle'}"
    

class Player(Entity):
    def __init__(self, frames, position, group, turned, collisions, inventory = None):
        super().__init__(frames, position, group, turned)
        self.collisions = collisions
        self.inventory = inventory
        self.stop = False
    
    def input(self):
        keys = pg.key.get_pressed()
        input = pg.math.Vector2(0, 0)
        if keys[pg.K_w]:
            input.y -= 1
            self.turned = 'up'
        if keys[pg.K_s]:
            input.y += 1
            self.turned = 'down'
        if keys[pg.K_a]:
            input.x -= 1
            self.turned = 'left'
        if keys[pg.K_d]:
            input.x += 1
            self.turned = 'right'
        self.direction = input.normalize() if input else input
    
    def update(self, dt):
        if not self.stop:
            self.input()
        self.behind = self.rect.centery

        self.rect.centerx += self.direction.x * self.speed * dt
        self.hitbox.centerx = self.rect.centerx
        self.collide('horizontal')

        self.rect.centery += self.direction.y * self.speed * dt
        self.hitbox.centery = self.rect.centery
        self.collide('vertical')
        if not self.stop:
            self.change()

    def collide(self, direction):
        for obj in self.collisions:
            if obj.hitbox.colliderect(self.hitbox):
                if direction == "horizontal":
                    if self.direction.x > 0:
                        self.hitbox.right = obj.hitbox.left
                    else:
                        self.hitbox.left = obj.hitbox.right
                    self.rect.centerx = self.hitbox.centerx
                else:
                    if self.direction.y > 0:
                        self.hitbox.bottom = obj.hitbox.top
                    else:
                        self.hitbox.top = obj.hitbox.bottom
                    self.rect.centery = self.hitbox.centery
                
    def set_inventory(self, inventory):
        self.inventory = inventory

    def get_inventory(self):
        return self.inventory

class NPC(Entity):
    def __init__(self, frames, position, group, turned, data):
        super().__init__(frames, position, group, turned)
        self.data = data
    
    def speak(self):
        dialog_key = 'default' if not self.data['defeated'] else 'defeated'
        return self.data['dialog'][dialog_key]
    
    def update(self, dt):
        self.change()

class Dialog:
    def __init__(self, npc, player, group, font):
        self.npc = npc
        self.player = player
        self.group = group
        self.font = font
        self.idx = 0
        self.dialog = Popup(self.npc, self.group, self.font, self.idx)
        self.start_time = pg.time.get_ticks()
        self.delay_duration = 500  # Delay in milliseconds
        self.delay_active = True

    def change_dialog(self):
        current_time = pg.time.get_ticks()
        
        # Handle initial delay without freezing the game
        if self.delay_active and (current_time - self.start_time) < self.delay_duration:
            return
        elif self.delay_active:
            self.delay_active = False
    
        if pg.key.get_just_pressed()[pg.K_f]:
            self.dialog.kill()
            self.idx += 1
            print(self.idx)
            if self.idx < len(self.npc.data['dialog']['default']):
                self.dialog = Popup(self.npc, self.group, self.font, self.idx)
            else:
                self.dialog.kill()
                self.player.stop = False

    def update(self):
        self.change_dialog()

class Popup(pg.sprite.Sprite):
    def __init__(self, npc, group, font, idx):
        super().__init__(group)
        self.image = font.render(npc.speak()[idx], True, 'blue')
        self.order = 4
        self.rect = self.image.get_frect(midbottom = npc.rect.midtop)

    
