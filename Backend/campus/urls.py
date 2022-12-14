from django.urls import path
from .views import *

urlpatterns = [
    path('building/', BuildingAllView.as_view()), # 전체 빌딩 조회 및 추가
    path('building/<int:building_pk>/', BuildingView.as_view()), # 특정 빌딩 세부사항 + 해당 빌딩 내 모든 층 목록 조회, 빌딩 수정 및 삭제
    path('floor/<int:floor_pk>/', FloorView.as_view()), # 특정 층 세부사항 + 해당 층 내 모든 그룹 목록 조회, 층 수정 및 삭제
    path('trashbin/<int:trashbin_pk>/', TrashbinView.as_view()), # 특정 쓰레기통 세부사항
    path('student/', StudentAllView.as_view()), # 학생 전체 목록 조회
    path('student/<int:student_pk>/', StudentView.as_view()), # 특정 학생 수정 및 삭제
    path('notification/', NotificationView.as_view()), # 쓰레기통 알림
    path('trashbin/record/', RecordView.as_view()),

]
