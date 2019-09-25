class Rectangle():
    def __init__(self, height, width):
        self.height = float(height)
        self.width = float(width)

    def area(self):
        print(f'{self.height * self.width:.2f}')  # 面積を表示(高さ×幅)
        return

    def diagonal(self):
        print(f'{(self.height ** 2 + self.width ** 2) ** 0.5:.2f}')  # 対角線の長さの表示
        return


def main():
    rectangle1 = Rectangle(height=5, width=6)
    rectangle1.area()  # 30.00
    rectangle1.diagonal()  # 7.81

    rectangle2 = Rectangle(height=3, width=3)
    rectangle2.area()  # 9.00
    rectangle2.diagonal()  # 4.24


if __name__ == '__main__':
    main()
