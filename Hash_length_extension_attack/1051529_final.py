import md5py
import struct
import sys

secret = "secret here"
initialData = "data here"
append = "something"

def pad(s):
        padlen = 64 - ((len(s) + 8) % 64)
        bit_len = 8*len(s)
        if(padlen < 64):
               s = s + '\x80' + '\x00' * (padlen - 1)
        a=struct.pack('<q', bit_len)
        a=[ chr(x) for x in a]
        b="".join(a)
        s=s+b
        return s

print ("This is the program that perform the hash attack to MD5!!!")
print ("You need to forge the signature and caculate the sum of first MagicNumber(1st)")

val = md5py.new(secret+initialData)
print ("You get the hash(secret + message1):", val.hexdigest())

#the code here:generate the signature 
payload = pad(secret+initialData)+append
legit = md5py.new(payload)
print ("The digital signature(hash(secret+message1+message2)) is:", legit.hexdigest())

#the code here:modify MagicNumber to acheive extension attack 
not_legit = md5py.new("z"*64)
not_legit.A, not_legit.B, not_legit.C, not_legit.D = md5py._bytelist2long(val.digest())
MagicSum=not_legit.A + not_legit.B + not_legit.C+ not_legit.D
not_legit.update(append)
print ("Your forged signature is:", not_legit.hexdigest())

if legit.hexdigest() == not_legit.hexdigest():
        print ("Success forged!")
        print ("Your MagicSum is:",MagicSum)
        if MagicSum==11891216107:
            print ("Correct!!!")
            print ("flag{HASH_LENGTH_EXTESION_ATTATCK}")
        else:
            print ("Wrong MagicSum!!!")
else:
        print ("Fail!")





