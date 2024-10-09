from requests_oauthlib import OAuth2Session
from Resources import utils as Utils

class MyOAuth2:
    def access_token_get(self, client_id, client_secret, scope, redirect_uri, token):
        '''
        A função access_token_get é responsável por obter o primeiro token, porém se ele já existir e estiver
        expirado o tempo de uso, será chamada uma função para atualizar o token (token_refresh). 
        Em ambos os casos, será retornado para o caso de teste um token pronto para uso.
        
        '''
        #First validade if there is a refresh token valid
        #PT-BR: Primeiro valida se existe um refresh token válido
        if token:
            #Now check if it is necessary to refresh the token
            #PT-BR: Agora checa se é preciso dar refresh no token
            if self._can_refresh_token(token) is True:
                token = self.token_refresh(client_id, client_secret, token)
                return token
            else:
                #Only return the actual token
                #PT-BR: Apenas retorna o token atual
                return token
        else:
            #Creates a new access_token and refresh_token
            #PT-BR: Cria um novo access_token e refresh_token
            client = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)

            #Redirect user to Spotify for authorization 
            #PT-BR: Redireciona o usuário para autenticação no Spotify
            #This only happen in the first time to get token
            #PT-BR: Isso acontece apenas na primeira vez obtendo o token
            authorization_url, state=client.authorization_url("https://accounts.spotify.com/authorize")
            print('\n \n Por favor visite esta URL e obtenha a URL callback: \n' + authorization_url)

            #Get the authorization verifier code from the callback url
            #PT-BR: Obtem o código verificador de autorização da url de retorno
            redirect_response = input('\n \nCole a redirect URL: ')

            token = client.fetch_token("https://accounts.spotify.com/api/token",
                                        authorization_response=redirect_response,
                                        client_secret=client_secret)
            return token
    
    def token_refresh(self, client_id, client_secret, token):
        extra = {'client_id': client_id, 
                'client_secret': client_secret,
                'refresh_token': token['refresh_token']}
        
        oauth_refresh = OAuth2Session(client_id, token=token)
        new_token = oauth_refresh.refresh_token("https://accounts.spotify.com/api/token", **extra)

        return new_token

    def _can_refresh_token(self, token):
        # In this case we already have a valid token
        #PT-BR: Nesse caso, já temos um token válido
        #Now we will check if the refresh token is expired
        #PT-BR: Agora vamos verificar se o token está expirado
        if Utils.check_timestamp_is_old(token["expires_at"]) is True:
            return True
        else:
            return False
        
        return True
