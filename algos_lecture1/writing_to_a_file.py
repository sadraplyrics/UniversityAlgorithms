# Предположим, что в папке created_&_read_files лежит пустой файл alg_text.txt
# Мы можем открыть его с помощью метода open и сохранить в перменную
# и закрыть методом close(). Ho дучше использовать with open ... тогда файл сам
# тогда файл сам закроется по выходу из блока, а перменные в которые мы сохраняли
# данные оттуда сохранятся на глобал фрейме

with open("created_&_read_files/alg_text.txt", "w") as empty: # открыли файл в блоке with, назвали empty 
    empty.write("I love IIE MSPU!!!!!!!!!!")# написали в файл что-нибудь

# по выходу из блока он закрылся, откроем снова в режиме чтения и проверим

with open("created_&_read_files/alg_text.txt", "r") as empty:  
    text_inside = empty.read()
    print(text_inside)

# Таким же образом можно создавать новые файлы
with open("created_&_read_files/new_file.txt", "w") as new_file:
    new_file.write("And I love IIE MSPU EVEN MORE!!!!")

# это создаст в указанном пути новый файл с названием new_file.txt
with open("created_&_read_files/new_file.txt", "r") as new_file:
    print(new_file.read()) # проверим
 
# добавим новых строчек

with open("created_&_read_files/new_file.txt", "a") as to_append:
    to_append.write("\nON A NEW LINE") # чтобы запись была с новой строк добавим \n в начало

with open("created_&_read_files/new_file.txt", "r") as to_append:
    print(to_append.read()) # проверим


# для того, чтобы программа не выключалась после каждой ошибки
# обработаем исключения

try: # поместим код, который нужно "попробовать" в try блок 
    with open(ошибка, "r+") as new_file:
        try:
            varible = new_file.read()
        except Exception as ex:
            print(ex) # в случае ошибки выведем ее и продлжим выполнение программы

except Exception as ex:
    print(ex)

print("THE END OD THE FILE") # Проверим, что даже с ошибкой доходим до конца