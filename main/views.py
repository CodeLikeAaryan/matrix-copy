from re import template
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from .forms import AddFile
from .models import Book
from .models import PersonalFiles
from django.views.generic import ListView, TemplateView


# Views

def landing(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'routes/landing.html')


def user_signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created succesfully ')
                return redirect('login')

        context = {'form': form}
        return render(request, 'routes/signup.html', context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Incorrect Username or Password')

        context = {}
        return render(request, 'routes/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    books = Book.objects.all()
    return render(request, "routes/dashboard.html", {
        'books': books
    })


@login_required(login_url='login')
def upload_file(request):

    return render(request, "routes/upload_file.html")


def book_list(request):
    books = Book.objects.all()

    return render(request, "routes/book_list.html", {
        'books': books
    })


def upload_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, "routes/upload_book.html",
                  {
                      'form': form
                  })


@login_required(login_url='login')
def create(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BookForm()
    return render(request, "routes/create_document.html",
                  {
                      'form': form
                  })


@login_required(login_url='login')
def add_file(request):
    if request.method == 'POST':
        form = AddFile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('notes')
    else:
        form = AddFile()
    return render(request, "routes/create_document.html",
                  {
                      'form': form
                  })


def delete_book(request, pk):
    if request.method == "POST":
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('dashboard')


@login_required(login_url='login')
def account(request):
    return render(request, 'routes/account.html')


@login_required(login_url='login')
def notes(request):
    context = {
        "data": [1, 2, 3, 4, 5],
        "category": "Notes"
    }

    return render(request, 'components/category.html', context)


@login_required(login_url='login')
def certificates(request):
    context = {
        "data": [1, 2, 3, 4, 5],
        "category": "Certificates"
    }

    return render(request, 'components/category.html', context)


@login_required(login_url='login')
def documents(request):
    context = {
        "data": [1, 2, 3, 4, 5],
        "category": "Documents"
    }

    return render(request, 'components/category.html', context)


@login_required(login_url='login')
def papers(request):
    context = {
        "data": [1, 2, 3, 4, 5],
        "category": "Question Papers"
    }

    return render(request, 'components/category.html', context)


@login_required(login_url='login')
def material(request):
    context = {
        "data": [1, 2, 3, 4, 5],
        "category": "Study Material"
    }

    return render(request, 'components/category.html', context)
