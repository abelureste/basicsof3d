import pygame
import math
from cube import faces, vertices

pygame.init()

game_width = 800
game_height = 800
FPS = 144
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True
font = pygame.font.SysFont("Arial", 20)

def point(xy):
    x, y = xy
    size = 10
    pygame.draw.rect(screen, "blue", (x - size/2, y - size/2, size, size))
    
    return x, y

def line(p1, p2):
   pygame.draw.line(screen, "green", p1, p2)

def screen_coordinates(xy):
    x, y = xy
    x = (x + 1) / 2 * game_width
    y = (1 - (y + 1) / 2) * game_height
    return x, y

def project(xyz):
    x, y, z = xyz
    x = x/z
    y = y/z
    return x, y

def translate_z(xyz, dz):
    x, y, z = xyz
    z = z + dz
    return x, y, z

def rotate_xz(xyz, angle):
    x, y, z = xyz
    c = math.cos(angle)
    s = math.sin(angle)
    rx = (x * c) - (z * s)
    y = y
    rz = (x * s) + (z * c)
    return rx, y, rz

dz = 1
angle = 0

def toggle_grid():
    pygame.draw.line(screen, "#D3D3D3", (400, 0), (400, 800))
    pygame.draw.line(screen, "#D3D3D3", (0, 400), (800, 400))

    screen.blit(font.render('y', True, "#D3D3D3"), (405, -5))
    screen.blit(font.render('-y', True, "#D3D3D3"), (405, 770))
    screen.blit(font.render('x', True, "#D3D3D3"), (785, 375))
    screen.blit(font.render('-x', True, "#D3D3D3"), (5, 375))

grid = False
vertex = False

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_g and grid != True:
        grid = True
      elif event.key == pygame.K_g and grid != False:
        grid = False
      if event.key == pygame.K_v and vertex != True:
        vertex = True
      elif event.key == pygame.K_v and vertex != False:
        vertex = False

  screen.fill("black")  

  screen.blit(font.render('toggle grid: g', True, "#D3D3D3"), (650, 740))
  screen.blit(font.render('toggle vertices: v', True, "#D3D3D3"), (650, 760))

  if(grid == True):
     toggle_grid()

  # RENDER GRAPHICS BELOW
  dt = 1 / FPS
  # dz += 1 * dt
  angle += math.pi * dt

  for f in faces:
    for i in range(len(f)):
        index_a = f[i]
        index_b = f[(i + 1) % len(f)]

        a = vertices[index_a]
        b = vertices[index_b]

        if vertex == True:
          line(point(screen_coordinates(project(translate_z(rotate_xz(a, angle), dz)))),
              point(screen_coordinates(project(translate_z(rotate_xz(b, angle), dz)))))
        else:
          line(screen_coordinates(project(translate_z(rotate_xz(a, angle), dz))),
              screen_coordinates(project(translate_z(rotate_xz(b, angle), dz))))


  pygame.display.flip()

  clock.tick(FPS)

pygame.quit()