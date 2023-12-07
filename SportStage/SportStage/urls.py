from django.contrib import admin
from django.urls import path
from proSportStage import views
from django.contrib.auth.views import LoginView
# from proSportStage.views import pagPrincipal


urlpatterns = [
    path('admin/', admin.site.urls),
    path('holamundo/', views.hola_mundo, name="hola mundo"),
    path('',views.loginUser, name="login"),
    # path('login/',views.login, name="login"),
    path('login/',LoginView.as_view(template_name='login.html'),name="login"),
    path('validar/',views.validar, name="validar"),
    path('registro/',views.registro,name="registro"),



    # path('',views.loginUsers, name="login"),
    # # ruta sin seccion path('login/',views.login, name="login"),
    # path('login/',LoginView.as_view (template_name='login.html'), name="login"),
    
    path('listarUsuarios/',views.consultarUsuarios,name='listarUsuarios'),
    path('listarEscenarios/',views.consultarEscenarios,name='listarEscenario'),
    path('insertarUsuarios/',views.insertarUsuarios,name='insertarUsuarios'),
    path('salir/',views.salir, name="salir"),
    path('principal/',views.pagPrincipal , name="principal"),
    path('reservar/',views.reservar,name="reservar"),

    path('misReservas/',views.misReservas,name="misReservas"),
    path('reservarEscenario/',views.reservarEscenario,name="reservarEscenario"),

    #Eliminar reserva
    path('eliminarReserva/<id>', views.eliminarReserva,name="eliminarReserva"),

   
]
