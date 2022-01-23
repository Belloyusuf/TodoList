from django.urls import path
from .views import StudentCreateView, StudentDeleteView, StudentUpdateView,\
    StudentListView, StudentDetailView, Display_allListView


urlpatterns = [
    path("add/", StudentCreateView.as_view(), name="add"),
    path("", StudentListView.as_view(), name="student_list"),
    path("update/<int:pk>/", StudentUpdateView.as_view(), name="student_update"),
    path("detail/<int:pk>/", StudentDetailView.as_view(), name="student_detail"),
    path("delete/<int:pk>/", StudentDeleteView.as_view(), name="student_delete"),
    path("display/", Display_allListView.as_view(), name="display_all"),
]
