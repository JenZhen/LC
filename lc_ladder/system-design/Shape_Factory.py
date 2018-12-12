#!/usr/local/bin/python3

# https://www.lintcode.com/problem/shape-factory/description?_from=ladder&&fromId=8
# Example
# 工厂模式是一种常见的设计模式。实现一个形状工厂 ShapeFactory 来创建不同的形状类。这里我们假设只有三角形，正方形和矩形三种形状。
#
# 样例
# ShapeFactory sf = new ShapeFactory();
# Shape shape = sf.getShape("Square");
# shape.draw();
# >>  ----
# >> |    |
# >> |    |
# >>  ----
#
# shape = sf.getShape("Triangle");
# shape.draw();
# >>   /\
# >>  /  \
# >> /____\
#
# shape = sf.getShape("Rectangle");
# shape.draw();
# >>  ----
# >> |    |
# >>  ----


"""
Solution:

Corner cases:
"""

"""
Your object will be instantiated and called as such:
sf = ShapeFactory()
shape = sf.getShape(shapeType)
shape.draw()
"""
class Shape:
    def draw(self):
        raise NotImplementedError('This method should have implemented.')

class Triangle(Shape):
    # Write your code here
    def draw(self):
        print("  /\\")
        print(" /  \\")
        print("/____\\")

class Rectangle(Shape):
    # Write your code here
    def draw(self):
        print(" ----")
        print("|    |")
        print(" ----")


class Square(Shape):
    # Write your code here
    def draw(self):
        print(" ----")
        print("|    |")
        print("|    |")
        print(" ----")


class ShapeFactory:
    # @param {string} shapeType a string
    # @return {Shape} Get object of type Shape
    def getShape(self, shapeType):
        # Write your code here
        if shapeType == "Triangle":
            return Triangle()
        elif shapeType == "Rectangle":
            return Rectangle()
        elif shapeType == "Square":
            return Square()
        else:
            return None

# Test Cases
if __name__ == "__main__":
    solution = Solution()
