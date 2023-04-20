#import imp
#from multiprocessing import context
#from multiprocessing import context
import imp
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Supplier
from .forms import SupplierForm
from django.template.loader import get_template
from xhtml2pdf import pisa
#from supplierapp.forms import SupplierForm

from supplierapp.models import Supplier
#from .forms import SupplierForm

# Create your views here.

def indexsup(request):
    return render(request, 'supplierapp/indexsup.html')


def staff(request):
    return render(request, 'supplierapp/staff.html')   


def supplier(request):
    sup = Supplier.objects.all() #using ORM
    #sup = Supplier.objects.raw('SELECT * FROM supplierapp_supplier')

    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplierapp-supplier')
    else:
        form = SupplierForm()
    context = {
        'sup' : sup,
        'form' : form, 

    }
    return render(request, 'supplierapp/supplier.html',context)

def supplier_delete(request, pk):
    sup_del = Supplier.objects.get(id=pk)
    if request.method=='POST':
        sup_del.delete()
        return redirect('supplierapp-supplier')
    return render(request,'supplierapp/supplier_delete.html')

def supplier_update(request, pk):
    sup_del = Supplier.objects.get(id=pk)
    if request.method=='POST':
        form = SupplierForm(request.POST, instance=sup_del)
        if form.is_valid():
            form.save()
            return redirect('supplierapp-supplier')
    else:
        form = SupplierForm(instance=sup_del)
    context={
        'form' : form,
    }
    return render(request, 'supplierapp/supplier_update.html',context)

def location(request):
    return render(request, 'supplierapp/location.html')  

def supplierReport(request):
    sup = Supplier.objects.all()
    template_path = 'supplierapp/supReport.html'
    context = {
        'sup' : sup,

    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="supplier_report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response  
    
    #return render(request, 'supplierapp/supReport.html',context)
    ###########################
def adminpage(request):
    return render(request,"admin.html")

def index(request):
    context = {}
    return  render(request,"index.html",context)

          