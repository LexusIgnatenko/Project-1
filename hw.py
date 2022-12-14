documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
    }


def add_doc():
    shelfff = input('Введите номер полки где будет лежать документ: ') 
    type = input('Введите тип документа: ')
    number = input('Введите номер документа: ')
    name = input('Введите название документа: ')
    doc = {'type': type, 'number': number, 'name': name}
    documents.append(doc)
    directories[shelfff].append(doc['number'])
    print ('Документ добавлен')


 

def get_list(documents):
    for doc in documents:
        print(doc['type'], doc['number'], doc['name'])

def number_doc(documents):
    nomer = input("Введите номер документа: ")
    for numbers in documents:
        if numbers["number"] == nomer:
            return numbers["name"]
    return 'Такого номера нет'

def shelf(dirs):
    nomer = input("Введите номер документа: ")
    for k,v in dirs.items():
        if nomer in v:
            return f'Документ находится на {k} полке'
    return 'Такого номера нет.'

def main(): 
    while True:
        command = input('Введите команду. a - чтобы добавить документ; g - чтобы получить список всех документов; n - чтобы получить имя документа по номеру; s - чтобы получить номер полки на которой лежит документ, q - чтобы выйти:  ')
        if command == 'a':
            add_doc()
            wanna = input('Хотите посмотреть все документы? ')
            if wanna == 'yes':
                print(documents)
                print(directories)
            else:
                print('See ya!')
                break
            


        if command == 'g':
            get_list(documents)

        if command == 'n':
            print(number_doc(documents))
        
        if command == 's':
            print(shelf(directories))
        if command == 'q':
            print('See ya!')
            break

main()
