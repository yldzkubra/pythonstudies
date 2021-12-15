import os

os.chdir("/home/kubra")

metin= open("metin.txt", "r")
text=metin.read()
find=("nisi")
'''
if text.__contains__(find)==True:
    print("{} metninde {} kelimesi bulunmaktadır".format(text,find))
else:
    print("kelime metinde bulunmamaktadır")
'''
text=text.replace("."," ")
text=text.replace(","," ")
textlist=text.split(" ")

if find in textlist :
    print("{} metninde {} kelimesi bulunmaktadır".format(text,find))
else:
    print("kelime metinde bulunmamaktadır")