# flexible parameter in a function
# *args, **kwargs
def mean(*numbers):
    total = 0
    for item in numbers:
        if isinstance(item, (int, float)):
            total += item
    return total / len(numbers)

def report(**marks):
    total_marks = 0
    for k,v in marks.items():
        print(f'{k} got {v} marks')
        total_marks += v
    return total_marks

print(report(ram=90, shyam=80, hari=70))
print(mean(1,2,3,1))
print(mean(1,2,3,4,5,6,7,8,9,10))
print(mean(12,31,2,31,231,3,45,123,1,23,123,12,31,23,1))
print(mean(12,'a',123,'123',123,12))