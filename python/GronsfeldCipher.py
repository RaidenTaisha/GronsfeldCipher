import string

alphupper = string.ascii_uppercase  #большие буквы
alphlower = string.ascii_lowercase  #маленькие буквы
msg = input()
key = input()
while ( len(msg)-len(key) < 0 ):
    buff = key[len(key)-1]
    key.replace(buff, "")

print(key)
