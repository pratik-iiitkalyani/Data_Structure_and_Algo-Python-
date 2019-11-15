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

print(sorted(list, key = lambda i: i['age']))
