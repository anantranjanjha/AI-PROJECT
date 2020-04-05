import psutil

file1 = open("Ai.txt","a")

#Boot Time Checking

boot_time=psutil.boot_time()
if(boot_time>1583211793.0):                        #Boot Time value Taken In PAst
    file1.write("boot Time Increased\n")
else:
    file1.write("Boot Time Decreased\n")
file1.write("Boot time While Writing Program = 1583211793.0 \n")
file1.write("Current Boot Time = ") 
file1.write(str(boot_time)+"\n")

file1.write("********************************************************************************************************************************************\n")

#CPU FREQUENCY CHECKING

freq=psutil.cpu_freq()
file1.write(str(freq)+"\n")
file1.write("Freq Checked While Writing Program = scpufreq(current=1500.0, min=0.0, max=1801.0)\n")
file1.write("********************************************************************************************************************************************\n")
#Battery

battery=psutil.sensors_battery()
file1.write(str(battery)+"\n")
if(battery.power_plugged==False):
    secsperpercentage=battery.secsleft/battery.percent
file1.write(str(secsperpercentage)+" Current Seconds/percentage \n")
file1.write("Battery Average While Writing Program 53687091.1875 Seconds/percentage\n")

file1.write("********************************************************************************************************************************************\n")
file1.close() 
file1 = open("Ai.txt","r")
file1.readlines()