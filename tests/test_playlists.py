import unittest
from Resources import utils as Utils
from Requests.request_oauth2 import MyOAuth2
from Requests.requests import Requests

class Playlists(unittest.TestCase):

    def setUp(self):
        '''
        é o método que permite definir instruções que serão executadas antes de cada caso de teste.
        Nesse exemplo, estou realizando 3 coisas:
        Primeiro estou carregando as informações presente em data.json;
        Segundo estou obtendo meu access_token e disponibilizando em uma variável para ser utilizada no caso de teste;
        Em terceiro estou instanciando minha classe Requests em uma variável que também será utilizada durante o caso de teste.
        '''
        self.data = Utils.load_json_file("data.json")

        #Get Token
        oauth2 = MyOAuth2()
        self.token = oauth2.access_token_get(self.data["client_id"],
                                            self.data["client_secret"],
                                            self.data["scope"],
                                            self.data["callback_uri"], 
                                            self.data["token"])

        self.access_token = self.token["access_token"]
        self.request = Requests()

    
    def test_get_playlist(self):
        '''
        É um caso de teste responsável por testar se é possível obter uma lista de playlists do nosso user id.
        Repare que aqui é utilizado o access_token e estou mandando meu user id (victormelkor). Troque para seu user id para que funcione em sua conta.
        Neste caso de teste estou apenas avaliando se o status code é 200.
        '''
        response = self.request.playlists_get(self.access_token, "victormelkor")

        assert response.status_code == 200

    def test_create_new_playlist(self):
        '''
        Este caso de teste valida a criação de uma nova playlist para o nosso user id.
        No body, vamos escrever algumas informações básicas da nossa playlist a ser criada.
        Neste caso de teste, o status code esperado é o 201, ou seja, foi possível realizar o create.
        '''
        body = {
            "name": "Playlist Python",
            "description": "Essa playlist foi criada via python requests",
            "public": True
        }

        response = self.request.playlist_create(self.access_token, "victormelkor", body)
        assert response.status_code == 201


    def tearDown(self):
        '''
        é um método que permite definir instruções que serão executadas ao final de cada caso de teste.
        Nesse caso, estamos dizendo para o tearDown atualizar no data.json o token que foi obtido lá no setUp 
        '''
        #Update the access token and refresh token in data.json
        self.data["token"] = self.token
        Utils.update_json_file("data.json", self.data)