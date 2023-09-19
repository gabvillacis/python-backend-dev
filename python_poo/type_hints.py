a: int = 3
b: float = 3.14
c: str = 'abc'
d: bool = False

print(a)
a = "tres"
print(a)

def add_numbers(num1: int, num2: int) -> None:
    print(num1 + num2)
    
add_numbers(5, 3)
add_numbers("hola", "mundo")

def substract_numbers(num1: int, num2: int) -> int:
    return num1 - num2

result = substract_numbers(50, 5)
print(result)

def multiplicar(n1: float, n2: float) -> float:
    return n1 * n2

result = multiplicar(5, 3)
print(result)
