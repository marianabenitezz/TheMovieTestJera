import requests
import json
from PIL import Image
from io import BytesIO

https = 'https://api.themoviedb.org/3/'
api_key = '?api_key=e11e8b1786788ea384c7accb4d9e5d92'

# 'id'
# 'original_title'
# 'overview'
# 'poster_path'
# 'release_date'
#  'vote_average'


def buscarRecomendacao(id):
    reco = requests.get(https + 'movie/' + str(id) + '/recommendations' +
                        api_key).json()['results']
    recomendacoes = []
    for i in range(len(reco)):
        recomendacoes.append(reco[i])

    return recomendacoes


def buscarFilme(palavra):
    search_query = https + 'search/movie' + api_key + '&language=en-US&page=1&query='
    aaa = search_query + palavra
    req = requests.get(aaa).json()["results"]
    filmes = []
    for i in range(len(req)):
        filmes.append(req[i])

    return filmes


def buscarImagem(path):
    response = requests.get(https + 't/p/original' + path)
    img = Image.open(BytesIO(response.content))

    return img