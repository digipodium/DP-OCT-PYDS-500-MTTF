class Cat:
    name = ""
    age = 0
    fur_color = ""
    breed = ""
    
    def eat(self):
        print("Cat is eating!")
    
    def sleep(self):
        print("Cat is sleeping!")

# creating objects
tom = Cat()
snow = Cat()

# updating attributes
tom.name = "Tom"
tom.age = 3
tom.fur_color = 'gray'
tom.breed = 'City Cat'
snow.name = 'Snowbell'
snow.age = 5
snow.fur_color = 'white'
snow.breed = 'Persian'

# calling methods
tom.eat()
snow.sleep()
tom.sleep()

# displaying attributes
print(tom.name, tom.age, tom.fur_color, tom.breed)
print(snow.name, snow.age, snow.fur_color, snow.breed)