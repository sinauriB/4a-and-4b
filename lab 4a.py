
# Sinauri Tapia Lab 4A




# starting doc 

# for 4A the program has to  process the  6 fields of data of  the  lab5.txt  csv file and store each  field into its own list 
# and re-process  the list (using for loop() )  to print  each rec(row)  fully with its house motto
# THEN AGAIN re-process the list (using ANOTHER forloop() ) to print avg age and 
#AND print the tallies  for each house alligance AND total number of people in the list 




#VARAIBLE dictionary
# records - is the total  number of rows processed in the csv file
# first_name is the 0(first)field in  csv file it stores the name of the user
# last_name is the 1(sec) field in the csv file  it stores last name of the user
# age is the 2(third) field in the csv file stores age of the user
# nickname is 3(fourth) field  in the csv file stores nickname of user
# house_of_alligance is the 4 (fifth) row in csv file stores the users house alligance
# mott_list is the 5 (sixth) field in the csv file stores the house of alligance motto
# ageF - is the total num of ages in the csv file and its used alongside the AVg()
# Average(): is used to calculate the avg age of user in the field 2.
# houseA - the total num of house alligance fields in the csv file
#  totalpeeps - the  total num of First and LAst name fields in csv file



#base program code --------------



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
    
    
    #  get avg age of user in age[] 
    
    
   for i in range(ageF):
    
    return sum(age) / len(age)
     
    print age[i] 

  
     # print total LAST AND FIRST name in field  for totalpeeps using func
    
   for i in range(len(first_name, last_name)):
     print first_name [i]   +  print last_name[i]
     
     
     # print total house alligance
     
     
     for i in range(len(house_of_alligance)):
      
      print house_of_alligance[i]
      
      
      
      
     
     
     
     
     
   
     
     
     
  
     
   
   
   
   
   
   
   
   
   
          
          
    
          
          
