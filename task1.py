from decimal import Decimal

number = Decimal(input("Введите число: "))
result = number.quantize(Decimal(input("Введите точность (0.0001): ")))
print(result)