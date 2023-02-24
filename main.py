import tkinter as tk
from normas_abnt import NormasABNT # importa a biblioteca NormasABNT para formatar as referências

class InterfaceGrafica:
    def __init__(self):
        # Cria a janela principal
        self.janela = tk.Tk()
        self.janela.title("Referências ABNT")
        
        # Cria um label com o título e um logo
        logo = tk.PhotoImage(file="logo.png")
        label_logo = tk.Label(self.janela, image=logo)
        label_logo.image = logo
        label_logo.pack(pady=10)
        label_titulo = tk.Label(self.janela, text="Referências ABNT", font=("Arial", 20))
        label_titulo.pack(pady=10)
        
        # Cria a caixa de texto para o usuário colar o texto
        label_texto = tk.Label(self.janela, text="Cole aqui o texto que você quer referenciar:")
        label_texto.pack(pady=10)
        self.caixa_texto = tk.Text(self.janela, width=80, height=10)
        self.caixa_texto.pack(padx=10, pady=5)
        
        # Cria a caixa de texto para o usuário colar o link do site
        label_link = tk.Label(self.janela, text="Cole aqui o link do site onde você encontrou o texto:")
        label_link.pack(pady=10)
        self.caixa_link = tk.Entry(self.janela, width=80)
        self.caixa_link.pack(padx=10, pady=5)
        
        # Cria o botão para pesquisar as referências
        botao_referencias = tk.Button(self.janela, text="Pegar Referências", command=self.pegar_referencias)
        botao_referencias.pack(pady=10)
        
        # Cria a caixa de texto para mostrar as referências
        label_referencias = tk.Label(self.janela, text="Referências:")
        label_referencias.pack(pady=10)
        self.caixa_referencias = tk.Text(self.janela, width=80, height=10)
        self.caixa_referencias.pack(padx=10, pady=5)
        
        # Inicia a janela
        self.janela.mainloop()

    def pegar_referencias(self):
        # Pega o texto e o link da caixa de texto e entrada, respectivamente
        texto = self.caixa_texto.get("1.0", "end")
        link = self.caixa_link.get()
        
        # Formata as referências usando a biblioteca NormasABNT
        normas = NormasABNT()
        referencias = normas.formatar_referencias(texto, link)
        
        # Mostra as referências na caixa de texto de referências
        self.caixa_referencias.delete("1.0", "end")
        self.caixa_referencias.insert("end", referencias)

if __name__ == "__main__":
    InterfaceGrafica()
