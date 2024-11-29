def quicksort(arr):
    """
    Выполняет быструю сортировку массива.

    :param arr: Список чисел, который нужно отсортировать.
    :return: Новый список, отсортированный в порядке возрастания.
    """
    # Базовый случай: пустой массив или массив с одним элементом уже отсортированы
    if len(arr) <= 1:
        return arr

    # Выбор опорного элемента (например, среднего элемента)
    pivot = arr[len(arr) // 2]

    # Разделение массива на три части: меньше pivot, равные pivot, больше pivot
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    # Рекурсивно сортируем части "less" и "greater", затем объединяем
    return quicksort(less) + equal + quicksort(greater)

# Пример использования:
unsorted_list = [-25, 28, 103, -78, 56, 99, 13, -8, 3, 1, 7, 0, 10, 2]
sorted_list = quicksort(unsorted_list)
print("Отсортированный список:", sorted_list)
