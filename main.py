from cookbook import read_cook_book, get_shop_list_by_dishes, merge_files_sorted_by_line_count
import json

if __name__ == '__main__':
    # Задача 1
    cook_book = read_cook_book('recipes.txt')
    print('--- Задача 1: cook_book ---')
    print(json.dumps(cook_book, ensure_ascii=False, indent=2))

    # Задача 2
    shop_list = get_shop_list_by_dishes(
        cook_book,
        ['Запеченный картофель', 'Омлет'],
        2
    )
    print('\n--- Задача 2: shop_list ---')
    print(json.dumps(shop_list, ensure_ascii=False, indent=2))

    # Задача 3
    files_to_merge = ['1.txt', '2.txt']
    merge_files_sorted_by_line_count(files_to_merge, 'merged_output.txt')
    print('\n--- Задача 3 ---')
    print('Файл merged_output.txt создан.')
