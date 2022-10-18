//You can use this code as guidance but DO NOT COPY/PASTE IT into your proyect, this code has copyrights

class Rectangle:
  
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self,x):
    self.width = x

  def set_height(self,x):
    self.height = x

  def get_area(self):
    return(self.width*self.height)
    
  def get_perimeter(self):
    return(self.width*2 + self.height*2)
    
  def get_diagonal(self):
    return((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    if self.width >=50 or self.height >=50:
      return("Too big for picture.")
    else:
      return(("*"*self.width+ "\n")*self.height)
    
  def get_amount_inside(self, shape):
    return((self.width//shape.width)*(self.height//shape.height))

  def __str__(self):
    return ('Rectangle(width={}, height={})'.format(self.width,self.height))

class Square(Rectangle):
  
  def __init__(self, side):
    
    self.side = side
    self.width = side
    self.height = side
    
  def set_width(self, x):
    self.set_side(x)

  def set_heigth(self, x):
    self.set_side(x)
    
  def set_side(self, side):
    self.side = side

  def __str__(self):
    return ("Square(side={})".format(self.side))

  def get_picture(self):
    return(("*"*self.side+ "\n")*self.side)
    
    
rect = shape_calculator.Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
