person = {'name':'egoing', 'address':'Seoul', 'interest':'Web'}
print(person['name'])

for k in person:
   print(k, person[k])

persons = [
    {'name':'egoing', 'address':'Seoul', 'interest':'Web'},
    {'name':'basta', 'address':'Seoul', 'interest':'IOT'},
    {'name':'blackdew', 'address':'Tongyeong', 'interest':'ML'}
]

print('==== persons ====')
for k in persons:
    for m in k:
        print(m, ':', k[m])
    print('-----------')