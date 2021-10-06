from lib import request, loader
from lib.parse import parse, save, parsed
from random import choice
from concurrent import futures

loader.load_combo('dork.txt')
loader.load_proxies('socks4')

output_data = []

def check(query):
   query = query.replace(' ', '+')
   proxy = choice(loader.proxies)
   headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-us","Connection": "keep-alive","Host": "www.bing.com","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",}
   for x in range(10, 110, 10):
      block_one = request.get_response('GET', url=f'https://www.bing.com/search?q={query}&PC=APPL&first={x}&FORM=PORE', headers=headers,proxies=proxy, timeout=10)
      text = block_one.response.text
      parse(text).extract('_ctf="rdr_T" href="(.*?)"', strict='http')
      for x in parsed:
         if x not in output_data:
            print(x)
            output_data.append(x)
            save(x + '\n')
      
   


#check('hello testing')

futures.ThreadPoolExecutor().map(check, loader.lines)

