from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, export_tasks_pdf
from .views import chatbot_response

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('export/pdf/', export_tasks_pdf, name='export_tasks_pdf'),
    path('chatbot/', chatbot_response, name='chatbot'),

]
