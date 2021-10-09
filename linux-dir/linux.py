import platform, os
import datetime, time

#platform information
plat = "Platform: " + platform.platform()

a = platform.system() #platform type extract

if (a == "Linux"): #check the platform type

    #initialize , sort and print the system time and year
    x = datetime.datetime.now()
    timeL  = x.strftime("%a %b %m %H:%M:%S")
    timezone = time.strftime(str(time.timezone))
    year = x.strftime("%Y")

    path = os.path.expanduser("~/Desktop/Entries_Lin.log") #path to the file

    f1 = open(path, "w") #create a log file to write details

    f1.write(plat + "\n \n" + timeL + " " + timezone + " " + year + "\n \n") #write the platform date and time details in the log file
    
    #access folders and subfolders in /usr/lib path -> write into the log file
    os.system('find /usr/lib/ -name "*.bin" -type f >>'+path)

    print("Log file is created at: " + path)