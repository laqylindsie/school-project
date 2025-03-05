import random
def get_random_python_code():
  # Generate a random number between 1 and 5
  num = random.randint(1, 5)

  # Based on the number, return a different piece of code
  if num == 1:
    return "print('Hello, World!')"
  elif num == 2:
    return "for i in range(5): print(i)"
  elif num == 3:
    return "numbers = [1, 2, 3, 4, 5]; for n in numbers: print(n)"
  elif num == 4:
    return "def greet(name): print('Hello, ' + name + '!')"
  else:
    return "greet('Alice')"
