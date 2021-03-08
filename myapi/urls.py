from django.urls import include, path
from . import views


urlpatterns = [
    path('list/', views.GetAllRecords.as_view()),
    path('read/<int:pk>', views.GetRecord.as_view()),
    path('create/', views.CreateRecord.as_view()),
    path('modify/<int:pk>', views.ModifyRecord.as_view()),
    path('remove/<int:pk>', views.RemoveRecord.as_view()),
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
]
