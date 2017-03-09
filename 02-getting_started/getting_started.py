from urllib.request import urlopen

response = urlopen('https://en.wikipedia.org/wiki/%22Hello,_World!%22_program')
html = response.read().decode('utf-8')
hidden_message = html.split('\n')[4][8:21]
result = '_-' * 2 ** 3 + hidden_message + '-_' * 2 ** 3
print(result)
import this
