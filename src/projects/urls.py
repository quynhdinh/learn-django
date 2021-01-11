from django.urls import path

from .views import(
    ProjectCreateView,
    ProjectDeleteView,
    ProjectDetailView,
    ProjectListView,
    ProjectUpdateView,
)

app_name='projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('create/', ProjectCreateView.as_view(), name='project-create'),
    path('<int:id>/', ProjectDetailView.as_view(), name='project-detail'),
    path('<int:id>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('<int:id>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
]