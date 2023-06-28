#function to convert the given string into relevant keyboard mobile number 
def str_num(l,str):
    n = len(str)
    lst = list()
    val = 0
    for i in range(n):
        pos = ord(str[i])-ord('A')
        lst.append(l[pos])
    for i in range(n):
        print(lst[i],end=" ")
l = ["2","22","222","3","33","333","4","44","444","5","55","555","6","66","666",\
"7","77","777","8","88","888","9","99","999","9999"]
str = input("Enter a string : ")
str_num(l,str)