import random


def binary_search(data,target,star, end):
    if star > end:
       return  False

    med = (star + end) // 2
    
    if data[med] == target:
       return  True

    elif data[med] < target:
       return  binary_search(data,target,med +1 ,end)

    elif data[med] > target:
       return  binary_search(data,target,star,med - 1)


if __name__ == '__main__':
    data = [random.randint(0,100) for i in range(10)]
    data.sort()
    
    print(data)
    
    target = int(input('what number would you like to find? '))
    found = binary_search(data, target, 0, len(data) -1)
    
    print(found)

    
