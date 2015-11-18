from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from contable.forms import UserCreationForm,EmpleadoForm,CuentaForm
from contable.models import Empleado,Puesto,Cuenta,TipoCuenta,Transaccion
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
#usuarios=''

# Create your views here.
@login_required(login_url='/ingresar')
def inicio(request):
    return render_to_response('index.html')






def planillaEmpleados(request):
    return render_to_response('planilla-empleados.html')
def catalogoCuentas(request):
    return render_to_response('catalogo-cuentas.html')



def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('../index')
    if request.method=='POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request,acceso)
                    return HttpResponseRedirect('../index')
                else:
                    return render_to_response('noactivo.html',context_instance=RequestContext(request))
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))
# global usuarios


def nuevo_usuario(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('../index')
	if request.method=='POST':
		formulario=UserCreationForm(request.POST)
		#clave1 = request.POST['password1']
		#clave2 = request.POST['password2']

		if formulario.is_valid():# and (clave1 == clave2):
		#	p = Perfil()
		#	p.nickname = request.POST['username']
		#	p.password = request.POST['password1']
		#	p.email = request.POST['email']
		#	p.save()
		#	m=Puntaje()
		#	m.credito=1000.0
		#	m.partidasGanadas=0
		#	m.perfil_id=p.id
		#	m.save()

			formulario.save()
			return HttpResponseRedirect('/')
		#else:
			#return HttpResponseRedirect('/usuario/nuevo')
	else:
		formulario=UserCreationForm()
	return render_to_response('nuevousuario.html',{'formulario':formulario}, context_instance=RequestContext(request))


@login_required(login_url='/ingresar')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/ingresar')



def ingresar_empleado(request):
    if request.POST:
        empForm=EmpleadoForm(request.POST)
        if empForm.is_valid():
            c=request.POST['Puesto']
            if (c=="0"):
                return HttpResponseRedirect('/empleado')
            else:
                p = Empleado()
                m = Puesto()
                p.nombre = request.POST['nombre']
                p.apellido = request.POST['apellido']
                p.salAgregado = 0
                p.horas = 0
                p.horasExtras = 0
                p.dui = request.POST['dui']
                p.nit = request.POST['nit']
                m=Puesto.objects.get(id=c)
                p.puesto = m
                p.save()
                return HttpResponseRedirect('/index')
    else:
        empForm=EmpleadoForm()
    args={}
    args.update(csrf(request))
    args['empForm'] = empForm
    return render_to_response('registrar_empleado.html',args)
   

def ingresar_cuenta(request):
    if request.POST:
        cuentForm=CuentaForm(request.POST)
        if cuentForm.is_valid():
            c=request.POST['Cuenta']
            if (c=="0"):
                return HttpResponseRedirect('/cuenta')
            else:
                a = Cuenta()
                s = TipoCuenta()
                a.nom_cuenta = request.POST['nom_cuenta']
                a.saldo = request.POST['saldo']
                s=TipoCuenta.objects.get(id=c)
                a.tipoCuenta = s
                a.save()
                return HttpResponseRedirect('/index')
    else:
        cuentForm=CuentaForm()
    args={}
    args.update(csrf(request))
    args['cuentForm'] = cuentForm
    return render_to_response('registrar_cuenta.html', args)

def transaccion(request):
    if request.method == "GET":
        return render(request ,'form-transaccion.html', {'cuentas':Cuenta.objects.all()})
    if request.method=="POST":
        t=Transaccion()
        tm=TipoMonto()
        c=Cuenta()
        t.monto=request.POST['monto1']
        tm=TipoMonto.objects.get(id="1")
        c=TipoMonto.objects.get(id="cuenta1")
        t.tipoMonto=tm
        t.cuenta = c
        t.fecha=0
        t.save()
        t.monto=request.POST['monto2']
        tm=TipoMonto.objects.get(id="2")
        c=TipoMonto.objects.get(id="cuenta2")
        t.tipoMonto=tm
        t.cuenta = c
        t.fecha=0
        t.save()
        return HttpResponseRedirect('/index')
    else:
        return HttpResponseRedirect('/transaccion')

    
