from cmu_graphics import *
import random

class Player: 
    pass #TO BE COMPLETED :(

class Obstacle:
    def __init__(self, shape, centerX, centerY, size, color, moving=False, speedX=0, speedY=0):
        self.shape = shape  # rectangle, circle, or triangle
        self.centerX = centerX
        self.centerY = centerY
        self.size = size
        self.color = color
        self.moving = moving
        self.speedX = speedX
        self.speedY = speedY
        self.collided = False

    def drawObstacle(self):
        if self.shape == "rectangle":
            drawRect(self.centerX - self.size // 2, self.centerY - self.size // 2, 
                     self.size, self.size, fill=self.color)
        elif self.shape == "circle":
            drawCircle(self.centerX, self.centerY, self.size // 2, fill=self.color)
        elif self.shape == "triangle":
            halfSize = self.size // 2
            points = [
                self.centerX, self.centerY - halfSize,  # Top
                self.centerX - halfSize, self.centerY + halfSize,  # Bottom left
                self.centerX + halfSize, self.centerY + halfSize  # Bottom right
            ]
            drawPolygon(*points, fill=self.color)

    def move(self, app):
        if self.moving:
            self.centerX += self.speedX
            self.centerY += self.speedY

            if self.centerX - self.size // 2 <= 0 or self.centerX + self.size // 2 >= app.width or checkCharacterCollision(app, self.centerX, self.centerY):
                self.speedX *= -1
            if self.centerY - self.size // 2 <= 0 or self.centerY + self.size // 2 >= app.height or checkCharacterCollision(app, self.centerX, self.centerY):
                self.speedY *= -1

class Platform: 
    def __init__(self, leftX, leftY): 
        self.leftX = leftX
        self.leftY = leftY 
        self.width = 80
        self.height = 10
    
    def drawPlatform(self): 
        drawRect(self.leftX, self.leftY, self.width, self.height, fill = 'antiqueWhite')

class Goal:
    def __init__(self, centerX, centerY): 
        self.centerX = centerX 
        self.centerY = centerY 
        self.radius = 40
    
    def drawGoal(self): 
        drawCircle(self.centerX, self.centerY, self.radius, fill='khaki')

def onAppStart(app): 
    start_onAppStart(app)
    instructions_onAppStart(app)
    game_onAppStart(app)

#start screen
def start_onAppStart(app): 
    app.instructionButtonLeftX = app.width // 2 - 160
    app.instructionButtonLeftY = app.height // 2 + 40
    app.startButtonLeftX = app.width // 2 + 10
    app.startButtonLeftY = app.height // 2 + 40
    app.buttonWidth = 150 
    app.buttonHeight = 50

#events
def start_onMousePress(app, mouseX, mouseY): 
    if (app.instructionButtonLeftX <= mouseX <= app.instructionButtonLeftX + app.buttonWidth) and (app.instructionButtonLeftY <= mouseY <= app.instructionButtonLeftY + app.buttonHeight): 
        setActiveScreen('instructions')
    
    if (app.startButtonLeftX <= mouseX <= app.startButtonLeftX + app.buttonWidth) and (app.startButtonLeftY <= mouseY <= app.startButtonLeftY + app.buttonHeight): 
        setActiveScreen('game')
#drawing
def drawStartTitle(app): 
    drawRect(0, 0, app.width, app.height, fill='floralWhite')
    drawLabel('trace 112', app.width // 2, app.height // 2 - 50, fill=gradient(rgb(255, 164, 164), rgb(255, 205, 164), rgb(255, 238, 164), rgb(207, 255, 164), rgb(164, 239, 255), rgb(164, 187, 255), rgb(193, 164, 255), rgb(255, 164, 231), start='left'), size=60, bold=True, align='center', border=rgb(214, 196, 160), font='montserrat')
    drawLabel('a fun drawing game', app.width // 2, app.height // 2 + 5, fill=rgb(71, 71, 71), size = 20, font='montserrat', bold=True)

def drawButtons(app): 
    buttonWidth = 150 
    buttonHeight = 50
    drawRect(app.instructionButtonLeftX, app.instructionButtonLeftY, app.buttonWidth, app.buttonHeight, fill='lightPink', border=rgb(230, 141, 154))
    drawRect(app.startButtonLeftX, app.startButtonLeftY, app.buttonWidth, app.buttonHeight, fill=rgb(176, 219, 176), border=rgb(106, 166, 106))
    drawLabel('instructions', app.buttonWidth // 2 + app.instructionButtonLeftX, app.buttonHeight // 2 + app.instructionButtonLeftY, fill='floralWhite', size = 15, bold=True, font='montserrat')
    drawLabel('start', app.buttonWidth // 2 + app.startButtonLeftX, app.buttonHeight // 2 + app.startButtonLeftY, fill='floralWhite', size = 15, bold=True, font='montserrat')

def start_redrawAll(app): 
    drawStartTitle(app)
    drawButtons(app)

# Instructions screen
def instructions_onAppStart(app): 
    app.backButtonLeftX = 20
    app.backButtonLeftY = 20
    app.backButtonWidth = 70
    app.backButtonHeight = 70

#events
def instructions_onMousePress(app, mouseX, mouseY): 
    if (app.backButtonLeftX <= mouseX <= app.backButtonLeftX + app.backButtonWidth and 
        app.backButtonLeftY <= mouseY <= app.backButtonLeftY + app.backButtonHeight): 
        setActiveScreen('start')

#drawing
def drawInstructionsTitle(app): 
    drawRect(0, 0, app.width, app.height, fill='floralWhite')
    drawLabel('How to Play', app.width // 2, 70, size=50, font='montserrat', bold=True, fill='black')

def drawInstructionsContent(app): 
    instructions = [
        "1. Use the left and right arrow keys to move your character.",
        "2. Draw paths with your mouse to guide the character through the obstacles.",
        "3. You start with 3 lives but when your character collides with an obstacle, it will lose one life.",
        "4. For every level, your goal is to make it to the yellow circle.",
        "5. Have fun!"
    ]

    for i, instruction in enumerate(instructions):
        drawLabel(instruction, app.width // 2, 150 + i * 40, size=20, font='montserrat', align='center', fill='black')

def drawBackButton(app): 
    drawRect(app.backButtonLeftX, app.backButtonLeftY, app.backButtonWidth, app.backButtonHeight, fill='honeydew', border=rgb(71, 71, 71))
    drawLabel('Back', app.backButtonLeftX + app.backButtonWidth // 2, app.backButtonLeftY + app.backButtonHeight // 2, 
              size=20, font='montserrat', bold=True, align='center', fill='black')

def instructions_redrawAll(app): 
    drawInstructionsTitle(app)
    drawInstructionsContent(app)
    drawBackButton(app)

#game screen
def game_onAppStart(app): 
    # Drawing coords
    app.drawingPaths = []
    app.currentPath = []

    # Character
    app.characterX = 100
    app.characterY = app.height - 100  
    app.characterRadius = 15  

    # Platforms
    app.platforms = []

    app.onPath = False
    app.lastY = app.characterY
    
    #Obstacles
    app.obstacles = []
    app.isColliding = False
    
    #Lives
    app.lives = 3
    
    generatePlatforms(app)
    generateGoal(app)
    generateObstacles(app)
    
def generatePlatforms(app): 
    # Starting platform 
    startPlatform = Platform(75, app.height - 50)
    app.platforms.append(startPlatform)
    
    minDistance = 150

    for _ in range(random.randint(2, 8)): 
        while True:
            newX = random.randint(50, app.width - 80)
            newY = random.randint(50, app.height - 10)
            overlapping = False
            
            # platforms aren't close to other platforms 
            for platform in app.platforms:
                if abs(platform.leftX - newX) < minDistance and abs(platform.leftY - newY) < minDistance:
                    overlapping = True
                    break
            
            if not overlapping:
                app.platforms.append(Platform(newX, newY))
                break

def generateGoal(app): 
    minDistanceFromCharacter = 150
    
    while True:
        randomX = random.randint(50, app.width - 50)
        randomY = random.randint(50, app.height - 50)
        
        # goal doesn't overlap w platforms
        overlapping = False
        for platform in app.platforms:
            if platform.leftX - 40 <= randomX <= platform.leftX + platform.width + 40 and \
               platform.leftY - 40 <= randomY <= platform.leftY + platform.height + 40:
                overlapping = True
                break

        # goal isn't too close to character
        distanceFromCharacter = ((randomX - app.characterX) ** 2 + 
                                 (randomY - app.characterY) ** 2) ** 0.5
        if not overlapping and distanceFromCharacter >= minDistanceFromCharacter:
            app.goal = Goal(randomX, randomY)
            break

def generateObstacles(app):
    numObstacles = random.randint(5, 10)
    minDistance = 150 

    for _ in range(numObstacles):
        while True:
            shape = random.choice(["rectangle", "circle", "triangle"])
            centerX = random.randint(50, app.width - 50)
            centerY = random.randint(50, app.height - 50)
            size = random.randint(30, 80)
            color = random.choice(["red", "blue", "green", "orange", "purple", "pink", "gray", "brown"])

            moving = random.choice([True, False])
            speedX = random.randint(-3, 3) if moving else 0
            speedY = random.randint(-3, 3) if moving else 0

            #not too close to other obstacles
            overlapping = False
            for obstacle in app.obstacles:
                distance = ((centerX - obstacle.centerX) ** 2 + (centerY - obstacle.centerY) ** 2) ** 0.5
                if distance < (size // 2 + obstacle.size // 2 + minDistance):
                    overlapping = True
                    break
            
            #not too close to platforms 
            for platform in app.platforms:
                if (platform.leftX - size <= centerX <= platform.leftX + platform.width + size and
                    platform.leftY - size <= centerY <= platform.leftY + platform.height + size):
                    overlapping = True
                    break
            
            #not close to character
            distanceFromCharacter = ((centerX - app.characterX) ** 2 + 
                                     (centerY - app.characterY) ** 2) ** 0.5
            if overlapping or distanceFromCharacter < minDistance:
                continue

            obstacle = Obstacle(shape, centerX, centerY, size, color, moving, speedX, speedY)
            app.obstacles.append(obstacle)
            break

#events
def game_onMouseDrag(app, mouseX, mouseY): 
    app.currentPath.append((mouseX, mouseY))

def game_onMouseRelease(app, mouseX, mouseY): 
    if app.currentPath:  
        app.drawingPaths.append(app.currentPath)
        app.currentPath = []

    evaluateClosestPoint(app)
    
def game_onStep(app):
    if not app.onPath and not isOnPlatform(app):
        app.characterY += 5 #gravity
        
    moveObstacles(app)

    app.verticalMovement = app.characterY - app.lastY
    app.lastY = app.characterY

    checkObstacleCollision(app)
    checkGoalCollision(app)

    app.characterX = max(app.characterRadius, min(app.characterX, app.width - app.characterRadius))
    app.characterY = min(app.characterY, app.height - app.characterRadius)
    
def game_onKeyPress(app, key):
    speed = 10

    if key == 'left':
        app.characterX -= speed
    elif key == 'right':
        app.characterX += speed
    
    # evaluate the closest point on all paths
    evaluateClosestPoint(app)

#helper functions
def evaluateClosestPoint(app): 
    closestPoint = findClosestPointOnPath(app, app.characterX, app.characterY, app.drawingPaths)

    if closestPoint:
        closestX, closestY = closestPoint
        distance = ((app.characterX - closestX) ** 2 + (app.characterY - closestY) ** 2) ** 0.5

        if distance <= app.characterRadius * 1.3 and not isAtPathEndpoint(app, closestX, closestY):
            app.characterX = closestX
            app.characterY = closestY - app.characterRadius
            app.onPath = True
        else:
            app.onPath = False
    else:
        app.onPath = False 

def moveObstacles(app):
    for obstacle in app.obstacles:
        obstacle.move(app)

def checkObstacleCollision(app):
    collision = False

    for obstacle in app.obstacles:
        if obstacle.shape == "rectangle":
            left = obstacle.centerX - obstacle.size // 2
            right = obstacle.centerX + obstacle.size // 2
            top = obstacle.centerY - obstacle.size // 2
            bottom = obstacle.centerY + obstacle.size // 2

            if (left <= app.characterX <= right and
                top <= app.characterY <= bottom):
                collision = True
                break

        elif obstacle.shape == "circle":
            dist = ((app.characterX - obstacle.centerX) ** 2 + 
                    (app.characterY - obstacle.centerY) ** 2) ** 0.5
            if dist <= app.characterRadius + obstacle.size // 2:
                collision = True
                break
            
        #check for triangle

    if collision:
        if not app.isColliding:
            app.lives -= 1
            app.isColliding = True
    else:
        app.isColliding = False 

def checkGoalCollision(app): 
    if app.goal:
        dist = ((app.characterX - app.goal.centerX) ** 2 + 
                (app.characterY - app.goal.centerY) ** 2) ** 0.5
        if dist <= app.characterRadius + app.goal.radius:
            generateGoal(app)

def checkCharacterCollision(app, obstacleX, obstacleY): 
    pass 

def isAtPathEndpoint(app, x, y):
    for path in app.drawingPaths:
        if len(path) >= 2:
            startX, startY = path[0]
            endX, endY = path[-1]
            if (x, y) == (startX, startY) or (x, y) == (endX, endY):
                return True
    return False

def isOnPlatform(app):
    for platform in app.platforms:
        if platform.leftX <= app.characterX <= platform.leftX + platform.width:
            if platform.leftY <= app.characterY + app.characterRadius <= platform.leftY + platform.height:
                return True
    return False

def isOnPath(app):
    for path in app.drawingPaths:
        for i in range(1, len(path)):
            x1, y1 = path[i - 1]
            x2, y2 = path[i]
            if isPointNearPath(x1, y1, x2, y2, app.characterX, app.characterY + app.characterRadius):
                return True
    return False

def findClosestPointOnPath(app, x, y, paths):
    minDistance = float('inf')
    closestPoint = None
    for path in paths:
        for i in range(1, len(path)):
            x1, y1 = path[i - 1]
            x2, y2 = path[i]
            projX, projY = closestPointOnSegment(x, y + app.characterRadius, x1, y1, x2, y2)

            if projX is not None and projY is not None:
                if min(x1, x2) <= projX <= max(x1, x2) and min(y1, y2) <= projY <= max(y1, y2):
                    distance = ((x - projX) ** 2 + (y - projY) ** 2) ** 0.5

                    if distance < minDistance or (distance == minDistance and projY < closestPoint[1]):
                        minDistance = distance
                        closestPoint = (projX, projY)

    return closestPoint if closestPoint and minDistance <= app.characterRadius * 1.3 else None

def closestPointOnSegment(x, y, x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    length_squared = dx * dx + dy * dy
    if length_squared == 0:  
        return x1, y1

    t = max(0, min(1, ((x - x1) * dx + (y - y1) * dy) / length_squared))
    closestX = x1 + t * dx
    closestY = y1 + t * dy
    return closestX, closestY
    
def isPointNearPath(x1, y1, x2, y2, targetX, targetY, tolerance=5):
    closestX, closestY = closestPointOnSegment(targetX, targetY, x1, y1, x2, y2)
    dist = ((targetX - closestX) ** 2 + (targetY - closestY) ** 2) ** 0.5
    return dist <= tolerance

#drawing
def drawLives(app): 
    drawLabel(f'{app.lives} Lives Left', 100, 50, size = 20)

def drawDrawing(app):
    #draw previous paths
    for path in app.drawingPaths:
        for i in range(1, len(path)):
            x1, y1 = path[i - 1]
            x2, y2 = path[i]
            drawLine(x1, y1, x2, y2, fill='black', lineWidth=5)
    
    #draw current path
    for i in range(1, len(app.currentPath)):
        x1, y1 = app.currentPath[i - 1]
        x2, y2 = app.currentPath[i]
        drawLine(x1, y1, x2, y2, fill='black', lineWidth=5)

def drawCharacter(app): 
    drawCircle(app.characterX, app.characterY, app.characterRadius, fill='red')

def drawPlatforms(app): 
    for platform in app.platforms: 
        platform.drawPlatform()

def drawGoal(app): 
    if app.goal: 
        app.goal.drawGoal()

def drawObstacles(app):
    for obstacle in app.obstacles:
        obstacle.drawObstacle()

def game_redrawAll(app): 
    # Background
    drawRect(0, 0, app.width, app.height, fill='floralWhite')
    drawLives(app)
    drawDrawing(app)
    drawPlatforms(app)
    drawGoal(app)
    drawObstacles(app)
    drawCharacter(app)

def main(): 
    runAppWithScreens(width=960, height=540, initialScreen='start')

main()