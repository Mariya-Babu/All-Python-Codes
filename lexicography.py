#Function to compare the given string in Dictonary order 
def compare(str1,str2):
    for i in range(len(str1)):
        if(str1[i]==str2[i]):
            continue
        elif(str1[i]<str2[i]):
            return 1
        elif(str1[i]>str2[i]):
            return 0
l = list()
n = int(input("Enter how  many strings you want compare : "))
# Taking the strings from the user 
for i in range(n):
    str = input("Enter string : ")
    l.append(str)
# Sorting the given strings in Dictonary order 
for i in range(n-1):
    for j in range(i+1,n):
        str1 = l[i]
        str2 = l[j]
        val=compare(str1,str2)
        if(val!=1):
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
print("After sorting the strings  ")
for i in range(n):
    print(l[i])

