from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from TestManagement.models.project import APIProject
from TestManagement.forms import ProjectForm


@login_required
def APIProject_manage(request):
    """
    Login successful, project management
    :param request:
    :return:
    """
    project_all = APIProject.objects.all()
    return render(request, "APIProject.html", {"APIProjects": project_all, "type": "list"})


@login_required
def add_project(request):
    """
    Add a new project
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "APIProject.html", {"type": "add"})
    elif request.method == "POST":
        project_name = request.POST.get("project_name", "")
        project_description = request.POST.get("project_description", "")
        project_status = request.POST.get("project_status", "")
        if project_name == "":
            return render(request, "APIProject.html", {"type": "add", "name_error": "Project name cannot be blank."})
        APIProject.objects.create(name=project_name, describe=project_description, status=project_status)
        return HttpResponseRedirect("/APIProject/")


@login_required
def edit_project(request, pid):
    """
    Edit a new project
    :param request:
    :return:
    """

    if request.method == "GET":
        if pid:
            p = APIProject.objects.get(id=pid)
            form = ProjectForm(instance=p)
            return render(request, "APIProject.html", {"type": "edit", "form": form, "id": pid})
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            describe = form.cleaned_data["describe"]
            status = form.cleaned_data["status"]
            update = APIProject.objects.get(id=pid)
            update.name = name
            update.describe = describe
            update.status = status
            update.save()
            return HttpResponseRedirect("/APIProject/")


