def selection_sort(arr):
    """
    Реализует алгоритм сортировки выбором.

    :param arr: Список чисел для сортировки.
    :return: Отсортированный список.
    """
    n = len(arr)
    for i in range(n):
        # Ищем индекс минимального элемента в оставшейся части массива
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Обмениваем текущий элемент с найденным минимальным
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Пример использования:
unsorted_list = [64, 25, 12, 22, 11]
sorted_list = selection_sort(unsorted_list)
print("Отсортированный список:", sorted_list)

participants = [("Alice", 34), ("Bob", 29), ("Charlie", 30), ("Dave", 25)]
# Сортировка по времени (второй элемент кортежа)
participants.sort(key=lambda x: x[1])  # Можно использовать selection_sort
print(participants)
