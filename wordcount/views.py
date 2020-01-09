# view.py directs urls to requested html pages using functions. It acts as a mediator between url routing and the html pages
# and the other important task of views.py is that it lets you code in python and enables passing information to the requested html pages
# We can also write pyton code inside html by using {%  %}

from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def count(request):
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}

    for word in wordlist:

        if word[0].lower() in alphabets:
            if word in worddictionary:
                worddictionary[word] += 1

            else:
                worddictionary[word] = 1
        else:
            wordlist.remove(word)

    sortedwords = sorted(worddictionary.items(),key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{'count':len(wordlist),'fulltext':fulltext, 'sortedwords':sortedwords})
