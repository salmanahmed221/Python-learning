# Duck Typing
class Duck:
    def quack(self):
        return "Quack!"


class Person:
    def quack(self):
        return "I'm Quacking Like a Duck!"


def in_the_forest(cake):
    print(cake.quack())


donald: Duck = Duck()
john: Person = Person()
in_the_forest(donald)
in_the_forest(john)
