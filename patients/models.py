from django.db import models
#from django-signature import signaturefield
from jsignature.fields import JSignatureField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import datetime, date

today = date.today()

def lmpdate_validator(LMP):
    if LMP > today:
        raise ValidationError("lmp cannot be a future date")
    

def edddate_validator(EDD):
    if EDD > today:
        raise ValidationError("edd cannot be a future date")    
    
# Create your models here.
class CustomUser(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    phonenumber = models.IntegerField(null=True)

class Patient(models.Model):
    # first_name = models.CharField(max_length=30, null=True)
    # last_name = models.CharField(max_length=30, null=True)
    full_name = models.CharField(max_length=100, null=True)
    nationality = models.CharField(max_length=10, null=True)
    age = models.IntegerField(null=True)
    maritalstatus = models.CharField(max_length=20, null=True)
    religion = models.CharField(max_length=20, null=True)
    educationlevel = models.CharField(max_length=30, null=True)
    residence = models.CharField(max_length=30, null=True)
    id_number = models.IntegerField(null=True)
    patient_number = models.IntegerField(null=True)


class NextofKin(models.Model):
    First_Name = models.CharField(max_length=30, null=True)
    Last_Name = models.CharField(max_length=30, null=True)
    Relationship = models.CharField(max_length=10, null=True)
    tel_number = models.CharField(max_length=15, null=True)
    Residence = models.CharField(max_length=30, null=True)
    patient = models.ForeignKey(Patient, max_length=100, on_delete=models.CASCADE)

class Payment(models.Model):
    # patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='payments', null=True)
    payment_type = models.CharField(max_length=50, null=True)



class Obstetric_historyformone(models.Model):

    RADIO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]
    
    LMP = models.DateField(validators=[lmpdate_validator], null=True, )
    EDD = models.DateField(validators=[edddate_validator], null=True)
    GRAVID = models.CharField(max_length=3, choices=RADIO_CHOICES, null=True, default='no')
    PARITY = models.IntegerField(validators=[
            MinValueValidator(1),
            MaxValueValidator(12)
        ], null=True)
    
class Obstetric_historyformtwo(models.Model):
        date_of_birth = models.IntegerField(null=True)
        sex = models.CharField(max_length=10, null=True)
        place_of_birth = models.CharField(max_length=30, null=True)
        weight = models.IntegerField(null=True)
        length_labour = models.CharField(max_length=10, null=True)
        Mode_of_delivery = models.CharField(max_length=30, null=True)
        pueperium = models.IntegerField(null=True)
        complications = models.CharField(max_length=30, null=True)
        feeding = models.CharField(max_length=30, null=True)

class Obstetric_historyformthree(models.Model):    
        life_state = models.BooleanField(null=True)
        menarche = models.IntegerField(null=True)
        cycle = models.CharField(max_length=20, null=True)
        length_menstrual = models.CharField(max_length=20, null=True)
        regularity = models.CharField(max_length=20, null=True)
        flow = models.CharField(max_length=20, null=True)
        present_pregnancy = models.CharField(max_length=20, null=True)
        date_of_quickening = models.DateField(null=True)
        gestation_on_firstvisit = models.IntegerField(null=True)
        clinical_estimation =models.CharField(max_length=100, null=True)
        complaints = models.CharField(max_length=100, null=True)
        length_pregnancy = models.CharField(max_length=20, null=True)
        Complaints =  models.CharField(max_length=30, null=True)
        pain = models.CharField(max_length=30, null=True)
        bleeding = models.BooleanField(null=True)
        vomiting = models.BooleanField(null=True)
        frequency = models.IntegerField(null=True)
        operations = models.IntegerField(null=True)
        blood_transfusion = models.BooleanField(null=True)
        recent_drugs_taken = models.CharField(max_length=30, null=True)
        admitting_officer = models.CharField(max_length=30, null=True)
        signature = JSignatureField(null=True)
        time = models.TimeField(null=True)

