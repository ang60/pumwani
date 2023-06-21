from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import *
from datetime import date
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordResetView
from .forms import PhonePasswordResetForm
from django_otp import match_token
from django.template.response import TemplateResponse



# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form':form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})


def settings_page(request):
    return render(request, 'settings.html')

@login_required
def phone_number_update(request):
    if request.method == 'POST':
        # Update the user's phone number
        phone_number = request.POST.get('phone_number')
        request.user.userprofile.phone_number = phone_number
        request.user.userprofile.save()
        return redirect('settings')
    else:
        return render(request, 'phone_number_update.html')
    
@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password has been changed.')
            return redirect('settings')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'password_change.html', {'form': form})


def obstetric_historyformone(request):
    if request.method == 'POST':
        form = obstetrichistoryformone(request.POST)
   
        if form.is_valid():
            form.save()
            return redirect('obstetric_historyformtwo')
        
    else:
        form = obstetrichistoryformone()

    return render(request, 'obstetric_historyformone.html', {'form':form})
    

def obstetric_historyformtwo(request):
    if request.method == 'POST':
        form = obstetrichistoryformtwo(request.POST)

        if form.is_valid():
            form.save()
            return redirect('obsterrichistoryformthree')
        
    else:
        form = obstetric_historyformtwo()

    return render(request, 'obstetrichistoryformtwo.html',{'form':form})

def obstetric_historyformthree(request):
    if request.method == 'POST':
        form = obstetrichistoryformthree(request.POST)
    

        if form.is_valid():
            form.save()
            return redirect('obstetrichistoryformfour')

    else:
        form = obstetrichistoryformthree()

    return render(request, 'obstetrichistoryformthree.html',{'form':form})

def obstetric_historyformfour(request):
    if request.method == 'POST':
        form = obstetrichistoryformfour(request.POST)

        if form.is_valid():
            form.save()
            return redirect('obstetrichistoryformfour')
        
        else:
            form = obstetrichistoryformfour()
    
    return render(request, 'obstetrichistoryformfour.html',{'form':form})

def obstetric_historyformfive(request):
    if request.method == 'post':
        form = obstetric_historyformsix(request.post)

        if form.is_valid():
            form.save()
            return redirect('obstetrichistoryformfive.html')
    else:
        form = obstetric_historyformfive

    return render(request, 'obstetrichistoryformfive.html',{'form':form})

def obstetric_historyformsix(request):
    if request.method == 'POST':
        form = obstetric_historyformsix(request.POST)

        if form.is_valid():
            form.save()
            return redirect('antenatalrecordsform')
    else:
        form = obstetric_historyformsix

    return render(request, 'obstetrichistoryformsix.html',{'form':form})

def patientform(request):
    if request.method == 'POST':
        form = newpatientregistrationform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('nextofkin')
    else:
        form = newpatientregistrationform()

    return render(request, 'newpatientregistrationform.html',{'form':form})

def payment_form(request):
    if request.method == 'POST':
        form = paymentform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('obstetric_historyformone')
    else:
        form = paymentform()

    return render(request, 'paymentform.html', {'form':form})

def payment_form(request):
    if request.method == 'POST':
        form = paymentform(request.POST)

        if form.is_valid():
            payment_type = form.cleaned_data['payment_type']
            Payment.objects.create(payment_type=payment_type)
            return redirect('obstetric_historyformone')
    else:
        form = paymentform()

    return render(request, 'paymentform.html', {'form': form})


def nextofkinform(request):
    if request.method == 'POST':
        form = nextofkinform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('paymentform')
    else:
        form = nextofkinform()

    return render(request, 'nextofkinform.html',{'form':form})

def antenatalrecordsform(request):
    if request.method == 'POST':
        form = antenatalrecordsform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('physicalexaminationform.html')
        else:
            form = antenatalrecordsform()

    return render(request, 'antenatalrecordsform.html',{'form':form})

def physicalexaminationform (request):
    if request.method =='POST':
        form = physicalexaminationsform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('tetanus_toxoidform')
    else:
        form = physicalexaminationsform()

    return render(request, 'physicalexaminationform.html',{'form':form})

def tetanus_toxoidform(request):
    if request.method == 'POST':
        form = tetanus_toxoidform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('tetanustoxoidform')
    else:
        form = tetanus_toxoidform()

    return render(request, 'tetanus_toxoidform.html',{'form':form})

def vitalsignsform(request):
    if request.method == 'POST':
        form = vitalsignsform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('fetalheartrate')
    else:
        form = vitalsignsform()

    return render(request, 'vitalsignsform.html',{'form':form})

def reportlabouroneform(request):
    if request.method == 'POST':
        form = reportlabouroneform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('reportlabourtwoform')
    else:
        form = reportlabouroneform()

    return render(request, 'reportlabouroneform.html',{'form':form})

