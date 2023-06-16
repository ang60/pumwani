from .models import *
from django import forms
from django.forms import ModelForm
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordResetForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'password', 'phonenumber')

class LoginForm(ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class SummaryOfLabourform(ModelForm):
    class Meta:
        model = summary_of_labour
        fields = "__all__"
        widgets = {
            'induction_of_labour': forms.Select(attrs={'class': 'form-control'}),
            'resuscitation': forms.Select(attrs={'class': 'form-control'}),
            'placenta': forms.Select(attrs={'class': 'form-control'}),
            'membarnes': forms.Select(attrs={'class': 'form-control'})
        }

class newpatientregistrationform(ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"

class paymentform(ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
        widgets = {
            'other insurances': forms.Select(attrs={'class': 'form-control'})
        }

class nextofkinform(ModelForm):
    class Meta:
        model = NextofKin
        fields = "__all__"        

class obstetrichistoryformone(ModelForm):
    class Meta:
        model = Obstetric_history
        fields = ['LMP','EDD','GRAVID','PARITY']

class obstetrichhistoryformtwo(ModelForm):
    class Meta:
        model = Obstetric_history
        fields = ['date_of_birth','sex','place_of_birth','weight','length_labour','Mode_of_delivery','pueperium','complications','feeding']


class obstetrichistoryformthree(ModelForm):
    class Meta:
        model = Obstetric_history
        fields = ['menarche','cycle','length_menstrual','regularity','flow','present_pregnancy','date_of_quickening','gestation_on_firstvisit','clinical_estimation','complaints','length_pregnancy','pain','bleeding','vomiting','frequency','operations','blood_transfusion','recent_drugs_taken','signature','time']

class obstetrichistoryformfour(ModelForm):
    class Meta:
        model = Obstetric_history
        fields = ['illness','date','treatment','others']

class obstetrichistoryformfive(ModelForm):
    class Meta:
        model = Obstetric_history
        fields = ['twin','TB','essen_hypert','sample','heart_did','relation','smoking','alcohol','sports']

class obstetrichistoryformsix(ModelForm):
    class Meta:
        model = Obstetric_history
        fields = ['blood_group','rhesus','hb','rbs','vdrl','serology','hep_b','urinalysis','clinics_attended','number_of_visits']
        widgets = {
            'blood_group': forms.Select(attrs={'class': 'form-control'}),
            'rhesus': forms.Select(attrs={'class': 'form-control'})
        } 

class  antenatalrecordsform(ModelForm):
    class Meta:
        model = antenatal_records
        fields = ['visit_number','date_records','weight_records','maturity','fundal_height','presentation','urine_analysis','palor','lie','fetal_heart_rate','fetal_movement','remarks','next_visit','sign','urine_analysis','engagement','blood_pressure']

class physicalexaminationsform(ModelForm):
    class Meta:
        model = physical_examination
        fields = ['bp','pulse_rate','respiratory_rate','temperature','SPO2','anaemia','oedema','weight','height','investigations','urine','fundal_height','presentation','position','lie','engagement','spleen','liver','proteins','ext_genitalia','vaginal_wall','fetal_position','consistency','dilation','membrane_or_cord_status','effacement','vaginal_discharge','acetone','sacral_promontory','sacral_curve','intrapubic_angle','intratuberous_diameter','volume']


class tetanus_toxoidform(ModelForm):
    class Meta:
        model = Tetanus_Toxoid
        fields = "__all__"

class tetanustoxoidform(ModelForm):
    class Meta:
        model = TetanusToxoid
        fields = "__all__"   


class vitalsignsform(ModelForm):
    class Meta:
        model = VitalSigns
        fields = "__all__"

class reportlabouroneform(ModelForm):
    class Meta:
        model = report_labourone
        fields = ['date_report_labour','report','began','membranes_ruptured','full_dilation','baby_born','placenta_expelled','amount_of_loss','date','hours','date_labour','drug_labour','time_labour','given_by','remarks']
        
class reportlabourtwoform(ModelForm):
    class Meta:
        model = report_labourtwo
        fields = "__all__"

class reportlabourthreeform(ModelForm):
    class Meta:
        model = Report_labourthree
        fields = "__all__"

class afterdeliveryform(ModelForm):
    class Meta:
        model =  after_delivery
        fields = "__all__"

class vitalsignsobservationchart(ModelForm):
    class Meta:
        model = Vital_Chart
        fields = "__all__"

class preanaestheticassementformone(ModelForm):
    class Meta:
        model = Pre_anaesthetic
        fields = ['date','operation','emergency','elective','past_history','present_condition','regular_condition','allergies','airway_assessment','heart_rate','blood_pressure','heart_sounds','pallor','edema','other']

class preanaestheticassementformtwo(ModelForm):
    class Meta:
        model = Pre_anaesthetic
        fields = ['respiratory_system','operation','pupils','other_cns','glascow_coma_scale','asa_class','investigations','preoperative_instructions','anesthetist_name','anesthetist_sign']

class magnesiumsulphateform(ModelForm):
    class Meta:
        model = Magnesium_sulphate
        fields = "__all__"

class preoperationformone(ModelForm):
     class Meta:
        model = Pre_operationone
        fields = "__all__"

class preoperationtwoform(ModelForm):
    class Meta:
        model = Pre_operationtwo
        fields = "__all__"

class preoperationthreeform(ModelForm):
    class Meta:
        model = Pre_operationthree
        fields = "__all__"

class preoperationfourform(ModelForm):
    class Meta:
        model = Pre_operationfour
        fields = "__all__" 

class beforeanaesthesiaform(ModelForm):
    class Meta:
        model = before_anaesthesia
        fields = "__all__"

class beforeincisionform(ModelForm):
    class Meta:
        model = before_incision
        fields = "__all__"

class beforeleavingorform(ModelForm):
    class Meta:
        model = before_leaving_OR
        fields = "__all__"

class anaestheticrecordform(ModelForm):
    class Meta:
        model = anaesthetic_record
        fields = "__all__"

class theatreoperationsform(ModelForm):
    class Meta:
        model = theatre_operations
        fields = "__all__"

class postoperationform(ModelForm):
    class Meta:
        model = post_operation
        fields = "__all__"

class impatienttreatmentform(ModelForm):
    class Meta:
        model = impatient_treatment
        fields = "__all__"

class nursingcareplanform(ModelForm):
    class Meta:
        model = nursing_care_plan
        fields = "__all__"

class dischargeform(ModelForm):
    class Meta:
        model = discharge
        fields = "__all__"

class cardexform(ModelForm):
    class Meta:
        model = cardex
        fields = "__all__"

class diseasecodeform(ModelForm):
    class Meta:
        model = disease_codes
        fields = "__all__"

class continuationsheetform(ModelForm):
    class Meta:
        model = continuation_sheet
        fields = "__all__"

class chargesheetform(ModelForm):
    class Meta:
        model = charge_sheet
        fields = "__all__"

class gatepassform(ModelForm):
    class Meta:
        model = gate_pass
        fields = "__all__"

class paymentparticularsform(ModelForm):
    class Meta:
        model = payment_particulars
        fields = "__all__"

class fetalheartrateform(ModelForm):
    class Meta:
        model = fetal_heart_rate
        fields = "__all__"

class dilationform(ModelForm):
    class Meta:
        model = dilation
        fields = "__all__"

class fourhourlytempform(ModelForm):
    class Meta:
        model = four_hourly_temp
        fields = "__all__"

class resultsofoperationform(ModelForm):
    class Meta:
        model = results_of_operation
        fields = "__all__"


class pulsebpform(ModelForm):
    class Meta:
        model = pulse_BP
        fields = "__all__"

class contractions(ModelForm):
    class Meta:
        model = contractions
        fields = "__all__"

class graphhistory(ModelForm):
    class Meta:
        model = graph
        fields = "__all__"

class intakeform(ModelForm):
    class Meta:
        model = intake
        fields = "__all__"

class outputform(ModelForm):
    class Meta:
        model = output
        fields = "__all__" 

class PhonePasswordResetForm(PasswordResetForm):
    phone_number = forms.CharField(max_length=10)

    def clean_email(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number:
            raise forms.ValidationError("please enter your phone number")
        return phone_number

class ForgotPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        label='Email',
        max_length=100,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control'})
    )
    
    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)
        self.fields['email'].widgets.attrs.update({'placeholder': 'enter your email'})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('please enter your email')
        return email

class PasswordCreationForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('password',)

class OTPVerificationForm(forms.Form):
    otp = forms.IntegerField()

    



    

    
            