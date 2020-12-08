from Strategy import Context, Strategy, SendToAll, SendToOne
from State import Test, Alarm, StateContext, State
from Alarming import ResponseCode, VFDUnit, IVFDUnit, Subject
from Firefighter import Firefighter, IFirefighter
import random

class Commander:
    def send_to_one(self,observers,brigade,alarm_type):
        context = Context(SendToOne(brigade.name))
        context.business_logic(observers)

    def send_to_all(self,observers,alarm_type):
        #TODO żeby działało dla wszystkich 
        context = Context(SendToAll(observers))
        #response
        context.business_logic(observers)
#DTG-53
class FirefighterSender(Firefighter):
    def __init__(self,firefighters):
        self.__firefighters = firefighters

    def send_to_firefighters(self)->Firefighter:
        for firefighter in self.__firefighters:
            print("Sending SMS from DTG-53 to:",firefighter.name,firefighter.surname)
        

        
def main():
    all_brigades = []
    #adding brigade's to alarming system
    brigade_one = VFDUnit('Fire Brigade in Chicago',25,111)
    all_brigades.append(brigade_one)
    brigade_two = VFDUnit('Fire Brigade in Miami',26,222)
    all_brigades.append(brigade_two)

    observers_base = Subject()
    observers_base.add_observer(brigade_one)
    observers_base.add_observer(brigade_two)

    #adding firefighters
    firefighter_one = Firefighter('Alan','Skarżyński',889440123)
    firefighter_two = Firefighter('Adriana','Należna',669340890)
    firefighter_three = Firefighter('Kazimierz','Podolak',880778234)

    #adding receivers to list
    firefighters = []
    firefighters.append(firefighter_one)
    firefighters.append(firefighter_two)
    firefighters.append(firefighter_three)

    sender = FirefighterSender(firefighters)

    #setting alarm
    alarm = StateContext(Test())
    
    #notyfying  via base station
    Commander().send_to_one(observers_base,brigade_one,alarm)
    
    #response
    response = 2
    brigade_response = brigade_one.notify(response)
    
    #alarm signal, notifying firefighters
    if brigade_response != ResponseCode.ERROR:
        print("[SYRENE SOUND] ALARMING!!!")
        sender.send_to_firefighters()
    else:
        print("No or wrong response from ",brigade_one, " unit!")
 
    #changing alarm state
    alarm.request_one()

    #notyfying all brigades via base station
    Commander().send_to_all(observers_base,alarm)

    #response
    response = 1
    response_error = ''
    random_responses =[response,response_error] 

    
    for brigade in all_brigades:
        random_response = random.choice(random_responses)
        answer = brigade.notify(random_response)
        if answer !=  ResponseCode.ERROR:
            print("[SYRENE SOUND] ALARMING!!!")
            sender.send_to_firefighters()
        else:
            print("No or wrong response from ",brigade.name, " unit!")

        
        
    #alarm signal

if __name__ == "__main__":
    main()