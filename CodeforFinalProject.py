#UI-"rawinput ask user "Please enter your zipcode to find the closest rape crisis center."
#create zipcode string 
#open CSV file
#read CSV file
#when it matches the zipcode in the CSV file it will print 
#code for  it to print if match found
#create string for print "Sorry no matches found. Please contact Rape and Incest National Network at 1-800-Stop-Rape"
#code if not match found
#add on to find closest rape crisis center to zipcode entered-create range of zipcode for each county in Cali
#add on to ensure that users do not enter any thing but 5 digits as zipcode 

#DO I NEED SUBLIMEREPL to allow INPUT of any kind? 
#UI code below 


#zipcode=raw_input('Please enter your zipcode to find your local rape crisis center.')
zipcode="94612"
print('Thank you!')


#Open CSV File
#addon make address all on one line-go back and take out commas between address info on csv 
foundmatch=False 
Rapecrisiscenters = open('CSV.py','r')
for center in Rapecrisiscenters:
    if zipcode in center:
       centername,address,city,state,postalcode,phone,website = center.split(",")
       print(centername)
       print(address)
       print(city)
       print(state)
       print(postalcode)
       print(phone)
       print(website)

       foundmatch=True

       break 
Rapecrisiscenters.close()


#if you don't find anything 
if foundmatch==False:
    print "Sorry, no centers found. Please call RAINN at 800.656.HOPE (4673) for help."
   				








