from django.urls import path

from .views import(
    ProjectCreateView,
    ProjectDeleteView,
    ProjectListView,
    ProjectUpdateView,
)

app_name='projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list')
]