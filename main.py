
import requests
import cv2 


files = {'file': open('deneme4.mp4', 'rb')}
headers = {'Accept': 'application/json', }
payload = {
        "file_type": "mp4",    #jpg , png , pdf
        }
res = requests.post("http://localhost:8000/uploadfile",files=files,headers=headers,data=payload)
print(res.status_code, res.json())

