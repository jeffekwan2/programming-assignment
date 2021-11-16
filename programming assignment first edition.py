'''
Simple Billing System

Created on Oct 6, 2020

@author: tchan
'''
import fileinput
import sys

def displayFile(datafile):
    for line in fileinput.input(datafile):
        sys.stdout.write(line)

    
def main():
    instructions = """\nEnter one of the following:
        1 to print the contents of input transaction file
        2 to print all valid input transaction data
        3 to enter adjustment transaction
        4 to print customer report
        Q to end \n"""
    
       
    while True:
        sys.stdout.write(instructions) 
        sys.stdout.flush()      
        choice = input( "Enter 1 to 4 " ) 

        if choice == "1":
            displayFile(sys.argv[1])
        elif choice == "2":
            print('%-20s%-30s%-9s%5s'%('Name','Address','Txn','Amount'))
            print('='*65)
            data=[('Fred Chan','213 Yuen Long Avenue','D',41.03),
                  ('Sue Wong','9102 Kowloon Circle','D',10.00),
                  ('Fred Chan','213 Yuen Long Avenue','C',0.01),
                  ('Baba Li','2000 E. 21st Street','D',450.00),
                  ('Sue Wong','9102 Kowloon Circle','C',5.50),
                  ('Jay Law','9103 Problem Area','C',25.00),
                  ('Fred Chan','213 Yuen Long Avenue','C',41.02)]
            for e in data:
                print('%-20s%-32s%-7s%6.2f'%e)
            
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "Q":
            break

    print ("End Simple Billing System")

if __name__ == "__main__":
    sys.argv = [sys.argv[0], 'datafile0.dat']
    displayFile(sys.argv[1])
    main()
