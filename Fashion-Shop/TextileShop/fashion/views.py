from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from xhtml2pdf import pisa
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

context ={}


# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('fashion/admin_dashboard.html')
    return render(request,'fashion/admin_dashboard.html')


#---------------------------------------------------------------------------------
#------------------------ ADMIN RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------

def admin_dashboard_view(request):
    #for both table in admin dashboard
    ordermngrs=models.Ordermngr.objects.all().order_by('-id')
    suppliers=models.Supplier.objects.all().order_by('-id')
    #for three cards
    ordermngrcount=models.Ordermngr.objects.all().filter(status=True).count()
    pendingordermngrcount=models.Ordermngr.objects.all().filter(status=False).count()

    suppliercount=models.Supplier.objects.all().filter(status=True).count()
    pendingsuppliercount=models.Supplier.objects.all().filter(status=False).count()

    ordercount=models.Order.objects.all().filter(status=True).count()
    pendingordercount=models.Order.objects.all().filter(status=False).count()
    mydict={
    'ordermngrs':ordermngrs,
    'suppliers':suppliers,
    'ordermngrcount':ordermngrcount,
    'pendingordermngrcount':pendingordermngrcount,
    'suppliercount':suppliercount,
    'pendingsuppliercount':pendingsuppliercount,
    'ordercount':ordercount,
    'pendingordercount':pendingordercount,
    }
    return render(request,'fashion/admin_dashboard.html',context=mydict)


# this view for sidebar click on admin page

def admin_ordermngr_view(request):
    return render(request,'fashion/admin_ordermngr.html')

def admin_view_ordermngr_view(request):
    ordermngrs=models.Ordermngr.objects.all().filter(status=True)
    return render(request,'fashion/admin_view_ordermngr.html',{'ordermngrs':ordermngrs})

def delete_ordermngr_from_fashion_view(request,pk):
    ordermngr=models.Ordermngr.objects.get(id=pk)
    user=models.User.objects.get(id=ordermngr.user_id)
    user.delete()
    ordermngr.delete()
    return redirect('admin-view-ordermngr')

def update_ordermngr_view(request,pk):
    ordermngr=models.Ordermngr.objects.get(id=pk)
    user=models.User.objects.get(id=ordermngr.user_id)

    userForm=forms.OrdermngrUserForm(instance=user)
    ordermngrForm=forms.OrdermngrForm(request.FILES,instance=ordermngr)
    mydict={'userForm':userForm,'ordermngrForm':ordermngrForm}
    if request.method=='POST':
        userForm=forms.OrdermngrUserForm(request.POST,instance=user)
        ordermngrForm=forms.OrdermngrForm(request.POST,request.FILES,instance=ordermngr)
        if userForm.is_valid() and ordermngrForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            ordermngr=ordermngrForm.save(commit=False)
            ordermngr.status=True
            ordermngr.save()
            return redirect('admin-view-ordermngr')
    return render(request,'fashion/admin_update_ordermngr.html',context=mydict)


def admin_add_ordermngr_view(request):
    userForm=forms.OrdermngrUserForm()
    ordermngrForm=forms.OrdermngrForm()
    mydict={'userForm':userForm,'ordermngrForm':ordermngrForm}
    if request.method=='POST':
        userForm=forms.OrdermngrUserForm(request.POST)
        ordermngrForm=forms.OrdermngrForm(request.POST, request.FILES)
        if userForm.is_valid() and ordermngrForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()

            ordermngr=ordermngrForm.save(commit=False)
            ordermngr.user=user
            ordermngr.status=True
            ordermngr.save()

            my_ordermngr_group = Group.objects.get_or_create(name='ORDERMNGR')
            my_ordermngr_group[0].user_set.add(user)

        #return HttpResponseRedirect('admin-view-ordermngr')
        return render(request,'fashion/admin_add_ordermngr.html',context=mydict)
    return render(request,'fashion/admin_add_ordermngr.html',context=mydict)

def admin_approve_ordermngr_view(request):
    #those whose approval are needed
    ordermngrs=models.Ordermngr.objects.all().filter(status=False)
    return render(request,'fashion/admin_approve_ordermngr.html',{'ordermngrs':ordermngrs})

def approve_ordermngr_view(request,pk):
    ordermngr=models.Ordermngr.objects.get(id=pk)
    ordermngr.status=True
    ordermngr.save()
    return redirect(reverse('admin-approve-ordermngr'))

def reject_ordermngr_view(request,pk):
    ordermngr=models.Ordermngr.objects.get(id=pk)
    user=models.User.objects.get(id=ordermngr.user_id)
    user.delete()
    ordermngr.delete()
    return redirect('admin-approve-ordermngr')

def admin_view_ordermngr_specialisation_view(request):
    ordermngrs=models.Ordermngr.objects.all().filter(status=True)
    return render(request,'fashion/admin_view_ordermngr_specialisation.html',{'ordermngrs':ordermngrs})

def admin_supplier_view(request):
    return render(request,'fashion/admin_supplier.html')

def admin_view_supplier_view(request):
    suppliers=models.Supplier.objects.all().filter(status=True)
    return render(request,'fashion/admin_view_supplier.html',{'suppliers':suppliers})

