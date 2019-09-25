class Circle():
    def __init__(self, radius):
        self.radius = radius  # 半径
        self.PI = 3.1415  # 円周率

    # 面積を計算
    def area(self):
        return round(self.radius ** 2 * self.PI, 2)  # 面積 = 半径×半径×円周率

    # 周囲長を計算
    def perimeter(self) -> float:
        return round(self.radius * 2 * self.PI, 2)  # 直径 = 半径×2×円周率


def main():
    # 半径1の円
    circle1 = Circle(radius=1)
    print(circle1.area())  # 3.14
    print(circle1.perimeter())  # 6.28

    # 半径3の円
    circle3 = Circle(radius=3)
    print(circle3.area())  # 28.27
    print(circle3.perimeter())  # 18.85


if __name__ == '__main__':
    main()
