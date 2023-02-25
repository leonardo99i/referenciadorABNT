import tkinter as tk
import pyperclip
from pybtex.database import BibliographyData, Entry
from pybtex.style.formatting import plain
from pybtex.style.labels import BaseLabelStyle
from pybtex.plugin import find_plugin
from PIL import Image, ImageTk

# Define um estilo ABNT customizado
class ABNTStyle(plain.Style):
    default_label_style = BaseLabelStyle()

# Cria a janela principal
root = tk.Tk()
root.title("Farma Academy - ABNT Formater")

# Carregando o logo
logo = Image.open('imagem.png')
logo_img = ImageTk.PhotoImage(logo)

# Criando o widget da imagem com o logo
logo_label = tk.Label(root, image=logo_img)
logo_label.pack()

# Função para alternar o tema da aplicação
def toggle_theme():
    current_theme = root["bg"]
    if current_theme == "white":
        root["bg"] = "black"
        text_box["bg"] = "black"
        text_box["fg"] = "white"
        link_box["bg"] = "black"
        link_box["fg"] = "white"
    else:
        root["bg"] = "white"
        text_box["bg"] = "white"
        text_box["fg"] = "black"
        link_box["bg"] = "white"
        link_box["fg"] = "black"

# Cria o botão para alternar o tema da aplicação
theme_button = tk.Button(root, text="Mudar Tema", command=toggle_theme)
theme_button.pack()

# Cria a caixa de texto
text_box = tk.Text(root)
text_box.pack()

# Cria a caixa de texto para o link
link_box = tk.Text(root, height=1)
link_box.pack()

# Função para formatar as referências
def format_references():
    # Pega o texto colado na caixa de texto
    text = text_box.get("1.0", tk.END).strip()

    # Pega o link colado na caixa de texto
    link = link_box.get("1.0", tk.END).strip()

    # Separa as linhas do texto em uma lista
    lines = text.split("\n")

    # Cria uma biblioteca vazia
    bib_data = BibliographyData()

    # Adiciona cada linha como uma entrada na biblioteca
    for i, line in enumerate(lines):
        entry = Entry('article', fields={'title': line})
        label = str(i+1)
        bib_data.add_entry(label, entry)

    # Define o estilo ABNT customizado
    style = ABNTStyle()

    # Formata as referências
    formatted_entries = []
    for key, entry in bib_data.entries.items():
        formatted_entry = style.format_entry(entry)
        formatted_entry.text = f"[{key}] " + formatted_entry.text
        formatted_entries.append(formatted_entry.text)

    # Junta as referências formatadas em um único texto
    formatted_text = "\n\n".join(formatted_entries)

    # Adiciona as referências formatadas ao texto na caixa de texto
    text_box.delete("1.0", tk.END)
    text_box.insert("1.0", formatted_text)

# Cria o botão para formatar as referências
format_button = tk.Button(root, text="Formatar Referências", command=format_references)
format_button.pack()

# Inicia a aplicação
root.mainloop()
