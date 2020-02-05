
# Sinauri Tapia Lab 4A




# starting doc 
# for 4A the program has to  process the  6 fields of data of  the  lab5.txt  csv file and store each  field into its own list 
# and re-process  the list (using for loop() )  to print  each rec(row)  fully with its house motto
# THEN AGAIN re-process the list (using ANOTHER forloop() ) to print avg age 




#VARAIBLE dictionary
# records - is the total  number of rows processed in the csv file
# first_name is the 0(first)row in  csv file it stores the name of the user
# last_name is the 1(sec) row in the csv file  it stores last name of the user
# age is the 2(third) row in the csv file stores age of the user
# nickname is 3(fourth) row in the csv file stores nickname of user
# house_of_alligance is the 4 (fifth) row in csv file stores the users house alligance
# mott_list is the 5 (sixth) row in the csv file stores the house of alligance motto










import cvs



records = 0
 
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

             motto == "And now my watch begins"

      elif house_of_alligance == "House of Tully":

          motto = "Family.Honor.Duty"

         elif house_of_alligance == "House of Lannister":

             motto = "Hear me roar!"

          elif house of alligance == "House of Baratheon":

             motto = "Ours is the fury"

        elif house_of_alligance == "House Taragaryen":

            motto =  "Fire & Blood"
          
          print("{0:10}, {1:10}, {2:10}, {3:19}, {4:10}".format(first_name[i],last_name[i],age[i],nickname[i],
                                                                house_of_alligance[i], mott_list[i]))
          
          
          
          
          
          
          
