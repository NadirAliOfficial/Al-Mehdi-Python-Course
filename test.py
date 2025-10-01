# def greet():
#     print("Hello, World")
#     print("Hello, World")
# greet()
# greet()



# def add_numbers(a,b):
#     print(a + b)


# add_numbers(4,7)
# add_numbers(12,6)
# add_numbers(121,60)




# def add_numbers(a, b):
#     return a + b 
# result = add_numbers(3, 5)
# print(result)


# def multiply(a, b, c):
#     return a * b * c 


# result = multiply(2, 3, 4) 
# print(result)


# def greet_user(name, greeting='Hello'): 
#     print(f'{greeting}, {name}!')


# greet_user('Salman')
# greet_user('Ali Babu', 'Hi') 
# greet_user("Ihsan")


# def describe_pet(animal='dog', name='Buddy'):    
#      print(f'I have a {animal} named {name}.') 

# describe_pet(animal='cat', name='Animal')
# describe_pet(animal='snake', name='Insect')
# describe_pet(animal='Lion', name='Animal')
# describe_pet()


# def math_operations(a, b):     
#     return a + b, a - b, a * b 


# sum_, diff, prod = math_operations(10, 5) 
# sum1_, diff1, prod1 = math_operations(12, 19) 


# print(f'Sum: {sum1_}, Difference: {diff1}, Product: {prod1}')
# print(f'Sum: {sum_}, Difference: {diff}, Product: {prod}')


def outer_function():    
    def inner_function():      
        print('This is the inner function.')   
    inner_function()
outer_function()
outer_function()