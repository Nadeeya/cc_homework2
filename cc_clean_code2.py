"""
20b6001, Nadeeya
clean-coding
clean code examples
"""
#explain yourself in code
def membership(points):
    if points>150:
        member = True;
        
    else: 
        member = False;
        
    return member;

def eligibleForDisc(points, age):
    if membership(points) and age>18:
        return True;
    
if eligibleForDisc(points,age):
    print("eligble for a discount!")
    
#explain of intent
#java

System.out.print("Enter 'o' to register the next vehicle, enter 'x' to terminate.");
         char next = Character.toLowerCase(sc.next().charAt(0));
         while(menu.validInput(next)==false){//if input is not x or o hence redo input
             next=Character.toLowerCase(sc.next().charAt(0));
            }   
          if(menu.inputXO(next)==false){//false = x
            System.out.println("Registration terminated.");
            break;
             }

#clarification
    for(int i=0;i<index;i++){
      if(carInsp[i].getId().equals(vehicleID)){//finding the vehicle
        carInsp[i].print();//printing the basic information of the car
        technicalInformation(carInsp, i , sc);//CALL TECHNICAL INFORMATION
      }
        

