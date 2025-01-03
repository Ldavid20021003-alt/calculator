import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Nullával való osztás!")
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        raise ValueError("Negatív számból nem lehet gyököt vonni!")
    return math.sqrt(x)

def percentage(x, y): # x százaléka y-nak
    return (x / 100) * y

# Memória funkciók (globális változóval, egyszerûsítve)
memory = 0

def memory_store(x):
    global memory
    memory = x

def memory_add(x):
    global memory
    memory += x

def memory_subtract(x):
    global memory
    memory -= x

def memory_clear():
    global memory
    memory = 0

def memory_recall():
    return memory

# Példa használat (teszteléshez):
if __name__ == "__main__":
    print(add(5, 3))       # 8
    print(divide(10, 2))  # 5.0
    try:
        print(divide(10, 0))
    except ZeroDivisionError as e:
        print(e)           # Nullával való osztás!
    print(square_root(25)) #5.0
    memory_store(10)
    memory_add(5)
    print(memory_recall()) #15
    memory_clear()
    print(memory_recall()) #0