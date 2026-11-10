class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

rectangle = Rectangle(3, 4)

print(rectangle.width)
print(rectangle.height)

rectangle.width = 5
rectangle.height = 6
print(rectangle.width)
print(rectangle.height)

rectangle.width = -2

del rectangle.width
del rectangle.height

#With @property, I can read and change values the same way I use normal variables: rectangle.width and rectangle.width = 5. With traditional methods, I’d have to write rectangle.get_width() and rectangle.set_width(5), which is longer and more cluttered. @property also keeps the validation logic (like rejecting negative values) hidden inside the class, so the code outside it stays clean. If I want to add checks or formatting later, I don’t need to change any code that already uses rectangle.width.