def delete_supplier_from_fashion_view(request,pk):
    supplier=models.Supplier.objects.get(id=pk)
    user=models.User.objects.get(id=supplier.user_id)
    user.delete()
    supplier.delete()
    return redirect('admin-view-supplier')

def update_supplier_view(request,pk):
    supplier=models.Supplier.objects.get(id=pk)
    user=models.User.objects.get(id=supplier.user_id)

    userForm=forms.SupplierUserForm(instance=user)
    supplierForm=forms.SupplierForm(request.FILES,instance=supplier)
    mydict={'userForm':userForm,'supplierForm':supplierForm}
    if request.method=='POST':
        userForm=forms.SupplierUserForm(request.POST,instance=user)
        supplierForm=forms.SupplierForm(request.POST,request.FILES,instance=supplier)
        if userForm.is_valid() and supplierForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            supplier=supplierForm.save(commit=False)
            supplier.status=True
            supplier.assignedOrdermngrId=request.POST.get('assignedOrdermngrId')
            supplier.save()
            return redirect('admin-view-supplier')
    return render(request,'fashion/admin_update_supplier.html',context=mydict)


def admin_add_supplier_view(request):
    userForm=forms.SupplierUserForm()
    supplierForm=forms.SupplierForm()
    mydict={'userForm':userForm,'supplierForm':supplierForm}
    if request.method=='POST':
        userForm=forms.SupplierUserForm(request.POST)
        supplierForm=forms.SupplierForm(request.POST,request.FILES)
        if userForm.is_valid() and supplierForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()

            supplier=supplierForm.save(commit=False)
            supplier.user=user
            supplier.status=True
            supplier.assignedOrdermngrId=request.POST.get('assignedOrdermngrId')
            supplier.save()

            my_supplier_group = Group.objects.get_or_create(name='SUPPLIER')
            my_supplier_group[0].user_set.add(user)

        return render(request,'fashion/admin_add_supplier.html',context=mydict)
    return render(request,'fashion/admin_add_supplier.html',context=mydict)

def admin_approve_supplier_view(request):
    #those whose approval are needed
    suppliers=models.Supplier.objects.all().filter(status=False)
    return render(request,'fashion/admin_approve_supplier.html',{'suppliers':suppliers})

def approve_supplier_view(request,pk):
    supplier=models.Supplier.objects.get(id=pk)
    supplier.status=True
    supplier.save()
    return redirect(reverse('admin-approve-supplier'))

def reject_supplier_view(request,pk):
    supplier=models.Supplier.objects.get(id=pk)
    user=models.User.objects.get(id=supplier.user_id)
    user.delete()
    supplier.delete()
    return redirect('admin-approve-supplier')



#--------------------- FOR Receiving SUPPLIER BY ADMIN START-------------------------

def admin_cancel_supplier_view(request):
    suppliers=models.Supplier.objects.all().filter(status=True)
    return render(request,'fashion/admin_cancel_supplier.html',{'suppliers':suppliers})

def cancel_supplier_view(request,pk):
    supplier=models.Supplier.objects.get(id=pk)
    qty=models.Order.objects.get(supplierId=supplier.get_id)
    q=qty.quantity
    assignedOrdermngr=models.User.objects.all().filter(id=supplier.assignedOrdermngrId)
    supplierDict={
        'supplierId':pk,
        'name':supplier.get_name,
        'mobile':supplier.mobile,
        'address':supplier.address,
        'item_code':supplier.item_code,
        'confirmedDate':supplier.confirmedDate,
        'todayDate':date.today(),
        'assignedOrdermngrName':assignedOrdermngr[0].first_name,
        'quantity':q
    }
    if request.method == 'POST':
        feeDict ={
            'units':int(request.POST['units'])*int(q),
            'Othercharges' : request.POST['Othercharges'],
            'Transportfee' : request.POST['Transportfee'],
            'total':(int(request.POST['units'])*int(q))+int(request.POST['Transportfee'])+int(request.POST['Othercharges'])
        }
        supplierDict.update(feeDict)
        #for updating to database supplierCancelDetails (pDD)
        pDD=models.SupplierCancelDetails()
        pDD.supplierId=pk
        pDD.supplierName=supplier.get_name
        pDD.assignedOrdermngrName=assignedOrdermngr[0].first_name
        pDD.address=supplier.address
        pDD.mobile=supplier.mobile
        pDD.item_code=supplier.item_code
        pDD.confirmedDate=supplier.confirmedDate
        pDD.cancelledDate=date.today()
        pDD.quantity=qty.quantity
        pDD.units=int(request.POST['units'])*int(q)
        pDD.Othercharges=int(request.POST['Othercharges'])
        pDD.Transportfee=int(request.POST['Transportfee'])
        pDD.total=(int(request.POST['units'])*int(q))+int(request.POST['Othercharges'])+int(request.POST['Transportfee'])
        pDD.save()
        return render(request,'fashion/supplier_final_bill.html',context=supplierDict)
    return render(request,'fashion/supplier_generate_bill.html',context=supplierDict)



