import cv2
import numpy as np
import playsound
import smtplib
Fire_Reported=0
Alarm_Status=False
def play_audio():
    playsound.playsound("alarm-sound.mp3",True)
video=cv2.VideoCapture("fire.mov")
def send_email_function():
    reciptentEmail="harininisha1219@gmail.com"
    reciptentEmail=reciptentEmail.lower()
    try:
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login("laro05649@gmail.com","vcyf ueej ngfa cnqo")
        server.sendmail("harininisha1219@gmail.com",reciptentEmail,"A fire Accident has occured in laro store")
        print("sent to {}".format(reciptentEmail))
        server.close()
    except Exception as e:
        print(e)
while True:
    ret,frame=video.read()
    frame=cv2.resize(frame,(1000,600))
    blur=cv2.GaussianBlur(frame,(15,15),0)
    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    lower=[18,50,50]
    upper=[35,255,255]
    lower=np.array(lower,dtype="uint8")
    upper=np.array(upper,dtype="uint8")
    mask=cv2.inRange(hsv,lower,upper)
    output=cv2.bitwise_and(frame,hsv,mask=mask)
    size_of_fire=cv2.countNonZero(mask)
    if int(size_of_fire)>15000:
        Fire_Reported=Fire_Reported+1
        if Fire_Reported>=1:
            if Alarm_Status==False:
                send_email_function()
                play_audio()
                Alarm_Status=True
                print("fire detected ,mail sent to fire service!!!!!")
    if ret==False:
        break
    cv2.imshow("Output",hsv)
    if cv2.waitKey(1)&0xFF==ord("q"):
        break
cv2.destroyAllWindows()
video.release()
