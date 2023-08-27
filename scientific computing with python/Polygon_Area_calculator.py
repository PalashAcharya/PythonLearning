class Rectangle:

  def __init__(self, width=0, height=0):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, h):
    self.height = h

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return ((self.width**2 + self.height**2)**.5)

  def get_picture(self):
    if (self.width > 50 or self.height > 50):
      return f"Too big for picture."
    else:
      picture_string1 = "*"
      picture_string = ""
      for i in range(self.width - 1):
        picture_string1 = picture_string1 + "*"
      for j in range(int(self.height)):
        picture_string = picture_string + picture_string1 + "\n"
    return picture_string

  def get_amount_inside(self, obj):
    res = self.get_area() // obj.get_area()
    return res

  def __repr__(self):
    return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):

  def __init__(self, length):
    self.height = length
    self.width = length

  def set_side(self, length):
    self.width = length
    self.height = self.width

  def __repr__(self):
    return f"Square(side={self.width})"

obj1 = Rectangle(8,16)
obj2 = Rectangle(4,4)
print(obj1.get_picture())