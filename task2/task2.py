import numpy as np


def function(array):
    a = np.transpose(array).tolist()
    a = [sorted(a[i]) if i % 2 == 0 else a[i] for i in range(len(a))]
    a = np.concatenate(a).tolist()
    if len(a) == 1 or len(a) == 2:
        return True
    d = a[1] - a[0]
    past_element = a[0]
    for i in range(1, len(a), 1):
        if a[i] - past_element != d:
            return False
        past_element = a[i]
    return True


array = []
with open('test.txt') as f:
    try:
        for line in f:
            array.append(list(map(int, line.split(', '))))
        print(function(array))
    except(RuntimeError, ValueError):
        print('Exception')
