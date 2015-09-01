from django.shortcuts import render

# Create your views here.

def index(request):
    #question_list = Question.objects.all()

    return render(
        request,
        "index.html",
        #{'question_list': question_list},
    )

