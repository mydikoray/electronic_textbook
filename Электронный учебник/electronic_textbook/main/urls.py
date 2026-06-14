from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('lectures/', views.lectures, name='lectures'),

    path(
        'lectures/<int:lecture_id>/',
        views.lecture_detail,
        name='lecture_detail'
    ),

    path(
        'lectures/<int:lecture_id>/view/',
        views.lecture_file_view,
        name='lecture_file_view'
    ),

    path(
        'lectures/<int:lecture_id>/file/',
        views.lecture_pdf_stream,
        name='lecture_pdf_stream'
    ),

    path(
        'laboratories/',
        views.laboratories,
        name='laboratories'
    ),
    path(
    'laboratories/<int:laboratory_id>/view/',
    views.laboratory_file_view,
    name='laboratory_file_view'
),

path(
    'laboratories/<int:laboratory_id>/file/',
    views.laboratory_pdf_stream,
    name='laboratory_pdf_stream'
), 
    path(
        'tests/',
        views.tests,
        name='tests'
    ),

    path(
        'test/<int:test_id>/',
        views.test_detail,
        name='test_detail'
    ),

   path(
    'presentation/',
    views.presentation,
    name='presentation'
),

path(
    'presentation/<int:presentation_id>/view/',
    views.presentation_file_view,
    name='presentation_file_view'
),

path(
    'presentation/<int:presentation_id>/file/',
    views.presentation_pdf_stream,
    name='presentation_pdf_stream'
),

    path(
        'materials/',
        views.materials,
        name='materials'
    ),

    path(
        'materials/<int:material_id>/view/',
        views.material_file_view,
        name='material_file_view'
    ),

    path(
        'materials/<int:material_id>/file/',
        views.material_file_stream,
        name='material_file_stream'
    ),

    path(
        'profile/',
        views.profile,
        name='profile'
    ),

    path(
        'admin-panel/',
        views.admin_panel,
        name='admin_panel'
    ),

    path(
        'teacher-panel/',
        views.teacher_panel,
        name='teacher_panel'
    ),

    path(
        'register/',
        views.register_view,
        name='register'
    ),

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

    path(
        'choose-role/',
        views.choose_role,
        name='choose_role'
    ),
]