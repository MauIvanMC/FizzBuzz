def fizzbuzz():
    for i in range (1,301):
        if i % 3 ==0 and i % 5 == 0:
            print(f"El numero {i} es multiplo de 3 y 5 'FizzBuzz'")
        elif i % 3 == 0:
            print(f"El numero {i} es multiplo de 3 'Fizz'")
        elif i % 5 == 0:
            print(f"El numero {i} es multiplo de 5 ''Buzz")
        else:
            print(i)

fizzbuzz()