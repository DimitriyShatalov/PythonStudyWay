# 5.Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Формула расстояния между двумя точками A(xa, ya) и B(xb, yb) на плоскости: 

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

# x1, y1, x2, y2 = map(int, input().split())
print((((x2 - x1)**2) + ((y2 - y1)**2))**0.5)