from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, response
from django.urls import reverse
from .models import Quizapplication



# Create your views here.


def home(request):
    app = Quizapplication.objects.all()
    if request.method == 'POST':
        answer = request.POST
        print(answer)
        Total_ques = len(answer)-1
        print(Total_ques)
        score = 0
        for i in answer:
            if i.isnumeric():
                result = Quizapplication.objects.filter(id = i)[0].correct_ans
                if result == answer[i]:
                    score += 1

                else:
                    print(result)
        return render(request, 'index.html', {'score':score, 'ques_answered':Total_ques, 'Total_ques':len(app), "app":app})
    
        
    return render(request, "index.html", {
        "app": app
    })

