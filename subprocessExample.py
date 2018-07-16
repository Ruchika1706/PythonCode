#subprocess is used to run the Linux commands
#it allows us to spawn processes , connect to their input/output/error pipes and obtain their return codes 
#Popen class to handle the creation and management in subprocess module. 
#communicate() returns a tuple, (stdoutdata, stderrdata), communicate means you want to execute the command 
import subprocess
pl = subprocess.Popen(['ps', '-U','0'], stdout=subprocess.PIPE).communicate()[0]
#p1 is array of bytes, decode in unicode representation 
print(pl.decode('utf-8'))
