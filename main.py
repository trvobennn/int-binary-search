"""
My version of a binary search. Works only for a sorted list of integers.
Includes unit tests that cover most basic cases.
"""


def handle_errors(search_list, value):
    if value not in search_list:
        raise ValueError('value not in array')


def find(search_list, value):
    if len(search_list) == 1 and value in search_list:
        return 0
    handle_errors(search_list, value)
    median_ind = 0
    if len(search_list) > 1:
        median_ind += len(search_list) // 2

        while True:
            search_val = search_list[median_ind]

            if search_val == value:
                return median_ind
            if value == search_list[median_ind + 1]:
                return median_ind + 1
            if value == search_list[median_ind - 1]:
                return median_ind - 1
            if value < search_val:
                median_ind -= median_ind // 2
            if value > search_val:
                median_ind += (len(search_list)-median_ind) // 2



import unittest


class Find_test(unittest.TestCase):
    def test_one_element_list(self):
        self.assertEqual(find([3],3),0)

    def test_three_element_list(self):
        self.assertEqual(find([1,2,4],2),1)

    def test_five_element_list_first(self):
        self.assertEqual(find([2,4,5,6,7],2),0)

    def test_five_element_list_second(self):
        self.assertEqual(find([2,4,5,6,7],4),1)

    def test_five_element_list_third(self):
        self.assertEqual(find([2,4,5,8,9],5),2)

    def test_five_element_list_last(self):
        self.assertEqual(find([2,4,7,9,10],10),4)

    def test_longer_array_1(self):
        self.assertEqual(find([1, 2, 4, 6, 7, 9, 10, 12, 13, 15, 17], 1), 0)

    def test_longer_array_2(self):
        self.assertEqual(find([1, 2, 4, 6, 7, 9, 10, 12, 13, 15, 17], 6), 3)

    def test_longer_array_3(self):
        self.assertEqual(find([1, 2, 4, 6, 7, 9, 10, 12, 13, 15, 17], 10), 6)

    def test_longer_array_4(self):
        self.assertEqual(find([1, 2, 4, 6, 7, 9, 10, 12, 13, 15, 17], 15), 9)

    def test_error_handling(self):
        with self.assertRaises(ValueError) as error1:
            find([2, 4, 5, 7, 8, 10], 3)
        self.assertEqual(type(error1.exception), ValueError)

if True:
    unittest.main()
