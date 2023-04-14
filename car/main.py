from machine import Pin,ADC 
import os



def remove_all():
    
    for file_name in os.listdir():
        os.remove(file_name)
    
def main():
    print("Welcome to RT-Thread MicroPython!")
    print(os.listdir())
    # remove_all()
    
    
    print(os.listdir())

    
    
    
    

        
    
    
    
if __name__ == '__main__':
    main()