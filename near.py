from math import * #import everything from math
import csv  #import csv to use csv functions such as reader

#open geocode.csv which contains the comma seperated values of all the hospitals
csvfile=open("geocode_health_center.csv","r")


#function to find nearest among two destinations
def nearest_two_latlongs(source, destination1,destination2):
    lat1, lon1 = source
    lat2, lon2 = destination1
    lat3, lon3 = destination2
    radius = 6371
    dlat1 ,dlon1= lat2-lat1,lon2-lon1
    dlat2 ,dlon2=lat3-lat1,lon3-lon1
    a = sin(dlat1/2) * sin(dlat1/2) + cos(lat1) \
        * cos(lat2) * sin(dlon1/2) * sin(dlon1/2)
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    dr1 = radius * c
    b = sin(dlat2/2) * sin(dlat2/2) + cos(lat1) \
        * cos(lat3) * sin(dlon2/2) * sin(dlon2/2)
    d = 2 * atan2(sqrt(b), sqrt(1-b))
    dr2 = radius * d
    if(dr1 < dr2):
        return destination1
    else:
        return destination2


  
#Take inputs from the user
lat=float(input("Enter Your Latitude position:"))
long=float(input("Enter Your Longitude position:"))
#a is answer list
a=[]

#read from csv file
spamreader = csv.reader(csvfile, delimiter=',')

#store all values into a rows list
rows=[r for r in spamreader]

#indexing starts from 1 because we ignore table headers
list1=rows[1]
list2=rows[2]
#assign first two values of destination latitudes and longitudes
dlat1,dlong1,dlat2,dlong2=float(list1[6]),float(list1[7]),float(list2[6]),float(list2[7])

#function call two find the nearest among two destinations from the source
a=(nearest_two_latlongs([lat,long],[dlat1,dlong1],[dlat2,dlong2]))
#run for loop to call the functions for all items in the list
#as already 1 and 2 indexes are referred and nearest one is in a
for i in range(3,len(rows)):
    list1=rows[i]

    #convert the data into float only if there are digits in the list
    if ((list1[6]) and (list1[6].isdigit())):
      if ((list1[6]) and (list1[7].isdigit())):
        dlat1=float(a[0])
        dlong1=float(a[1])
        dlat2=float(list1[6])
        dlong2=float(list1[7])
        a=nearest_two_latlongs([lat,long],[dlat1,dlong1],[dlat2,dlong2])

#function to get the data back to the original form which converted to float before
def formatNumber(num):
  if num % 1 == 0:
    return int(num)
  else:
    return num

#function call to formatNumber function and turn float to string and store answer to alat and along
alat=str(formatNumber(a[0]))
along=str(formatNumber(a[1]))

#close csvfile.txt
csvfile.close()

#again open the file to read contents
csvfile=open("geocode.csv","r")

spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

#loop for entire data in the file
for i in spamreader:
  if i[6]==alat and i[7]==along:
    #Now, it's time to print the resultant data to screen
    print("\nDetails of the Hospital near to the give location is:")
    print("------------------------------------------------------")
    print("State:",i[0])
    print("District:",i[1])
    print("Sub District:",i[2])
    print("Facility Type:",i[3])
    print("Facility Name:",i[4])
    print("Facility Address:",i[5])
    print("Latitude:",i[6])
    print("Longitude:",i[7])
    print("ActiveFlag_C:",i[8])
    print("NOTIONAL_PHYSICAL:",i[9])
    print("Location Type:",i[10])
    print("TYPE OF FACILITY:",i[11])
    print("Nin_N:",i[12])
    print("------------------------------------------------------")
    break
input()
csvfile.close()
