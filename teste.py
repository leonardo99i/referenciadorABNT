import tkinter as tk

def muda_tema():
    if root["bg"] == "white":
        root["bg"] = "black"
        root["fg"] = "white"
    else:
        root["bg"] = "white"
        root["fg"] = "black"

root = tk.Tk()
root.title("Referenciador ABNT")
root.geometry("800x600")
root.config(bg="white")

logo = tk.PhotoImage(file="imagem.png")
logo_label = tk.Label(root, image=logo)
logo_label.pack()

titulo_label = tk.Label(root, text="Referenciador ABNT", font=("Arial", 24))
titulo_label.pack(pady=10)

trocar_tema = tk.Button(root, text="Trocar Tema", command=muda_tema)
trocar_tema.pack(pady=10)

texto_label = tk.Label(root, text="Cole seu texto aqui:")
texto_label.pack()

texto_entry = tk.Text(root, height=10)
texto_entry.pack()

link_label = tk.Label(root, text="Cole o link da fonte:")
link_label.pack()

link_entry = tk.Entry(root)
link_entry.pack()

def gerar_referencias():
    texto = texto_entry.get("1.0", tk.END)
    link = link_entry.get()
    # código para gerar as referências na norma ABNT
    texto_referenciado = "Referências geradas:\n\n" # adicionar referências formatadas aqui
    texto_entry.delete("1.0", tk.END)
    texto_entry.insert("1.0", texto_referenciado)

referencias_btn = tk.Button(root, text="Gerar Referências", command=gerar_referencias)
referencias_btn.pack(pady=10)

root.mainloop()
#Note que a função muda_tema foi definida no início do código e passada como argumento para o botão trocar_tema. Certifique-se de que o nome da função esteja escrito corretamente e que ela esteja acessível a partir do escopo em que o botão é definido.




