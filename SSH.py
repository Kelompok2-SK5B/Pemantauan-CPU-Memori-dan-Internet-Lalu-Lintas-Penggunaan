from paramiko.client import SSHClient,AutoAddPolicy

client = SSHClient()
client2 = SSHClient()

client.set_missing_host_key_policy(AutoAddPolicy())
client.connect("10.0.2.15",22,"rani","toxicteros")

client2.set_missing_host_key_policy(AutoAddPolicy())
client2.connect("192.168.43.43",22,"dellasantika","raimunanasional")

while(True):  
  stdin,stdout,stderr = client.exec_command('python3 ppmonitoring.py')
  stdin, stdout, stderr = client.exec_command('python3 Keliling&Luas.py')
  
  lines = stdout.readlines()
  lines_err = stderr.readlines()

  lines2 = stdout.readlines()
  lines_err2 = stderr.readlines()
  
  for i in lines_err:
    print(i)
  for i in lines:
    print(i)

client.close()
