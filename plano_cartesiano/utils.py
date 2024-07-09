import matplotlib.pyplot as plt

class PlanoCartesiano:
     
    def __init__(self, linhas = 1, colunas = 1, figsize = None):
        self._fig, self._ax = plt.subplots(nrows=linhas, ncols=colunas, figsize=figsize)
        self._linhas = linhas
        self._colunas = colunas
        self._figsize = figsize
        self.configurar_eixos()

    def configurar_eixos(self, x_inicial = 0, y_inicial = 0):
        index = 0
        while index < self._linhas:
            current_ax = self.get_ax(index)
            current_ax.axhline(y=y_inicial, color='k')
            current_ax.axvline(x=x_inicial, color='k')
            current_ax.grid(True, which='both')
            index += 1

    def alterar_limites_eixos(self, limite_eixo_x = [-10, 10], limite_eixo_y = [-10, 10], index = None):
        current_ax = self.get_ax(index)
        current_ax.set_xlim(limite_eixo_x)
        current_ax.set_ylim(limite_eixo_y)

    def inserir_pontos(self, titulo = "Plano Cartesiano", valores_eixo_x = [], valores_eixo_y = [], label = None, label_eixo_x = "X", label_eixo_y = "Y", 
                       grid = True, legenda = True, cor = None, index = None):
        current_ax = self.get_ax(index)
        current_ax.plot(valores_eixo_x, valores_eixo_y, label=label, color=cor)
        current_ax.set_title(titulo)
        current_ax.set_xlabel(label_eixo_x)
        current_ax.set_ylabel(label_eixo_y)
        current_ax.grid(grid)
        if legenda:
            current_ax.legend()

    def inserir_ponto(self, coordenada = (), cor = "black", tamanho = 70, index = None):
        current_ax = self.get_ax(index)
        current_ax.scatter(coordenada[0], coordenada[1], color=cor, s=tamanho)
        
    def inserir_anotacao(self, titulo = None, coordenada = (), coordenada_titulo = None, cor = "black", tipo = "->", centralizacao = "center", index = None):
        current_ax = self.get_ax(index)
        if coordenada_titulo == None:
            coordenada_titulo = (coordenada[0], coordenada[1] + 20)
        current_ax.annotate(titulo, xy=(coordenada[0], coordenada[1]), xytext=(coordenada_titulo[0], coordenada_titulo[1]),
            textcoords='offset points', arrowprops=dict(facecolor=cor, arrowstyle=tipo), ha=centralizacao)
        
    def renderizar(self, tight = False):
        if tight:
            plt.tight_layout()
        plt.show()
    
    ## Getters and Setters
    def get_fig(self):
        return self._fig
    
    def get_ax(self, index = None):
        return self._ax if index == None or self._linhas == 1 else self._ax[index]