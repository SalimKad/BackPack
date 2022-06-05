# TP1 KADIRI HASSANI Salim - JOSEPH Robin

#Version 1 : 
#Première option, cette méthode cherche à avoir l'utilité maximale en gardant un poids inférieur ou égal au poids maximal. 

gave_list = [[18,14], [37,2], [1,4], [25,3], [4,50], [12,7], [9,10], [16,9], [7,24], [5,21]] # liste des objets, avec poids et valeurs
max_weight = int(input("Entrer le poids maximal que peut contenir le sac à dos : "))

def greedy_method(gave_list) :
    used_list = gave_list

    for item in used_list :
        item.append(used_list.index(item))
        item.append(item[1]/item[0])
        
    #print(used_list)
    used_list.sort(key=lambda x: x[3], reverse=True) # sort by ratio
    #print(used_list)

    while weight_sum(used_list) > max_weight :
        used_list.pop()
        #print(used_list)
    return used_list

def brut_force_method(max_weight,gave_list) :
    weights = list_convert(gave_list)[0]
    prices = list_convert(gave_list)[1]

    if (len(weights) == 0 or max_weight == 0) :
        return 0
    
    if (weights[len(weights)-1] > max_weight) :
        return brut_force_method(len(weights)-1,max_weight,weights,prices)
   
    else:
        return max(prices[len(weights)-1] + brut_force_method(len(weights)-1,max_weight-weights[len(weights)-1],weights,prices),
                   brut_force_method(len(weights)-1,max_weight,weights,prices))

def weight_sum(gave_list) :
    sum = 0
    for item in gave_list :
        sum += item[0]
    return sum

def value_sum(gave_list) :
    sum = 0
    for item in gave_list :
        sum += item[1]
    return sum

def display_backpack(gave_list) :
    print("\nLes objets dans le sac à dos sont : ")
    for item in gave_list :
        print("Numéro {}, qui pèse {} et a une valeur de {}, donc un ratio de {}".format(item[2], item[0], item[1], item[3]))
    print("Le poids total du sac à dos actuel est donc de : {}".format(weight_sum(gave_list)))
    print("La valeur totale du sac à dos actuel est donc de : {}".format(value_sum(gave_list)))


def list_convert(gave_list) :
    weight_list = []
    value_list = []
    for item in gave_list :
        weight_list.append(item[0])
        value_list.append(item[1])
    return [weight_list, value_list]


display_backpack(greedy_method(gave_list))




#Version 2 : Fonction BackPack en utilisant l'appel récursif
#Contrairement à la méthode précédente, cette méthode permet d'arriver au poids maximal exactement


def sommexac(n,max_weight,weights,prices):

    if(n==0 or max_weight==0):
        return 0
    
    if (weights[n-1]>max_weight):
        return sommexac(n-1,max_weight,weights,prices)
   
    else:
        return max(prices[n-1] + sommexac(n-1,max_weight-weights[n-1],weights,prices),
                   sommexac(n-1,max_weight,weights,prices))
    

print("\n\nRésultat de la fonction récursive :")
weights = [18,37,1,25,4,12,9,16,7,5]
prices = [14,2,4,3,50,7,10,9,24,21]
n = len(weights)

 
print("L'utilité maximale que l'on peut avoir avec un poids total de exactement {} est : {}\n".format(max_weight,sommexac(n,max_weight,weights,prices)))