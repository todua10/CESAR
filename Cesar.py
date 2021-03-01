arr1 = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
        'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

arr2 = []
for i in range(len(arr1)):
    arr2.append(arr1[i])


def change_arr2():
    for i in range(number):
        arr2.append(arr2[0])
        arr2.remove(arr2[0])


with open("ввод.txt", "r") as file:
    contents = file.read()
    contents = contents.lower()
    number = int(3)
    contentse = ""
    change_arr2()
    for i in contents:
        trigger = False
        for j in range(len(arr1)):
            if i == arr1[j]:
                contentse += arr2[j]
                trigger = True
        if trigger == False:
            contentse += i
contentse = contentse.title()
with open("вывод.txt", "w") as file:
    file.write(contentse)
