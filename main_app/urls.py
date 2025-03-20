from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('travels/', views.travels_index, name='index'),
    path('travels/planned/', views.planned_trips, name='planned_trips'),
    path('travels/completed/', views.completed_trips, name='completed_trips'),
    path('travels/<int:travel_id>/', views.travels_detail, name='detail'),
    path('travels/planned/create/', views.PlannedTripCreate.as_view(), name='planned_trip_create'),
    path('travels/completed/create/', views.CompletedTripCreate.as_view(), name='completed_trip_create'),
    #path('travels/create/', views.TravelCreate.as_view(), name='travels_create'),
    path('travels/<int:pk>/update/', views.TravelUpdate.as_view(), name='travels_update'),
    path('travels/<int:pk>/delete/', views.TravelDelete.as_view(), name='travels_delete'),
    path('travels/<int:travel_id>/add_checking/', views.add_checking, name='add_checking'),
    
    # Checklist Model
    path('checklists/', views.checklists_index, name = 'checklists_index'),
    path('checklists/<int:pk>/', views.ChecklistDetail.as_view(), name='checklists_detail'),
    path('checklists/create/', views.ChecklistCreate.as_view(), name='checklists_create'),
    path('checklists/<int:pk>/update/', views.ChecklistUpdate.as_view(), name='checklists_update'),
    path('checklists/<int:pk>/delete/', views.ChecklistDelete.as_view(), name='checklists_delete'),

    # M:M
    path('travels/<int:travel_id>/assoc_checklist/<int:checklist_id>/', views.assoc_checklist, name='assoc_checklist'),
    path('travels/<int:travel_id>/unassoc_checklist/<int:checklist_id>/', views.unassoc_checklist, name='unassoc_checklist'),

    # Signup URL
    path('account/signup/', views.signup, name='signup'),

    # Search
    path('search/', views.search_trips, name='search_trips')
]