from calendar import calendar, day_name
import speech_recognition as  sr
import datetime
import pyttsx3

while 1>0:
     global time
     global date
     global speaker
     time=str(datetime.datetime.time(datetime.datetime.now()))
     date=str(datetime.datetime.date(datetime.datetime.now()))
     speaker=pyttsx3.init()
     speaker.say("I am listening")
     speaker.runAndWait()
     r=sr.Recognizer()
     with sr.Microphone() as source2:   
          r.adjust_for_ambient_noise(source2,duration=0.2)
          audio2=r.listen(source2)
          text=r.recognize_google(audio2,language="en-IND")
     print(text)
     def speak_the_spoken(text):   
          speaker.say(text)
          speaker.runAndWait()
     def speak_TIME(time):    
          speaker.say("The time is")
          speaker.say(time)
          speaker.runAndWait()
     def speak_DATE(date):    
          speaker.say("Todays date is")
          speaker.say(date)
          speaker.runAndWait()
     def speak_NAME():   
          speaker.say("My name is ")
          speaker.say("The    speaker")
          speaker.runAndWait()
     def speak_DAYNAME(dayint):
          li=["Monday","Tueday","Wednesday","Thursday","Friday","Saturday","Sunday"]
          for i in range(7):
               if dayint==i:
                    print("The day is:",li[i])
                    speaker.say("Today is ")
                    speaker.say(li[i])
                    speaker.runAndWait()
               else:
                    pass
     if text.find("time")>=0 and text.find("date")>=0:
          time=time.replace(":","replace")
          time=time.replace(".","replace")
          li=["Hours","Minute","Second"]
          for i in range(3):
               time=time.replace("replace",li[i],1)
          speak_TIME(time)
          speak_DATE(date)
     elif text.find("time")>=0:
          time=time.replace(":","replace")
          time=time.replace(".","replace")
          li=["Hours","Minute","Second"]
          for i in range(3):
               time=time.replace("replace",li[i],1)
          print(time)
          speak_TIME(time)
     elif text.find("date")>=0:
          speak_DATE(date)
     elif text.find("your")>=0 and text.find("name")>=0:
          speak_NAME()
     elif text.find("day")>=0 or text.find("today")>=0:
          dayname=datetime.datetime.weekday(datetime.datetime.now())
          speak_DAYNAME(dayname)    
     elif text.find("shut")>=0 or text.find("down")>=0 or text.find("stop")>=0:
          speaker.say("Have a great one.")
          speaker.runAndWait()
          quit()
