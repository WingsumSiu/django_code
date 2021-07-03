# from django.urls import path
# from django.shortcuts import get_object_or_404, render

# from . import views


# app_name = 'my_app'
# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
   
# ]

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'my_app/results.html', {'question': question})

# general view
from django.urls import path

from . import views

app_name = 'my_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]