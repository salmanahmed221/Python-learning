class Human:
    def eating(self, food: str) -> None:
        print(f"Human is eating {food}")


obj121: Human = Human()
obj121.eating("Biryani")
print(dir(obj121))


class Human1(object):
    def eating(self, food: str) -> None:
        print(f"Human is eating {food}")


print(dir(object))

obj211: Human1 = Human1()
obj211.eating("Biryani")
print(dir(obj211))
