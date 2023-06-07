import json
dict2 = {'d': 6, 'c': 4}
with open('example_2.json') as json_file:
    dictdump = json.load(json_file)

    print(dictdump['book'][1])
    print(type(dictdump))
    print(dictdump)