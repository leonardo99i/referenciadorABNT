function formatReferences() {
    // Pega o texto colado na caixa de texto
    const text = document.getElementById("references").value.trim();
  
    // Separa as linhas do texto em uma lista
    const lines = text.split("\n");
  
    // Cria uma lista vazia para armazenar as referências formatadas
    const formatted = [];
  
    // Cria uma expressão regular para identificar o título da referência
    const titleRegex = /(?<=^|\n)(.+)(?=\n|$)/g;
  
    // Formata cada linha como uma referência e adiciona na lista de referências formatadas
    for (let i = 0; i < lines.length; i++) {
      const title = lines[i].match(titleRegex);
      if (title) {
        const formattedRef = "[" + (i + 1) + "] " + title[0];
        formatted.push(formattedRef);
      }
    }
  
    // Junta as referências formatadas em um único texto e adiciona na caixa de texto de referências formatadas
    document.getElementById("formatted").value = formatted.join("\n\n");
  }
  