# Уважаемые проверяющие!
# Получилось слишком просто проитерироваться по вложенному списку...
#  Возможно, я что-то сделал не так?!


import types


def flat_generator(list_of_lists):

    for i in list_of_lists:
        for j in i:
            flat_iterator_item = j
            yield flat_iterator_item



def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    # for flat_iterator_item in flat_generator(list_of_lists_1):
    #     print(flat_iterator_item)
    #
    # l = list(flat_generator(list_of_lists_1))
    #
    # print(l)


    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        # print(flat_iterator_item)
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    #
    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
