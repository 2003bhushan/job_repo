import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mfakerproject2.settings')
import django
django.setup()
from app1.models import *
from faker import Faker
from random import *
f=Faker()
def phonegen():
    d1=randint(6,9)
    num=""+str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)
def nagafake():
    date=f.date()
    company=f.random_element(elements=["amz",'cts','tcs','wipro','tm'])
    title=f.random_element(elements=["ase",'pde','pfs','jsf','ds'])
    eligibility=f.random_element(elements=["b.tech",'mca','mtech','bsc','phd'])
    add=f.address()
    phone=phonegen()
    email=f.email()
    hydjob.objects.get_or_create(date=date,company=company,title=title,eligibility=eligibility,add=add,phone=phone,email=email)
def bhufake():
    date=f.date()
    company=f.random_element(elements=["amz",'cts','tcs','wipro','tm'])
    title=f.random_element(elements=["ase",'pde','pfs','jsf','ds'])
    eligibility=f.random_element(elements=["b.tech",'mca','mtech','bsc','phd'])
    add=f.address()
    phone=phonegen()
    email=f.email()
    bngjob.objects.get_or_create(date=date,company=company,title=title,eligibility=eligibility,add=add,phone=phone,email=email)
def raofake():
    date=f.date()
    company=f.random_element(elements=["amz",'cts','tcs','wipro','tm'])
    title=f.random_element(elements=["ase",'pde','pfs','jsf','ds'])
    eligibility=f.random_element(elements=["b.tech",'mca','mtech','bsc','phd'])
    add=f.address()
    phone=phonegen()
    email=f.email()
    chennaijob.objects.get_or_create(date=date,company=company,title=title,eligibility=eligibility,add=add,phone=phone,email=email)
n=int(input("enter"))
for i in range(n):
    nagafake()
    raofake()
    bhufake()
print("successfully") 
