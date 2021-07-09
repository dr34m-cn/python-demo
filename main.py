from aService.serviceData import serviceData
from confService.confService import setConf
import json

with open('conf.json','r') as f1:
    conf = json.loads(f1.read())
    setConf(conf)


serviceData.run()