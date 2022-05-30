def backpack(n,weight_capacity,weights,prices):

    if(n==0 or weight_capacity==0):
        return 0
    
    if (weights[n-1]>weight_capacity):
        return backpack(n-1,weight_capacity,weights,prices)
   
    else:
        return max(prices[n-1] + backpack(n-1,weight_capacity-weights[n-1],weights,prices),
                   backpack(n-1,weight_capacity,weights,prices))
    


weights = [18,37,1,25,4,12,9,16,7,5]
prices = [14,2,4,3,50,7,10,9,24,21]
n = len(weights)
weight_capacity = 50
 
print(knapsack(n,weight_capacity,weights,prices))