from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from contable.forms import UserCreationForm,EmpleadoForm
from contable.models import Empleado,Puesto,Cuenta,TipoCuenta,Transaccion, TipoMonto
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
import time
#usuarios=''

# Create your views here.
@login_required(login_url='/ingresar')
def inicio(request):
    return render_to_response('index.html')

def error(request):
    return render_to_response('error.html')

def planillaEmpleados(request):
    e=Empleado.objects.all()
    p=Puesto.objects.all()
    emp=Empleado()
    pue=Puesto()
    if request.method=='POST':
        he=request.POST['horasExtras']
        cod=request.POST['codigo']
        emp1=Empleado.objects.get(id=cod)
        p1=Puesto.objects.get(id=emp1.puesto_id)
        emp1.horasExtras=he
        emp1.salDevengado=round((float(he)*p1.pHoraExtra)+p1.salBase,2)
        emp1.isss=round(emp1.salDevengado*0.075,2)
        emp1.afp=round(emp1.salDevengado*0.0675,2)
        if emp1.salDevengado>338.67:
            emp1.renta=round(emp1.salDevengado*0.0083333,2)
        emp1.salPagar = round(emp1.salDevengado-emp1.isss-emp1.afp-emp1.renta,2)
        emp1.save()
    return render(request, 'planilla-empleados.html', {'empleado':e, 'puesto':p})

def catalogoCuentas(request):
    return render(request, 'catalogo-cuentas.html', {'cuentas':Cuenta.objects.order_by('tipoCuenta_id'), 'tipoCuenta':TipoCuenta.objects.all()})

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
                p.horasExtras = 0
                p.isss=0
                p.afp=0
                p.renta=0
                p.salDevengado=0
                p.salPagar=0
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
    if request.method == 'GET':
        return render(request ,'registrar_cuenta.html', {'tipo':TipoCuenta.objects.all()})
    if request.POST:
        c=request.POST['Cuenta']
        if (c=="0"):
            return HttpResponseRedirect('/cuenta')
        else:
            a = Cuenta()
            s = TipoCuenta()
            a.nom_cuenta = request.POST['nom_cuenta']
            a.saldo = 0
            s=TipoCuenta.objects.get(id=c)
            a.tipoCuenta = s
            a.montoCargo=0
            a.montoAbono=0
            a.save()
            return HttpResponseRedirect('/index')
    return render(request,'registrar_cuenta.html')

def transaccion(request):
    if request.method == "GET":
        return render(request ,'form-transaccion.html', {'cuentas':Cuenta.objects.all()})
    
    if request.method=="POST":    
        count=int(request.POST['counter'])
        i=1
        l=1
        montoCa=0
        montoAb=0
        for k in range(count):
            var1='cuenta'+str(l)
            var2='monto'+str(l)
            mont=float(request.POST[var2])
            #cid=Cuenta.objects.get(id=request.POST[var1])
            #tc1=TipoCuenta.objects.get(id=1)
            #tc2=TipoCuenta.objects.get(id=2)
            #tc3=TipoCuenta.objects.get(id=3)
            #tc4=TipoCuenta.objects.get(id=4)
            #if cid.tipoCuenta==tc4: #es resultado
            if l%2==0: #es abono
                montoAb=montoAb+mont
            else:
                montoCa=montoCa+mont
            #if cid.tipoCuenta==tc1: #si es activo
                #activo=activo+mont
            #if cid.tipoCuenta==tc2:
                #pasivo=pasivo+mont
            #if cid.tipoCuenta==tc3:
                #pasivo=pasivo+mont
            l=l+1
        if montoCa==montoAb: #partida doble
            for j in range(count): 
                c=Cuenta()
                #t=Transaccion()
                #tc=TipoCuenta()
                var1='cuenta'+str(i)
                var2='monto'+str(i)
                monto=float(request.POST[var2])            
                c=Cuenta.objects.get(id=request.POST[var1])
                tm1=TipoMonto.objects.get(id=1)
                tm2=TipoMonto.objects.get(id=2)
                #t.monto=monto
                #t.cuenta=c
                if i%2==0:
                    #t.tipoMonto=tm2  #es abono
                    c.montoAbono=c.montoAbono+monto
                else:
                    #t.tipoMonto=tm1   #es cargo
                    c.montoCargo=c.montoCargo+monto
                #if t.tipoMonto==tm1: #si es cargo
                    #if c.tipoCuenta==1:#si es activo
                        #c.montoCargo=c.montoCargo+monto
                    #else:   # es pasaivo,capital o resultado
                        #c.montoAbono=c.montoAbono+monto
                #if t.tipoMonto==tm2: #si es abono
                    #if c.tipoCuenta==1: #si es activo
                        #c.montoAbono=c.montoAbono+monto
                    #else: #si es pasivo, capital o resultado
                        #c.montoCargo=c.montoCargo+monto
                #t.fecha=time.strftime("%x")
                #t.save()
                c.save()
                i=i+1
        else:
            return HttpResponseRedirect('/error')
        return HttpResponseRedirect('/index')
    else:
        return HttpResponseRedirect('/transaccion')

def eliminar_emp(request):
    if request.method == 'GET':
        return render(request ,'eliminar_empleado.html', {'eliminar':Empleado.objects.all()})
    if request.method=="POST":
        ele=Empleado.objects.get(id=request.POST['eliminar'])
        ele.delete()
        return HttpResponseRedirect('/index')
    else:
        return HttpResponseRedirect('/eliminar')
        
        
        
    
