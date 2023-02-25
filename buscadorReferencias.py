import tkinter as tk
import tkinter.scrolledtext as st
from citeproc.py2compat import *
from citeproc.source.json import CiteProcJSON
from citeproc import CitationStylesStyle, CitationStylesBibliography
import json

root = tk.Tk()
root.title("Referenciador ABNT")
root.geometry("800x600")
root.configure(bg='white')

logo = tk.PhotoImage(file="imagem.png")
logo_label = tk.Label(root, image=logo, bg="white")
logo_label.pack()

titulo_label = tk.Label(root, text="Referenciador ABNT", font=("Arial", 20), bg="white")
titulo_label.pack()

texto_label = tk.Label(root, text="Cole aqui o texto que deseja referenciar:", font=("Arial", 12), bg="white")
texto_label.pack()

texto = st.ScrolledText(root, height=10, font=("Arial", 12))
texto.pack()

link_label = tk.Label(root, text="Cole aqui o link da página onde encontrou o texto:", font=("Arial", 12), bg="white")
link_label.pack()

link = tk.Entry(root, width=50, font=("Arial", 12))
link.pack()

def gerar_referencias():
    texto_referenciado = texto.get("1.0", "end")
    url = link.get()

    # Transforma o texto em formato JSON para ser utilizado pelo citeproc-py
    refs = []
    refs.append({
        "id": "1",
        "type": "article-journal",
        "title": texto_referenciado,
        "container-title": "",
        "author": "",
        "issued": "",
        "URL": url
    })
    bib_source = CiteProcJSON(json.dumps({"items": refs}))
    
    # Carrega o estilo de referências ABNT e gera a bibliografia formatada
    with open("abnt.csl") as estilo_arquivo:
        estilo = CitationStylesStyle(json.load(estilo_arquivo))
    bibliografia = CitationStylesBibliography(estilo, bib_source, formatter = PlainText)

    # Formata a bibliografia de acordo com o estilo ABNT
    bibliografia.register(bib_source)
    bib_formatted = bibliografia.bibliography()

    # Exibe a bibliografia formatada na caixa de texto
    texto.delete("1.0", "end")
    texto.insert("end", bib_formatted)

botao_referencias = tk.Button(root, text="Gerar Referências", command=gerar_referencias)
botao_referencias.pack()

root.mainloop()
