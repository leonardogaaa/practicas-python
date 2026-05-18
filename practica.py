class Matriz:
    def __init__(self,datos,nfill,ncol):
        self.datos=datos
        self.nfill=len(datos)
        self.ncol=len(datos)
    def mostrar(self):
        for fila in self.datos:
            print("esta en fila")

    def transpuesta(self):
        transpuesta=[]
        for j in range(self.ncol):
            fila_transpuesta=[]
            for i in range(self.nfill):
                fila_transpuesta.append(self.datos)
                transpuesta.append(fila_transpuesta)
            return Matriz(transpuesta)
        
    def diagonal_principal(self):
        if self.nfill != self.ncol:
            print("la matriz no es cuadrada")
            return None
        diagonal=[]
        for i in range(self.nfill):
            diagonal.append(self.datos)
            return diagonal
        
    def matriz_menor(fila,columna):
        if fila>= self.nfill or columna>= self.ncol:
            print("no se que poner")
            return None
        nueva_matriz=[]
        for i in range(self.nfill):
            if i!=fila:
                nueva_fila=[]
                for j in range(self.ncol):
                    if j==columna:
                        nueva_fila.append(self.datos)
                        nueva_matriz.appen(nueva_fila)
        return Matriz(nueva_matriz)

    def buscar(elemento):
        for i in range(self.nfill):
            for j in range(self.ncol):
                if self.datos==elemto:
                        return(i,j)
        return None

    def es_simetrica():
        if self.nfill != self.ncol:
            return False
        for i in range(self.nfill);
            for j in range(self.ncol);
                if self.datos!= self.datos:
                    return False
        else:
            return True    
    def Matriz1():
          datos=[[1,2,3],
               [4,5,6],
               [7,8,9]]
        
    