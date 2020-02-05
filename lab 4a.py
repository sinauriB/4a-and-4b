
import csv


#VARAIBLE FOR TOTAL RECORDS IN A CSV FILE 

records = 0

















#documentation
 
#LIST IN THE CSV  FILE 
first_name = []
last_name = []
age = []
nickname = []
house_of_alligance = []
 
mott_list = []

with open("C:/Users/008010554/Desktop/lab4a.txt") as txtfile:
     file = csv.reader(txtfile)

     for rec in file:

          records +=1
          
          first_name.append(rec[0])
          last_name.append(rec[1])
          age.append(rec[2])
          nickname.append(rec[3])
          house_of_alligance.append(rec[4])
          mott_list.append(motto)      
         



for i in range(0,records):


         print("{0:10}, {1:10}, {2:10}, {3:19}, {4:10}".format(first_name[i],last_name[i],age[i],nickname[i],house_of_alligance[i]))

                
                
for i in range(0,records):

         if house_of_alligance[i] == "House Stark":

             motto = "Winter is Coming"

        elif house_of_alligance[i] == "Night's Watch":

             motto == " And now my watch begins"

      elif house_of_alligance == "House of Tully":

          motto = "Family.Honor.Duty"

         elif house_of_alligance == "House of Lannister":

             motto = "Hear me roar"

          elif house of alligance == "House of Baratheon":

             motto = "ours is the fury"

        elif house_of_alligance == "House Taragaryen":

            motto =  "fire & blood"

        
         print("{0:10}, {1:10}, {2:10}, {3:19}, {4:10}".format(first_name[i],last_name[i],age[i],nickname[i],house_of_alligance[i], mott_list[i]))
