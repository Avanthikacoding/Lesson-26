"""Write a program to return - 1. zipped list from two lists 2. elements of two lists zipped together, but 2nd list in reverse order 3. elements of two lists zipped into a dictionary"""
s1 = [5,15,25]
s2 = ["Ava" , "Avi" , "Avanthika"]
s3 = list(zip (s1 , s2))
print(s3)

list5 = [2,7,0,1,55]
list10 = [445,335,555,657,879]
result = list10[::-1]
print(result)
result5 = zip(list5 , result)
#print(result5)
for x,y in list (result5):
    print(x,y)

list15 = [7,6,5,0,8]
list20 = ["hi" , "bye" , "hey" , "yh" , "ok"]
result100 = {list20:list15 for list20,list15 in zip(list20,list15)}
print(result100)
