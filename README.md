# OD-01-02-03

## 01 - Полиндром
## 02 - Мокирование и тестирование API
## 03 - Сортировка

## 03 Сортировка

### Быстрая сортировка

### Пояснение:
- Базовый случай: Если массив имеет длину 0 или 1, он уже отсортирован, и его можно сразу вернуть.
- Выбор опорного элемента (pivot): Используется элемент в середине списка (arrlen(arr) // 2), но можно использовать первый или последний элемент.
- Разделение:
  - Все элементы меньше pivot идут в список less.
  - Все элементы равные pivot идут в список equal.
  - Все элементы больше pivot идут в список greater.
- Рекурсия: Применяем быструю сортировку к less и greater, а затем объединяем результаты.

## Алгоритм сортировки выбором (selection sort)

### Пошаговый пример:
Для массива 64, 25, 12, 22, 11 алгоритм работает следующим образом:
1. Находим минимальный элемент (11) и меняем его с первым элементом (64).
   - Массив: 11, 25, 12, 22, 64.
2. В оставшейся части 25, 12, 22, 64 находим минимальный (12) и меняем его со вторым элементом (25).
   - Массив: 11, 12, 25, 22, 64.
3. Повторяем шаги до конца.
   - Итоговый массив: 11, 12, 22, 25, 64.

### Практическое использование:
Сортировка выбором редко используется в реальных приложениях из-за сложности O(n^2), что делает её медленной для больших массивов. Однако она может быть полезна в следующих ситуациях:

- Образовательные цели: Алгоритм легко реализовать и понять, что делает его популярным для обучения основам сортировки.
- Сортировка небольших массивов: Когда размер данных невелик, сортировка выбором может быть достаточно быстрой.
- Массивы с ограничениями: Если данные хранятся в структуре, где нельзя использовать другие подходы, например, с ограничением на использование памяти.
- Подготовка данных для оптимизации: Алгоритм может быть использован как первый этап для частичной сортировки перед более сложным алгоритмом.