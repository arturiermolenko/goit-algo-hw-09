# goit-algo-hw-09
### Порівняння ефективності жадібного алгоритму та алгоритму динамічного програмування:
#### Часова складність:

Жадібний алгоритм (find_coins_greedy): O(n), де n — кількість номіналів монет. Швидкий, працює за фіксований час.\
Динамічне програмування (find_min_coins): O(value * n), де value — сума. Повільніше через перебір можливих варіантів для кожної суми.

#### Продуктивність:

Жадібний алгоритм: Швидко знаходить рішення, але не завжди оптимальне, якщо набір монет не підходить.\
Динамічне програмування: Завжди знаходить оптимальне рішення, але може бути повільним для великих сум.

#### Підсумок:

Жадібний: Швидкий і ефективний для наборів монет, де завжди можна вибрати найбільший номінал.\
Динамічний: Гарантує оптимальне рішення, але менш ефективний для великих сум через складність перебору.