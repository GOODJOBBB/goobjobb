from django.shortcuts import render, redirect
from .models import Firstapp
from .forms import MemoForm
# Create your views here.


def index(request):
    context = dict()
    request.POST.get('mydata')
    all_memo = Firstapp.objects.all()
    context['all_memo'] = all_memo
    return render(request, 'index.html',context)

def detail(request, detail_id):
    context={}
    one_memo = Firstapp.objects.get(id=detail_id) #예를 들면 5번 id 글을 가져오겠다는것
    
    context['one_memo'] = one_memo
    return render(request, 'detail.html', context)

def create(request):
    context=dict()
    context['memoform'] = MemoForm()
    if request.method =="POST":
        myform = MemoForm(request.POST,request.FILES)
        if myform.is_valid():
            myform.save()
            return redirect('index')
        else:
            context['memoform']=myform
    return render(request, 'create.html',context)
