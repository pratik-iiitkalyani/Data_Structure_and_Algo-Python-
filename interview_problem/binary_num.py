# num = int(input("number:"))
# print(bin(num))

def DecimaltoBinary(num):
    if num>1:
        DecimaltoBinary(num//2)
    print(num%2,end = "")
x = int(input("number:"))
print(DecimaltoBinary(x))