def reportlabourtwoform(request):
    if request.method =='POST':
        form = reportlabourtwoform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('reportlabourthree')
    else:
        form =reportlabourtwoform()

    return render(request, 'reportlabourtwoform.html',{'form':form})

def reportlabourthreeform(request):
    if request.method =='POST':
        form = reportlabourthreeform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('continuationsheetform')
    else:
        form = reportlabourthreeform()

    return render(request, 'reportlabourthreeform.html',{'form':form})

def continuation_sheetform(request):
    if request.method == 'POST':
        form = continuationsheetform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('cardexform')
    else:
        form = continuationsheetform()

    return render(request, 'continuationsheetform.html',{'form':form})

def pre_anaestheticformone(request):
    if request.method == 'POST':
        form = preanaestheticassementformone(request.POST)

        if form.is_valid():
            form.save()
            return redirect('pre_anaestheticformtwo')
    else:
        form = preanaestheticassementformone()

    return render(request, 'pre_anaestheticformone.hmtl',{'form':form})

def pre_anaestheticformtwo(request):
    if request.method == 'POST':
        form = preanaestheticassementformtwo(request.POST)

        if form.is_valid():
            form.save()
            return redirect('magnesiumsulphateform')
    else:
        form = preanaestheticassementformtwo()

    return render(request, 'pre_anaestheticformtwo.html',{'form':form})

def magnesium_sulphateform(request):
    if request.method == 'POST':
        form = magnesiumsulphateform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('preoperationformone')
    else:
        form = magnesiumsulphateform()

    return render(request, 'magnesiumsulphateform.html',{'form':form})

def pre_operationformone(request):
    if request.method =='POST':
        form = preoperationformone(request.POST)

        if form.is_valid():
            form.save()
            return redirect('preoperationformtwo')
    else:
        form = preoperationformone()

    return render(request, 'preoperationformone.html',{'form':form})

def pre_operationformtwo(request):
    if request.method == 'POST':
        form = preoperationtwoform(request.POST)

        if  form.is_valid():
            form.save()
            return redirect('preoperationformtwo')
    else:
        form = preoperationtwoform()

    return render(request, 'preopreatioformtwo.html',{'form':form})

def pre_operationformthree(request):
    if request.method == 'POST':
        form = preoperationthreeform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('preoperationformfour')
    else:
        form = preoperationthreeform()

    return render(request, 'preoperationformfour.html',{'form':form})

def pre_operationformfour(request):
    if request.method == 'POST':
        form = preoperationfourform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('beforeincisionform')
    else:
        form = pre_operationformfour()
    return render(request, 'preopreationformfour.html',{'form':form})

def before_incisionform(request):
    if request.method =='POST':
        form = beforeincisionform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('beforeleavingform')
    else:
        form = beforeincisionform()

    return render(request, 'before_incisionform.html',{'form':form})

def before_leavingorform(request):
    if request.method == 'POST':
        form = beforeleavingorform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('anaestheticrecordform')
    else:
        form = beforeleavingorform()

    return render(request, 'beforeleavingorform.html',{'form':form})

def anaesthetic_recordform(request):
    if request.method == 'POST':
        form = anaestheticrecordform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('theatreoperationsform')
    else:
        form = anaestheticrecordform()

    return render(request, 'anaestheticrecordform.html',{'form':form})

def theatre_operationsform(request):
    if request.method == 'POST':
        form = theatreoperationsform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postoperationform')
    else:
        form = theatreoperationsform()

    return render(request, 'theatreoperationsform.html',{'form':form})

def post_operationform(request):
    if request.method == 'POST':
        form = postoperationform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('impatienttreatmentform')
    else:
        form = postoperationform()

    return render(request, 'postoperationform.html',{'form':form})

def impatient_treatmentform(request):
    if request.method == 'POST':
        form =impatienttreatmentform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('nursingcareplanform')
    else:
        form = impatienttreatmentform()

    return render(request, 'impatienttreatmentform.html',{'form':form})

def nursing_careplanform(request):
    if request.method == 'POST':
        form = nursingcareplanform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dischargeform')
    else:
        form = nursingcareplanform()

    return render(request, 'nursingcareplanform.html',{'form':form})

def discharge_form(request):
    if request.method == 'POST':
        form = dischargeform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('cardexform')
    else:
        form = dischargeform()

    return render(request, 'dischargeform.html',{'form':form})

def cardex_form(request):
    if request.method == 'POST':
        form = cardexform(request.POST) 

        if form.is_valid():
            form.save()
            return redirect('diseasecodeform')
    else:
        form = cardexform()

    return render(request, 'cardexform.html',{'form':form})

def disease_codeform(request):
    if request.method == 'POST':
        form = diseasecodeform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('chargesheetform')
    else:
        form = diseasecodeform()

    return render(request, 'diseasecodeform.html',{'form':form})

