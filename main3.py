def solsad(v,w,n,Weight):
    V=[x[:] for x in [[0]*(Weight+1)] * (n+1)] # intialisation de V
    for i in range(0,n):
        for j in range(Weight+1):
            if w[i]<=j: # on ajoute l'élément i
                V[i][j]=max(V[i-1][j],v[i]+V[i-1][j-w[i]])
            else: # l'élément i n'est pas ajouté
                V[i][j]=V[i-1][j]
    return V[n][Weight]

solsad([1,2,3,4,5],[1,2,3,4,5],5,5)
