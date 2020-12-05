from Brigade import Observer, Subject
from Strategy import Context,Strategy, SendToAll, SendToOne

def main():
    brigade_one = Observer("Fire Brigade in Chicago",881435221)
    #print(brigade_one.get_observator())
    brigade_two = Observer("Fire Brigade in Miami",880221908)

    observers_base = Subject()
    observers_base.add_observer(brigade_one)
    observers_base.add_observer(brigade_two)
    
    context = Context(SendToOne(brigade_one.name))
    context.business_logic(observers_base)

    #TODO żeby działało dla wszystkich 
    '''context.strategy = SendToAll()
    context.business_logic(observers_base)
    '''
    
    

if __name__ == "__main__":
    main()