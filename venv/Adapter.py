import ICD
import requests

def myCon(IP,port,version):

    mySD=ICD.sd()
    payload = {'POST':mySD.retur_sd()}
    server='http://'+IP+':'+port
    r = requests.post(server, json=payload)
    return r


def sendData(IP,port,data):
    payload={'POST':data}
    #payload  = {'POST': 'DATA from ICD'}
    server='http://'+IP+':'+port
    r=requests.post(server,json=payload)
    return r
