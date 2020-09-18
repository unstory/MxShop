#coding=utf8

'''
题目描述：
一个芬兰人进了一个房间，房间有一排椅子，椅子上有一些人坐在，还剩一些空位，他要选择一个座位坐下，
这个位子要尽可能远离已经坐着的人，请给出算法，自行定义数据结构和输入输出
解题思路：
椅子按顺序排列(从左到右排列)，可以抽象成列表(list)，列表中1代表椅子上有人坐，0代表椅子上没人坐
尽可能远离已经坐着的人，就是要离[最近的人] 的 [距离尽可能大]
分两种情况考虑：
1.若最前面的位置没人坐，则距离是离右边第一个有人坐的位置的距离；若最后面的位置没人坐，则距离是离最后一个有人坐的椅子的距离
2. 若选择的座位的两边都有人坐，则距离是离两边座位最近的距离
'''
# 两个人的中间位置
# 初始位置没有人
# 最后面的位置没有人


def getSeatIndex(input_list):
    '''
    获取有人坐的椅子的下标
    param:
    input_list: list, 输入的数据，椅子的状态，1代表有人坐，0代表没人坐
    return:
    index_list: list, 有人坐的椅子的下标的列表
    '''
    index_list = []
    for i in range(len(input_list)):
        if input_list[i] == 1:
            index_list.append(i)
    return index_list

def getMaxIndexDistance(index_list, input_len):
    '''
    获取最大距离的下标和最大距离
    param
    index_list：list, 所有有人坐的椅子的下标
    input_len: int, 总共的椅子数目
    return:
    index->int：最大距离的下标, distance->int：最大距离
    '''
    max_distance = -1
    max_index = -1
    if not index_list:    # 没有人坐
        return max_index, max_distance
    
    if len(index_list) == input_len:  # 坐满人
        return max_index, max_distance
    
    if len(index_list) == 1:  # 只有一个人坐，选最左边或者最右边的座位
        if index_list[0] - 0 >= input_len - index_list[0]:
            return 0, index_list[0] - 0
        else:
            return input_len - 1, input_len - 1 - index_list[0]
        
    if index_list[0] != 0:   # 第一个位置没人坐
        max_distance = index_list[0]
        max_index = 0    
        
    for i in range(1, len(index_list) - 1):  # 第二个位置到倒数第二个位置
        tmp_index = (index_list[i] - index_list[i - 1]) // 2  # 取两个座位的中间位置
        tmp_distance =  min(tmp_index - index_list[i - 1], index_list[i] - tmp_index)  # 取两个距离中的最小值
        if tmp_distance > max_distance:
            max_index = tmp_index
            max_distance = tmp_distance
            
    if index_list[-1] != input_len - 1:  # 最后的位置没人坐
        tmp_index = index_list[-1]
        tmp_distance = input_len - 1 - index_list[-1]
        if tmp_distance > max_distance:
            max_index = tmp_index
            max_distance = tmp_distance
    else:                               # 最后的位置有人坐
        tmp_index = (index_list[-1] - index_list[-2]) // 2  # 取两个座位的中间位置
        tmp_distance =  min(tmp_index - index_list[-2], index_list[-1] - tmp_index)       
        if tmp_distance > max_distance:
            max_index = tmp_index
            max_distance = tmp_distance    
    return max_index, max_distance

def main():
    input_list = [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0]  # 1代表有人坐，0代表没人坐
    index_list = getSeatIndex(input_list)
    input_len = len(input_list)
    index, distance = getMaxIndexDistance(index_list, input_len)   
    print(f"the choose of seat index is: {index}, max distance is: {distance}")

    input_list = []  # 1代表有人坐，0代表没人坐
    index_list = getSeatIndex(input_list)
    input_len = len(input_list)
    index, distance = getMaxIndexDistance(index_list, input_len)   
    print(f"the choose of seat index is: {index}, max distance is: {distance}")
    
    input_list = [1, 1, 1]  # 1代表有人坐，0代表没人坐
    index_list = getSeatIndex(input_list)
    input_len = len(input_list)
    index, distance = getMaxIndexDistance(index_list, input_len)   
    print(f"the choose of seat index is: {index}, max distance is: {distance}")
   
    input_list = [1, 0, 0, 1]  # 1代表有人坐，0代表没人坐
    index_list = getSeatIndex(input_list)
    input_len = len(input_list)
    index, distance = getMaxIndexDistance(index_list, input_len)   
    print(f"the choose of seat index is: {index}, max distance is: {distance}") 
    
    input_list = [1, 0, 0, 1, 0, 0, 0, 1]  # 1代表有人坐，0代表没人坐
    index_list = getSeatIndex(input_list)
    input_len = len(input_list)
    index, distance = getMaxIndexDistance(index_list, input_len)   
    print(f"the choose of seat index is: {index}, max distance is: {distance}") 
    
if __name__ == "__main__":
    main()
    