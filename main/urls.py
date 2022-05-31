from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name="home"),
    path('connexion/', views.loginPage, name="login"),
    path('connexion/failed', views.loginFailer, name="loginF"),
    path('deconnexion/', views.logoutUser, name="logout"),
    path('inscription/', views.signupPage, name="signup"),
    path('dashboard/', views.dashboardPage, name="dashboard"),
    path('recherche/', views.searchPage, name="search"),
    path('compte/', views.profilPage, name="profil"),
    path('compte/modifier', views.profilEdit, name="profil_edit"),
    path('nouvelle-demande/', views.demandCreationPage, name="demand_creation"),
    path('modifier-demande/<str:demande_sujet>', views.editCreationPage, name="demande_edit"),
    path('votre-demande/<int:pk>', views.detailPage, name="demand_detail"),
    path('categories/<str:category_name>', views.categoriesPage, name="cat_detail"),
    path('categories', views.allCategories, name="all_cat"),
]