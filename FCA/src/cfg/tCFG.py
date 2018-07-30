import json
from configparser import SafeConfigParser

def main():

    #with open('./FCA/src/cfg/json.json', 'r') as f:
    with open('/usr/src/app/src/cfg/json.json', 'r') as f:
      
        config = json.load (f)
        #print config
        for item in config:
            #print item
            #print config[item]
            lvINDEX=0
            for params in config[item]:
                for key, value in params.iteritems():
                    print item +'/'+str(lvINDEX)+'/'+key, value
                lvINDEX+=1

if __name__=='__main__':
    main()

   

