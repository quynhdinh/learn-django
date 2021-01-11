from django.shortcuts import render,get_object_or_404
from django.urls import reverse

from django.views.generic import(
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView

)

from .forms import ProjectModelForm
from .models import Project

class ProjectCreateView(CreateView):
    template_name = 'projects/project_create.html'
    form_class = ProjectModelForm
    queryset = Project.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ProjectListView(ListView):
    template_name = 'projects/project_list.html'
    queryset = Project.objects.all()

class ProjectDetailView(DetailView):
    template_name = 'projects/project_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Project, id=id_)

class ProjectUpdateView(UpdateView):
    template_name = 'projects/project_create.html'
    form_class = ProjectModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Project, id=id_)

    def form_valid(selfself, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ProjectDeleteView(DeleteView):
    template_name='projects/project_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Project, id=id_)

    def get_success_url(self):
        return reverse('project:project-list')