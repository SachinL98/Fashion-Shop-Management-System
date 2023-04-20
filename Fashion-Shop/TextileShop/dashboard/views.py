from django.shortcuts import render,redirect
from django.http import HttpResponse
from dashboard.models import utilitybill
from dashboard.models import employee_salasry
from stockapp.models import Item
from fashion.models import SupplierCancelDetails
from salesapp.models import Sales
from dashboard.forms import employeesalForm
from dashboard.forms import utilitybillForm
from django.contrib import messages


from django.views.generic import View
 
#importing get_template from loader
from django.template.loader import get_template
 
#import render_to_pdf from util.py 

from xhtml2pdf import pisa


navbar = {}

# Create your views here.
def indexSVD(request):

    if 'username' not in request.session:
        return  redirect("index")
    else :
        type = request.session.get('type')

        navbar['navbar'] = "finance"

        if type == "admin" or type == "finance manager":
            
            return render(request,'dashboard/indexSVD.html',navbar)
        else :
            return  redirect("index")

def employeeSVD(request):
    sals = employee_salasry.objects.raw('SELECT * FROM dashboard_employee_salasry GROUP BY date ORDER BY date DESC ')
    
    if request.method=='POST':
        form=employeesalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-employeeSVD')
    else:
        form=employeesalForm()
    
    #names=supplier.objects.all()
    #form=employeesalForm(request.POST)
    # j=0
    #for i in names:
    #   if ids.name==form.name:
    #      j=1
    #
    #if j==1:
    #   massge
    #else:
    #    from.save


    employeedit={
        'sals':sals,
        'form':form,
    }
    return render(request,'dashboard/employeeSVD.html',employeedit)

def employee_deleteF(request,pk):
    employee=employee_salasry.objects.get(id=pk)
    if request.method=='POST':
        employee.delete()
        return redirect('dashboard-employeeSVD')
    return render(request,'dashboard/employee_deleteF.html')

def employee_updateF(request,pk):
    employee=employee_salasry.objects.get(id=pk)
    if request.method=='POST':
        form=employeesalForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('dashboard-employeeSVD')
    else:
       form=employeesalForm(instance=employee) 
    context={
        'form':form,
    }
    return render(request,'dashboard/employee_updateF.html',context)

def itemSVD(request):
    itemsF=Item.objects.all()
    itemdet={
        'itemsF':itemsF
    }
    return render(request,'dashboard/itemSVD.html',itemdet)

def orderSVD(request):
    ordersF=SupplierCancelDetails.objects.all()
    orderdet={
        'ordersF':ordersF
    }
    return render(request,'dashboard/orderSVD.html',orderdet)


def salesSVD(request):
    salesF=Sales.objects.all()
    salesdet={
        'salesF':salesF
    }
    return render(request,'dashboard/salesSVD.html',salesdet)

def utilitySVD(request):
    bills=utilitybill.objects.all()
    #bills=utilitybill.objects.raw('SELECT*FROM dashboard_utilitybill')

    if request.method=='POST':
        form=utilitybillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-utilitySVD')
    else:
        form=utilitybillForm()
    
    utilbill={
        'bills':bills,
        'form':form
    }
    return render(request,'dashboard/utilitySVD.html',utilbill)

def utility_deleteF(request,pk):
    bill=utilitybill.objects.get(id=pk)
    if request.method=='POST':
        bill.delete()
        return redirect('dashboard-utilitySVD')
    return render(request,'dashboard/utility_deleteF.html')

def utility_updateF(request,pk):
    bill=utilitybill.objects.get(id=pk)
    if request.method=='POST':
        form=utilitybillForm(request.POST,instance=bill)
        if form.is_valid():
            form.save()
            return redirect('dashboard-utilitySVD')
    else:
       form=utilitybillForm(instance=bill)
     
    context={
        'form':form,
    }
    return render(request,'dashboard/utility_updateF.html',context)

def reportSVD(request):

    return render(request,'dashboard/reportSVD.html')

#create pdf file for report
def reportSVD_pdf(request, *args, **kwargs):

    #get calculate cost
    utilir=utilitybill.objects.raw('SELECT * FROM dashboard_utilitybill where MONTH(curdate())=MONTH(date)')
    t1=0
    for i in utilir:
        t1=t1+i.price

    ordersr=SupplierCancelDetails.objects.raw('SELECT * FROM fashion_supplierCancelDetails where MONTH(curdate())=MONTH(cancelledDate)')
    t2=0
    for i in ordersr:
        t2=t2+i.total
    
    emps=employee_salasry.objects.raw('SELECT * FROM dashboard_employee_salasry where MONTH(curdate())=MONTH(date)')
    t3=0
    for i in emps:
        t3=t3+i.netsal

    cost=t1+t2+t3
    
    #calculate net income
    salesr=Sales.objects.raw('SELECT * FROM salesapp_sales where MONTH(curdate())=MONTH(Date)')
    
    inc=0
    for i in salesr:
        inc=inc+i.totalPrice
    
    net_income=inc-cost



    template_path = 'dashboard/reportSVD_pdf.html'
    context = {
        'utilir':utilir,
        'ordersr':ordersr,
        'emps':emps,
        'salesr':salesr,
        'cost':cost,
        'inc':inc,
        'net_income':net_income,
        't1':t1,
        't2':t2,
        't3':t3,
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="Finance_Report.pdf"'
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

def search_emp(request):
    if request.method=="POST":
        searchemp = request.POST['searchemp']
        if len(searchemp)==0:
            messages.success(request,"Please fill all the fields !!! ")
            return render(request,'dashboard/indexSVD.html')

        else:
            results=employee_salasry.objects.filter(empid__contains=searchemp)
            return render(request,'dashboard/search_emp.html',{'results':results})
    else:
        return render(request)
    
###################
def adminpage(request):

    return render(request,"admin.html")

def index(request):
    context = {}
    return  render(request,"index.html",context)
# Create your views here.
