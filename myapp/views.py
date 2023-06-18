from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Socio_act
import csv, sqlite3, os
#En esta capa se realiza las tareas de navegacion entre paginas, la carga del archivo csv y la actualizacion del mismo mediante los metodos existentes.
def index(request):
    return render(request, 'index.html')
def lista(request):
    registros = Socio_act.objects.all()
    return render(request, 'lista.html', {'registros': registros})


def subir(request):
    dir = 'media/'

    if request.method == 'POST'and request.FILES['myfile']:
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save('base.csv', myfile)
        return render(request,'index.html')
    else:
        return render(request, 'upload.html')



def import_csv(request):
    sociosActualizar = []
    sociosAgregar = []
    with open("media/base.csv", "r") as csv_file:
        data = list(csv.reader(csv_file, delimiter=","))
        for row in data[1:]:
           if Socio_act.objects.filter(id = row[0]).exists():
                valor_CedulaRuc=Socio_act.objects.get(id=row[0]).cedulaRUC
                if len(valor_CedulaRuc) <= 10:
                    valor_CedulaRuc=row[3]
                sociosActualizar.append(
                    Socio_act(
                        id=row[0],
                        nombre=row[1],
                        apellido=row[2],
                        cedulaRUC=valor_CedulaRuc,
                        ciudad=row[4],
                        provincia=row[5],
                        correo=row[6],
                    )
                )
           else:
               sociosAgregar.append(
                    Socio_act(
                        id=row[0],
                        nombre=row[1],
                        apellido=row[2],
                        cedulaRUC=row[3],
                        ciudad=row[4],
                        provincia=row[5],
                        correo=row[6],
                    )
                )
               datos_correo=row[6]
               print("Enviar correo de bienvenida a:" + datos_correo)
               
    Socio_act.objects.bulk_create(sociosAgregar)
    Socio_act.objects.bulk_update(sociosActualizar,['nombre','apellido','cedulaRUC','ciudad', 'provincia','correo'])
    
    return HttpResponse("Realizado")
