from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth


# Create your views here.


def index(request):
    """
    Login actions
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "index.html")
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        if username == "" or password == "":
            return render(request, "index.html", {"error": "Username or password cannot be blank."})

        user = auth.authenticate(username=username, password=password)
        if user is None:
            return render(request, "index.html", {"error": "Invalid username or password."})
        else:
            auth.login(request, user)  # record login status
            return HttpResponseRedirect("/APIProject/")


def logout(request):
    """
    Logout actions
    :param request:
    :return:
    """
    auth.logout(request)
    return HttpResponseRedirect("/index/")