# Buscador de Referências ABNT

Este projeto é um buscador de referências ABNT, que recebe um termo de busca e busca na web as referências bibliográficas correspondentes ao termo. O objetivo deste projeto é facilitar a busca e a formatação de referências bibliográficas para estudantes, professores e pesquisadores que precisam seguir as normas ABNT.

## Funcionalidades

O buscador de referências ABNT possui as seguintes funcionalidades:

- Receber um termo de busca do usuário
- Buscar nas fontes configuradas pelo usuário as informações necessárias para gerar a referência bibliográfica correspondente ao termo de busca
- Gerar uma referência bibliográfica no formato ABNT a partir das informações coletadas nas fontes
- Exibir a referência bibliográfica gerada na tela para o usuário

## Como usar

Para utilizar o buscador de referências ABNT, basta executar o script `buscador_referencias.py` a partir da linha de comando. Ao executar o script, uma janela será aberta na tela, onde o usuário pode inserir o termo de busca desejado e clicar no botão "Buscar Referência". Em seguida, o buscador buscará a referência correspondente e exibirá o resultado na janela.

## Como configurar

Para configurar as fontes de busca, basta editar o arquivo `fontes.txt`, adicionando ou removendo as URLs das fontes que deseja utilizar.

## Tecnologias utilizadas

O buscador de referências ABNT foi desenvolvido em Python, utilizando as seguintes bibliotecas:

- requests: para realizar as requisições HTTP às fontes de busca
- BeautifulSoup: para extrair as informações necessárias das páginas HTML
- tkinter: para criar a interface gráfica do buscador


## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.
