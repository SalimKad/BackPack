"""
The BackPack problem can be compared to this new problem :
We have to choose the biggest elements of a list so that their sum is equal to a given number.
"""

gave_list = [50, 11, 13, 7, 15, 18, 9, 20, 12, 10, 8, 16, 14, 17, 19, 11, 13, 7, 15, 18, 9, 20, 12, 10, 8, 16, 14, 17, 19]

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
    print(list_sum)
    if list_sum < sum or list==[]:
        return -1
    elif list_sum == sum:
        return 0
    else :
        return 1

def main():
    #This function will call the other functions
    used_list = list_sort(gave_list)
    final_list = []
    sum_to_reach = int(input("Enter the sum you want to reach : "))

    while exact_sum(final_list, sum_to_reach) == -1 :
        print(final_list)
        print(used_list)

        if exact_sum(final_list, sum_to_reach-used_list[0])  < 0 and len(used_list) > 0 :
            print("We can't reach the sum")
            final_list.append(used_list[0])
            used_list.remove(used_list[0])
            
        elif exact_sum(final_list, sum_to_reach-used_list[0])  > 0 and len(used_list) > 0 :
            print("we will remove the last element")
            final_list.remove(final_list[-1])

main()
"""


def main(list,max):
    final_list = []
    sum = 0

    gave_list = list_sort(list)
    final_list = try_to_fill(gave_list, max, final_list)
    
    while (exact_sum(final_list,  sum) == -1) and gave_list != []:
        print(final_list)
        gave_list.remove(final_list[-1])
        final_list.remove(final_list[-1])
        final_list = try_to_fill(gave_list, max, final_list)
        print(final_list)
        
        

def try_to_fill(gave_list, max, started_list):
    #started list is the list that is already filled
    final_list = started_list
    used_list = gave_list

    while exact_sum(final_list,max) < 0 and len(used_list) > 0 :
        if exact_sum(used_list,max) + used_list[0] <= 0 :
            final_list.append(used_list[0])
            used_list.remove(used_list[0])
        else :
            used_list.remove(used_list[0])

    return final_list
            
        
"""


"""def try_to_fill(list, sum):
    final_list = []

    for i in range(0, len(list)):
        if (exact_sum(final_list, sum) == -1):
            sum += list[i]
            final_list.append(list[i])
    
    if (exact_sum(final_list, sum) == 0):
        return final_list
    else : 
        return final_list[-1]"""
