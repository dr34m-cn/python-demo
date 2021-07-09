conf = None

def setConf(req):
    global conf
    conf = req

def getConf():
    return conf