import random
import math
import pygame
from GameObject import *

class Game:
    def __init__(self, width, height):
        #Inicializamos pygame con pygame.init()
        pygame.init()

        self.W = width
        self.H = height
        self.Window = pygame.display.set_mode((width, height))
        self.ResourceDictionary = {}
        self.GameObjectList = []
        self.Running = True
        self.Clock = pygame.time.Clock()
        self.ElapsedTime = 0
        self.EnemySpawn = 100
        self.Score = 0
        self.ScoreBarText = pygame.font.Font('freesansbold.ttf', 22).render('SCORE: {0}'.format(self.Score), True, "white", "black")
        self.ScoreBar = self.ScoreBarText.get_rect()

    def Run(self):
        #Cargar todo lo que voy a necesitar. Imagenes.
        self.LoadImage("astronave.png", "Player")
        self.LoadImage("ovni.png", "Ovni")
        self.LoadImage("bullet.png", "Bala")
        self.LoadImage("background.jpg", "BG")

        #Ya que cargué todos mis assets y mis sprites.
        #Crear mis objetos iniciales.
        self.Player = PlayerClass(self.ResourceDictionary["Player"], 200, 400)
        self.AddGameObject(self.Player)

        self.ScoreBar.center = (self.W *5 // 6, 15)
        #Mientras no quiera salir del juego.
        while self.Running:
            #Sacamos el tiempo entre cuadros.
            deltaTime = 1 / self.Clock.tick(60)

            self.HandleEvents()
            self.Update(deltaTime)
            self.ElapsedTime += 1
            self.Render()
            #print(self.ElapsedTime)

            if self.ElapsedTime % self.EnemySpawn == 0:
                generatedEnemy = OvniClass(self.ResourceDictionary["Ovni"], random.randrange(0, 400), 10)
                self.AddGameObject(generatedEnemy)
                generatedEnemy = None


    def LoadImage(self, path, ID):
        image = pygame.image.load(path)
        self.ResourceDictionary[ID] = image
        return image

    def AddGameObject(self, gameObject):
        self.GameObjectList.append(gameObject)

    def Update(self, deltaTime):
        for object in self.GameObjectList:
            object.Update(deltaTime)
            self.ValidateCollision(object)

    def ValidateCollision(self, gameObject):
            if type(gameObject) is BulletClass:
                if gameObject.Y < 0:
                    self.GameObjectList.remove(gameObject)
                    print("Bala borrada")

                else :
                    for object in self.GameObjectList:
                        if type(object) is OvniClass:
                            distance = getDistance(gameObject, object)
                            if distance < 24 :
                                print("Impacto")
                                self.Score += object.Value
                                self.GameObjectList.remove(object)
                                self.GameObjectList.remove(gameObject)
                                print(self.Score)

            if type(gameObject) is PlayerClass:
                for object in self.GameObjectList:
                    if type(object) is OvniClass:
                        distance = getDistance(gameObject, object)
                        if distance < 24 :
                            print("Impacto entre jugador y nave")
                            #self.Score += object.Value
                            self.GameObjectList.remove(object)
                            #self.GameObjectList.remove(gameObject)
                            self.Running = False
                            #print(self.Score)

    def Render(self):
        self.Window.fill((0,0,0))

        display_surface = pygame.display.set_mode((self.W, self.H))
        #pygame.display.set_caption('Show Text')
        self.ScoreBarText = pygame.font.Font('freesansbold.ttf', 22).render('SCORE: {0}'.format(self.Score), True, "white", "black")
        self.Window.blit(self.ScoreBarText, self.ScoreBar)

        for object in self.GameObjectList:
            object.Render(self.Window)

        pygame.display.flip()

    def HandleEvents(self):
        #Actualizar los eventos de python.
        for event in pygame.event.get():
            #self.CheckButtonPress(event, pygame.KEYDOWN, pygame.K_LEFT)
            #self.CheckButtonPress(event, pygame.KEYDOWN, pygame.K_RIGHT)
            #self.CheckButtonPress(event, pygame.KEYDOWN, pygame.K_UP)
            #self.CheckButtonPress(event, pygame.KEYDOWN, pygame.K_DOWN)

            if self.CheckButtonPress(event, pygame.KEYDOWN, pygame.K_RIGHT):
                self.Player.Move("Right")

            if self.CheckButtonPress(event, pygame.KEYDOWN, pygame.K_LEFT):
                self.Player.Move("Left")

            if self.CheckButtonPress(event, pygame.KEYDOWN, pygame.K_SPACE):
                generatedBullet = BulletClass(self.ResourceDictionary["Bala"], self.Player.X, self.Player.Y)
                self.Player.Shoot(generatedBullet)
                self.AddGameObject(generatedBullet)

            if event.type == pygame.QUIT:
                self.Running = False

    def CheckButtonPress(self, event, type, key):
        if event.type == type:
                    if event.key == key:
                        return True
        return False

def getDistance(gameObjectA, gameObjectB):
    distance = math.sqrt( (gameObjectA.X - gameObjectB.X)**2 + (gameObjectA.Y - gameObjectB.Y)**2 )
    return distance