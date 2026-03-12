import TODO
print(TODO.__doc__)

def Cryptic_Number():
    L, R = map(int, input().split())
    list_1=[]
    list_2=[]
    list_3=[]
    for i in range(L,R+1):
        #print("i=",i)
        if i%7==0 and i%5!=0:
            #print(f"{i} is divisible by 7 and not divisible by 5")
            list_1.append(i)
    #print(list_1)
    #CHECK FOR PALINDROME
    for i in list_1:
        if i!=reversed("i"):
            #print(f"{i} is not palindrom")
            list_2.append(i)
    #print(list_2)
    #REMOVING REPEATED DIGITS ELEMENTS
    for i in list_2:
        has_repeated=False
        for digit in str(i):
            if str(i).count(digit)>1:
                has_repeated=True
                break
        if not has_repeated:
            list_3.append(i)
    #print(list_3)
    
    if list_3:
        print(" ".join(map(str,list_3)))
    else:
        print(-1)
                
Cryptic_Number() 

#THIS CODE CAN BE WRITTEN IN THREE LINE BUT FOR NOW I HAVW WRITTEN IT IN THIS WAY

   
