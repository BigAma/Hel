from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from main.models import Professionnel, Category, Demande_client, UserProfil
from main.forms import CategoryForm, Demande_clientForm, UserProfilForm, Demande_clientForm1

# Create your views here.


def home(request):
    categories = Category.objects.all()[0:4]

    context = {
        'categories' : categories
    }
    return render(request, 'main/index.html', context)

def loginFailer(request):
    return render(request, 'main/login_fail.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:dashboard')
        else:
            return redirect('main:loginF')
    return render(request, 'main/login.html')

@login_required(login_url='main:login')
def logoutUser(request):
    logout(request)
    return redirect('main:home')

def signupPage(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        profilform = UserProfilForm(data=request.POST)
        if form.is_valid() and profilform.is_valid():
            user = form.save()
            profile = profilform.save(commit=False)
            profile.user_profil = user
            profile.user_username = user.username
            profile.save()
            login(request, user)
            return redirect('main:dashboard')
    else:
        form = UserCreationForm()
        profilform = UserProfilForm()
    return render(request, 'main/signup.html', {'form': form, 'profilform': profilform})

@login_required(login_url='main:login')
def dashboardPage(request):
    user = request.user
    demandes = Demande_client.objects.filter(demande_utilisateur=user).order_by('-demande_creation')
    
    context = {
        'demandes': demandes
    }
    return render(request, 'main/dashbord.html', context)

def searchPage(request):
    cat = Category.objects.all()
    catlen = len(cat)
    catt = []
    cat1 = []
    cat2 = []
    cat3 = []
    pop = False

    for i in range(catlen):
        catt.append(cat[i])

    if catlen <= 5:
        cat1 = catt
    elif catlen > 5 and catlen <= 10:
        for j in range(5):
            cat1.append(catt[j])
        for k in range(5,catlen):
            cat2.append(catt[k])
    elif catlen > 10 and catlen <= 15:
        for g in range(5):
            cat1.append(catt[g])
        for m in range(5,10):
            cat2.append(catt[m])
        for b in range(10,catlen):
            cat3.append(catt[b])
    else:
        for f in range(5):
            cat1.append(catt[f])
        for w in range(5,10):
            cat2.append(catt[w])
        for v in range(10,16):
            cat3.append(catt[v])
        pop = True
 
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    if q != '':
        categories_search = Category.objects.filter(
            Q(category_name__icontains=q) |
            Q(category_description__icontains=q)
        )
        categories_search_count = categories_search.count()
    else:
        categories_search = ''
        categories_search_count = 0

    context = {
        'categories' : categories_search,
        'categories_count' : categories_search_count,
        'cat1': cat1,
        'cat2': cat2,
        'cat3': cat3,
        'pop': pop
    }
    return render(request, 'main/recherche.html', context)

def categoriesPage(request, category_name):
    categorie = get_object_or_404(Category, category_name=category_name)
    context = {
        'categorie': categorie
    }
    return render(request, 'main/categories.html', context)


def allCategories(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories
    }
    return render(request, 'main/allcategories.html', context)

@login_required(login_url='main:login')
def profilPage(request):
    user = request.user
    userprofile = UserProfil.objects.filter(user_username=request.user.username)
    demandes = Demande_client.objects.filter(demande_utilisateur=user).order_by('-demande_creation')
    
    context = {
        'demandes': demandes,
        'userprofile': userprofile
    }
    return render(request, 'main/profil.html', context)

@login_required(login_url='main:login')
def profilEdit(request):
    user = request.user
    user2 = get_object_or_404(UserProfil, user_profil=user)
    if request.method == 'POST':
        formm = UserCreationForm(request.POST, instance=user)
        form = UserProfilForm(request.POST, instance=user)
        if form.is_valid() and formm.is_valid():
            form.save()
            formm.save()
            redirect('main:profil')
    else:
        formm = UserCreationForm(instance=user)
        form = UserProfilForm(instance=user2)

    context = {
        'form1' : formm,
        'form2' : form
    }
    return render(request, 'main/profil_edit.html', context)


@login_required(login_url='main:login')
def demandCreationPage(request):

    if request.method == 'POST':
        form = Demande_clientForm(request.POST)
        if form.is_valid():
            demande = form.save(commit=False)
            demande.demande_utilisateur = request.user
            demande.save()
            return redirect('main:dashboard')
    else:
        form = Demande_clientForm()

    context = {
        'form' : form,
    }
    return render(request, 'main/demand_creation.html', context)


@login_required(login_url='main:login')
def editCreationPage(request,demande_sujet):
    demande = get_object_or_404(Demande_client, demande_sujet=demande_sujet)

    if request.method == 'POST':
        form = Demande_clientForm1(request.POST, instance=demande)
        if form.is_valid():
            form.save()
            return redirect('main:dashboard')
    else:
        form = Demande_clientForm1(instance=demande)

    context = {
        'demande': demande,
        'form' : form,
    }
    return render(request, 'main/demand_creation.html', context)


@login_required(login_url='main:login')
def detailPage(request,pk):
    demande = get_object_or_404(Demande_client, id=pk)

    context = {
        'demande': demande,
    }
    return render(request, 'main/demand-detail.html', context)