class Obstetric_historyformfour(models.Model):    
        illness = models.BooleanField(null=True)
        obstetric_date = models.DateField(null=True)
        treatment = models.CharField(max_length=50, null=True)
        others =models.CharField(max_length=100, null=True)

class Obstetric_historyformfive(models.Model):        
        condition = models.CharField(max_length=100 ,null=True)
        twin = models.BooleanField(null=True)
        TB = models.BooleanField(null=True)
        essen_hypert = models.BooleanField(null=True)
        sample = models.CharField(max_length=100, null=True)
        heart_did = models.BooleanField(null=True)
        relation = models.CharField(max_length=100 , null=True)
        history_date = models.DateField(null=True)
        smoking = models.BooleanField(null=True)
        alcohol = models.BooleanField(null=True)
        sports = models.CharField(max_length=100, null=True)

class Obstetric_historyformsix(models.Model):    
        blood_group = models.CharField(max_length=5 , null=True)
        rhesus = models.CharField(max_length=10 , null=True)
        hb = models.FloatField(null=True)
        rbs = models.FloatField(null=True)
        vdrl = models.BooleanField(default=False)
        serology = models.CharField(max_length=100, null=True)
        hep_b = models.BooleanField(default=False)
        urinalysis = models.CharField(max_length=100, null=True)
        clinics_attended = models.TextField(blank=True)
        number_of_visits = models.IntegerField(null=True)


class past_medical_and_surgical_history (models.Model):
    illness = models.CharField(max_length=100)
    tb = models.BooleanField(default=False)
    renal = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    essen_hypert = models.BooleanField(default=False)
    heart = models.BooleanField(default=False)
    medical_date = models.DateField()
    treatment = models.TextField(blank=True)
    others = models.TextField(blank=True)

class antenatal_records(models.Model):
    family_history = models.ForeignKey(Obstetric_historyformone, on_delete=models.CASCADE)
    visit_number = models.PositiveIntegerField()
    antenatal_date_records = models.DateField()
    weight_records = models.FloatField(null=True)
    maturity = models.CharField(max_length=100, null=True)
    urine_analysis = models.CharField(max_length=100, null=True)
    fundal_height = models.FloatField(null=True)
    blood_pressure = models.CharField(max_length=20, null=True)
    presentation = models.CharField(max_length=100, null=True)
    palor = models.BooleanField(default=False)
    lie = models.CharField(max_length=100, null=True)
    fetal_heart_rate = models.PositiveIntegerField()
    fetal_movement = models.CharField(max_length=100, null=True)
    engagement = models.BooleanField(default=False)
    remarks = models.TextField(blank=True)
    next_visit = models.DateField()
    sign = JSignatureField(null=True)
 
class physical_examination(models.Model):
    bp = models.IntegerField(null=True)
    pulse_rate = models.IntegerField(null=True)
    respiratory_rate = models.IntegerField(null=True)
    temperature = models.IntegerField(null=True)
    SPO2 = models.IntegerField(null=True)
    anaemia = models.BooleanField(default=False)
    oedema = models.BooleanField(default=False)
    weight = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    urine = models.TextField(blank=True)
    investigations = models.TextField(blank=True)
    fundal_height = models.IntegerField(null=True)
    presentation = models.CharField(max_length=100, null=True)
    lie = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100, null=True)
    engagement = models.BooleanField(default=False)
    spleen = models.BooleanField(default=False)
    liver = models.BooleanField(default=False)
    proteins = models.CharField(max_length=100, null=True)
    ext_genitalia = models.CharField(max_length=100, null=True)
    vaginal_wall = models.CharField(max_length=100, null=True)
    fetal_position = models.CharField(max_length=100, null=True)
    consistency = models.CharField(max_length=100, null=True)
    dilation = models.FloatField(null=True)
    membrane_or_cord_status = models.CharField(max_length=100, null=True)
    effacement = models.CharField(max_length=100, null=True)
    vaginal_discharge = models.CharField(max_length=100, null=True)
    acetone = models.BooleanField(default=False)
    sacral_promontory = models.FloatField(null=True)
    sacral_curve = models.FloatField(null=True)
    ischial_spines = models.FloatField(null=True)
    intrapubic_angle = models.FloatField(null=True)
    intratuberous_diameter = models.FloatField(null=True)
    volume = models.FloatField(null=True)

