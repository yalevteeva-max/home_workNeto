import os

def read_cook_book(file_path: str) -> dict:
    cook_book = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]

    i = 0
    while i < len(lines):
        dish_name = lines[i]
        i += 1

        if i >= len(lines):
            break

        ingredients_count = int(lines[i])
        i += 1

        ingredients = []
        for _ in range(ingredients_count):
            if i >= len(lines):
                break
            ingredient_line = lines[i]
            i += 1

            parts = [part.strip() for part in ingredient_line.split('|')]
            if len(parts) != 3:
                continue

            ingredient_name, quantity_str, measure = parts
            quantity = int(quantity_str)

            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })

        cook_book[dish_name] = ingredients

    return cook_book


def get_shop_list_by_dishes(cook_book: dict, dishes: list, person_count: int) -> dict:
     shop_list = {}

     for dish in dishes:
        if dish not in cook_book:
            continue

        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']

            if name in shop_list:
                shop_list[name]['quantity'] += quantity
            else:
                shop_list[name] = {
                    'measure': measure,
                    'quantity': quantity
                }

     return shop_list


def merge_files_sorted_by_line_count(file_paths: list, output_path: str) -> None:
    file_info = []

    for path in file_paths:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        line_count = len(lines)
        file_info.append((path, line_count, lines))

    file_info.sort(key=lambda x: x[1])

    with open(output_path, 'w', encoding='utf-8') as out_file:
        for path, line_count, lines in file_info:
            file_name = os.path.basename(path)
            out_file.write(f"{file_name}\n")
            out_file.write(f"{line_count}\n")
            for line in lines:
                out_file.write(line)
