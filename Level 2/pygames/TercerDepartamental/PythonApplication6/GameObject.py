import pygame

class GameObjectClass:
    def __init__(self, image, posX, posY):
        self.X = posX
        self.Y = posY
        self.Image = image
        self.Speed = 5
        self.DeltaMovement = 0
        self.Dead = False

    def Update(self, deltaTime):
        if self.Dead:
            return

        #print("Player Update")

    def Render(self, window):
        if self.Dead:
            return

        window.blit(self.Image, (self.X, self.Y))

    def Destroy(self):
        self.Dead = True

class OvniClass(GameObjectClass):
    def __init__(self, image, posX, posY):
        self.VelocidadVertical = 1
        self.Value = 10
        return super().__init__(image, posX, posY)

    def Update(self, deltaTime):
        if self.Y <= 520:
            self.Y = self.Y + self.VelocidadVertical
        return

    def collide(self):
        print("Collide")
        return


class BulletClass(GameObjectClass):
    def __init__(self, image, posX, posY):
        self.VelocidadVertical = -5
        return super().__init__(image, posX, posY)

    def Update(self, deltaTime):

        if self.Y > 0 - 16:
            self.Y = self.Y + self.VelocidadVertical

        return

class PlayerClass(GameObjectClass):
    def __init__(self, image, posX, posY):
        self.VelocidadVertical = 0
        return super().__init__(image, posX, posY)

    def Update(self, deltaTime):
        #Actualiza la posición de Player hasta llegar al tope de la pantalla

        if self.X < 0:
            self.X = 0

        #El 72 es por el tamaño del ancho "real" que tiene la imagen
        elif self.X + 72 > 520:
            self.X = 520 - 72

        if self.X >= 0 and (self.X + 72) <= 520:
            self.X = self.X + self.DeltaMovement

        return

    def Jump(self):
        self.VelocidadVertical = -20

    def Shoot(self, Bullet):
        print("Disparo")
        #crear una partícula
        #esa partícula avanza sobre y
        #después de llegar al límite de la pantalla, debe desaparecer

    def Move(self, direction):
        if direction == 'Left':
            self.DeltaMovement = -self.Speed
            print("Left")

        if direction == 'Right':
            self.DeltaMovement = self.Speed
            print("Right")


