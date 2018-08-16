from django.urls import path, re_path


from .views import *

# url 이름을 가지고 패턴을 찾고자 할 때 namespace를 사용하려면 app_name 이 필수

app_name = 'bookmark'

urlpatterns = [

    # name으로 맨앞에 url 패턴을 찾고 싶을 때

    # 함수형 뷰는 함수이름만
    # 클래스형 뷰는 클래스이름.as_view()

    path('', BookmarkListView.as_view(), name='list'),
    path('write/', BookmarkCreateView.as_view(), name='write'),

    # <1:2> 1.데이터타입 / data 이름
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', BookmarkDetailView.as_view(), name='detail'),

    # re_path (regexp,,), 정규식

]
