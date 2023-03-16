#  Здравствуйте, Кирилл!
# Пришлось воспользоваться Вашей наводкой!
# Спасибо!
#  Хотя я и сам в тот момент понял (методом проб и ошибок),
#  что необходима 2-я переменная для обхода по вложенному списку

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.main_list_cursor = 0  # курсор основного списка
        self.nested_list_cursor = -1  # курсор списка вложенного в основной список
        return self

    def __next__(self):

        self.nested_list_cursor += 1
        # увеличиваем nested_list_cursor

        # если во вложенном списке элементы закончились,
        if self.nested_list_cursor == len(self.list_of_list[self.main_list_cursor]):
            self.main_list_cursor += 1
            self.nested_list_cursor = 0
            # то переходи на следующий список увеличив main_list_cursor
            # и обнуляем main_list_cursor


        if self.main_list_cursor == len(self.list_of_list):
            raise StopIteration

        flat_iterator_item = self.list_of_list[self.main_list_cursor][self.nested_list_cursor]
        return flat_iterator_item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    # for flat_iterator_item in FlatIterator(list_of_lists_1):
    #     # print(flat_iterator_item)

    l = list(FlatIterator(list_of_lists_1))

    print(l)


    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
