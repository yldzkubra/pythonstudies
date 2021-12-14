def faktöriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktöriyel(n-1)

x=int(input("sayıyı giriniz:"))
print(faktöriyel(x))

        
        

