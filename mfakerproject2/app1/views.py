from django.shortcuts import render
from app1.models import *
def hyd_get(req):
    hd=hydjob.objects.all()
    type="hydjobs"
    return render(req,"app1/hyd.html", context={"hd":hd,"type":type})
def bng_get(req):
    hd=bngjob.objects.all()
    type="bengjobs"
    return render(req,"app1/hyd.html", context={"hd":hd,"type":type})
def chennai_get(req):
    hd=chennaijob.objects.all()
    type="chjobs"
    return render(req,"app1/hyd.html", context={"hd":hd,"type":type})
def home(req):
    return render(req,"app1/index.html")
