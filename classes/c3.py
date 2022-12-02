import random
# class subclass(super_class)
class MyList(list): # inherits from list
    
    def shuffle(self):
        random.shuffle(self)
    
    def get_random(self):
        return random.choice(self)


a = MyList([12, 121, 3,1,2,4,5,1,2,5])
a.sort()
print(a)
a.shuffle()
print(a)
print("random item from list = ",a.get_random())

