import matplotlib.pyplot as plt

class PlanoCartesiano:
     
    def __init__(self, titulo = "Plano Cartesiano", titulo_eixo_x = "X", titulo_eixo_y = "Y", limite_eixo_x = [-10, 10], limite_eixo_y = [-10, 10]):
        fig, ax = plt.subplots()
        self.fig = fig
        self.ax = ax
        self.set_titulo(titulo)
        self.set_titulo_eixo_x(titulo_eixo_x)
        self.set_titulo_eixo_y(titulo_eixo_y)
        self.set_limite_eixo_x(limite_eixo_x)
        self.set_limite_eixo_y(limite_eixo_y)
        self.__configurar_eixos()

    def __configurar_eixos(self):
        self.ax.axhline(y=0, color='k')
        self.ax.axvline(x=0, color='k')
        self.ax.grid(True, which='both')

    def inserir_pontos(self, valores_x, valores_y, titulo = None):
        self.ax.plot(valores_x, valores_y, label=titulo)

    def inserir_ponto(self, coordenada, tipo = "ro"):
        self.ax.plot(coordenada[0], coordenada[1], tipo)
        
    def inserir_anotacao(self, titulo, coordenada, coordenada_titulo = None, cor = "black", tipo = "->", centralizacao = "center"):
        if coordenada_titulo == None:
            coordenada_titulo = (coordenada[0], coordenada[1] + 5)
        self.ax.annotate(titulo, xy=(coordenada[0], coordenada[1]), xytext=(coordenada_titulo[0], coordenada_titulo[1]),
            textcoords='offset points', arrowprops=dict(facecolor=cor, arrowstyle=tipo), ha=centralizacao)
        
    def renderizar(self):
        plt.title(self.titulo)
        plt.xlabel(self.titulo_eixo_x)
        plt.ylabel(self.titulo_eixo_y)
        plt.legend()
        plt.grid(True)
        plt.show()


    ## Getters and Setters
    def get_titulo(self):
        return self.titulo
    
    def set_titulo(self, titulo):
        self.titulo = titulo
        plt.title(self.titulo)

    def get_titulo_eixo_x(self):
        return self.titulo_eixo_x
    
    def set_titulo_eixo_x(self, titulo_eixo_x):
        self.titulo_eixo_x = titulo_eixo_x
        plt.xlabel(self.titulo_eixo_x)

    def get_titulo_eixo_y(self):
        return self.titulo_eixo_y
    
    def set_titulo_eixo_y(self, titulo_eixo_y):
        self.titulo_eixo_y = titulo_eixo_y
        plt.ylabel(self.titulo_eixo_y)

    def get_limite_eixo_x(self):
        return self.limite_eixo_x
    
    def set_limite_eixo_x(self, limite_eixo_x):
        self.limite_eixo_x = limite_eixo_x
        self.ax.set_xlim(limite_eixo_x)

    def get_limite_eixo_y(self):
        return self.limite_eixo_y
    
    def set_limite_eixo_y(self, limite_eixo_y):
        self.limite_eixo_y = limite_eixo_y
        self.ax.set_ylim(limite_eixo_y)