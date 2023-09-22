class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)
    

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)
    
    def get_area(self):
        return self.width * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        if(self.width > 50 or self.height > 50):
            return "Too big for picture."
        
        rectangle_row = ("*" * self.width) + "\n"
        rectangle = rectangle_row * self.height

        return rectangle
    
    def get_amount_inside(self, rectangle):
        if(not isinstance(rectangle, Rectangle)):
            raise TypeError("The argument 'rectangle' should be of type Rectangle or Square")
        
        counter = 0
        y = rectangle.height
        while y <= self.height:
            x = rectangle.width
            while x <= self.width:

                counter += 1

                x += rectangle.width
            y += rectangle.height
        
        return counter


class Square(Rectangle):
    def __init__(self, side):
        self.width = self.height = side


    def __str__(self):
        return "Square(side={})".format(self.width)


    def set_side(self, side):
        self.width = self.height = side

    def set_width(self, width):
        self.width = self.height = width
    
    def set_height(self, height):
        self.height = self.width = height
