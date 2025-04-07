n = int(input())
occured =set()
def squareSum(n):
    return sum(int(i)**2 for i in str(n))
def isHappy(n):
    flag = True
    while squareSum(n)!=1 :
        occured.add(n)
        n = squareSum(n)
        if n in occured:
            flag=False
            break
    if flag:
        return True
    else:
        return False
# n = int(input())
print(isHappy(n))



