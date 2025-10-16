# num = 12%10
# num2 = 12/10
# print(num) == 2
# print(num2) == 1
# value = 12
def sumaNum(a):
    if a < 10:
        return a
    return sumaNum(a//10) + sumaNum(a%10)
print(sumaNum(1234567891011121314151617181920))