class Tetanus_Toxoid(models.Model):    
    tetanus_toxoid_1_before = models.DateField()
    tetanus_toxoid_2_before = models.DateField()
    tetanus_toxoid_3_before = models.DateField()
    tetanus_toxoid_4_before = models.DateField()
    tetanus_toxoid_5_before = models.DateField()
    tetanus_toxoid_1_after = models.DateField()
    tetanus_toxoid_2_after = models.DateField()
    tetanus_toxoid_3_after = models.DateField()
    tetanus_toxoid_4_after = models.DateField()
    tetanus_toxoid_5_after = models.DateField()

class TetanusToxoid(models.Model):
    first_visit = models.DateField()
    second_visit = models.DateField()
    third_visit = models.DateField()
    fourth_visit = models.DateField()

class VitalSigns(models.Model):
    date_vital_signs = models.DateField()
    temperature_vital_signs = models.DecimalField(max_digits=5, decimal_places=2)
    time_vital_signs = models.TimeField()
    blood_pressure_vital_signs = models.CharField(max_length=20, null=True)
    pulse_vital_signs = models.PositiveIntegerField()
    respiratory_rate = models.PositiveIntegerField()
    name_vital_signs = models.CharField(max_length=100, null=True)

class report_labourone(models.Model):
    date_report_labour = models.DateField()
    report = models.TextField(blank=True)
    #drugs_during_labour(models.Model):
    began = models.DateTimeField()
    membranes_ruptured = models.DateTimeField()
    full_dilation = models.DateTimeField()
    baby_born = models.DateTimeField()
    placenta_expelled = models.DateTimeField()
    amount_of_loss = models.DecimalField(max_digits=5, decimal_places=2)
    duration_date = models.DateField()
    hours = models.PositiveIntegerField()
    #duration_of_labour(models.Model):
    date_labour = models.DateField()
    time_labour = models.TimeField()
    drug_labour = models.CharField(max_length=100, null=True)
    given_by = models.CharField(max_length=100, null=True)
    dose_labour = models.IntegerField(null=True)
    remarks = models.TextField(blank=True)

class report_labourtwo(models.Model):
    perinuem = models.TextField(blank=True)
    satures = models.IntegerField(null=True)
    by_when = models.DateField()
    
class Report_labourthree(models.Model):
    first_stage_duration = models.TimeField()
    second_stage_duration = models.TimeField()
    third_stage_duration = models.TimeField()
    total_time = models.CharField(max_length=100, null=True)
    delivered_by = models.CharField(max_length=100, null=True)
    doctor = models.CharField(max_length=100, null=True)
    midwife = models.CharField(max_length=100, null=True)
    student_or_nurse = models.CharField(max_length=100, null=True)

class after_delivery(models.Model):
    condition_of_the_mother = models.TextField(blank=True)
    condition_of_the_baby = models.TextField(blank=True)
    fundus = models.CharField(max_length=100)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    pulse = models.PositiveIntegerField()
    respiration = models.PositiveIntegerField()
    sex = models.CharField(max_length=10, null=True)
    loss_pv = models.BooleanField(default=False)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    blood_pressure = models.CharField(max_length=20, null=True)
    birth_notification_no = models.CharField(max_length=20, null=True)
    remarks = models.TextField()
    date_of_notification = models.DateField()
    placenta_weight = models.DecimalField(max_digits=5, decimal_places=2)
    notified = models.BooleanField(default=False)
    abnormalities = models.TextField()

class Vital_Chart(models.Model):
    name = models.CharField(max_length=100, null=True)
    ip_number = models.CharField(max_length=20, null=True)
    vital_date = models.DateField()
    time = models.TimeField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    blood_pressure = models.CharField(max_length=20)
    pulse = models.PositiveIntegerField()
    respiratory_rate = models.PositiveIntegerField()

