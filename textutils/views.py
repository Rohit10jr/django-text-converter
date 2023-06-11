#i have created this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name':'rohit', 'place':'cosmos'}
    return render(request, 'index.html', params)

def analyze(request):
    #getting the text
    djtext=request.POST.get('text', 'default')

    #check the checkbox values
    removepunc=request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    extraspaceremover=request.POST.get('extraspaceremover', 'off')

    #check which checkbox is on 
    if removepunc == "on":

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^*_~'''
        analyzed=''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'removed punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    
    if(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
       
        params={'purpose':'changed to uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    
    if(newlineremover=='on'):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
       
        params={'purpose':'removed newlines', 'analyzed_text': analyzed}
        djtext=analyzed 
        # return render(request, 'analyze.html', params)
    

    if(extraspaceremover=='on'):
        analyzed=""
        for index, char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
       
        params={'purpose':'removed newlines', 'analyzed_text': analyzed}
        # djtext=analyzed
        # return render(request, 'analyze.html', params)

    if (removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on" ):
        return HttpResponse("error, simply not working")
        
    
    return render(request, 'analyze.html', params)

#just an example endpoint
def ex1(request):
    s = '''<h2>NAVIGATION  BAR</h2>
        <a href="https://www.apple.com">apple</a><br>
        <a href="http://www.google.com">google</a><br>
        <a href="http://www.microsoft.com">microsoft</a><br>
        <a href="http://www.aramco.com">aramco</a><br>
        <a href="http://www.amazon.com">amazon</a><br>'''
    return HttpResponse(s)