#--------------for Dispatch supplier bill (pdf) download and printing
import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return



def download_pdf_view(request,pk):
    cancelDetails=models.SupplierCancelDetails.objects.all().filter(supplierId=pk).order_by('-id')[:1]
    dict={
        'supplierName':cancelDetails[0].supplierName,
        'assignedOrdermngrName':cancelDetails[0].assignedOrdermngrName,
        'address':cancelDetails[0].address,
        'mobile':cancelDetails[0].mobile,
        'item_code':cancelDetails[0].item_code,
        'confirmedDate':cancelDetails[0].confirmedDate,
        'cancelledDate':cancelDetails[0].cancelledDate,
        'Othercharges':cancelDetails[0].Othercharges,
        'units':cancelDetails[0].units,
        'Transportfee':cancelDetails[0].Transportfee,
        'total':cancelDetails[0].total,
        'quantity':cancelDetails[0].quantity,
    }
    return render_to_pdf('fashion/download_bill.html',dict)

#################################################


def generatepdf(request):

    buf = io.BytesIO()
    c = canvas.Canvas(buf,pagesize=letter,bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)

    cancelDetails=models.SupplierCancelDetails.objects.all()
    result = CancelDetails.objects.all()

    lines = []

    for od in result:
       lines.append("SupplierId : " + od.supplierId)
       lines.append("item_code : " + od.item_code)
       lines.append("Quantity : " + od.quantity)
       lines.append("Total : " + od.total)
       lines.append("Date : " + od.cancelddate)
       lines.append("====================")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf,as_attachment=True,filename='orders.pdf')







#-----------------ORDER START--------------------------------------------------------------------

def admin_order_view(request):
    return render(request,'fashion/admin_order.html')

def admin_view_order_view(request):
    orders=models.Order.objects.all().filter(status=True)
    return render(request,'fashion/admin_view_order.html',{'orders':orders})

def admin_add_order_view(request):
    orderForm=forms.OrderForm()
    mydict={'orderForm':orderForm,}
    if request.method=='POST':
        orderForm=forms.OrderForm(request.POST)
        if orderForm.is_valid():
            order=orderForm.save(commit=False)
              
            order.ordermngrId=request.POST.get('ordermngrId')
            order.supplierId=request.POST.get('supplierId')
            order.ordermngrName=models.User.objects.get(id=request.POST.get('ordermngrId')).first_name
            order.supplierName=models.User.objects.get(id=request.POST.get('supplierId')).first_name
          
            order.status=True
            order.save()
            
            quantity = request.POST.get('quantity')
            item_code = request.POST.get('item_code')
            colour = request.POST.get('colour')
            category = request.POST.get('category')
            
            
            subject = "Order Confirmation"
            message = "Hello You have received an order from Jayananda Fashion \n Order Quantity : " + quantity + "\n Item Code : " + item_code +  "\n Item color :  " + colour + "\n Item Category  " + category 
     
            send_mail(
                    subject,message,'jayanandanafachion@gmail.com',['slsachinlakshan@gmail.com']
            )
            
        return render(request,'fashion/admin_add_order.html',context=mydict)
    return render(request,'fashion/admin_add_order.html',context=mydict)

def admin_approve_order_view(request):
    #those whose approval are needed
    orders=models.Order.objects.all().filter(status=False)
    return render(request,'fashion/admin_approve_order.html',{'orders':orders})

def approve_order_view(request,pk):
    order=models.Order.objects.get(id=pk)
    order.status=True
    order.save()
    return redirect(reverse('admin-approve-order'))

def reject_order_view(request,pk):
    order=models.Order.objects.get(id=pk)
    order.delete()
    return redirect('admin-approve-order')


def admin_view_cancel_supplier_view(request):
    canceldsuppliers=models.SupplierCancelDetails.objects.all()
    return render(request,'fashion/admin_view_cancel_supplier.html',{'canceldsuppliers':canceldsuppliers})

#---------------------------------------------------------------------------------
#------------------------ ADMIN RELATED VIEWS END ------------------------------
#---------------------------------------------------------------------------------



# #------------------------ SUPPLIER RELATED VIEWS END ------------------------------
# #---------------------------------------------------------------------------------








#---------------------------------------------------------------------------------
#------------------------ ABOUT US AND CONTACT US VIEWS START ------------------------------
#---------------------------------------------------------------------------------
def aboutus_view(request):
    return render(request,'fashion/aboutus.html')

def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message, EMAIL_HOST_USER, EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'fashion/contactussuccess.html')
    return render(request, 'fashion/contactus.html', {'form':sub})


#---------------------------------------------------------------------------------
#------------------------ ADMIN RELATED VIEWS END ------------------------------
#---------------------------------------------------------------------------------


def printFile(request):
    order = models.SupplierCancelDetails.objects.all()

    template_path = 'fashion/printFile.html'  ##get template
    context['order'] = order

    response = HttpResponse(content_type = 'application/pdf')
    response['content_Disposition'] = 'filename = "order_report.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html,dest=response)
    
    if pisa_status.err:
        return HttpResponse('We had some errors')
    return response


