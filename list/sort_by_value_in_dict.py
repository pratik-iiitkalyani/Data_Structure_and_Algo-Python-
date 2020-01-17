# sort by value of Dictionary in list of Dic

l = [
    {
        "name": "pratik",
        "age": 30
    },
    {
        "name": "raja",
        "age": 16
    },
    {
        "name": "saurabh",
        "age": 20
    }
]

print(sorted(l, key = lambda i: i['age']))

# d = {
#     1 : 2,
#     2 : 1
# }

# print(sorted((v,k) for k,v in d.items()))
