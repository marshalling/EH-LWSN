import math

import ftf
from EHLWSN_EA.Algorithm.Utils.GetData import getData_solar


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
    return allocated


def update_r(r, e):
    temp = r[0] + r[1] - e
    del (r[0])
    r[0] = temp
    return r


def execute(dataset):
    ftf_single_opt_ea_list = []
    for i in range(len(dataset)):
        e_list = single_optimal_ftf(dataset[i])
        ftf_single_opt_ea_list.append(e_list)
    print(ftf_single_opt_ea_list)
    ftf_global_opt_ea_list = []

    # 外层循环遍历每个索引
    for i in range(len(ftf_single_opt_ea_list[0])):
        temp_list = []  # 用于存储当前索引对应的值
        # 内层循环遍历每个子列表
        for sublist in ftf_single_opt_ea_list:
            temp_list.append(sublist[i])  # 将当前索引对应的值添加到临时列表中
        min_value = min(temp_list)  # 找到临时列表中的最小值
        ftf_global_opt_ea_list.append(min_value)  # 将最小值添加到结果列表中
    return ftf_global_opt_ea_list


if __name__ == '__main__':
    dataset = getData_solar()
    # dataset = [6,0,0]
    ftf_global_opt_ea_list = execute(dataset)
    print(ftf_global_opt_ea_list)
    fair_utility=0
    for item in ftf_global_opt_ea_list:
        fair_utility = fair_utility + math.log(1 + item)
    print("Fail utility:", fair_utility)

    # # 输出能量分配值
    # # 将列表中的每个元素转换为字符串
    # str_list = [str(item) for item in ftf_global_opt_ea_list]
    # # 使用 join() 来连接
    # result = ", ".join(str_list)
    # with open("result_dataset/ftf_result_energy.txt", "w") as f:
    #     f.write(", ".join(str_list))  # 将列表用逗号分隔，并写入

    # 输出网络累计效用结果
    T_ours = []
    # 累积值
    T_sum = 0
    # 遍历原始数组
    for num in ftf_global_opt_ea_list:
        T_sum += math.log(1+num)
        T_ours.append(T_sum)
    # 将列表中的每个元素转换为字符串
    T_ours = [str(item) for item in T_ours]
    # 使用 join() 来连接
    result = ", ".join(T_ours)
    with open("result_dataset/ftf_result_utility.txt", "w") as f:
        f.write(", ".join(T_ours))  # 将列表用逗号分隔，并写入

