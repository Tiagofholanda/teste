import requests

# Exemplo de API de uma corretora fictícia
API_URL = 'https://api.minhacorretora.com.br'
CPF = 'seu_cpf'
TOKEN = 'seu_token_de_acesso'

# Função para obter carteira de ações
def get_carteira_acoes():
    endpoint = f'{API_URL}/carteira'
    headers = {'Authorization': f'Bearer {TOKEN}'}
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Erro ao obter carteira de ações'}

# Exemplo de uso da função
carteira_acoes = get_carteira_acoes()
print(carteira_acoes)

