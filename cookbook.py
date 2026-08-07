def parse_recipe_file(file_path: str) -> dict:
    cook_book = {}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден.")
        return cook_book
    
    i = 0
    while i < len(lines):
        dish_name = lines[i]
        i += 1
        
        if i >= len(lines):
            break
        
        try:
            ingredients_count = int(lines[i])
        except ValueError:
            print(f"Ошибка: ожидалось число ингредиентов для '{dish_name}'")
            i += 1
            continue
        i += 1
        
        ingredients = []
        for _ in range(ingredients_count):
            if i >= len(lines):
                break
            
            parts = lines[i].split(' | ')
            if len(parts) == 3:
                ingredients.append({
                    'ingredient_name': parts[0],
                    'quantity': int(parts[1]),
                    'measure': parts[2]
                })
            i += 1
        
        if ingredients:
            cook_book[dish_name] = ingredients
    
    return cook_book


def get_shop_list_by_dishes(dishes: list, person_count: int, cook_book: dict) -> dict:
    shop_list = {}
    
    for dish in dishes:
        if dish not in cook_book:
            print(f"Предупреждение: блюдо '{dish}' не найдено в cook_book")
            continue
        
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']
            
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += quantity
            else:
                shop_list[ingredient_name] = {
                    'measure': measure,
                    'quantity': quantity
                }
    
    return shop_list