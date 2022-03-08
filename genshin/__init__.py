#######
# imports
#######

import ramael
import os

#######
# class imports
#######



#######
# actual wrapper
#######

class api:
    def __init__(self,type,local):
      self.type=type
      self.file=f"genshin.{type}.json"
      r = ramael.get(url=f"https://api.genshin.dev/{self.type}/all")
      locel = {}
      exec(f"x = {r.text} ",{},locel)
      x = locel["x"]
      files = []
      self.db = 0
      if local == True:
        if r.status != 200:
          with open(self.file,"r") as db:
            c = db.read()
          self.db = c
        
        
        for file in os.listdir(os.getcwd()):
          files.append(file)
        if self.file not in files:
          # this is incase the api is unreachable
          os.system(f"touch genshin.{self.type}.json")
          with open(self.file,"w") as db:
            db.write(str(x))
        else:
          with open(self.file,"r") as db:
            c = db.read()
          if c != x:
            with open(self.file,"w") as db:
              db.write(str(x))
          else:
            self.db = x
      else:
        if r.status != 200:
          return "request failed, issue with api"
        self.db = x

    
    @property
    def values(self):
      
      r = ramael.get(url=f"https://api.genshin.dev/{self.type}/")
      locel = {}
      exec(f"x = {r.text} ",{},locel)
      x = locel["x"]
      return x

    def get(self,q):
      r = ramael.get(url=f"https://api.genshin.dev/{self.type}/{q}")
      return r.json()
      
          
    def search(self,n):
      for item in self.db:
        z = dict(item)
        
        if z["name"].lower() == n.lower():
          return z


class Genshin:
  def __init__(self,local=True):
    self.api_obj = api
    self.local = local
  @property
  def types(self):
    r = ramael.get(url=f"https://api.genshin.dev")
    x = r.json()
    return x["types"]
  def api(self,type):
    return self.api_obj(type,self.local)
    
  
