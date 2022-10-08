import requests
import os
import json
import base64
from datetime import datetime
import time

def orderingJson(improper):
    return  improper['d'].replace(',',',"').replace(':','":').replace('{','{"').replace('":0',':0').replace('":1',':1').replace('":2',':2').replace('":3',':3').replace('":4',':4').replace('":5',':5').replace('":6',':6').replace('":7',':7').replace('":8',':8').replace('":9',':9').replace('d:','d":').replace('p:','p":').replace('e:','e":').replace('D:','D":').replace('"{','{')
 

def sendDataToServer(id,lat,lng,alarm,timestamp):
    data = "http://13.52.238.152:5055/?id="+str(id)+"&lat="+str(lat)+"&lon="+str(lng)+"&timestamp="+str(timestamp)+"&alarm="+str(alarm)+""
    print(data)
    RespAlarm=requests.get("http://13.52.238.152:5055/?id="+str(id)+"&lat="+str(lat)+"&lon="+str(lng)+"&timestamp="+str(timestamp)+"&alarm="+str(alarm)+"",timeout = 10,headers = {"Connection": "keep-alive"})
    print(RespAlarm)
    
def getLiveLocation(RespPosParams,noo):
    #RespPosParams = {"UserID":10465,"isFirst":False,"TimeZones":'8:00',"DeviceID":516415}
    #RespPosParams = {"UserID":10465,"isFirst":False,"TimeZones":'4:00',"DeviceID":504742}
    RespAlarm=requests.post("http://gps123.org/Ajax/DevicesAjax.asmx/GetDevicesByUserID", json =RespPosParams)
    resp = json.loads(RespAlarm.text)
    try:
        respx = json.loads(orderingJson(resp))
        print(respx['devices'])
        for i in respx['devices']:
            #print(i["sn"]) #baiduLat,baiduLng,speed,status
            #if(i["status"] != 'Offline'):
            #sendDataToServer("9705001673",i["baiduLat"],i["baiduLng"],"",int(time.time()))
            sendDataToServer(noo,i["baiduLat"],i["baiduLng"],"",int(time.time()))
            
    except:
        print("Could not parse data" , resp )
    
def getExceptionMessage(RespPosParams1,RespPosParams,noo,last_Update):
    #RespPosParams = {"DeviceID":516415,"TimeZones":'8:00'}
    #RespPosParams = {"DeviceID":504742,"TimeZones":'4:00'}
    RespAlarm=requests.post("http://gps123.org/Ajax/DevicesAjax.asmx/GetDevicesByUserID", json =RespPosParams1)
    resp = json.loads(RespAlarm.text)
    lat = ""
    lng = ""
    try:
        respx = json.loads(orderingJson(resp))
        print(respx['devices'])
        for i in respx['devices']:
            lat = i["baiduLat"]
            lng = i["baiduLng"]   
            #print(i["sn"]) #baiduLat,baiduLng,speed,status
            #if(i["status"] != 'Offline'):
            #sendDataToServer("9705001673",i["baiduLat"],i["baiduLng"],"",int(time.time()))
            sendDataToServer(noo,i["baiduLat"],i["baiduLng"],"",int(time.time()))
            
    except:
        print("Could not parse data" , resp )
        
    RespAlarm=requests.post("http://gps123.org/Ajax/ExceptionMessageAjax.asmx/GetExceptionMessageByDeviceID", json =RespPosParams)
    resp = json.loads(RespAlarm.text)
    #try:
    xx = orderingJson(resp)
    print(xx)
    respx = json.loads(orderingJson(resp))
    print(respx['ems'])
    for i in respx['ems']:
        if(int(i["sn"]) > last_Update):
            last_Update = int(i["sn"])
            print(i["sn"])
            if(i["notificationType"] == 9):
                sendDataToServer(i["sn"],lat,lng,"sos",int(time.time()))
            if(i["notificationType"] == 53):
                sendDataToServer(i["sn"],lat,lng,"accident",int(time.time()))
    return last_Update
    #except:
    #    print("Could not parse data" , resp )

last_Update1 = 0
last_Update2 = 0
    
while True:
    #getLiveLocation({"UserID":10465,"isFirst":False,"TimeZones":'8:00',"DeviceID":516415},"9705001690")
    #getLiveLocation({"UserID":10465,"isFirst":False,"TimeZones":'4:00',"DeviceID":504742},"9705001673")
    #time.sleep(1)
    #sendDataToServer()
    #getExceptionMessage({"DeviceID":516415,"TimeZones":'8:00'},"9705001690")
    time.sleep(1)
    last_Update1 = getExceptionMessage({"UserID":10465,"isFirst":False,"TimeZones":'4:00',"DeviceID":504742},{"DeviceID":504742,"TimeZones":'4:00'},"9705001673",last_Update1)
    time.sleep(1)
    last_Update2 = getExceptionMessage({"UserID":10465,"isFirst":False,"TimeZones":'8:00',"DeviceID":516415},{"DeviceID":516415,"TimeZones":'8:00'},"9705001690",last_Update2)
    time.sleep(5)
    #print(json_RespDevices,len(json_RespDevices))
#return jsonify([firealarm,faultalarm])http://13.52.238.152:5055/?id=1234567890&lat=23.0&lon=25.0&timestamp=1648415734&alarm=sos
#http://13.52.238.152:5055/?id=9705001673&lat=25.223664&lon=55.452843&timestamp=2022-10-06T22:20:52.207Z

