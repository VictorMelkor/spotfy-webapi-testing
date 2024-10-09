import requests


class Requests:

    def playlists_get(self, access_token, userid):
        '''
        É a função que chamaremos para listar todas as playlists do nosso user id.
        No meu exemplo estou solicitando a visualização de apenas 1 playlist (limit). 
        Observe que é utilizado o método GET do requests.
        '''
        base_url = "https://api.spotify.com/v1/users/"
        url = base_url + userid + '/playlists'

        headers = {"Authorization": "Bearer" + access_token}
        query = {"limit": 1}

        return requests.get(url=url, headers=headers, params=query)
    

    def playlist_create(self, access_token, userid, body):
        '''
        É a função que chamaremos para criar uma nova playlist para nosso user id. 
        As informações da playlist (campo body) deverão ser criadas durante o caso de teste. 
        A função recebe os parâmetros, formata e realiza uma request do tipo POST.
        '''
        base_url = "https://api.spotify.com/v1/users"
        url = base_url + userid + '/playlists'

        headers = headers = {"Authorization": "Bearer" + access_token}

        return requests.post(url=url, headers=headers, json=body)