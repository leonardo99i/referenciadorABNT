  // Função para alternar o tema da página
  function toggleTheme() {
    const body = document.querySelector('body');
    if (body.classList.contains('light-theme')) {
      body.classList.remove('light-theme');
      body.classList.add('dark-theme');
    } else {
      body.classList.remove('dark-theme');
      body.classList.add('light-theme');
    }
  }
  
  // Associa as funções aos elementos da página
  document.querySelector('#search-button').addEventListener('click', () => {
    const text = document.querySelector('#input-text').value;
    const link = document.querySelector('#input-link').value;
    searchReferences(text, link);
  });
  document.querySelector('#theme-button').addEventListener('click', toggleTheme);