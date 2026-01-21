import pygame
import math

pygame.init()

game_width = 800
game_height = 800
FPS = 120
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True

def point(xy):
    x = xy[0]
    y = xy[1]
    size = 10

    pygame.draw.rect(screen, "green", (x - size/2, y - size/2, size, size))

def line(p1, p2):
   pygame.draw.line(screen, "green", ())

def screen_coordinates(xy):
    x = xy[0]
    y = xy[1]
    x = (x + 1) / 2 * game_width
    y = (1 - (y + 1) / 2) * game_height
    return x, y

def project(xyz):
    x = xyz[0]
    y = xyz[1]
    z = xyz[2]
    x = x/z
    y = y/z
    return x, y

def translate_z(xyz, dz):
    x = xyz[0]
    y = xyz[1]
    z = xyz[2]
    z = z + dz
    return x, y, z

def rotate_xz(x, y, z, angle):
    c = math.cos(angle)
    s = math.sin(angle)
    rx = (x * c) - (z * s)
    y = y
    rz = (x * s) + (z * c)
    return rx, y, rz

points = [
   (0.25, 0.25, 0.25),
   (-0.25, 0.25, 0.25),
   (-0.25, -0.25, 0.25),
   (0.25, -0.25, 0.25),

   (0.25, 0.25, -0.25),
   (-0.25, 0.25, -0.25),
   (-0.25, -0.25, -0.25),
   (0.25, -0.25, -0.25),
]

faces = [
   [0, 1, 2, 3],
   [4, 5, 6, 7],
]

dz = 1
angle = 0

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill("black")

  # RENDER GRAPHICS BELOW
  dt = 1 / FPS
  # dz += 1 * dt
  angle += math.pi * dt #

  for coords in points: 
    x = coords[0] 
    y = coords[1] 
    z = coords[2] 
    point(screen_coordinates(project(translate_z(rotate_xz(x, y, z, angle), dz)))) 

  '''
  for f in range(len(faces)):
    for i in f:
        a = points[f[i]]
        b = points[f[(i + 1) % len(f)]]
        point(screen_coordinates(project(translate_z(rotate_xz(x, y, z, angle), dz)))) 
        point(screen_coordinates(project(translate_z(rotate_xz(x, y, z, angle), dz))))
  '''

  pygame.display.flip()

  clock.tick(FPS)

pygame.quit()