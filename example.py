p_x=int(input("x  kordinatlarını giriniz"))
p_y=int(input("y kordinatlarını giriniz"))
triangle=[[1,1],[2,5],[5,4]]

b_x=triangle[1][0]-triangle[0][0]
c_x=triangle[2][0]-triangle[0][0]
b_y=triangle[1][1]-triangle[0][1]
c_y=triangle[2][1]-triangle[0][1]
x=p_x-triangle[0][0]
y=p_y - triangle[0][1]

d=b_x*c_y - c_x*b_y
Wa=(x*(b_y-c_y)+y*(c_x-b_x)+b_x*c_y-c_x*b_y)/d
Wb=(x*c_y-y*c_x)/d
Wc=(y*b_x-x*b_y)/d

if Wa>0 and Wa<1 :
    if Wb>0 and Wb<1:
        if Wc>0 and Wc<1:
            print("girilen nokta alan sınırları içerisindedir")
        else:
            print("girilen nokta alan sınırlı içerisinde değildir")
    else:
            print("girilen nokta alan sınırlı içerisinde değildir")
else:
            print("girilen nokta alan sınırlı içerisinde değildir")
