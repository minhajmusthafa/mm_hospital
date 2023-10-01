"""
URL configuration for MM_hospital project.

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
from django.urls import path
from hospital_modules import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.login1),
    path('adminnhome',views.adminhome),
    path('addddoctorr',views.add_doctor),
    path('adddschedule/<id>',views.add_schedule),
    path('updateeschedule/<id>',views.update_schedule1),
    path('viewwdoctor',views.view_doctor1),
    path('viewwpatient',views.view_patient1),
    path('viewwschedule',views.view_schedule1),
    path('viewappointedpatientfradmin/<id>',views.viewAppointedPatientad),
    path('deletepatientad/<id>',views.deletepatient1),
    path('viewwrating',views.view_rating1),
    path('deletedoctorr/<id>',views.deletedoctor),
    path('updatedoctorr/<id>',views.updatedoctor),
    path('deleteschedulee/<id>',views.delete_schedule),
    path('adminnpatientdls/<id>',views.adminPatientDetails),
    #-------------------- doctor --------------------------------------------------------#
    path('doctorrhome',views.doctorhome),
    path('updatefromdoc',views.updatedoctord),
    path('viewscedulefrdoc',views.view_scheduledoc),
    path('view_appointed_patientt/<id>',views.view_appointed_patient),
    path('addprescription/<id>',views.add_prescription),
    path('add_prescription_post/<id>',views.add_prescription_post),
    path('viewprescription/<id>',views.view_prescription),
    path('delete_drug/<id>',views.deletedrug),
    path('update_drug/<id>',views.updatedrug),
    path('delete_patient_appointment/<id>',views.deletepatientappointment),
    path('patientDetails/<id>',views.patientDetails),
    path('changepassword',views.changePass),
    path('docviewrating',views.viewRating),
    path('chatdocget/<id>',views.chatdocget),
    path('chatdocc/<id>',views.chatdoc),
    #--------------------------- patient -------------------------------------------------#
    path('patientthome',views.patientHome),
    path('registerrpatient',views.regPatient),
    path('viewweditprofilee',views.viewUpdatePatient),
    path('pviewDoctor',views.pViewDoc),
    path('viewschedulepp',views.pViewSchedule),
    path('book/<id>',views.bookappointment),
    path('pviewdocprofile/<id>',views.ViewDocProfile),
    path('viewbooked',views.viewbooked),
    path('pViewPrescription/<id>',views.pViewPrescription),
    path('rateedoctor/<id>',views.rate),
    path('chgpasspatient',views.changePassPatient),
    path('chatpatientget/<id>',views.chatpatget),
    path('chatpatientpost/<id>',views.chatpat),


    #--------------------------- android ------------------------------------------------#
    path('loginnn',views.loginnn),
    path('reggandroid',views.reggandroid),
    path('updprof',views.updprof),
    path('viewprof',views.viewprof),
    path('viewscheduleand',views.viewscheduleand),
    path('bookappointmentand',views.bookappointmentand),
    path('viewbookedand',views.viewbookedand),
    path('viewprescriptionand',views.viewprescriptionand),
    path('ratte',views.ratte),
    path('viewdoctorand',views.viewdoctorand),
    path('viewdocprofand',views.viewdocprofand),
    path('changepassand',views.changepassand),
    path('chatandget',views.chatandget),
    path('chatandpost',views.chatandpost),






]
