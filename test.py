"""gave_list = [50, 11, 13, 7, 15, 18, 9, 20, 12, 10, 8, 16, 14, 17, 19, 11, 13, 7, 15, 18, 9, 20, 12, 10, 8, 16, 14, 17, 19,5,3,2]

using_list = gave_list

def main(list,max):
    final_list = []
    sum=0
    j=0
    for i in range(0,len(list)):
        if(sum+list[i]<max):
            sum=sum+list[i]
            final_list[j]=list[i]
            j+=1    
    print(final_list)


def list_sort(list):
    #This function will sort the list
    gave_list = list
    returning_list = []

    while len(gave_list) > 0:
        biggest = gave_list[0]
        for i in range(0,len(gave_list)):
            if gave_list[i] > biggest:
                biggest = gave_list[i]
        returning_list.append(biggest)
        gave_list.remove(biggest)
        
    return returning_list

def exact_sum(list, sum):
    #This function will check if the sum of the list is equal to the sum
    list_sum = 0
    for i in list:
        list_sum += i
    if list_sum < sum:
        return -1
    elif list_sum == sum:
        return 0
    else :
        return 1
"""
    

def backpack_recursive(list, max_weight, current_weight, current_value, current_list):
    #This function will find the best solution
    if current_weight == max_weight:
        return current_value
    elif current_weight > max_weight:
        return 0
    else:
        for i in range(0, len(list)):
            if current_weight + list[i] <= max_weight:
                current_weight += list[i]
                current_value += list[i]
                current_list.append(list[i])
                backpack_recursive(list, max_weight, current_weight, current_value, current_list)
                current_weight -= list[i]
                current_value -= list[i]
                current_list.remove(list[i])
            else:
                continue
        return current_value


def backpack_dynamic(list, max_weight):
    #This function will find the best solution
    current_weight = 0
    current_value = 0
    current_list = []
    for i in range(0, len(list)):
        if current_weight + list[i] <= max_weight:
            current_weight += list[i]
            current_value += list[i]
            current_list.append(list[i])
        else:
            continue
    return current_value

gave_list = [50, 11, 13, 7, 15, 18, 9, 20, 12, 10, 8, 16, 14, 17, 19, 11, 13, 7, 15, 18, 9, 20, 12, 10, 8, 16, 14, 17, 19,5,3,2]

using_list = gave_list

max_weight = int(input("Enter the maximum weight: "))
