def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

# Пример использования
lst = [1, 2, 2, 3, 4, 4, 5]
print(unique_elements(lst))  # [1, 2, 3, 4, 5]