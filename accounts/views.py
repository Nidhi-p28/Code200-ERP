from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import CollegeAdminSignupForm
from django.contrib import messages

def admin_signup(request):
    if request.method == "POST":
        form = CollegeAdminSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "College registered successfully! You can now log in.")
            return redirect("login")  # we’ll configure login soon
    else:
        form = CollegeAdminSignupForm() 
    return render(request, "accounts/admin_signup.html", {"form": form})


# accounts/views.py
from django.http import HttpResponse

def test(request):
    return HttpResponse("URL is working!")


from django.contrib.auth.decorators import login_required

@login_required
def dashboard_redirect(request):
    if request.user.role == "superadmin":
        return redirect("superadmin_dashboard")
    elif request.user.role == "admin":
        return redirect("admin_dashboard")
    elif request.user.role == "staff":
        return redirect("staff_dashboard")
    elif request.user.role == "student":
        return redirect("student_dashboard")
    else:
        return redirect("login")