class Pre_anaesthetic(models.Model):
    Pre_anaesthetic_date = models.DateField()
    operation = models.CharField(max_length=100, null=True)
    emergency = models.BooleanField(default=False)
    elective = models.BooleanField(default=False)
    past_history = models.TextField()
    present_condition = models.TextField()
    regular_condition = models.TextField()
    allergies = models.TextField()
    airway_assessment = models.TextField()
    heart_rate = models.PositiveIntegerField()
    blood_pressure = models.CharField(max_length=20)
    heart_sounds = models.TextField()
    pallor = models.BooleanField(default=False)
    edema = models.BooleanField(default=False)
    other = models.TextField()
    respiratory_system = models.CharField(max_length=200, null=True)
    operation = models.CharField(max_length=100, null=True)
    pupils = models.CharField(max_length=100, null=True)
    glascow_coma_scale = models.CharField(max_length=200, null=True)
    other_cns = models.TextField()
    asa_class = models.PositiveIntegerField()
    investigations = models.TextField(blank=True)
    preoperative_instructions = models.TextField()
    anesthetist_name = models.CharField(max_length=100, null=True)
    anesthetist_sign = JSignatureField(null=True)

class Magnesium_sulphate(models.Model):
    Magnesium_sulphate_date = models.DateField()
    time = models.TimeField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    pulse = models.PositiveIntegerField()
    blood_pressure = models.CharField(max_length=20, null=True)
    respiratory_rate = models.PositiveIntegerField()
    urine = models.CharField(max_length=100, null=True)
    output = models.CharField(max_length=100, null=True)
    deep_tendon_reflex = models.CharField(max_length=100, null=True)

class Pre_operationone(models.Model):
    surname = models.CharField(max_length=100, null=True)
    procedure = models.CharField(max_length=100, null=True)
    reg_no = models.CharField(max_length=100, null=True)
    surgeon = models.CharField(max_length=100, null=True)
    sex = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    ward = models.CharField(max_length=100, null=True)
    doctor = models.CharField(max_length=100, null=True)
    dept = models.CharField(max_length=100, null=True)
    Pre_operationone_date = models.DateField()
    anesthetist = models.CharField(max_length=100, null=True)

class Pre_operationtwo(models.Model):
    time_done = models.DateTimeField()
    bp_pre_op = models.CharField(max_length=20, null=True)
    temp_pre_op = models.DecimalField(max_digits=5, decimal_places=2)
    cvp = models.DecimalField(max_digits=5, decimal_places=2)
    pulse_pre_op = models.IntegerField(null=True)
    weight_pre_op = models.DecimalField(max_digits=5, decimal_places=2)
    resp_pre_op = models.IntegerField()
    height_pre_op = models.DecimalField(max_digits=5, decimal_places=2)
    fetal_hr = models.IntegerField(null=True)
    xray_scan = models.BooleanField(null=True)
    ecg = models.FileField(upload_to='ecg_files/', blank=True)
    other_form = models.FileField(upload_to='other_forms/', blank=True)
    bladder_emptied_time = models.DateTimeField()
    urinalysis = models.TextField()
    comments = models.TextField()

class Pre_operationthree(models.Model):
    pre_op_visit_done = models.BooleanField()
    or_nurse_name = models.CharField(max_length=100, null=True)
    sign = JSignatureField()
    prepared_by = models.CharField(max_length=100, null=True)
    handed_over_by = models.CharField(max_length=100, null=True)
    time_arrived_reception = models.DateTimeField()
    received_by = models.CharField(max_length=100, null=True)

