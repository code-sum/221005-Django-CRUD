from django.shortcuts import render

# Create your views here.

# 요청 정보를 받아서..
def index(request):

    # 원하는 페이지를 render..
    return render(request, 'articles/index.html')