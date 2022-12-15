from multiprocessing import Process
import platform
import psutil
import time
import sys
import hashlib
import time
import os

root_dir = os.getcwd()

def encryption(filename, password):
    f = False
    write_file = open(root_dir+"/output/encrypted-parallel.txt", "w")
    try:
        passfile = open(root_dir+"/input/"+filename, "r")
    except:
        print("Wordlist Not Found !!")
        sys.exit(0)
    print("working....")
    pass_wrd = password.encode('utf-8')
    password_digest = hashlib.md5(pass_wrd.strip()).hexdigest()
    for word in passfile:
        enc_wrd = word.encode('utf-8')
        digest  = hashlib.md5(enc_wrd.strip()).hexdigest()
        write_file.write((digest + password_digest) + "\n")
    print('Done')

def decryption(filename, hash, password):
  passfile = open(root_dir+"/input/"+filename,"r")
  found = 0
  for word in passfile:
    wordhash = hashlib.md5(word.encode('utf-8').strip()).hexdigest()
    passhash = hashlib.md5(password.encode('utf-8').strip()).hexdigest()
    finalhash = wordhash + passhash
    if finalhash == hash:
      print("plain text of the given hash is ",word)
      found = 1
      break

  if found == 0:
    print('Word with the given hash not found..!')

if __name__ == '__main__':
  print('System Details\n')

  print("="*40, "System Information", "="*40)
  uname = platform.uname()
  print(f"System: {uname.system}")
  print(f"Node Name: {uname.node}")
  print(f"Release: {uname.release}")
  print(f"Version: {uname.version}")
  print(f"Machine: {uname.machine}")
  print(f"Processor: {uname.processor}")

  print("="*40, "CPU Info", "="*40)

  print("Physical cores:", psutil.cpu_count(logical=False))
  print("Total cores:", psutil.cpu_count(logical=True))

  cpufreq = psutil.cpu_freq()
  print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
  print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
  print(f"Current Frequency: {cpufreq.current:.2f}Mhz")

  print("\nWelcome to md5 encryption/decryption..\n\n")

  while(1):
      print("Your Choice\n")
      print("1. Encryption")
      print("2. Decryption")
      print("3. Exit")
      choice = str(input("Enter your choice: "))
      if choice == '1':
        password = input('\nEnter Password for your encryption: ')
        start = time.time()
        p = Process(target=encryption, args=('wordlist.txt',password))
        p.start()
        p.join()
        end = time.time()

        print('Time for encryption: ', (end-start),'seconds')
      elif choice == '2':
        passwordhash = input("enter the hash to crack: ")
        password = input('Enter the same Password you used for encryption: ')
        start = time.time()
        p = Process(target=decryption, args=('wordlist.txt',passwordhash, password))
        p.start()
        p.join()
        end = time.time()

        print('Time for decryption: ', (end-start),'seconds')
      elif choice == '3':
        sys.exit(0)
      else:
        print("Invalid Choice\n")
