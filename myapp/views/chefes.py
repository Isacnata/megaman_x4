import requests
from django.shortcuts import render

def get_all_chefes(request):
    # URL da sua API Flask (ajuste a URL conforme necessário)
    api_url = 'http://127.0.0.1:5000/chefes'
    
    # Fazendo a requisição GET para a API Flask
    response = requests.get(api_url)
    
    if response.status_code == 200:
        # Se a requisição foi bem-sucedida, obtemos os dados
        chefes = response.json()  # Retorna os dados em formato JSON
    else:
        # Caso contrário, exibimos uma mensagem de erro
        chefes = []
    
    # Renderizando a página e passando os dados dos chefes
    return render(request, 'chefes_list.html', {'chefes': chefes})