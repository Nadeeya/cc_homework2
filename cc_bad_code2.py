"""
20b6001, Nadeeya
clean-coding
bad coding examples
"""
#explain yourself in code
def membership(points):
    if points>150:
        member = True;
        
    else: 
        member = False;
        
    return member;

# check to see if customer is eligible for a discount
if membership(points) and age>18:
    print("eligble for a discount!")


#explain of intent
#java

System.out.print("Enter 'o' to register the next vehicle, enter 'x' to terminate.");
         char next = Character.toLowerCase(sc.next().charAt(0));
         while(menu.validInput(next)==false){//try again input
             next=Character.toLowerCase(sc.next().charAt(0));
            }   
          if(menu.inputXO(next)==false){//false = x
            System.out.println("Registration terminated.");
            break;
             }
          
#warning consequences
 System.out.print("Please enter 'o' to store the next vehicle technical information and 'x' to terminate: ");
         //have to change to lower case since it is case sensitive.
        char n = Character.toLowerCase(sc.next().charAt(0));
        while(m.validInput(n)==false){
         n= Character.toLowerCase(sc.next().charAt(0));
        }
        if(m.inputXO(n)==false){//n=x
         System.out.println("Storing system terminated.");
         next = false;
      }


     

