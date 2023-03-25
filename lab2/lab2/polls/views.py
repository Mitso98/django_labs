from django.utils import timezone
from django.shortcuts import render, redirect
from polls.models import Questions, Votes
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.db.models import Sum
from django.core.paginator import Paginator
from polls.forms import QuestionsForm
from django.contrib import messages
# Create your views here.


def showAllQuestions(req):
    questions = Questions.objects.all().order_by('id')
    # votes = Votes.objects.values('question_id_id').annotate(
    #     count=Sum('up_down')).order_by('question_id_id')

    # setup pagination
    p = Paginator(questions, 1)
    page = req.GET.get('page')
    questions_paginated = p.get_page(page)

    ctx = {
        'questions': questions_paginated,
    }
    return render(req, 'polls_index.html', ctx)


def showQuestion(req, id):
    q = get_object_or_404(Questions, id=id)
    ctx = {
        'question': q
    }
    return render(req, 'polls_question_details.html', ctx)


def create_question(req):
    if req.method == 'POST':
        form = QuestionsForm(req.POST)
        if form.is_valid():
            q = form.save(commit=False)
            q.pub_date = timezone.now()
            q.user_id = req.user.id
            q.save()
            return redirect('polls')
    else:
        form = QuestionsForm()

    ctx = {
        'form': form
    }
    return render(req, 'add_poll.html', ctx)


def delete_question(req, id):
    q = get_object_or_404(Questions, id=id)
    if q.user_id == req.user.id:
        q.delete()
        return redirect('polls')
    else:
        messages.success(req, 'You are not authorized to delete his question!')
        return redirect('polls')


def update_question(req, id):
    q = get_object_or_404(Questions, id=id)
    if q.user_id == req.user.id:
        if req.method == 'POST':
            q.question_text = req.POST['question_text']
            q.save()
            return redirect('polls')
        else:
            form = QuestionsForm()
            return render(req, 'poll_update.html', {'form': form})

    messages.success(
        req, 'You are not authorized to update his question!')
    return redirect('polls')


def up_vote(req, q_id, user_id):
    vote = Votes(question_id=q_id, user_id=user_id, up_down=1)
    vote.save()

    return redirect(req.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def down_vote(req, q_id, user_id):
    vote = Votes(question_id=q_id, user_id=user_id, up_down=-1)
    vote.save()
    return redirect(req.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
