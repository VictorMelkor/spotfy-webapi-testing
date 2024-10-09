import json
from os.path import join, dirname
import time

def load_json_file(filename):
    '''
    será utilizada para procurar e abrir nosso arquivo data.json.
    '''
    absolute_path = join(dirname(__file__), filename)

    with open(absolute_path) as read_file:
        return json.loads(read_file.read())
    

def update_json_file(filename, newinfo):
    '''
    será utilizada para abrir nosso data.json e atualizar as informações que estiverem nele (Exemplo: atualizar o token de acesso).
    '''
    absolute_path = join(dirname(__file__), filename)

    with open(absolute_path, 'w') as write_file:
        json.dump(newinfo, write_file, indent=2)


def check_timestamp_is_old(timestamp_refreshtoken):
    '''
    será utilizada para validar se o token de acesso já expirou, comparando o timestamp atual do sistema com o timestamp que está salvo em data.json.
    '''
    timestamp_now = time.time()
    if timestamp_refreshtoken < timestamp_now:
        return True
    elif timestamp_refreshtoken > timestamp_now:
        return False
    
    return True