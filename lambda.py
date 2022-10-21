my_square = lambda x: x*x
my_sum = lambda *args: sum(args)
cube = (lambda x:x*x*x)(4)

numbers = [8, 66, 12, 14, 15, 77, 99, 109, 88, 56, 335, 26, 785]

even_numbers = list(filter(lambda x: x%2 == 0, numbers))
squared_numbers = list(map(lambda x: x*x, numbers))

print(even_numbers)
print(squared_numbers)

def myFunction(num):
    return lambda x: x * num

ten_multiplier = myFunction(10)
print(ten_multiplier(2))