# 2.Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

asnwer = True

for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            if not (x and y and z) != (not x) or (not y) or (not z):
            
                answer = False
print(answer)