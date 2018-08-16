from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# view의 두종류 : 함수형 / 클래스형
# 장고의 목적 : 귀찮은거 하기 싫어서
# 클래스형 : 자주 쓰는 기능을 상속 받아서 간단하게 생성

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bookmark
from django.urls import reverse_lazy

# list view
class BookmarkListView(ListView):
    model = Bookmark
    # 클래스형 뷰는 기본적으로 렌더링할 템플릿 파일이 지정이 되어 있습니다.
    # bookmark/bookmark_list.html


class BookmarkCreateView(CreateView):
    model = Bookmark # 입력화면에 출력된 form 태그를 자동으로 만들어 줌.
    # _form 원레이름 : create, update 에서 사용
    template_name_suffix = '_create'
    # 입력받을 필드 목록
    fields = ['site_name','url']
    # get_absulte_url 를 호출 아래가 없으면
    success_url = reverse_lazy('bookmark:list')


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    template_name_suffix = '_update'
    fields = ['site_name','url']


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')


class BookmarkDetailView(DetailView):
    model = Bookmark


# def list(request):
#     return HttpResponse("List Page")

# def write(request):
#     return HttpResponse("Write Page")

# def update(request):
#     return HttpResponse("Update Page")

# def delete(request):
#     return HttpResponse("Delete Page")