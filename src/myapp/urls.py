from django.urls import path
from myapp import views
app_name="myapp"


urlpatterns=[
path("m/",views.TaskList,name="list"),
path('ajax/task/',views.AjaxTaskList,name="ajax_list"),
path('l/',views.TaskDisplay,name="display"),
path('ajax/display/',views.AjaxTaskDisplay,name="ajax_display"),
path('i/',views.IndexView,name="index"),
path('ajax/index/',views.AjaxIndexView,name="getUsers"),
path('',views.UserAddView,name="add"),
path('ajax/add/user/',views.AjaxUserAddView,name="ajax_user")
]
