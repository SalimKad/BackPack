
#Version 2 : Fonction BackPack en utilisant l'appel récursif


def sommexac(n,weight_capacity,weights,prices):

    if(n==0 or weight_capacity==0):
        return 0
    
    if (weights[n-1]>weight_capacity):
        return sommexac(n-1,weight_capacity,weights,prices)
   
    else:
        return max(prices[n-1] + sommexac(n-1,weight_capacity-weights[n-1],weights,prices),
                   sommexac(n-1,weight_capacity,weights,prices))
    


weights = [18,37,1,25,4,12,9,16,7,5]
prices = [14,2,4,3,50,7,10,9,24,21]
n = len(weights)
weight_capacity = 50
 
print("L'utilité maximale que l'on peut avoir avec un poids total de", weight_capacity, "est : " ,sommexac(n,weight_capacity,weights,prices))