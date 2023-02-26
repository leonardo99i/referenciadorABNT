const apiKey = "1c258907-5fb1-422c-95cf-47fe606354a1";

async function getReference(url) {
  const apiUrl = `https://opengraph.io/api/1.1/site/${encodeURIComponent(
    url
  )}?app_id=${apiKey}`;
  const response = await fetch(apiUrl);
  const data = await response.json();

  if (data.error) {
    return data.error;
  }

  const title = data.hybridGraph.title || "";
  const author = data.hybridGraph.author || "";
  const publication = data.hybridGraph.site_name || "";
  const date = new Date(data.hybridGraph.published_time).toLocaleDateString() || "";
  const link = url;

  const citation = `${author}, ${title}, ${date}, Disponível em: <${link}>.`;

  return citation;
}

document.getElementById("searchButton").addEventListener("click", async () => {
  const urlInput = document.getElementById("urlInput");
  const url = urlInput.value.trim();

  if (url === "") {
    return;
  }

  const referenceOutput = document.getElementById("referenceOutput");
  referenceOutput.innerText = "Buscando referência...";

  try {
    const citation = await getReference(url);
    referenceOutput.innerText = citation;
  } catch (error) {
    referenceOutput.innerText = `Erro ao buscar referência: ${error.message}`;
  }
});
