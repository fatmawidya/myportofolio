from django.urls import path

from main.views import show_education, show_main, show_experience, create_experience, get_experience_json, get_experience_xml, delete_experience

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"), 
    path('experience/create/', create_experience, name='create_experience'),

    # API Endpoints
    path('api/experience/json/', get_experience_json, name='get_experience_json'),
    path('api/experience/xml/', get_experience_xml, name='get_experience_xml'),

    # Delete Endpoint
    path('experience/<uuid:id>/delete/', delete_experience, name='delete_experience'),
]