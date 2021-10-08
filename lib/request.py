import requests

success = 0
fail = 0
custom = 0
rety = 0
ban = 0
parsed = []


def retry(function, retries=5):
   def wrap_data(*args, **kwargs):
      global rety
      tries = 0
      while retries > tries:
         try:
            return function(*args, **kwargs)
         except requests.ConnectionError:
            tries += 1
            rety += 1
   return wrap_data

class get_response:
   @retry
   def __init__(self, method, url, *args, **kwargs):
      self.response = requests.request(method, url, *args, **kwargs)

   def success(self, save=False, statement='', save_this=''):
      global success
      if statement in self.response.text:
         success += 1
         if save:
            open('success.txt', 'a', encoding='utf-8').writelines(save_this)

   def fail(self, statement=''):
      global fail
      if statement in self.response.text:
         fail += 1

   def custom(self, save=False, statement='', save_this=''):
      global custom
      if statement in self.response.text:
         custom += 1
         if save:
            open('custom.txt', 'a', encoding='utf-8').writelines(save_this)
         
   def _banned(self):
      global ban
      if self.response.status_code == 200:
         ban+=1

def result(update=0):
   print(f'success={success} fail={fail} custom={custom} retries={rety} ban={ban}')

