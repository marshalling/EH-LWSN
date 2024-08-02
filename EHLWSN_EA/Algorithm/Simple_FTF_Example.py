from pylab import *
import math

'''
Simple Euclidean shortest path solution;
This solution is only for reference to understand 
the "Euclidean shortest path" energy allocation solution,
 but it is more complex than FTF.
'''


def single_opt_t(data):
    ls = []
    for i in range(len(data)):
        sum = 0
        for j in range(0, i + 1):
            sum += data[j]
        ls.append(sum / (i + 1))
    return min(ls)


def update_r(data, es):
    temp = data[0] + data[1] - es
    del (data[0])
    data[0] = temp
    return data


def single_opt_list(data, B):
    opt_list = []
    for i in range(len(data) - 1):
        es = single_opt_t(data)
        if data[0] - es > B:
            es = data[0] - B
        opt_list.append(es)
        if data[0] - es > B:
            es = data[0] - B
        data = update_r(data, es)
    opt_list.append(data[0])
    return opt_list


if __name__ == '__main__':
    B = 1
    data = [8, 0, 4, 2]
    print(single_opt_list(data, B))
    fair_utility = 0
    for item in single_opt_list(data, B):
        fair_utility = fair_utility + math.log(1 + item)
    print("Fail utility:", fair_utility)
