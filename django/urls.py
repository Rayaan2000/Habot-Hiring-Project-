from django.urls import path

from .views import StudentCreateAPIView


urlpatterns = [

    path(
        "students/",
        StudentCreateAPIView.as_view(),
        name="student-create"
    ),

]