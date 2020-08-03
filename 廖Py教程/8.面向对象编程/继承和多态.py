'''
例子一
Animal父亲
DOg和Cat儿子

父亲啥都有
儿子啥都没有
'''
# class Animal(object):
#     def run(self):
#         print('Animal is running...')

# class Dog(Animal):
#     pass

# class Cat(Animal):
#     pass

# dog=Dog()
# dog.run()

# cat=Cat()
# cat.run()

'''
例子二
Animal父亲
DOg和Cat儿子

父亲啥都有
儿子也有

Dog可以看成Animal，但Animal不可以看成Dog。


'''
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')
   

class Cat(Animal):
    def run(self):
        print('Cat is running...')
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

dog=Dog()
dog.run()

cat=Cat()
cat.run()

def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())