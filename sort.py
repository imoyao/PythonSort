#coding=utf-8
import random

def bubbleSort(sortList):
    '''冒泡排序'''
    for num in range(len(sortList)-1, 0, -1):
        for i in range(num):
            if sortList[i] > sortList[i + 1]:
                sortList[i], sortList[i + 1] = sortList[i + 1], sortList[i]
    return sortList

def selectSort(sortList):
    '''选择排序'''
    for index in range(len(sortList) - 1, 0, -1):
        position = 0
        for i in range(1, index + 1):
            if sortList[i] > sortList[position]:
                position = i
        sortList[position], sortList[index] = sortList[index], sortList[position]
    return sortList

def insertSort(sortList):
    '''插入排序'''
    for index in range(1, len(sortList)):
        position = index
        temp = sortList[position]
        while position > 0 and sortList[position - 1] >= temp:
            sortList[position] = sortList[position - 1]
            position = position - 1
        sortList[position] = temp
    return sortList

def quickSort(sortList, low, high):
    '''快速排序（使用迭代思想）'''
    if low < high:
        pos = findPos(sortList, low, high)
        quickSort(sortList, low, pos - 1)
        quickSort(sortList, pos + 1, high)
    return sortList

def findPos(sortList, left, right):
    '''找到分治点'''
    temp = sortList[left]
    while left < right:   
        if left < right and sortList[right] >= temp:
            right -= 1
        sortList[left] = sortList[right]
        if left < right and sortList[left] <= temp:
            left += 1
        sortList[right] = sortList[left]
    sortList[left] = temp
    return left

# def randList():
#     '''生成长度为100的1000以内随机数列'''
#     numList = []
#     for i in range(100):
#         num = random.randint(1, 1000)
#         numList.append(num)
#     return numList

# result = quickSort(randList(), 0, len(randList()) - 1)
# print (result)
if __name__ == '__main__':
    # 定义排序列表
    sortList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # 冒泡排序
    bubbleSort(sortList)
    # 选择排序
    selectSort(sortList)
    # 插入排序
    insertSort(sortList)
    # 快速排序
    quickSort(sortList,0, len(sortList)-1)
    print(sortList)