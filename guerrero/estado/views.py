from django.shortcuts import render
from estado.models import Estado,Partecuerpo,Detallecuerpo,Demonio,Batalla
from django.urls import  reverse_lazy
from estado.forms import Estadoform,Partecuerpoform,Detallecuerpoform,Demonioform,Batallaform
from django.views import generic
from django.http import  HttpResponse
# Create your views here.

#Vistas de Estados
class Estadoview(generic.ListView):
    model = Estado
    template_name = 'listar_estado.html'
    context_object_name = 'estado'
class Estadoinsertar(generic.CreateView):
     model = Estado
     context_object_name = 'estado'
     template_name = 'form_estado.html'
     form_class = Estadoform
     success_url=reverse_lazy("Estado:Estados")
class Estadoeditar(generic.UpdateView):
     model = Estado
     context_object_name = 'estado'
     template_name = 'form_estado.html'
     form_class = Estadoform
     success_url=reverse_lazy("Estado:Estados")
class Estadoeliminar(generic.DeleteView):
     model = Estado
     context_object_name = 'estado'
     template_name = 'delete_estado.html'
     form_class = Estadoform
     success_url=reverse_lazy("Estado:Estados")
#Vistas de Partecuerpo
class Partecuerpoview(generic.ListView):
    model = Partecuerpo
    template_name = 'listar_partecuerpo.html'
    context_object_name = 'partecuerpo'
class Partecuerpoinsertar(generic.CreateView):
     model = Partecuerpo
     context_object_name = 'partecuerpo'
     template_name = 'form_partecuerpo.html'
     form_class = Partecuerpoform
     success_url=reverse_lazy("Partecuerpo:Partecuerpos")
class Partecuerpoeditar(generic.UpdateView):
     model = Partecuerpo
     context_object_name = 'partecuerpo'
     template_name = 'form_partecuerpo.html'
     form_class = Partecuerpoform
     success_url=reverse_lazy("Partecuerpo:Partecuerpos")
class Partecuerpoeliminar(generic.DeleteView):
     model = Partecuerpo
     context_object_name = 'partecuerpo'
     template_name = 'delete_partecuerpo.html'
     form_class = Partecuerpoform
     success_url=reverse_lazy("Partecuerpo:Partecuerpos")
#Vistas de Detallecuerpo
class Detallecuerpoview(generic.ListView):
    model = Detallecuerpo
    template_name = 'listar_detallecuerpo.html'
    context_object_name = 'detallecuerpo'
class Detallecuerpoinsertar(generic.CreateView):
     model = Detallecuerpo
     context_object_name = 'detallecuerpo'
     template_name = 'form_detallecuerpo.html'
     form_class = Detallecuerpoform
     success_url=reverse_lazy("Detallecuerpo:Detallecuerpos")
class Detallecuerpoeditar(generic.UpdateView):
     model = Detallecuerpo
     context_object_name = 'detallecuerpo'
     template_name = 'form_detallecuerpo.html'
     form_class = Detallecuerpoform
     success_url=reverse_lazy("Detallecuerpo:Detallecuerpos")
class Detallecuerpoeliminar(generic.DeleteView):
     model = Detallecuerpo
     context_object_name = 'detallecuerpo'
     template_name = 'delete_detallecuerpo.html'
     form_class = Detallecuerpoform
     success_url=reverse_lazy("Detallecuerpo:Detallecuerpos")
#Vistas de Demonio
class Demonioview(generic.ListView):
    model = Demonio
    template_name = 'listar_demonio.html'
    context_object_name = 'demonio'
class Demonioinsertar(generic.CreateView):
     model = Demonio
     context_object_name = 'demonio'
     template_name = 'form_demonio.html'
     form_class = Demonioform
     success_url=reverse_lazy("Demonio:Demonios")
class Demonioeditar(generic.UpdateView):
     model = Demonio
     context_object_name = 'demonio'
     template_name = 'form_demonio.html'
     form_class = Demonioform
     success_url=reverse_lazy("Demonio:Demonios")
class Demonioeliminar(generic.DeleteView):
     model = Demonio
     context_object_name = 'demonio'
     template_name = 'delete_demonio.html'
     form_class = Demonioform
     success_url=reverse_lazy("Demonio:Demonios")
#Vistas de Batalla
class Batallaview(generic.ListView):
    model = Batalla
    template_name = 'listar_batalla.html'
    context_object_name = 'batalla'
class Batallainsertar(generic.CreateView):
     model = Batalla
     context_object_name = 'batalla'
     template_name = 'form_batalla.html'
     form_class = Batallaform
     success_url=reverse_lazy("Batalla:Batallas")
class Batallaeditar(generic.UpdateView):
     model = Batalla
     context_object_name = 'batalla'
     template_name = 'form_batalla.html'
     form_class = Batallaform
     success_url=reverse_lazy("Batalla:Batallas")
class Batallaeliminar(generic.DeleteView):
     model = Batalla
     context_object_name = 'batalla'
     template_name = 'delete_batalla.html'
     form_class = Batallaform
     success_url=reverse_lazy("Batalla:Batallas")


def demonio_print(self, pk=None):
    import io
    from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import Table

    response = HttpResponse(content_type='application/pdf')
    buff = io.BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    demonios = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Demonio", styles['Heading1'])
    demonios.append(header)
    headings = ('Id', 'demonio', 'detalle ')
    if not pk:
        todosdemonio = [(p.id, p.DemonioNombre, p.detallecuerpo)
                           for p in Demonio.objects.all().order_by('pk')]
    else:
        todosdemonio = [(p.id, p.DemonioNombre, p.detallecuerpo)
                           for p in Demonio.objects.filter(id=pk)]

    t = Table([headings] + todosdemonio)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))

    demonios.append(t)
    doc.build(demonios)
    response.write(buff.getvalue())
    buff.close()
    return response
