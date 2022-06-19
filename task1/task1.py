def function(array):
    d = {i: array.count(i) for i in array}
    max_amount = max(d.values())
    result = [k for k, v in d.items() if v == max_amount]
    result.sort()
    return result


# file = input()
with open('task1/test.txt') as f:
    for line in f:
        try:
            array = list(map(int, line.split(', ')))
            print(function(array))
        except (RuntimeError, ValueError):
            print('Exception')
