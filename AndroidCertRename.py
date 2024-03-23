import os
import sys
from cryptography import x509
from hashlib import md5

if(len(sys.argv)==1):
    print(f"Usage: {sys.argv[0]} certificate_path")
    quit()
cert_path=sys.argv[1]
cert_dir=os.path.dirname(cert_path)
if not os.path.exists(cert_path):
    print(f"certificate path {cert_path} not exist")
    quit()
new_name=""
with open(cert_path,"rb") as file:
    cert=x509.load_pem_x509_certificate(file.read())
    new_name=format(int.from_bytes(md5(cert.subject.public_bytes()).digest()[0:4],byteorder="little"),"08x")+".0"
os.rename(cert_path,os.path.join(cert_dir,new_name))
print(f"File has been renamed to {new_name}")