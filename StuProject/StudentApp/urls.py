from django.urls import path
from . import views

urlpatterns = [
    path('addstu/',views.addStudentModelForm,name='add_stu'),
    path('showstu/',views.showStudent,name='show_stu'),
    path('delete/<int:i>/',views.deleteStudent,name='delete_stu'),
    path('update/<int:i>/',views.updateStudent,name='update_stu'),
]