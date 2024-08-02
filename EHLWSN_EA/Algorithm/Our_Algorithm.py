from pylab import *
import math

from EHLWSN_EA.Algorithm import ftf
from EHLWSN_EA.Algorithm.Utils.GetData import getData_solar

#-----------------------
def single_optimal_ftf(data):
    b_min = 0
    b_max = float('inf')
    b_0 = 0
    allocated = []
    alg_ftf = ftf.ftf(b_min, b_max, b_0)
    allocated1 = alg_ftf.allocate(data)
    if len(allocated1) < len(data):
        allocated1.append(data[len(data) - 1])
    allocated.extend(allocated1)
    return allocated[0]


def our_global_opt_min(data):
    our_single_opt_e=[]
    temp_list=[]
    for item in data:
        temp_list.append(single_optimal_ftf(item))
    our_single_opt_e.append(min(temp_list))
    our_global_opt_e=min(our_single_opt_e)
    return our_global_opt_e


def update_r(r, e):
    for item in r:
        temp = item[0] + item[1] - e
        del (item[0])
        item[0] = temp
    return r


def execute(dataset):
    # 首先求出每个节点的最优能量分配序列
    our_global_opt_ea_list = []
    for i in range(len(dataset[0]) - 1):
        e = our_global_opt_min(dataset)
        our_global_opt_ea_list.append(e)
        dataset = update_r(dataset, e)
    our_global_opt_ea_list.append(our_global_opt_min(dataset))
    return our_global_opt_ea_list


if __name__ == '__main__':
    dataset = getData_solar()
    ours_global_opt_ea_list = execute(dataset)
    print(ours_global_opt_ea_list)
    fair_utility = 0
    for item in ours_global_opt_ea_list:
        fair_utility = fair_utility + math.log(1 + item)
    print("Fail utility:", fair_utility)
    print(ours_global_opt_ea_list)

    # 能量结果输出

    # str_energy = [str(item) for item in ours_global_opt_ea_list]
    #
    # # 使用 join() 来连接
    # result = ", ".join(str_energy)
    # with open("result_dataset/ours_result_energy.txt", "w") as f:
    #     f.write(", ".join(str_energy))  # 将列表用逗号分隔，并写入

    # 网络累计效用结果输出
    T_ours = []
    # 累积值
    T_sum = 0
    # 遍历原始数组
    for num in ours_global_opt_ea_list:
        T_sum += math.log(1+num)
        T_ours.append(T_sum)
    # 将列表中的每个元素转换为字符串
    T_ours = [str(item) for item in T_ours]
    # 使用 join() 来连接
    result = ", ".join(T_ours)
    with open("result_dataset/ours_result_utility.txt", "w") as f:
        f.write(", ".join(T_ours))  # 将列表用逗号分隔，并写入
