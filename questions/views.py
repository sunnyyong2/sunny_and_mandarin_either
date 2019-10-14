from django.shortcuts import render, redirect
from .models import Question, Choice, Comment
import random
# Create your views here.


def index(request):
    questions = Question.objects.all()

    if questions:
        question = random.choice(questions)
    else:
        question = ''

    context = {
        'question': question
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == "POST":
        content = request.POST.get('content')
        choice1 = request.POST.get('choice1')
        choice2 = request.POST.get('choice2')

        question = Question.objects.create(
            content=content,
            choice1=choice1,
            choice2=choice2
        )

        c1 = Choice.objects.create(
            question=question,
            content=choice1,
            count=0
        )

        c2 = Choice.objects.create(
            question=question,
            content=choice2,
            count=0
        )

        return redirect('questions:index')
        # question을 만든다
    else:
        return render(request, 'form.html')


def update(request, q_id):
    question = Question.objects.get(id=q_id)

    if request.method == "POST":
        content = request.POST.get('content')
        choice1 = request.POST.get('choice1')
        choice2 = request.POST.get('choice2')

        question.content = content
        question.choice1 = choice1
        question.choice2 = choice2
        question.save()

        choices = question.choice_set.all()
        c1 = choices[0]
        c2 = choices[1]
        c1.content = choice1
        c2.content = choice2

        c1.save()
        c2.save()

        return redirect('questions:detail', q_id)

    else:

        context = {
            'question': question
        }

        return render(request, 'form.html', context)


def detail(request, q_id):
    question = Question.objects.get(id=q_id)

    choices = question.choice_set.all()
    c1 = choices[0]
    c2 = choices[1]
    total = choices[0].count + choices[1].count

    if total == 0:
        c1_ratio = 0
        c2_ratio = 0
    else:
        c1_ratio = round((choices[0].count / total)*100, 2)
        c2_ratio = round((choices[1].count / total)*100, 2)

    context = {
        'question': question,
        'c1': c1,
        'c2': c2,
        'c1_ratio': c1_ratio,
        'c2_ratio': c2_ratio
    }

    return render(request, 'detail.html', context)


def delete(request, q_id):
    question = Question.objects.get(id=q_id)
    question.delete()

    return redirect('questions:index')


def choice_update(request, q_id, c_id):
    choice = Choice.objects.get(id=c_id)
    choice.count += 1
    choice.save()

    return redirect('questions:detail', q_id)


def create_comment(request, q_id, c_id):
    choice = Choice.objects.get(id=c_id)

    username = request.POST.get('username')
    text = request.POST.get('text')

    Comment.objects.create(choice=choice, username=username, text=text)

    return redirect('questions:detail', q_id)
