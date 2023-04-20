from django.shortcuts import render,redirect
from django.http import HttpResponse
from salesapp.models import Sales
from salesapp.forms import SalesForm
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import View
from salesapp.forms import SalesForm

# Create your views here.

def indexSales(request):

     if 'username' not in request.session:
        return  redirect("index")
     else :
        type = request.session.get('type')

       
        if type == "admin" or type == "salesManager":
          return render(request,'salesapp/indexSales.html')
        else :
          return  redirect("index")
     

def sales(request):
     sales = Sales.objects.all()
     #sales = Sales.objects.raw('SELECT * FROM salesapp_sales')
     
     if request.method =='POST':
          form = SalesForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('salesapp-sales')
     else:
          form = SalesForm()
     
     context = {
          'sales': sales,
          'form': form,
     }
     return render(request,'salesapp/sales.html',context)
    


def sales_delete(request, pk):
     sale = Sales.objects.get(id=pk)
     if request.method=='POST':
          sale.delete()
          return redirect('salesapp-sales')
     return render(request, 'salesapp/sales_delete.html')

def sales_update(request, pk):
     sale = Sales.objects.get(id=pk)
     if request.method=='POST':
          form = SalesForm(request.POST, instance=sale)
          if form.is_valid():
               form.save()
               return redirect('salesapp-sales')
     else:
          form = SalesForm(instance=sale)
     context={
          'form': form,
     }
     return render(request, 'salesapp/sales_update.html', context)

def pdf_report_create(request):
     sales = Sales.objects.raw('SELECT * FROM salesapp_sales WHERE MONTH(curdate())=MONTH(Date)')

     template_path = 'salesapp/report.html'
     context = {'sales':sales }
    # Create a Django response object, and specify content_type as pdf
     response = HttpResponse(content_type='application/pdf')
     response['Content-Disposition'] = ' filename="Sales Report.pdf"'
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

def order(request):
     return render(request,'salesapp/order.html')

def logout(request):
     return render(request,'salesapp/logout.html')

###########################
def adminpage(request):
    return render(request,"admin.html")

def index(request):
    context = {}
    return  render(request,"index.html",context)
# Create your views here.
