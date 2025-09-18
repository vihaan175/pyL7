list = ['Apple' , 'Guava' , 'Mango' , 'Banana' , 'Kiwi']

print(list[0])
print(list[-2])
print(list[1:4])
list.append("Lychee")
list.remove("Guava")
print(list)
list.sort()
print(list)
list.pop(1)
print(list)
list.reverse()
print(list)

def test (lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result


students = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]

print("the original list was\n",students)
print("after coverting into dictionary\n",test(students))


