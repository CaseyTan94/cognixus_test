from django.urls import path
from todo_list import views

urlpatterns = [
    path("",views.ListTodoAPIView.as_view(),name="todo_list"),
    path("create/", views.CreateTodoAPIView.as_view(),name="todo_create"),
    path("update/<int:pk>/",views.UpdateTodoAPIView.as_view(),name="update_todo"),
    path("delete/<int:pk>/",views.DeleteTodoAPIView.as_view(),name="delete_todo"),

    path("v2/<int:pk>/", views.TodoDetail.as_view()),
    path("v2/", views.TodoList.as_view()),
]