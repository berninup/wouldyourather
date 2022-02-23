from optparse import Option
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import WouldYouRather
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin




def signup(request):

    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'invalid credentials - please try again'

    form = UserCreationForm
    context = {'form': form, 'error': error_message}
    return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')

def question_index(request):
    questions = WouldYouRather.objects.all()
    return render(request , 'questions/index.html', {'questions': questions})

def question_detail(request, question_id):
    question = WouldYouRather.objects.get(id=question_id)
    total = question.option_one_count + question.option_two_count
    print(total)

    return render(request, 'questions/detail.html', {
      'question': question,  
    })

def results(request, question_id):
    question = WouldYouRather.objects.get(id=question_id)
    total = question.option_one_count + question.option_two_count
    option_one_percent = int((question.option_one_count / total) * 100)
    option_two_percent = int((question.option_two_count / total) * 100)
    print(option_one_percent)
    return render(request, 'questions/results.html', {
        'question': question,
        'option_one_percent': option_one_percent,
        'option_two_percent': option_two_percent,
        'total': total
    })


def vote(request, question_id):
    question = WouldYouRather.objects.get(id = question_id)
    selected_option= request.POST['group1']
    
    

    print(selected_option)
    
    if selected_option == 'choice1':
        question.option_one_count += 1
    if selected_option == 'choice2':
        question.option_two_count += 1

    question.save()

    return redirect('results', question_id)


class WouldYouRatherCreate(LoginRequiredMixin, CreateView):
    model = WouldYouRather
    fields = ("question", "option_one", "option_two")
    
        