from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("Hello, Good Morning")

# def about(request):
#     return HttpResponse('''About <a href = "https://getbootstrap.com/docs/5.3/getting-started/introduction/">BootStrap</a>''')


def index(request):
    # return HttpResponse("Hello, Good Morning")
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removeFunc = request.POST.get('removeFunc', 'off')
    toupper = request.POST.get('toupper', 'off')
    newliineremover = request.POST.get('newliineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    # print(removeFunc)
    # print(djtext)
    if removeFunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
             analyzed = analyzed + char  
        params = {'purpose':'Removed punctuations', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    
    if toupper == 'on':
        analyzed = ""
        for char in djtext:
             analyzed = analyzed + char.upper()  
        params = {'purpose':'Converted to UPPER CASE', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed

    
    if newliineremover == 'on':
        analyzed = ""
        for char in djtext:
                if char !="\n" and char != "\r":
                 analyzed = analyzed + char  
        params = {'purpose':'New Lines Removed', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed

    
    if spaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and  djtext[index + 1] == " "):
                analyzed = analyzed + char  
        params = {'purpose':'Extra Space Removed', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed

    
    if charcount == 'on':
        count = 0
        for char in djtext:
            count = count + 1
        params = {'purpose':'Character count', 'analyzed_text':count}
        # return render(request, 'analyze.html', params)
        # djtext = count

    if removeFunc != "on" and toupper != "on" and newliineremover != "on" and spaceremover !="on" and charcount != "on":
        return HttpResponse("Need to click the option!")   


    return render(request, 'analyze.html', params)


  
    




# def removeFunc(request):
#     print(request.GET.get('text', 'default'))
#     return HttpResponse("Remove Func")

# def capitalizeFirst(request):
#     return HttpResponse("capitalizeFirst")

# def newlineremover(request):
#     return HttpResponse("newlineremover")

# def spaceremover(request):
#     return HttpResponse("spaceremover")

# def charcount(request):
#     return HttpResponse("charcount")