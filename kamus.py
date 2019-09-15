#Import Modules
try:
    import requests, os, re
except ImportError as err:
    print(err)

os.system("clear") #clear screen

class Colors(object):
    c='\033[0;36m'      # Cyan
    co='\033[0m'        #close

class Banner(Colors): #Banner

    print(f"""

  /////|
 ///// |
|~~~|  |
|===|  |    
|4  |  | {Colors.c}By: 407 AEX{Colors.co}
| 0 |  |
|  7| /
|===|/
'---'

    """)


class Transalate(Banner): #Super Class


    def __init__(self, frm, to, text):
        self.frm = frm
        self.to = to
        self.text = text
        
    # main func
    def bahasaDaerah(self):
        try:
            req = requests.get(f"https://www.kamusdaerah.com/?bhs={self.frm}&bhs2={self.to}&q={self.text}", timeout=6).text
            query = re.findall(r"<div class='arti'>.*? </div>(.*?)<div class='bahasa'>", str(req))
            for x in range(len(query)):
                print(f"Artinya: {query[x]}")
        except ConnectionError as err:
            print(err)
        except requests.Timeout as err:
            print(err)
        except Exception as err:
            print(err)

       
#Calling function
if __name__ == "__main__":
    while(True):
        frm = input("[*]Dari bahasa mana?: ")
        to = input("[*]Transalate ke?: ")
        text = input("[*]Text: ")
        Transalate(frm, to, text).bahasaDaerah()
        