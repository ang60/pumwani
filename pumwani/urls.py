"""
URL configuration for pumwani project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from patients.views import *
from django.urls import path, include
from django.contrib.auth import views as auth_views




urlpatterns = [
   path('admin/', admin.site.urls),
   path('settings/', settings_page, name='settings'),
   path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
   path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
   #path('register/',register, name='register'),
   path('settings/phone/', phone_number_update, name='phone_number_update'),
   path('password/', password_change, name='password_change'),
   path('obstetric/', obstetric_historyformone, name='obstetric_historyformone'),
   path('obstetric/', obstetric_historyformtwo, name='obstetric_historyformtwo'),
   path('obstetric/', obstetric_historyformthree, name='obstetric_historyformthree'),
   path('obstetric/', obstetric_historyformfour, name='obstetric_historyformfour'),
   path('obstetric/', obstetric_historyformfive, name='obstetric_historyformfive'),
   path('obstetric/', obstetric_historyformsix, name='obstetric_historyformsix'),
   path('patient/', patientform, name='patientform'),
   path('payment_form/', payment_form, name='payment_form'),
   path('nextofkin/', nextofkinform, name='nextofkin'),
   path('antenatal/', antenatalrecordsform, name='antenatalrecordsform'),
   path('physicalexamination/', physicalexaminationform, name='physicalexaminationform'),
   path('tetanustoxoid/', tetanus_toxoidform, name='tetanus_toxoidform'),
   path('tetanustoxoid/', tetanustoxoidform, name='tetanustoxoidform'),
   path('reportonlabourone/', reportlabouroneform, name='reportlabouroneform'),
   path('reportlabourtwo/', reportlabourtwoform, name='reportlabourtwoform'),
   path('reportlabourthree/', reportlabourthreeform, name='reportlabourthreeform'),
   path('continuationsheet/', continuation_sheetform, name='continuation_sheetform'),
   path('preanaestheticone/', pre_anaestheticformone, name='pre_anaestheticformone'),
   path('preanaesthetictwo/', pre_anaestheticformtwo, name='pre_anaestheticformtwo'),
   path('magnesiumsulphate/', magnesium_sulphateform, name='tetanus_toxoidform'),
   path('preoperationone/', pre_operationformone, name='pre_operationformone'),
   path('preoperationtwo/', pre_operationformtwo, name='pre_operationformtwo'),
   path('preoperationthree/', pre_operationformthree, name='pre_operationformthree'),
   path('preoperationfour/', pre_operationformfour, name='pre_operationformfour'),
   path('beforeincison/', before_incisionform, name='before_incisionform'),
   path('beforeleavingor/', before_leavingorform, name='beforeleavingorform'),
   path('anaestheticrecord/', anaesthetic_recordform, name='anaesthetic_recordform'),
   path('theatreoperation/', theatre_operationsform, name='theatre_operationsform'),
   path('impatienttreatment/', impatient_treatmentform, name='impatient_treatmentform'),
   path('nursingcareplan/', nursing_careplanform, name='nursing_careplanform'),
   path('discharge/', discharge_form, name='discharge_form'),
   path('cardex/', cardex_form, name='cardex_form'),
   path('diseasecode/', disease_codeform, name='disease_codeform'),
   path('chargesheet/', charge_sheetform, name='charge_sheetform'),
   path('gatepass/', gatepass_form, name='gatepass_form'),
   path('paymentparticulars/', payment_particularsform, name='payment_particularsform'),
   path('fetalheartrate/', fetal_heartrateform, name='fetal_heartrateform'),
   path('fourhourlytemp/', four_hourlytempform, name='four_hourlytempform'),
   path('summaryoflabour/', summaryoflabourform, name='summaryoflabourform'),
   path('intake/', intake_form, name='intake_form'),
   path('output/', output_form, name='output_form'),
   path('summaryoflabour/', summaryoflabourform, name='summaryoflabourform'),
   path('displaypatient/', display_patient, name='display_patient'),
   path('password-reset/', PhonePasswordResetView.as_view(), name='password_reset'),
   path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
   path('create_password/', create_password, name='create_password'),
   path('verify_otp/', verify_otp, name='verify_otp'),

   

]
