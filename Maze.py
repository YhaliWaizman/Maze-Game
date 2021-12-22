import pygame
from colorama import ansi, init
from colorama import Fore, Back, Style
import TextBox as tb
from time import sleep, time


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (153, 0, 153)
PATH = (153, 153, 102)
LRED = (255, 128, 128)


def printMaze(maze):
	for i in range(0, len(maze)):
		for j in range(0, len(maze[0])):
			if (maze[i][j] == 'u'):
				print(Fore.WHITE + str(maze[i][j]), end=" ")
			elif (maze[i][j] == 'c'):
				print(Fore.GREEN + str(maze[i][j]), end=" ")
			else:
				print(Fore.RED + str(maze[i][j]), end=" ")

		print('\n')

# Find number of surrounding cells

def surroundingCells(rand_wall, maze):
	s_cells = 0
	if (maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
		s_cells += 1
	if (maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
		s_cells += 1
	if (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
		s_cells += 1
	if (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
		s_cells += 1
	return s_cells


#Maze drawer on the screen
def openscreenMaze(maze):
    size = [len(maze[0])*10, len(maze)*10]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Maze")
    background_color = (255, 255, 255)
    screen.fill(background_color)
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 'w':
                pygame.draw.rect(screen, (153, 0, 153), [x*10, y*10, 10, 10])
            elif maze[y][x] == 'c':
                pygame.draw.rect(screen, (153, 153, 102), [x*10, y*10, 10, 10])
    pygame.display.flip()
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause = False
            elif event.type == pygame.KEYDOWN:
                pause = False
    pygame.quit()


def playMaze(maze):
    pygame.init()
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    clock = pygame.time.Clock()
    space = 10
    size = [len(maze[0])*10, len(maze)*10]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("RandomMaze - Yhali:)")
    background_color = (255, 255, 255)
    screen.fill(background_color)
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 'w':
                pygame.draw.rect(screen, PURPLE, [x*10, y*10, 10, 10])
            elif maze[y][x] == 'c':
                pygame.draw.rect(screen, PATH, [x*10, y*10, 10, 10])
    i = len(maze[0]) - 1
    j = len(maze) - 1
    maze[j][i] = 'c'
    i = 0
    j = 0
    maze[j][i] = 'c'
    for i in range(len(maze[0])):
        if maze[i][0] != 'c' and i != 0:
            maze[i][0] = 'c'
        if maze[i][0] == 'c' and i != 0:
            break
    direction = -1
    pygame.display.flip()
    done = False
    pygame.mixer.music.load('BackgroundMusic.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1, 0.0)
    pygame.draw.rect(screen, RED, [i*space, j*space, space, space])
    try:
        while not done:
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        direction=0
                    elif event.key==pygame.K_DOWN:
                        direction=1
                    elif event.key==pygame.K_LEFT:
                        direction=2
                    elif event.key==pygame.K_RIGHT:
                        direction=3
                    else:
                        pass
                if direction == 0 and maze[j-1][i] == 'c':
                    pygame.draw.rect(screen, PATH, [i*space, j*space, space, space])
                    j -= 1
                    pygame.draw.rect(screen, RED, [i*space, j*space, space, space])
                elif direction == 1 and maze[j+1][i] == 'c':
                    pygame.draw.rect(screen, PATH, [i*space, j*space, space, space])
                    j += 1
                    pygame.draw.rect(screen, RED, [i*space, j*space, space, space])
                elif direction == 2 and maze[j][i-1] == 'c':
                    pygame.draw.rect(screen, PATH, [i*space, j*space, space, space])
                    i -= 1
                    pygame.draw.rect(screen, RED, [i*space, j*space, space, space])
                elif direction == 3 and maze[j][i+1] == 'c':
                    pygame.draw.rect(screen, PATH, [i*space, j*space, space, space])
                    i += 1
                    pygame.draw.rect(screen, RED, [i*space, j*space, space, space])
                else:
                    pass

                pygame.display.flip()
                clock.tick(120)
    except IndexError:
        image  = pygame.image.load('WinScreen.png')
        screen.blit(image, (0, 0))
        pygame.display.flip()
        clock.tick(120)
        pygame.mixer.music.stop()
        pygame.mixer.music.load('WinGame.mp3')
        pygame.mixer.music.play(-1, 0.0)
        sleep(5)
        again = tb.openBox()
        if again == 'y':
            playMaze(maze)
        else:
            exit()
        time.sleep(2)
    except KeyboardInterrupt:
        pygame.quit()