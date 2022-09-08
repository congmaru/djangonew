from django.shortcuts import render, redirect, get_object_or_404
from .models import Maru
from django.views.decorators.http import require_http_methods,require_POST
from .forms import MaruForm

# Create your views here.
def index(request):
    maru = Maru.objects.all()
    context = {
        'maru' : maru,
    }
    return render(request, 'cong/index.html', context)

#GET, POST 2가지 http method 요청이 들어오므로, 데코레이터 사용
@require_http_methods(['GET','POST'])
def create(request):
    #사용자의 입력 후 요청이 왔을 때
    if request.method =='POST':
        form = MaruForm(request.POST)
        #유효성검사
        if form.is_valid():
            #form.save()는 객체를 반환한다
            maru = form.save()
            return redirect('cong:index')
    #사용자가 처음으로 생성 페이지에 접근했을 때
    else:
        #form을 만들고
        form = MaruForm()
    context={
        'form':form,
    }
    return render(request, 'cong/create.html', context)

def detail(request, pk):
    # maru = Maru.objects.get(pk=pk)
    # get_object_or_404 = 데이터를 조회하지 못하면 404에러를 띄워라
    # 일반적으로 웹에서 없는 데이터 조회시 404 에러를 띄움
    # 웹 서버랑 연동하게 되면 더 자세히 이해할 수 있음
    maru = get_object_or_404(Maru, pk=pk)
    context = {
        'maru':maru,
    }

    return render(request, 'cong/detail.html', context)


@require_http_methods(['GET','POST'])
def update(request,pk):
    maru=get_object_or_404(Maru,pk=pk)
    if request.method == 'POST':
        form = MaruForm(request.POST, instance=maru)
        if form.is_valid():
            form.save()
            return redirect('cong:detail', maru.pk)
    else:
        form = MaruForm(instance=maru)
    context = {
        'maru':maru,
        'form':form,
    }
    return render(request, 'cong/update.html', context)

@require_POST
def delete(request,pk):
    maru=get_object_or_404(Maru,pk=pk)
    maru.delete()
    return redirect('cong:index')