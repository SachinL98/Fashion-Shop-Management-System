from django.shortcuts import render,redirect
from django.http import HttpResponse
from stockapp.models import Item
from stockapp.forms import ItemForm
from django.contrib import messages
from django.contrib.auth.models import User



import os
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

# Create your views here.
def indexstock(request):
    workers = User.objects.all()
    workers_count = workers.count()
    items = Item.objects.all()
    items_count = items.count()


    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('stockapp-index')  
    else:
        form = ItemForm()

    context ={
        'form': form,
        'items': items,
        'workers' :workers,
        'workers_count': workers_count,
        'items_count':items_count,
    

 }
      
    return render(request, 'stockapp/indexstock.html',context) 





def item(request):
     products = Item.objects.all() #using ORM
     items_count = products.count()
     workers = User.objects.all()
     workers_count = workers.count()


     if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            item_name = form.cleaned_data.get('name')
            messages.success(request, f'{item_name} has been added successfully!')
            return redirect('stockapp-item')          
            
     else:
        form = ItemForm()

     context = {
          'products': products,
          'form':form,
          'items_count':items_count,
          'workers_count' : workers_count,

          
     }

     return render (request, 'stockapp/item.html', context)


def item_delete(request, pk):
    product = Item.objects.get(id=pk)
    if request.method=='POST':
        product.delete()
        return redirect('stockapp-item')
    return render(request, 'stockapp/item_delete.html')


def item_update(request, pk):
    item = Item.objects.get(id=pk)
    if request.method=='POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('stockapp-item')

    else:
        form = ItemForm(instance=item)    

    context = {
        
        'form': form,
       
    }

    return render(request, 'stockapp/item_update.html', context)

def report(request):
    item = Item.objects.all()
    products = Item.objects.all() 

    template_path = 'stockapp/report.html'
    context = {
        'products': products,
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Report.pdf"'
    
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

######################
def adminpage(request):
    return render(request,"admin.html")

def index(request):
    context = {}
    return  render(request,"index.html",context)