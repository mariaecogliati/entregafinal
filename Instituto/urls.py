from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio , name="home"),
    path("ver_cursos", views.ver_cursos , name="cursos"),
    path("ver_alumnos", views.ver_alumnos , name="alumnos"),
    path("ver_profesores", views.ver_profesores , name="profesores"),
    path("alta_curso", views.alta_curso),
    path("alta_alumno", views.alta_alumno),
    path("alta_profesor", views.alta_profesor),
    path("buscar_curso", views.buscar_curso),
    path("buscar", views.buscar),
    path("eliminar_curso/<int:id>" , views.eliminar_curso , name="eliminar_curso"),
    path("editar_curso/<int:id>" , views.editar_curso , name="editar_curso"),
    path("eliminar_alumno/<int:id>" , views.eliminar_alumno , name="eliminar_alumno"),
    path("editar_alumno/<int:id>" , views.editar_alumno , name="editar_alumno"),    
    path("eliminar_profesor/<int:id>" , views.eliminar_profesor , name="eliminar_profesor"),
    path("editar_profesor/<int:id>" , views.editar_profesor , name="editar_profesor"),
    path("login", views.login_request , name="Login"),
    path("register", views.register , name="Register"),
    path("logout" , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path("editarPerfil" , views.editarPerfil , name="EditarPerfil")
 

]