class Pre_operationfour(models.Model):
    complete_consent_form = models.BooleanField()
    complete_anaesthesia_assessment = models.BooleanField()
    blood_result_hb = models.BooleanField(verbose_name='Blood Result: Hb*')
    blood_result_u_and_es = models.BooleanField(verbose_name='Blood Result: U&E’s')
    blood_result_blood_sugar = models.BooleanField(verbose_name='Blood Result: Blood Sugar')
    x_match = models.BooleanField(verbose_name='X-Match')
    medication_pre_medication = models.BooleanField(verbose_name='Medication: Pre-medication')
    medication_regular_medication = models.CharField(max_length=200, verbose_name='Medication: Regular Medication (specify)', null=True)
    allergies = models.BooleanField(null=True)
    nil_by_mouth_fasted_from = models.DateTimeField(verbose_name='Nil by mouth: fasted from')
    contact_lens_removed = models.BooleanField(null=True)
    hearing_aid_limb_removed = models.BooleanField(null=True)
    implants_prosthetics = models.BooleanField(null=True)
    dental_caps_crowns_bridge_work_present = models.BooleanField(null=True)
    dentures_removed_loose_teeth = models.BooleanField(null=True)
    jewellery_valuables_removed = models.BooleanField(null=True)
    makeup_nail_vanish_removed = models.BooleanField(null=True)
    bath_shower_going_on = models.BooleanField(verbose_name='Bath/Shower/Going On', null=True)
    shave_skin_preparation = models.BooleanField(verbose_name='Shave/Skin Preparation', null=True)
    surgical_site_marked = models.BooleanField(verbose_name='Surgical Site Marked', null=True)

class before_anaesthesia(models.Model):
    patient_confirm_identity = models.BooleanField(null=True)
    site_marked = models.BooleanField(null=True)
    anesthesia_check_complete = models.BooleanField(null=True)
    pulse_oximeter_on_patient = models.BooleanField(null=True)
    known_allergy = models.BooleanField(null=True)
    difficult_airway_aspiration_risk = models.CharField(max_length=100, null=True)
    blood_loss_risk = models.CharField(max_length=100, null=True)

class before_incision(models.Model):
    team_introduced = models.BooleanField(default=False)
    patient_info_confirmed = models.BooleanField(default=False)
    antibiotics_given = models.BooleanField(default=False)
    critical_events = models.CharField(max_length=200, null=True)
    anticipated_blood_loss = models.CharField(max_length=100, null=True)
    critical_steps = models.TextField(blank=True)
    case_duration = models.CharField(max_length=50, null=True)
    concerns_to_anaesthetist = models.TextField(blank=True)
    concerns_to_nursing_team = models.BooleanField(default=False)
    sterility_confirmed = models.BooleanField(default=False)
    equipment_issues = models.BooleanField(default=False)
    essential_imaging_displayed = models.BooleanField(default=False)

class before_leaving_OR(models.Model):
    team_introduced = models.BooleanField(default=False)
    patient_info_confirmed = models.BooleanField(default=False)
    antibiotics_given = models.BooleanField(default=False)
    nurse_verbal_confirmation = models.CharField(max_length=200, null=True)
    procedure_name = models.CharField(max_length=100, null=True)
    instrument_count_completed = models.BooleanField(default=False)
    equipment_issues = models.BooleanField(default=False)
    recovery_concerns = models.TextField(blank=True)

