## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## a dog is being defined as an animal
class Dog(Animal):

    def __init__(self, name):
        ## the name of the dog is being defined as a dog and an animal
        self.name = name

## a cat is being defined as an animal
class Cat(Animal):

    def __init__(self, name):
        ## the name of the cat is being defined as a cat and an animal
        self.name = name

## a person is being defined as an object
class Person(object):

    def __init__(self, name):
        ## the name of the cat is being defined as a cat and an animal
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## sets up the Employee is a person isntance
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic? creates an object of Employee/Person with a self applied name
        super(Employee, self).__init__(name)
        ## the name of the salary is being defined as an object
        self.salary = salary

## a Fish is a object
class Fish(object):
    pass

## a Salmon is a Fish
class Salmon(Fish):
    pass

## a Halibut is a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has a pet named satan which is-a Cat
mary.pet = satan

## frank has 120000 Employees
frank = Employee("Frank", 120000)

## frank has a pet rover which is-a Dog
frank.pet = rover

## flipper is a Fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harr is a Halibut
harry = Halibut()