def potenciacion(a,b):
    if a == 0:
        return 1
    if b == 0:
        return 1
    elif b == 1:
        return a
    return potenciacion(a, b - 1) * a

print(potenciacion(4,2))