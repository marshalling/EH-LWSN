import math
import mallec
from EHLWSN_EA.Algorithm.Utils.GetData import getData_solar


def single_optimal_mallec(data):
    b_0 = 0
    allocated = []
    alg_mallec = mallec.MallecOptimal(len(data))
    allocated1 = alg_mallec.allocate(data, b_0)
    allocated.extend(data)
    return allocated1


def mallec_global_opt_min(data):
    our_single_opt_e = []
    temp_list = []
    for item in data:
        temp_list.append(single_optimal_mallec(item))
    our_single_opt_e.append(min(temp_list))
    our_global_opt_e = min(our_single_opt_e)
    return our_global_opt_e


def execute(dataset):
    mallec_global_opt_ea_list = []
    for i in range(len(dataset[0]) - 1):
        e = mallec_global_opt_min(dataset)
        # print("1e:", e)
        mallec_global_opt_ea_list.append(e)
        dataset = update_r(dataset, e)
    mallec_global_opt_ea_list.append(mallec_global_opt_min(dataset))
    return mallec_global_opt_ea_list


def update_r(r, e):
    for item in r:
        temp = item[0] + item[1] - e
        del (item[0])
        item[0] = temp
    return r


if __name__ == '__main__':
    dataset = getData_solar()
    # dataset = [[8,0,4,2],[2,6,3,5]]
    mallec_global_opt_ea_list = execute(dataset)
    print(mallec_global_opt_ea_list)
    fair_utility = 0
    for item in mallec_global_opt_ea_list:
        fair_utility = fair_utility + math.log(1 + item)
    print("Fail utility:", fair_utility)

    # 输出能量分配值
    # 将列表中的每个元素转换为字符串
    str_list = [str(item) for item in mallec_global_opt_ea_list]
    # 使用 join() 来连接
    result = ", ".join(str_list)
    with open("result_dataset/mallec_result_energy.txt", "w") as f:
        f.write(", ".join(str_list))  # 将列表用逗号分隔，并写入

    # 输出网络累计效用结果
    T_ours = []
    # 累积值
    T_sum = 0
    # 遍历原始数组
    for num in mallec_global_opt_ea_list:
        T_sum += math.log(1+num)
        T_ours.append(T_sum)
    # 将列表中的每个元素转换为字符串
    T_ours = [str(item) for item in T_ours]
    # 使用 join() 来连接
    result = ", ".join(T_ours)
    with open("result_dataset/mallec_result_utility.txt", "w") as f:
        f.write(", ".join(T_ours))  # 将列表用逗号分隔，并写入


