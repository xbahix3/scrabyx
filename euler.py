from lib import request, parse
from re import sub
from concurrent import futures

list = [i for i in range(1,758)]

def check(n):
   response = request.get_response('GET', f'https://projecteuler.net/minimal={n}').response.text
   text = 7*'~'+f'[+{n}+]'+7*'~'+f'''\n{sub('<(.*?)>', '', response)}\n'''+19*'~'
   parse.save(text)
   print(n)

futures.ThreadPoolExecutor().map(check, list)
   
   
