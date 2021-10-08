import re

parsed = []

class parse:
   def __init__(self, content):
      self.content = content
   def extract(self, value, remove_duplicates=True, strict=''):
      extracted = re.findall(value, self.content)
      parsed.clear()
      for line in extracted:
         if strict in line:
            if remove_duplicates==True:
               if line not in parsed:
                  parsed.append(line)
            else :
               parsed.append(line)
            
def save(value, output='output.txt'):
   open(output, 'a', encoding='utf-8').writelines(value)
      
      
