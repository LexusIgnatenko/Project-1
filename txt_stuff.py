with open('recepies.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        recepie_name = i.strip()
        ingredients_count = file.readline()
        ingredients = []
        for p in range(int(ingredients_count)):
            recepie = file.readline().strip().split(' | ')
            product, quantity, word = recepie
            ingredients.append({'product': product, 'quantity': quantity, 'measure': word})
        file.readline()
    cook_book[recepie_name] = ingredients

    
def get_shop_list_by_dishes(person_count, **dishes):
    for p in ingredients:
        if p == dishes:
            quantity = quantity * person_count
            print(dishes)
get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'])
