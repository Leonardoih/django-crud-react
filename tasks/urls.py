from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from tasks import views

#api versioning
router = routers.DefaultRouter()
router.register(r"tasks", views.TaskView, "tasks")

urlpatterns = [
    path("api/v1/",include(router.urls) ),
    path("docs/", include_docs_urls(title="Tasks API")),
    
    
]

"""este codigo genera una api rest con django y django rest framework
GET /api/v1/tasks/ -> lista todas las tareas
POST /api/v1/tasks/ -> crea una tarea
GET /api/v1/tasks/1/ -> muestra la tarea con id 1
PUT /api/v1/tasks/1/ -> actualiza la tarea con id 1
DELETE /api/v1/tasks/1/ -> elimina la tarea con id 1
"""