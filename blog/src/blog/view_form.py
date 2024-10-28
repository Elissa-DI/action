from . import models, forms
from django.shortcuts import render, redirect
def index(request):
    form = forms.PostForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("orm-index")
        ...
    return render(request, "post_create.html", {"form": form})