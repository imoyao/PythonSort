# coding=utf-8
import random


class PySort:
    def __init__(self, rand_list=None):
        self.rand_list = rand_list

    @staticmethod
    def random_list(length=100, rand_range=1000):
        """
        产生一个长度为 length ,取值范围为 rand_range 的随机列表
        :param length: int,随机列表长度
        :param rand_range: int,随机数范围
        :return: list,
        """
        return [random.randint(1, rand_range) for _ in range(length)]

    @staticmethod
    def seq_length(seq):
        if seq is not None:
            return len(seq)
        raise Exception('Seq should not be None.')

    def quick_sort(self, _random_seq=None):
        """
        快速排序
        :param _random_seq:
        :return:
        """
        length = len(_random_seq)
        if length <= 1:
            return _random_seq

        cmp_item = _random_seq[0]
        left_seq = []
        right_seq = []
        for item in _random_seq[1:]:
            left_seq.append(item) if item <= cmp_item else right_seq.append(item)
        return self.quick_sort(left_seq) + [cmp_item] + self.quick_sort(right_seq)

    def bubble_sort(self, _random_seq=None):
        """
        冒泡排序
        :param _random_seq:
        :return:
        """
        length = self.seq_length(_random_seq)
        if length <= 1:
            return _random_seq
        for i in range(length - 1):
            swapped = False
            for j in range(length - 1 - i):
                if _random_seq[j] > _random_seq[j + 1]:
                    swapped = True
                    _random_seq[j], _random_seq[j + 1] = _random_seq[j + 1], _random_seq[j]
            while not swapped:
                break
        return _random_seq

    def select_sort(self, _random_seq=None):
        """
        选择排序
        :param _random_seq:
        :return:
        """
        length = self.seq_length(_random_seq)
        if length <= 1:
            return _random_seq
        for i in range(length - 1):
            min_item_index = i
            for j in range(i + 1, length):
                if _random_seq[j] < _random_seq[min_item_index]:
                    min_item_index = j
            _random_seq[min_item_index], _random_seq[i] = _random_seq[i], _random_seq[min_item_index]
        return _random_seq

    def insert_sort(self, _random_seq=None):
        """
        
        :param _random_seq: 
        :return: 
        """
        length = self.seq_length(_random_seq)
        if length <= 1:
            return _random_seq
        for index in range(1, length):
            while index > 0 and _random_seq[index - 1] > _random_seq[index]:
                _random_seq[index - 1], _random_seq[index] = _random_seq[index], _random_seq[index - 1]
                index -= 1
        return _random_seq


if __name__ == '__main__':
    sort = PySort()
    _random_seq = sort.random_list()
    print(f'Before sort list:{_random_seq}')
    i_sorted = sort.insert_sort(_random_seq)
    s_sorted = sort.select_sort(_random_seq)
    b_sorted = sort.bubble_sort(_random_seq)
    q_sorted = sort.quick_sort(_random_seq)
    assert i_sorted == s_sorted == b_sorted == q_sorted
    print(f'After sorted list:{i_sorted}')
