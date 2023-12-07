from types import resolve_bases
from django.shortcuts import render, HttpResponse
from proSportStage.models import escenariosReserva
from proSportStage.models import LoginUsuarios,reservas
from django.contrib.auth import login,authenticate,logout, models
from django.shortcuts import redirect

def hola_mundo(request):
    return HttpResponse("""<h1>hola mundo</h1><a class="dropdown-item" href="/salir">Salir</a>""")

def pagPrincipal(request):
     return render(request,"principal.html")

def index(request):
     return render(request,"principal.html")

def loginUser(request):
     return render(request,"login.html")

def salir(request):
     return render(request,"login.html")

def registro(request):
    return render(request,"registro.html")

# def loginUsers(request):
#     return render(request,"login.html")
def consultarUsuarios(request):
    usuario=LoginUsuarios.objects.get(id=2)
    return HttpResponse(usuario.nombre)
    
def consultarEscenarios(request):
     escenario=escenariosReserva.objects.get(id=600)
     return HttpResponse(escenario.nombre)

def validar(request):
    if request.method=="POST":
        usuarioForm=request.POST["usuario"]
        claveForm=request.POST["clave"]
        user = authenticate(username=usuarioForm, password = claveForm)
        if user is not None:
            login(request,user)
            return render(request,"principal.html")
        else:
            return HttpResponse("""Usuario o contraseña incorrectos!!!<br><a class="dropdown-item" href="/login">volver</a>""")
             
    
   
def insertarUsuarios(request):
    if request.method == "POST":
        nombreReg=request.POST['nombre']
        cedulaReg=request.POST['cedula']
        cedu= int(cedulaReg)
        direccionReg=request.POST['direccion']
        emailReg=request.POST['email']
        claveReg=request.POST['clave']
        rolReg=request.POST['rol']

        try: 
            LoginUsuarios.objects.get(cedula=cedu)
        except LoginUsuarios.DoesNotExist:
            usuario=LoginUsuarios(nombre=nombreReg,cedula=cedu,direccion=direccionReg,email=emailReg,clave=claveReg,rol=rolReg)
           # user = models.User(password=claveReg, is_superuser=rolReg, username=nombreReg, is_staff=1, is_active=1, date_joined=1)
            usuario.save()
            #user.save()
            
            return HttpResponse("""se guardo el usuario <a class="dropdown-item" href="/salir">Ingresar</a>""")
        return HttpResponse("""'usuario exite <a class="dropdown-item" href="/registro">volver</a>'""")
        # if usuarioDB==nombreReg:
        #    return HttpResponse("usuario existente")
        # else:
            
        #     return HttpResponse("usuario creado")

   
def salir(request):
    return render(request,"login.html")

def reservar(request):
    escenarios=escenariosReserva.objects.all()
    user=LoginUsuarios.objects.all()
    data={
        'escenarios':escenarios,
        
    }
    return render(request,"reservar.html",data)

def reservarEscenario(request):
    if request.method == "POST":
        fechaRe=request.POST['fecha']
        horaRe=request.POST['hora']
        usuarioRe=request.POST['usuario']
        usuario = LoginUsuarios.objects.get(pk=usuarioRe)
        escenarioRe=request.POST['escenario']
        escenario=escenariosReserva.objects.get(pk=escenarioRe)
        guardarReserva=reservas(fecha=fechaRe,hora=horaRe,id_usuario=usuario,id_escenario=escenario)
        guardarReserva.save()

    return HttpResponse("""Reserva Guardada Satisfactoriamente!!!<br><a class="dropdown-item" href="/reservar">volver</a>""")

def misReservas(request):
    reserv = reservas.objects.raw('SELECT r.id, r.fecha, e.nombre as enombre, u.nombre as unombre FROM reservas as r LEFT join escenarios as e ON r.id_escenario_id = e.id LEFT JOIN usuarios as u ON r.id_usuario_id = u.id')
    data= {
        'reserv': reserv
    }
    return render(request,"reservas.html", data)


 #Create your views here

def eliminarReserva(request, id):
    intance = reservas.objects.get(id=id)
    intance.delete()
    
    return redirect(to='misReservas')