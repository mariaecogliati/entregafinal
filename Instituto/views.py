from django.shortcuts import render
from Instituto.models import Curso , Alumno , Profesor , Avatar
from django.http import HttpResponse
from django.template import loader
from Instituto.forms import Curso_formulario , UserEditForm , Alumno_formulario , Profesor_formulario
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

def inicio(request):
    return render( request , "padre.html")

def ver_cursos(request):
    cursos = Curso.objects.all()
    return render(request , "cursos.html", { "cursos": cursos })

def ver_alumnos (request):
    alumnos = Alumno.objects.all()
    return render(request , "alumnos.html", { "alumnos": alumnos })

def ver_profesores (request):
    profesores = Profesor.objects.all()
    return render(request , "profesores.html", { "profesores": profesores })

@login_required
def alta_curso(request):
    if request.method == "POST":
        curso = Curso( Nombre = request.POST["Nombre"] , Comision = request.POST["Comision"])
        curso.save()
        return render(request , "formcurso.html")
    return render(request , "formcurso.html")

@login_required
def alta_alumno(request):
    if request.method == "POST":
        alumno = Alumno( Nombre = request.POST["Nombre"] , Apellido = request.POST["Apellido"] , Documento = request.POST["Documento"])
        alumno.save()
        return render(request , "formalumno.html")
    return render(request , "formalumno.html")

@login_required
def alta_profesor(request):
    if request.method == "POST":
        profesor = Profesor( Nombre = request.POST["Nombre"] , Apellido = request.POST["Apellido"] , Documento = request.POST["Documento"])
        profesor.save()
        return render(request , "formprofe.html")
    return render(request , "formprofe.html")
    
def buscar_curso(request):
    return render(request, "buscar_curso.html")

def buscar(request):

    if request.GET["Nombre"]:
        Nombre = request.GET["Nombre"]
        cursos = Curso.objects.filter(Nombre__icontains= Nombre)
        return render( request , "resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")
    
def eliminar_curso(request , id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    curso = Curso.objects.all()
    return render(request , "cursos.html" , {"cursos":curso})

def eliminar_alumno(request , id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    alumno = Alumno.objects.all()
    return render(request , "alumnos.html" , {"alumnos":alumno})

def eliminar_profesor(request , id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    profesor = Profesor.objects.all()
    return render(request , "profesores.html" , {"profesores":profesor})

def editar_curso(request , id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.Nombre = datos["Nombre"]
            curso.Comision = datos["Comision"]
            curso.save()
            curso = Curso.objects.all()
            return render(request , "cursos.html" , {"cursos":curso})
    else:
        mi_formulario = Curso_formulario(initial={"Nombre":curso.Nombre , "Comision":curso.Comision})
    return render( request , "editar_curso.html" , {"mi_formulario": mi_formulario , "curso":curso})

def editar_alumno(request , id):
    alumno = Alumno.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Alumno_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno.Nombre = datos["Nombre"]
            alumno.Apellido = datos["Apellido"]
            alumno.Documento = datos["Documento"]
            alumno.save()
            alumno = Alumno.objects.all()
            return render(request , "alumnos.html" , {"alumnos":alumno})
    else:
        mi_formulario = Alumno_formulario(initial={"Nombre":alumno.Nombre , "Apellido":alumno.Apellido , "Documento":alumno.Documento})
    return render( request , "editar_alumno.html" , {"mi_formulario": mi_formulario , "alumno":alumno})

def editar_profesor(request , id):
    profesor = Profesor.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Profesor_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor.Nombre = datos["Nombre"]
            profesor.Apellido = datos["Apellido"]
            profesor.Documento = datos["Documento"]
            profesor.save()
            profesor = Profesor.objects.all()
            return render(request , "profesores.html" , {"profesores":profesor})
    else:
        mi_formulario = Profesor_formulario(initial={"Nombre":profesor.Nombre , "Apellido":profesor.Apellido , "Documento":profesor.Documento})
    return render( request , "editar_profesor.html" , {"mi_formulario": mi_formulario , "profesor":profesor})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario , password=contra)
            if user is not None:
                login(request , user )
                avatares = Avatar.objects.filter(user=request.user.id)
                return render( request , "inicio.html" , {"usuario":usuario , "url":avatares[0].imagen.url})
            else:
                return HttpResponse(f"Usuario no encontrado")
        else:
            return HttpResponse(f"FORM INCORRECTO {form}")
    form = AuthenticationForm()
    return render( request , "login.html" , {"form":form})


def register(request):   
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado")
    else:
        form = UserCreationForm()
    return render(request , "registro.html" , {"form":form})

def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":
        
        mi_formulario = UserEditForm(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            return render(request , "inicio.html")

    else:
        miFormulario = UserEditForm(initial={"email":usuario.email})
    
    return render( request , "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})


