from django.urls import path

from main.views import show_education, show_main, show_experience, create_experience, get_experience_json, get_experience_xml, delete_experience, edit_experience, create_education, edit_education, delete_education, register, login, logout, login_user, logout_user, toggle_star

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    # Experience Endpoints
    path("experience/", show_experience, name="show_experience"),
    path("experience/create/", create_experience, name="create_experience"),
    path("experience/<uuid:id>/edit/", edit_experience, name="edit_experience"),
    path("experience/<uuid:id>/delete/", delete_experience, name="delete_experience"),

    # Education Endpoints
    path("education/", show_education, name="show_education"), 
    path("education/create/", create_education, name="create_education"),
    path("education/<uuid:id>/edit/", edit_education, name="edit_education"),
    path("education/<uuid:id>/delete/", delete_education, name="delete_education"),

    # API Endpoints
    path("api/experience/json/", get_experience_json, name="get_experience_json"),
    path("api/experience/xml/", get_experience_xml, name="get_experience_xml"),

    #login logout
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),

    #STARS
    path(
    "experience/<uuid:experience_id>/star/",
        toggle_star,
        name="toggle_star",
    ),
]