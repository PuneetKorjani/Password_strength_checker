# password Complexity checker
from colorama import init , Fore , Style
init(autoreset=True)
import re
specialChar = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

inputpassword = input( "Enter the password : - ")



def main():
    while(True):
        print(Fore.YELLOW + "1. For  Feedback of your password : ")
        print(Fore.YELLOW + "2. For checking password complexity : ")
        print(Fore.YELLOW + "3. Exit : ")
        choice = input("Enter your choice :- ")

        # print("Feedback of your Entered Password :-")
        if choice == '1':
            if (len(inputpassword)>=8 and  any(char.isupper() for char in inputpassword) and not any (char.isnumeric() for char in  inputpassword)):


               print(Fore.BLUE + "Password difficulty is easy ")
               break
            elif (len(inputpassword)>=8 and  any(char.isupper() for char in inputpassword) and any (char.isnumeric()for char in inputpassword) and not re.search(r'[!@#$%^&*(),.?":{}|<>]',inputpassword)):
                print(Fore.BLUE + "Password difficulty is medium ")
                break

        
           


                
        
            elif(len(inputpassword)>=8 and  any(char.isupper() for char in inputpassword) and any (char.isnumeric() for char in  inputpassword) and re.search(r'[!@#$%^&*(),.?":{}|<>]',inputpassword)):
                print(Fore.GREEN + "Pasword difficulty is  Strong")
                break

            
           
            else:
                 print(Fore.RED + "Password is weak")
           
            
        elif choice == '2':
            
            ComplexityCheck(inputpassword)
            break
        elif choice == '3':
            print("Program over!")
            exit()
        else:
            print("Invalid input")

        
    
       
               
       
            
        



       








def ComplexityCheck(inputpassword):
    # first check :-  the length of the password
    if(len(inputpassword)<8):
        print(Fore.CYAN +"Password is too short")
        return False
        # second check :-  the password should have at least one uppercase letter
    elif not any(char.isupper() for char in inputpassword):
        print(Fore.CYAN + "Password Should have atleast one Uppercase Letter")
        return False
        # third check :-  the password should have at least one number 
    elif not any (char.isnumeric() for char in inputpassword):
        print(Fore.CYAN + "Password Should have at least one number")
        return False
    elif (specialChar.search(inputpassword) == None):
        print(Fore.CYAN + "The Password does not have Special Character in it!")
        return False
    else:
        # Feedback(inputpassword)
        print(Fore.GREEN  + "you can use this Password")
        return True
               





main()







