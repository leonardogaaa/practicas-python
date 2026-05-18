ma t riz = [ [ 1 , 2 , 3 ] ,
[ 2 , 1 , 4 ] ,
[ 3 , 4 , 1 ] ]
class matriz:
    def __init__(self, matriz, nfil , ncol):
        self.matriz=matriz
        self.nfil=len(matriz)
        self.ncol=len(matriz[0])
    def mostrar(self):
        for i in range (self.nfil):
            for j in range (self.ncol):
                print (matriz[i][j])
    def transpuesta(self):
        trans=[]
        for i in range (self.ncol):
            fila=[]
            for j in range (self.nfil):
                val=matriz[j][i]
                fila.append(val)
        trans.append(fila)
        return trans 
    def diagonal_principal(self):
        print(matriz[i][i])
    def matriz_menor(self):
        tamaño=int(input("ingrese el tamaño:") )
        princi=[]
        for i in range (0,tamaño):
            fila=[]
            for j in range(0, tamaño):
                val=matriz[i][j]
                fila.append(val)
        princi.append(fila)
        return princi
    
    def es_simetrica(self):
        for i in range(self.nfil):
            principal=[]
            for j in range(self.ncol):
                val=matriz[i][i]
                principal.append(val)
        return principal

        for i in range(self.nfil):
            transpuesta=[]
            for j in range(self.ncol):
                if i+j==len(matriz)-1:
                    val=matriz[i][j]
                    transpuesta.append(val)
        return transpuesta

        for i in range(len(principal)):
            if not principal[i] in transpuesta:
                return False
            return True 
                