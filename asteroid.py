import pygame, random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    else:
      log_event("asteroid_split")
      angle = random.uniform(20, 50)
      angle1 = self.velocity.rotate(angle)
      angle2 = self.velocity.rotate(angle * -1)
      split_radius = self.radius - ASTEROID_MIN_RADIUS
      split1 = Asteroid(self.position.x, self.position.y, split_radius)
      split2 = Asteroid(self.position.x, self.position.y, split_radius)
      split1.velocity = angle1 * 1.2
      split2.velocity = angle2 * 1.2