# Equation Solver - Started in 2021 in Blida
# To help my classmates solve math
import math
print("=== حل معادلة من الدرجة الثانية ax² + bx + c = 0 ===")
a = float(input("ادخل a: "))
b = float(input("ادخل b: "))
c = float(input("ادخل c: "))
delta = b*b - 4*a*c
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"الحلان هما: x1 = {x1} و x2 = {x2}")
elif delta == 0:
    x = -b / (2*a)
    print(f"حل واحد: x = {x}")
else:
    print("لا يوجد حل حقيقي - Delta سالب")
