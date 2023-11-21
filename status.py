
from hikvisionapi import Client
import time
cam = Client('http://192.168.0.145', 'admin', 'Lums@hik12345', timeout=1)
response = cam.PTZCtrl.channels[1].status(method='get')
# print(response)
xA = int(response['PTZStatus']['AbsoluteHigh']['elevation'])
yA = int(response['PTZStatus']['AbsoluteHigh']['azimuth'])
zA = int(response['PTZStatus']['AbsoluteHigh']['absoluteZoom'])
while True:
    response = cam.PTZCtrl.channels[1].status(method='get')
    time.sleep(.5)
    xB = int(response['PTZStatus']['AbsoluteHigh']['elevation'])
    yB = int(response['PTZStatus']['AbsoluteHigh']['azimuth'])
    zB = int(response['PTZStatus']['AbsoluteHigh']['absoluteZoom'])
    #print(xA, yA, zA, xB, yB, zB)
    if yA != yB or xA != xB or zA != zB:
        print("changes")
        yA = yB
        xA = xB
        zA = zB
    else:
        print("stable")