def charge_sheetform(request):
    if request.method == 'POST':
        form = chargesheetform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('gatepassform')
    else:
        form = chargesheetform()

    return render(request, 'chargesheetform.html',{'form':form})

def gatepass_form(request):
    if request.method == 'POST':
        form = gatepassform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('paymentparticularsform')
    else:
        form = gatepassform()

    return render(request, 'gatepassform.html',{'form':form})

def payment_particularsform(request):
    if request.method == 'POST':
        form = paymentparticularsform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('paymentparticularsform')
    else:
        form = paymentparticularsform()

    return render(request, 'paymentpartricularsform.html',{'form':form})
                
                
def fetal_heartrateform(request):
    if request.method == 'POST':
        form = fetalheartrateform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dilation')
    else:
        form = fetalheartrateform()

    return render(request, 'fetalheartrateform.html',{'form':form})

def dilation_form(request):
    if request.method == 'POST':
        form = dilationform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('fourhourlytempform')
    else:
        form = dilationform()

    return render(request, 'dilationform.html',{'form':form})

def four_hourlytempform(request):
    if request.method == 'POST':
        form = fourhourlytempform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('summaryoflabour')
    else:
        form = fourhourlytempform()

    return render(request, 'fourhourlytempform.html',{'form':form})

def summaryoflabourform(request):
    if request.method == 'POST':
        form = SummaryOfLabourform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('reportonlabourform')
    else:
        form = SummaryOfLabourform()

    return render(request, 'summaryoflabourform.html',{'form':form})

def intake_form(request):
    if request.method == 'POST':
        form = intakeform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('outputform')
    else:
        form = intakeform()

    return render(request, 'intakeform.html',{'form':form})

def output_form(request):
    if request.method == 'post':
        form = outputform(request.post)

        if form.is_valid():
            form.save()
            return redirect('vitalsignsobservationchart')
    else:
        form = outputform()

    return request(request, 'outputform.html',{'form':form})   

def display_patient(request):
    current_date = date.today()
    data = Patient.objects.filter(date_field = current_date).values('full_name', 'patient_number')

    context = {
        'data':data
    } 

    return render(request, 'display_patients.html',context)     
        
class PhonePasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    form_class = PhonePasswordResetForm  
    
class ForgotPasswordView(PasswordResetView):
    template_name = 'Forgot_Password.html'
    email_template_name = 'forgot_password_email.html'
    form_class = ForgotPasswordForm                                                                                                                              

def create_password(request):
    if request.method == 'POST':
        form = PasswordCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to your desired page
    else:
        form = PasswordCreationForm()
    return render(request, 'create_password.html', {'form': form})

def PasswordResetConfirm(request):
    return render(request, 'PasswordResetConfirm.html')

def addpatientconfirm(request):
    return render(request, 'addpatientconfirm.html')

def doctorsdashboard(request):
    return render(request, 'doctorsdashboard.html')

def patienthistory(request):
    return render(request, 'patienthistory.html')

def menupoopup(request):
    return render(request, 'menuppopup.html')

def sidemenupopup(request):
    return render(request, 'sidemenupopup.html')


def logo(request):
    return render(request, 'logo.html')

def welcomepage(request):
    return render(request, 'welcomepage.html')


@login_required
def verify_otp(request):
    if request.method == 'POST':
        form = OTPVerificationForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data['otp']
            if match_token(request.user, otp):
                # OTP is valid
                # Do something (e.g., update user profile, grant access, etc.)
                return redirect('home')  # Redirect to your desired page
            else:
                # Invalid OTP
                form.add_error('otp', 'Invalid OTP. Please try again.')
    else:
        form = OTPVerificationForm()
    return render(request, 'verify_otp.html', {'form': form})

def successregistration(request):
    return render(request, 'successregistration.html')

def afterdelivery(request):
    if request.method == 'POST':
        form = afterdeliveryform(request.post)

        if form.is_valid():
            form.save()
            return redirect('postoperationformone.html')
        
    return render(request, 'afterdelivery.html',{'form':form}) 

def resultsofoperation(request):
    if request.method == 'POST':
        form = resultsofoperationform(request.post)

        if form.is_valid():
            form.save()
            return redirect('pulsebp.html') 

    return render(request, 'resultofoperation.html',{'form':form}) 

def pulsebp(request):
    if request.method == 'POST':
        form = pulsebpform(request.post)

        if form.is_valid():
            form.save()
            return redirect('contractions.html')
        
    return render(request, 'pulsebp.html',{'form':form})  

def contractions(request):
    if request.method == 'POST':
        form = contractions(request.post)

        if form.is_valid():
            form.save()
            return redirect('summaryoflabour.html')
        else:
            form = contractions()

    return render(request, 'contractions.html',{'form':form})      
             
    

