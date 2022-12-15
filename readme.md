In serial task:

Command to run the program:

- for mac user:
    python3 serial_md5.py

- for windows user
    python serial_md5.py

When program runs it will ask you for your encryption password. You can pass any password you want and it will do
file encryption based on your password.
After getting password from user, it will open wordlist file and traverse each word and encrypt it,
After encryption it will save encryption string of each word in output folder.
After the encryption completed.
Program will ask you to pass any md5 hash. You can copy hash from output folder and pass it over there.
The program will then decrypt the hash and find the plain text word in the wordlist file.
The time is find using the time library and we can see how much time it will take on encryption and decryption.


In parallel task:
The steps remain same but in this program, we run the program in multi threaded manner using multiprocessing library.
This program will then divide the program into different processess and do encryption and decryption.
This will then join the process. We can calculate the time as done in serial code.

