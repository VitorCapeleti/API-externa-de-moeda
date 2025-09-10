import sys
sys.path.append('/home/vitor/Documentos/Projetos/Consumir API py')
from consumirAPI.api.dataCoin import *
def list_infos():
    data = get_data_coin()
    return data
print(list_infos())