class anaesthetic_record(models.Model):
    ip_number = models.CharField(max_length=20, null=True)
    operation_name = models.CharField(max_length=100, null=True)
    anaesthetists = models.CharField(max_length=100, null=True)
    age = models.IntegerField(blank=True, null=True)
    surgeons = models.CharField(max_length=100, blank=True)
    record_date = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True)
    premedication_type = models.CharField(max_length=100, null=True)
    premedication_time_given = models.CharField(max_length=50, null=True)
    premedication_effects = models.CharField(max_length=100, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    airway_oro_nasopharyngeal_rl_blind = models.BooleanField(default=False)
    airway_oro_nasotracheal_cuff_pack = models.BooleanField(default=False)
    airway_endobronchial_rl_undermask = models.BooleanField(default=False)
    ifi_hand_rl = models.BooleanField(default=False)
    ifi_arm_rl = models.BooleanField(default=False)
    ifi_leg_rl = models.BooleanField(default=False)

class theatre_operations(models.Model):
    operation_date = models.DateField(blank=True, null=True)
    operation_diagnosis = models.CharField(max_length=100, null=True)
    surgeon = models.CharField(max_length=100, null=True)
    assistant_surgeons = models.CharField(max_length=200, null=True)
    scrub_nurse = models.CharField(max_length=100, null=True)
    anaesthetist = models.CharField(max_length=100, null=True)
    anesthesia_type = models.CharField(max_length=100, null=True)
    incisions = models.TextField(blank=True)
    operation_procedure = models.TextField(blank=True)

class post_operation(models.Model):
    #identification of patients
    identification_band = models.BooleanField(default=False)
    inpatient_number = models.CharField(max_length=20, null=True)
    state_of_consciousness = models.CharField(max_length=100, null=True)
    indication = models.CharField(max_length=100, null=True)
    post_operation_class = models.CharField(max_length=100, null=True)
    the_file = models.CharField(max_length=100, null=True)
    #physical assesment 
    bleeding_at_incision = models.CharField(max_length=100, null=True)
    bleeding_per_vagina = models.CharField(max_length=100, null=True)
    contraction = models.CharField(max_length=100, null=True)
    infusions_or_transfusions = models.CharField(max_length=100, null=True)
    urine_output_catheter = models.CharField(max_length=100, null=True)
    #vital signs
    temp_post_operation = models.IntegerField(null=True)
    resprate_post_operation = models.IntegerField(null=True)
    pulse_post_opeartion = models.IntegerField(null=True)
    bp_post_operation = models.IntegerField(null=True)
    #checklist
    baby_name = models.IntegerField(null=True)
    baby_sex = models.IntegerField(null=True)
    baby_bwt = models.IntegerField(null=True)
    baby_ip_number = models.IntegerField(null=True)
    baby_as = models.IntegerField(null=True)
    baby_outcome = models.CharField(max_length=100, null=True)
    mother_outcome = models.CharField(max_length=100, null=True)
    recording_file = models.CharField(max_length=100, null=True)
    doctor_or_anaesthetic_notes = models.CharField(max_length=100, null=True)
    time_patient_is_received_from_theatre = models.TimeField(null=True)
    cc_matron = models.CharField (max_length=100, null=True)
    cc_theatre = models.CharField(max_length=100, null=True)
    cc_post_surgical_wards = models.CharField(max_length=100, null=True)

class impatient_treatment(models.Model):
    impatient_name = models.CharField(max_length=100, null=True)
    impatient_ip_NO = models.CharField(max_length=100, null=True)
    impatient_sex = models.CharField(max_length=100, null=True)
    impatient_ward = models.CharField(max_length=100, null=True)
    consultant = models.CharField(max_length=100, null=True)
    impatient_date = models.CharField(max_length=100, null=True)
    #prescription
    drug = models.CharField(max_length=100, null=True)
    route = models.CharField(max_length=100, null=True)
    dose = models.CharField(max_length=100, null=True)
    AM_PM = models.TimeField()
    FR_DU = models.CharField(max_length=100, null=True)
    prescription_name = models.CharField(max_length=100, null=True)
    prescription_sign = JSignatureField()

class nursing_care_plan(models.Model):
    nursing_name = models.CharField(max_length=100, null=True)
    nursing_IP_NO = models.IntegerField(null=True)
    nursing_age = models.IntegerField(null=True)
    nursing_DOA = models.IntegerField(null=True)
    nursing_time = models.TimeField()
    nursing_diagnosis = models.TextField(blank=True)
    goal_expected = models.TextField(blank=True)
    nursing_intervention_statement = models.TextField(blank=True)
    evaluation = models.TextField(blank=True)
    nursing_sign = JSignatureField()

class discharge(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    IP_NO = models.IntegerField(null=True)
    DOD = models.IntegerField(null=True)
    DOA = models.IntegerField(null=True)
    #mode of delivery
    SVD = models.IntegerField(null=True)
    EL_C_S = models.IntegerField(null=True)
    EM_C_S = models.IntegerField(null=True)
    mast_insertion_stitch = models.CharField(max_length=100, null=True)
    birth_weight = models.IntegerField(null=True)
    AS = models.IntegerField(null=True)
    #diagnosis on admission
    acitve_labour = models.CharField(max_length=100, null=True)
    latent_labour = models.CharField(max_length=100, null=True)
    complications = models.CharField(max_length=100, null=True)
    infections = models.CharField(max_length=100, null=True)
    pressure_PET_eclampsia = models.CharField(max_length=100, null=True)
    bleeding = models.CharField(max_length=100, null=True)
    #management
    skilled_normal_delivery = models.CharField(max_length=100, null=True)
    cs = models.CharField(max_length=100, null=True)
    others = models.CharField(max_length=100, null=True)
    HPT_management = models.CharField(max_length=100, null=True)
    bleeding_management = models.CharField(max_length=100, null=True)
    outcome_stable = models.CharField(max_length=100, null=True)
    outcome_dead = models.CharField(max_length=100, null=True)
    normal_delivery_post_SUD = models.CharField(max_length=100, null=True)
    surgical_delivery_post_cs = models.CharField(max_length=100, null=True)
    #medical mx pregnacy complication
    discharge_meds = models.CharField(max_length=100, null=True)
    follow_up_date = models.DateField()
    discharge_name = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    discharge_sig  = JSignatureField()

class cardex(models.Model):
    cardex_date = models.DateField()
    cardex_time = models.TimeField()
    nursing_cardex = models.TextField(blank=True)
    cardex_sign = JSignatureField()

class disease_codes(models.Model):
    codes = models.CharField(max_length=200, null=True)

class continuation_sheet(models.Model):
    continuation_date = models.DateField()
    continuation_time = models.TimeField()
    clinical_notes = models.TextField(blank=True)
    continuation_treatment = models.TextField(blank=True)

class charge_sheet(models.Model):
    charge_date = models.DateField()
    service_offered = models.CharField(max_length=200, null=True)
    amount = models.IntegerField(null=True)
    charge_done_by = models.CharField(max_length=200, null=True)

class gate_pass(models.Model):
    NHIF_waived = models.CharField(max_length=100, null=True)
    Receipt_number = models.IntegerField(null=True)
    amount_paid = models.IntegerField(null=True)
    diagnosis_on_admission = models.CharField(max_length=200, null=True)
    diagnosis_on_discharge = models.CharField(max_length=200, null=True)
    discharge_time = models.TimeField()

class payment_particulars(models.Model):
    Cash_NHIF = models.CharField(max_length=100, null=True)
    waiver_number = models.IntegerField(null=True)
    amount = models.IntegerField(null=True)
    admission_diagnosis = models.CharField(max_length=100, null=True)
    discharge_diagnosis = models.CharField(max_length=200, null=True)

class summary_of_labour(models.Model):
    induction_of_labour = models.CharField(max_length=200, null=True)
    hours = models.TimeField()
    number_of_VE = models.IntegerField(null=True)
    length_of_labour = models.IntegerField(null=True)
    mode_of_delivery = models.CharField(max_length=200, null=True)
    mins = models.TimeField()
    uteranoic_drugs = models.CharField(max_length=200, null=True)
    baby_apgar_score = models.CharField(max_length=200, null=True)
    mintues = models.TimeField()
    resuscitation = models.CharField(max_length=200, null=True)
    placenta = models.CharField(max_length=200, null=True)
    membranes = models.CharField(max_length=200, null=True)
    abnormal_placenta_weight = models.IntegerField(null=True)
    blood_loss = models.IntegerField(null=True)
    perineal_repair = models.CharField(max_length=200, null=True)
    baby_length = models.IntegerField(null=True)
    baby_weight = models.IntegerField(null=True)
    HC = models.IntegerField(null=True)
    drugs_given = models.CharField(max_length=100, null=True)
    mother_Bp = models.IntegerField(null=True)
    mother_pulse = models.IntegerField(null=True)
    mother_resp = models.IntegerField(null=True)
    labour_delivery = models.CharField(max_length=200, null=True)
    time_and_of_delivery = models.DateTimeField()

class fetal_heart_rate(models.Model):
    fetal_name = models.CharField(max_length=200, null=True)
    fetal_date_of_admission = models.DateField()
    fetal_para = models.CharField(max_length=200, null=True)
    fetal_gravida = models.CharField(max_length=200, null=True)
    fetal_time_of_admission = models.TimeField()
    fetal_hospital_number = models.IntegerField(null=True)
    fetal_ruptured_membranes = models.CharField(max_length=200, null=True)
    fetal_x_axis = models.FloatField(null=True)
    fetal_y_axis = models.FloatField(null=True)

class dilation(models.Model):
    dilation_name = models.CharField(max_length=200, null=True)
    dilation_date_of_admission = models.DateField()
    dilation_para = models.CharField(max_length=200, null=True)
    dilation_gravida = models.CharField(max_length=200, null=True)
    dilation_time_of_admission = models.TimeField()
    dilation_hospital_number = models.IntegerField(null=True)
    dilation_ruptured_membranes = models.CharField(max_length=200, null=True)
    dilation_x_axis = models.FloatField(null=True)
    dilation_y_axis = models.FloatField(null=True)

class four_hourly_temp(models.Model):
    blood_pressure_x_axis = models.FloatField(null=True)
    temperature_y_axis = models.FloatField(null=True)

class results_of_operation(models.Model):
    operation_x_axis = models.FloatField(null=True)
    operation_y_axis = models.FloatField(null=True)

class pulse_BP(models.Model):
    pulse_BP_name = models.CharField(max_length=200, null=True)
    pulse_BP_date_of_admission = models.DateField()
    pulse_BP_para = models.CharField(max_length=200, null=True)
    pulse_BP_gravida = models.CharField(max_length=200, null=True)
    pulse_BP_time_of_admission = models.TimeField()
    pulse_BP_hospital_number = models.IntegerField(null=True)
    pulse_BP_ruptured_membranes = models.CharField(max_length=200, null=True)
    pulse_BP_x_axis = models.FloatField(null=True)
    pulse_BP_y_axis = models.FloatField(null=True)
    
class contractions(models.Model):
    contractions_name = models.CharField(max_length=200, null=True)
    contractions_date_of_admission = models.DateField()
    contractions_para = models.CharField(max_length=200, null=True)
    contractions_gravida = models.CharField(max_length=200, null=True)
    contractions_time_of_admission = models.TimeField()
    contractions_hospital_number = models.IntegerField(null=True)
    contractions_ruptured_membranes = models.CharField(max_length=200, null=True)
    contractions_x_axis = models.FloatField(null=True)
    contractions_y_axis = models.FloatField(null=True)

class graph(models.Model):
    x_axis_input = models.FloatField(null=True)
    y_axis_input = models.FloatField(null=True)

class Hour(models.Model):
    hour = models.CharField(max_length=10 ,null=True)    


class intake(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hour = models.ForeignKey(Hour, on_delete=models.CASCADE)
    bottle = models.CharField(max_length=100, null=True)
    infused = models.CharField(max_length=100, null=True)
    intravenous_type = models.CharField(max_length=100, null=True)
    amount = models.IntegerField(null=True)
    alimentary_type = models.CharField(max_length=100, null=True)


class output(models.Model):
    vomit = models.CharField(max_length=100, null=True)
    stool = models.CharField(max_length=100, null=True)
    Alimentary_amount = models.CharField(max_length=100, null=True)
    others = models.CharField(max_length=100, null=True)
    urine_specificgraity = models.CharField(max_length=100, null=True)
    N_gast = models.CharField(max_length=100, null=True)
    hour = models.ForeignKey(Hour, on_delete=models.CASCADE )



