import abc
import enum

class ResponseCode(enum.Enum):
    ALARM_OK=1
    TEST_OK=2 
    ERROR=0


class IVFDUnit(metaclass=abc.ABCMeta):
    pass
    #ResponseCode notify(CCIR_code):


class VFDUnit(IVFDUnit):
    def __init__(self, unit,code, alarm):
        self.__unit_name = unit
        self.__test_code = code 
        self.__alarm_code = alarm

    def notify(self,CCIR_CODE):
        #TODO return "error"
        return 0

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


obj= VFDUnit(1,2,3)
obj.name = 'ola'
print(obj.name)