function searchReferences() {
    const inputText = document.getElementById("input-text").value.trim();
    const inputLink = document.getElementById("input-link").value.trim();
  
    if (!inputText || !inputLink) {
      alert("Por favor, insira o texto e o link.");
      return;
    }
  
    const outputText = formatReferences(inputText, inputLink);
    document.getElementById("output-text").value = outputText;
  }
  
  function formatReferences(text, link) {
    const authors = getAuthors(text);
    const year = getYear();
    const title = getTitle(text);
    const siteName = getSiteName(link);
    const retrievedFrom = getRetrievedFrom(link);
  
    let outputText = `${authors.toUpperCase()}. ${year}. ${title}. ${siteName}. ${retrievedFrom}`;
  
    return outputText;
  }
  
  function getAuthors(text) {
    const regex = /(([A-Z]{1}[a-z]+([ |-][A-Z]{1}[a-z]+)*){1,3})/g;
    const matches = text.match(regex);
    const formattedAuthors = matches.map((match) => match.trim()).join(', ');
    return formattedAuthors;
  }
  
  function getYear() {
    const date = new Date();
    return date.getFullYear();
  }
  
  function getTitle(text) {
    const match = text.match(/<title>(.+?)<\/title>/i);
    return match ? match[1].trim() : "";
  }
  
  function getSiteName(link) {
    const regex = /([a-z]+\.[a-z]+)/i;
    const match = link.match(regex);
    return match ? match[1] : "";
  }
  
  function getRetrievedFrom(link) {
    return `Disponível em: <${link}>.`;
  }
  