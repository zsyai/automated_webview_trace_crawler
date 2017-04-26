import pexpect 
import time  
def sshcmd(usr, ip, passwd, cmd): 
  ret = -1
  ssh = pexpect.spawn('ssh %s@%s "%s"' % (usr, ip, cmd)) 
  try: 
    i = ssh.expect(['password:', 'continue connecting (yes/no)?'], timeout=5) 
    if i == 0 : 
      ssh.sendline(passwd) 
    elif i == 1: 
      ssh.sendline('yes\n') 
      ssh.expect('password: ') 
      ssh.sendline(passwd) 
    ssh.sendline(cmd) 
    r = ssh.read() 
    file_object = open('thefile.txt', 'w')
    file_object.write(r)
    file_object.close( )
    ret = 0
  except pexpect.EOF: 
    print "EOF"
    ssh.close() 
    ret = -1
  except pexpect.TIMEOUT: 
    print "TIMEOUT"
    ssh.close() 
    ret = -2 
  return ret

def scpcmd(usr, ippath, localpath, passwd): 
  ret = -1
  ssh = pexpect.spawn('scp %s@%s %s' % (usr, ippath, localpath)) 
  try: 
    i = ssh.expect(['password:', 'continue connecting (yes/no)?'], timeout=5) 
    if i == 0 : 
      ssh.sendline(passwd) 
    elif i == 1: 
      ssh.sendline('yes\n') 
      ssh.expect('password: ') 
      ssh.sendline(passwd)
    #time.sleep(120) 
    r = ssh.read() 
    #print r
    ret = 0
  except pexpect.EOF: 
    print "EOF"
    ssh.close() 
    ret = -1
  except pexpect.TIMEOUT: 
    print "TIMEOUT"
    ssh.close() 
    ret = -2 
  return ret

#sshcmd('pkusei','162.105.175.15','pkucloud','ls ~/wandoujia-apks/data/')
#scpcmd('pkusei','162.105.175.15:~/wandoujia-apks/data/018*.apk','/home/liang/Desktop/500app/ApkRepo/','pkucloud')
