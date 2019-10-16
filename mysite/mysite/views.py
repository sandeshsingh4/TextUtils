# I have created these file - sandesh
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html')
    #return HttpResponse("<h1>Home Page</h1>")

def aboutus(request):
    return render(request,'aboutus.html')
    #return HttpResponse("<h1>Home Page</h1>")

def contactus(request):
    return render(request,'contactus.html')
    #return HttpResponse("<h1>Home Page</h1>")

def analyze(request):
    # Get the text
    dj_text = request.POST.get('text','default')

    # Check the checkbox value
    remove_punc = request.POST.get('remove_puncuation','off')
    upper_case = request.POST.get('capitalize','off')
    new_line_removers = request.POST.get('new_line_remover','off')
    character_counter = request.POST.get('char_count','off')
    #analyzed = ""
    #Check which checkbox value is ON
    if remove_punc == "on":
        puncuations = '''!()-[]{};:''""\,<>./?@#$%^&*~_'''
        analyzed = ""
        for char in dj_text:
            if char not in puncuations:
                analyzed += char
        params = {'purpose':'Remove Puncuations', 'analyzed_text': analyzed}
        dj_text = analyzed
        #return render(request,'analyze.html', params)
        #return HttpResponse(remove_punc,"<h1>remove_puncuation Page<a href = '/'>back</a></h1>")

    if(upper_case == "on"):
        analyzed = ""
        analyzed += dj_text.upper()
        params = {'purpose': 'Capitalized Text', 'analyzed_text': analyzed}
        dj_text = analyzed
        #return render(request, 'analyze.html', params)

    if (new_line_removers == "on"):
        analyzed = ""
        for char in dj_text:
            if char != "\n" and char!="\r":
                analyzed += char
        params = {'purpose': 'Removed New Line Character', 'analyzed_text': analyzed}
        dj_text = analyzed
        #return render(request, 'analyze.html', params)

    if (character_counter == "on"):
        analyzed = ""
        char_count = 0
        for char in dj_text:
            if char != " ":
                char_count += 1
        params = {'purpose': 'Total Number of Character', 'analyzed_text': char_count}
        dj_text = analyzed
        #return render(request, 'analyze.html', params)

    if(upper_case != "on" and char_count!= "on" and new_line_removers != "on" and upper_case!= "on"):
        return HttpResponse("Error 404")

    return render(request, 'analyze.html', params)