list1=[{
    "id":"123",
    "code":"true"
},{
    "id":"456",
    "code":"false"
}]
import time
a=0
while True:
    a=a+1
    for item in list1:   
        if a==10:
            item["code"]="@@@@@@@@@@@@@@@@@@@@@@@@"
        print(item["id"])
        print(item["code"])
    time.sleep(1)
