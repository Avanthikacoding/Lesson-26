numbers1 = [1,3,5,7,9]
numbers2 = [2,4,6,8,0]
result = map(lambda x,y: x + y , numbers1 , numbers2)
print(list(result))

num1 = [2,4,7,9,5,4]
def square(n):
    return n*n
result1 = map(square , num1)
print(list(result1))