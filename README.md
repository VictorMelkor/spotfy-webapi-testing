# spotify-webapi-testing

Este projeto foi desenvolvido para estudos de como criar requests no Python para listar e gerenciar Playlists e realizar autenticação OAuth2 para a API do Spotify Web.
O desenvolvimento acompanhou o incrível passo-a-passo constante na postagem https://medium.com/@pedron.ketlin/python-requests-spotify-web-api-63cce3641c66 escrito por Ketlin Pedron, embora tenham sido feitas modificações.

### Requisitos:
Para desenvolver o projeto é necessário habilitar um profile developer junto ao Spotify, que pode ser feito pelo link: https://developer.spotify.com/.

### Arquivo dados.json:
• Os itens client_id e client_secret que devem ser preenchidos no arquivo dados.json, na pasta Resources, são fornecidos pelo Spotify ao se habilitar o profile developer.
• Para aquisição da Callback URL, utilizei inicialmente o Postman para acessar os endpoints de autenticação de usuário e manipulação de playlists.
• Os Scopes são necessários para definir as operações que serão realizadas, podendo ser verificados aqui: https://developer.spotify.com/documentation/general/guides/scopes/

O preenchimento do arquivo deve ser feito de forma individualizada, com os dados privados do usuário, logo, as informações preenchidas são apenas para ilustração.

O campo "token" está vazio pois o projeto realiza o preenchimento durante sua execução, após autenticação.

### Tests:
É necessário alterar o nome do usuário no arquivo test_playlists.py, nas linhas 36 e 52, para realização dos testes conforme o preenchimento do arquivo dados.json.

### Considerações finais:
No mais, tentei replicar o projeto citado no artigo como parte de meus estudos de request e API, adicionando algumas docs strings para meu próprio entendimento e também para possíveis leitores.

Continuamos em busca de evolução!