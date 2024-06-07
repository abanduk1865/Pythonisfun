# People speed because it saves time  when your traveling to a place.
# My program will calculate the time that will be saved speeding.
# I will compare the time spent speeding vs going the speed limit.
# The time saved will be reported in minutes.

speed = float(input("Enter your average speed in miles/hour"))
speedlimit = float(input(" Enter miles/ hour speed limit "))
distance =  float(input( "enter the distance in miles "))
                  
time= distance / speedlimit
speedtime = distance / speed


print(time, speedtime)
                  
Minutes_in_hour = 60

speedtimein = speedtime*Minutes_in_hour
timein = time*Minutes_in_hour

if speed > speedlimit:
     savedtime =timein-speedtimein
else:
    print(" safe driver but no time saved")

print(f'time taken at your speed {speedtimein:.2f} minutes')
print(f'time taken at speed limit {timein:.2f} minutes')
print(f'time saved in minutes {savedtime:.2f}')                  
