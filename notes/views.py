from django.shortcuts import render
from django.shortcuts import redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados

        if isinstance(request.POST.get('delete'), str):
            Note.objects.filter(id=int(request.POST.get('delete'))).delete()

        elif isinstance(request.POST.get('update'), str):
            Note.objects.filter(id=int(request.POST.get('update'))).update(title = title,content = content)
        
        else:
            note = Note(title, content)
            note.save()

        return redirect('index')
    else:
        all_notes = Note.objects.all()
        # print(all_notes)
        return render(request, 'notes/index.html', {'notes': all_notes})

def tags(request):
    if request.method == 'POST':
        tag = request.POST.get('tag')
        return redirect('lista')
    else:
        lista = Note.objects.values_list("tag", flat = True).distinct()
        if len(lista)==0:
            erros = "Nenhuma Tag Criada"
        else:
            erros = ""
        
        return render(request, 'notes/lista.html',{"tags": lista, "erro":erros})


# def index(request):
#     if request.method == 'POST':
#         title = request.POST.get('titulo')
#         content = request.POST.get('detalhes')

#         if isinstance(request.POST.get('delete'), str):
#             Note.objects.filter(id=int(request.POST.get('delete'))).delete()

#         elif isinstance(request.POST.get('update'), str):
#             Note.objects.filter(id=int(request.POST.get('update'))).update(title = title,content = content)
        
#         else:
#             Note.objects.create(title = title,content = content, tag = tag)
#         return redirect('index')
#     else:
#         all_notes = Note.objects.all()
#         return render(request, 'notes/index.html', {'notes': all_notes})
