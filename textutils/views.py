from django.shortcuts import render
from django.http import HttpResponse
import re
# Create your views here.
def index(req):
    return render(req, 'index.html')
def charcount(req):
    charcountText = req.GET.get("text", 'default')
    return HttpResponse(f"<h1>this is char count page </br> char Count : {len(charcountText)}</h1>")

def analyzer(req):
    s = req.POST.get('text', 'default')
    removepunc = req.POST.get('removepunc', 'off')
    fullcaps = req.POST.get('fullcaps', 'off')
    newlineremove = req.POST.get('newlineremover', 'off')
    extraspaceremover = req.POST.get('extraspaceremover', 'off')
    
    analyzed = s
    if removepunc == "on":
        analyzed =  re.sub(r'[^\w\s]', '', s)

    
    if fullcaps == "on":
        print(analyzed)
        analyzed  = analyzed.upper()
    if newlineremove == "on":
        print(analyzed)
        analyzed = analyzed.replace("\n", " ").replace("\r", "")
    if extraspaceremover == 'on':
        analyzed = "  ".join(analyzed.split())
        
    return render(req, 'result.html', {'analyzed_text': analyzed, "purpose": "result is completed"})
    
def capitalfirst(req):
    return HttpResponse("<h1>this is capitalfirst page</h1>")
def space_remove(req):
    return HttpResponse("<h1>this is space remove page</h1>")
