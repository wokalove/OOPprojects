from abc import ABC, abstractmethod
import enum

#DSP-50
class ResponseCode(enum.Enum):
    ALARM_OK = 1,
    TEST_OK = 2, 
    ERROR = 0


class IVFDUnit(ABC):
    @abstractmethod
    def notify(self,CCIR_code):
        pass

#observer
class VFDUnit(IVFDUnit):
    def __init__(self, unit=0,code=0, alarm=0):
        self.__unit_name = unit
        self.__test_code = code 
        self.__alarm_code = alarm

    def notify(self,CCIR_CODE):
        if CCIR_CODE == int(', '.join(map(str,ResponseCode.ALARM_OK.value ))):
            print(self.__unit_name,"is ready on alarm!")
        elif CCIR_CODE == int(', '.join(map(str,ResponseCode.TEST_OK.value ))):
            print(self.__unit_name,"is ready on test!")
        else:
            return ResponseCode.ERROR

    @property
    def name(self):
        return self.__unit_name
    @name.setter
    def name(self,name):
        self.__unit_name = name

    
    @property
    def test(self):
        return self.__test_code
    @test.setter
    def test(self,test):
        self.__test_code = test
    
    
    @property
    def alarm(self):
        return self.__alarm_code
    @alarm.setter
    def alarm(self,alarm):
        self.__alarm_code = alarm

class Subject(VFDUnit):
    def __init__(self):
        self.__observers_collection = []
    def add_observer(self,brigade)->VFDUnit:
        self.__unit_name = brigade
        self.__observers_collection.append(brigade)

    def remove_observer(self,brigade):
        pass

    def notify_all(self):
        for observer in self.__observers_collection:
            observer.notify()
    
    def get_observators(self):
        return self.__observers_collection

    def show_observators(self):
        for observator in self.__observers_collection:
            print("Brigade:",observator.name,"Test:",observator.test,"Alarm:",observator.alarm)
'''
brigade_one= VFDUnit('Fire Brigade in Chicago',2,3)
brigade_two= VFDUnit('Fire Brigade in Miami',244,3332)

observers_base = Subject()
observers_base.add_observer(brigade_one)
observers_base.notify_all()

'''