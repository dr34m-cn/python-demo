from bService import bService
from bService.serviceData import serviceData

def run():
    print('aServiceDataRun')
    bService.run()
    serviceData.run()

if __name__ == "__main__":
    run()