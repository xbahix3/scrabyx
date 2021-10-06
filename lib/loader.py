users = []
passwords = []
lines = []
proxies = []

def load_combo(file, separator=':'):
   try:
      with open(file, 'r', encoding="ISO-8859-1") as f:
         for line in f.readlines():
            if separator in line:
               users.append(line.split(separator)[0])
               passwords.append(line.split(':')[1].replace('\n',''))
               lines.append(line.replace('\n',''))
            else:
               lines.append(line.replace('\n',''))
   except FileNotFoundError:
      print("Please make sure that file exists and don't forget the extention .txt .\n")

def load_proxies(type):
   try:
      if type in ['https', 'http', 'socks4', 'socks5'] :
         with open('proxies.txt', 'r') as file:
            for line in file.readlines():
               line = line.replace('\n','')
               proxies.append({'http': f'{type}://{line}','https': f'{type}://{line}',})
   
   except FileNotFoundError:
      print("Please make sure that file exists and don't forget the extention .txt .\n")
