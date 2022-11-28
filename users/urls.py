from . import views
from django.urls import path
from .views import CreateForm, CreateComment, CreateUni

app_name = 'users'

urlpatterns = [
    path('form/', views.FormsListView.as_view(), name='form_list'),
    path('formcreate/', CreateForm.as_view(), name='create_form'),
    path('comment/', views.CommentListView.as_view(), name='comment_list'),
    path('commentcreate/', CreateComment.as_view(), name='create_comment'),
    path('uni/', views.UniListView.as_view(), name='university_list'),
    path('unicreate/', CreateUni.as_view(), name='create_university'),
]


