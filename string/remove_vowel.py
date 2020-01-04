# list = [A,B,C,D,E.F.G.H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
string = input("Enter any string to remove all vowels from it: ")
def rem_vowel(string):
    vowels = ("a","e",'i','o','u')
    for i in string.lower():
        if i in vowels:
            string = string.replace(i,"")
    return string
print(rem_vowel(string))