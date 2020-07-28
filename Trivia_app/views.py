from django.shortcuts import render
from Trivia_app.models import Test
from django.shortcuts import redirect
import datetime
# Create your views here.

def home(request):
    return render(request, 'home.html')

def create_quiz(request):
    return render(request, 'create_quiz.html')

def start_quiz(request):
    if request.method == 'POST':        
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        name = request.POST.get('name')
        White = request.POST.get('White')
        Yellow = request.POST.get('Yellow')
        Orange = request.POST.get('Orange')
        Green = request.POST.get('Green')
        if White and Orange and Green and Yellow:
            answer = White + ' ' + Orange + ' ' +  Green  + ' ' + Yellow
        if White or Yellow or Orange or Green:
            if White and not Yellow and not Orange and not Green:                
                answer = White
            elif Yellow and not White and not Orange and not Green:                                
                answer = Yellow
            elif Orange and not White and not Yellow and not Green:                
                answer = Orange
            elif Green and not White and not Yellow and not Orange:                
                answer = Green
            elif Yellow and White and not Orange and not Green:            
                answer = Yellow + ' ' +  White
            elif White and Orange and not Green and not Yellow:                
                answer = White + ' ' +  Orange
            elif White and Green and not Yellow and not Orange:                                
                answer = White + ' ' + Green                
            elif White and Yellow and Orange and not Green:                
                answer = White + ' ' + Yellow + ' '  +  Orange
            elif White and Yellow and Green and not Orange:                
                answer = White + ' ' + Yellow + ' ' +  Green
            elif Yellow and Green and Orange and not White:                
                answer = Yellow + ' ' +  Green + ' ' + Orange
            elif Green and Orange and White and not Yellow:                
                answer = Green + ' ' +  Orange + ' ' + White
        if not name:
            name = answer
        if answer:
            current_date = datetime.datetime.now()            
            Test(created_at=current_date, name=name, answer=answer,question=question).save()            
            count = Test.objects.filter(name=name).count()        
            context = {
                'name':name,
            }
            if count == 1:
                context = {
                    'name':name,
                }
                return render(request, 'page1.html', context)        
            elif count == 2:
                context = {
                    'name':name,
                }
                return render(request, 'page2.html', context)        
            elif count == 3:
                details = Test.objects.filter(name=name)
                context = {
                    'name':name,
                    'details':details,
                }
                return render(request, 'result.html', context)                           
            else:
                return redirect('/')
    else:
        return render(request, 'home.html')

def view_all(request):    
    qs = Test.objects.all()
    return render(request, 'view_all.html', {'qs':qs})













