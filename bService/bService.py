from confService.confService import getConf
def run():
    conf = getConf()
    print('bServiceRun',conf)
    print("conf['user']",conf['user'])