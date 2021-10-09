import math

class Rectangle:
  def __init__(self,width,height):
    self.width = width
    self.height = height

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self,width):
    self.width= width

  def set_height(self,height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    pic = ''
    if self.height > 50 or self.width > 50:
      return "Too big for picture."
    else:
      for i in range(self.height):
        pic += '*' * self.width + '\n'
      return (pic)

  def get_amount_inside(self, shape):
    return math.floor(self.width / shape.width) * math.floor(self.height / shape.height)

class Square(Rectangle):
  def __init__(self,side):
    self.side = side
    self.width = side
    self.height = side
    
  def set_side(self,side):
    self.side = side
    self.width = side
    self.height = side

  def __str__(self):
    return f"Square(side={self.width})"