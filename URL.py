import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('o site pudim não está acesível no momento')
else:
    print('o site pudim está acessível')
    print(site.read())