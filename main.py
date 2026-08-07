import os
import pprint
from cookbook import parse_recipe_file, get_shop_list_by_dishes


def get_file_info(file_path: str) -> tuple:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    file_name = os.path.basename(file_path)
    line_count = len(lines)
    content = ''.join(lines)
    
    return file_name, line_count, content


def merge_files(file_paths: list, output_file: str) -> None:
    files_info = []
    
    for file_path in file_paths:
        file_name, line_count, content = get_file_info(file_path)
        files_info.append((file_name, line_count, content))
    
    files_info.sort(key=lambda x: x[1])
    
    with open(output_file, 'w', encoding='utf-8') as output:
        for file_name, line_count, content in files_info:
            output.write(f"{file_name}\n")
            output.write(f"{line_count}\n")
            output.write(content)
            # Добавляем пустую строку между файлами (кроме последнего)
            if file_name != files_info[-1][0]:
                output.write("\n")


def main():
    cook_book = parse_recipe_file('recipes.txt')
    
    print("Задача №1: Словарь cook_book")
    print("-" * 50)
    pprint.pprint(cook_book, width=100, sort_dicts=False)
    print()
    
    dishes = ['Запеченный картофель', 'Омлет']
    person_count = 2
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
    
    print(f"Задача №2: Список покупок для {dishes} на {person_count} персоны")
    print("-" * 50)
    pprint.pprint(shop_list, width=100, sort_dicts=False)
    print()
    
    print("Задача №3: Объединение файлов")
    print("-" * 50)
    
    merge_files(['1.txt', '2.txt'], 'result.txt')
    
    with open('result.txt', 'r', encoding='utf-8') as f:
        print(f.read())


if __name__ == '__main__':
    main()