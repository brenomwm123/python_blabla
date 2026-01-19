import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLerror:
    print('O site nao esta acessivel')
else:
    print('Pudim ta torano')
    