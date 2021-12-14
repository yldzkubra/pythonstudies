x=int(input("sayı giriniz:"))
a=0
while  a <= x :
    a+=1
    remainder= x % a
    if remainder == 0 :
        print("tam böleni:",a)