'''
{"d":"{ems:[{id:122983673,name:\"V45C-01673\",sn:\"9705001673\",model:\"V45C\",notificationType:9,deviceID:504742,note:\"\",deviceDate:\"2022/10/06 13:48\",createDate:\"2022/10/06 14:47\",deleted:0},{id:122925836,name:\"V45C-01673\",sn:\"9705001673\",model:\"V45C\",notificationType:9,deviceID:504742,note:\"\",deviceDate:\"2022/10/05 00:10\",createDate:\"2022/10/05 01:01\",deleted:0}]}"}

{"ems":[{"id":122998055,"name":"V45C-01673","sn":"9705001673","model":"V45C","notificationType":9,"deviceID":504742,"note":"","deviceDate":"2022/10/06 20:52","createDate":"2022/10/06 21:50","deleted":0},{"id":122983673,"name":"V45C-01673","sn":"9705001673","model":"V45C","notificationType":9,"deviceID":504742,"note":"","deviceDate":"2022/10/06 13:48","createDate":"2022/10/06 14:47","deleted":0},{"id":122925836,"name":"V45C-01673","sn":"9705001673","model":"V45C","notificationType":9,"deviceID":504742,"note":"","deviceDate":"2022/10/05 00:10","createDate":"2022/10/05 01:01","deleted":0}]}

[{'id': 504742, 'locationID': '1', 'groupID': -1, 'serverUtcDate': '2022-10-06 18:49:26', 'deviceUtcDate': '2022-10-06 18:49:26', 'baiduLat': '25.25994', 'baiduLng': '55.33093', 'ofl': '1', 'speed': '0.00', 'course': '998', 'dataType': '3', 'dataContext': '0-97', 'distance': '36.1025', 'isStop': 1, 'stopTimeMinute': 79, 'carStatus': '', 'status': 'Stop'}]


GetDevicesByUserID

{UserID:10465,isFirst:false,TimeZones:'8:00',DeviceID:516415}
{"d":"{devices:[{id:516415,locationID:\"1\",groupID:-1,serverUtcDate:\"2022-10-07 03:00:35\",deviceUtcDate:\"2022-10-07 02:59:06\",baiduLat:\"25.25994\",baiduLng:\"55.33093\",latitude:\"25.25994\",longitude:\"55.33093\",ofl:\"0\",speed:\"0.00\",course:\"998\",dataType:\"3\",dataContext:\"0-40\",distance:\"1.3054\",isStop:1,stopTimeMinute:2,carStatus:\"\",status:\"Stop\"}]}"}



GetExceptionMessageByDeviceID
{DeviceID:516415,TimeZones:'8:00'}
{,…}
d
: 
"{ems:[{id:122999528,name:\"V45C-01690\",sn:\"9705001690\",model:\"V45C\",notificationType:5,deviceID:516415,note:\"\",deviceDate:\"2022/10/07 02:57\",createDate:\"2022/10/07 02:57\",deleted:0},{id:122999429,name:\"V45C-01690\",sn:\"9705001690\",model:\"V45C\",notificationType:5,deviceID:516415,note:\"\",deviceDate:\"2022/10/07 02:51\",createDate:\"2022/10/07 02:51\",deleted:0},{id:122999420,name:\"V45C-01690\",sn:\"9705001690\",model:\"V45C\",notificationType:5,deviceID:516415,note:\"\",deviceDate:\"2022/10/07 02:50\",createDate:\"2022/10/07 02:50\",deleted:0},{id:122999417,name:\"V45C-01690\",sn:\"9705001690\",model:\"V45C\",notificationType:53,deviceID:516415,note:\"\",deviceDate:\"2022/10/07 02:50\",createDate:\"2022/10/07 02:50\",deleted:0},{id:122998511,name:\"V45C-01690\",sn:\"9705001690\",model:\"V45C\",notificationType:53,deviceID:516415,note:\"\",deviceDate:\"2022/10/07 02:10\",createDate:\"2022/10/07 02:10\",deleted:0},{id:122998498,name:\"V45C-01690\",sn:\"9705001690\",model:\"V45C\",notificationType:53,deviceID:516415,note:\"\",deviceDate:\"2022/10/07 02:09\",createDate:\"2022/10/07 02:09\",deleted:0},{id:122998477,name:\"V45C-01690\",sn:\"9705001690\",model:\"V45C\",notificationType:53,deviceID:516415,note:\"\",deviceDate:\"2022/10/07 02:08\",createDate:\"2022/10/07 02:08\",deleted:0},{id:122998371,name:\"V45C-01690\",sn:\"9705001690\",model:\"V45C\",notificationType:5,deviceID:516415,note:\"\",deviceDate:\"2022/10/07 02:01\",createDate:\"2022/10/07 02:01\",deleted:0},{id:122998354,name:\"V45C-01690\",sn:\"9705001690\",model:\"V45C\",notificationType:5,deviceID:516415,note:\"\",deviceDate:\"2022/10/07 02:01\",createDate:\"2022/10/07 02:01\",deleted:0},{id:122998279,name:\"V45C-01690\",sn:\"9705001690\",model:\"V45C\",notificationType:5,deviceID:516415,note:\"\",deviceDate:\"2022/10/07 01:59\",createDate:\"2022/10/07 01:59\",deleted:0},{id:122998201,name:\"V45C-01690\",sn:\"9705001690\",model:\"V45C\",notificationType:5,deviceID:516415,note:\"\",deviceDate:\"2022/10/07 01:56\",createDate:\"2022/10/07 01:56\",deleted:0}]}"

Cloud Berry 

'''