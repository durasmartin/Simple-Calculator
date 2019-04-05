#Calculator

import sys
from math import *
import time


#Functions
def add():
    number1=int(raw_input("Write the first number:"))
    number2=int(raw_input("Write the second number:"))
    result=(number1+number2)
    print("\n")
    print("Result: "+str(result))
    print("\n")
    
def substract():
    number1=int(raw_input("Write the first number:"))
    number2=int(raw_input("Write the second number:"))
    result=(number1-number2)
    print("\n")
    print("Result: "+str(result))
    print("\n")
 
def multiply():
    number1=int(raw_input("Write the first number:"))
    number2=int(raw_input("Write the second number:"))
    result=(number1*number2)
    print("\n")
    print("Result: "+str(result))
    print("\n")

def divide():
    number1=int(raw_input("Write the first number:"))
    number2=int(raw_input("Write the second number:"))
    result=(number1/number2)    
    print("\n")
    print("Result: "+str(result))
    print("\n")
    
    
#Loop
def main():
    while True:
        print("1. Add")
        print("2. Substract")
        print("3. Multiply")
        print("4. Divide")
        
        choice=raw_input("Write what you'd like to do:")
        if choice=="1":    
            add()
        elif choice=="2":
            substract()
            
        elif choice=="3":
            multiply()
        
        elif choice=="4":
            divide()
            
        else:
            time.sleep(2)
            print("\n")
            print("Choose a valid option!")
        
        
        
main()        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        