import re


from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    params={'name':'Praveen','Lastname':'Acharya'}
    return render(request,'index1.html',params)
    
def about(request): 
    punctuations = '''!()-[]{};:'"\,.<>/?@#$%^&*_~'''
    newline="\n"
    txt=request.POST.get('text','defualt')
    space_remover=request.POST.get('spaceremover','off')
    check_box=request.POST.get('remove','off') #check box on or not 4
    upper_case=request.POST.get('uppercase','off')
    lower_case=request.POST.get('lowercase','off')
    line_remove=request.POST.get('lineremove','off')
    filtered_text=txt
    params={'checkbox':check_box,'txt':txt}
    
    if space_remover=='on':
        new_text=""
        for index in filtered_text:
            if index!=" " or (new_text and new_text[-1]!=" ") :
                new_text+=index
        
        if filtered_text[len(filtered_text)-1]!=" ":
            new_text+=filtered_text[len(filtered_text)-1]
        filtered_text=new_text
        params={'checkbox':check_box,'txt':filtered_text}
    filtered_text=""
    if check_box=='on':
        for sym in params['txt']:
            if sym not in punctuations:
                filtered_text+=sym  
        params['txt']=filtered_text
    if check_box=='off':
        filtered_text=txt
    
    if upper_case=='on':
        temp=params['txt']
        temp=temp.upper()
        params['txt']=temp
        print(params)
        
        
    filtered_text=params['txt']

    if line_remove=='on': 
        text=""
        for char in filtered_text:
            if char!="\n" and char!="\r":
                text+=char
        params['txt']=text


        

    if lower_case=='on':
        temp=params['txt']
        temp=temp.lower()
        params['txt']=temp
        
    params['count']=len(params['txt'])
      
    return render(request,'about1.html',params)

def contact_us(request):
    return render(request,'contactus.html',params)

