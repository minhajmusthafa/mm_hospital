import datetime

from django.contrib.auth.hashers import make_password

from django.core.files.storage import FileSystemStorage
from django.db.models import Avg, Max
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from requests import session

from hospital_modules.models import *



# Create your views here.



def login1(request):
    if request.method == "POST":
        u = request.POST['textfield']
        p = request.POST['textfield2']

        res=login.objects.filter(username = u,password = p)

        if res.exists():
            res = res[0]
            if res.user_type=='admin':
                return redirect('/adminnhome')
            elif res.user_type=='doctor':
                request.session['lid']=res.id
                return redirect('/doctorrhome')
            elif res.user_type=='patient':
                request.session['lid']=res.id
                return redirect('/patientthome')

            return HttpResponse('ok')
        else :
            return HttpResponse('<script>alert("user not found");window.location="/"</script>')




    else :
        return render(request,'index.html')

def adminhome(request):



    return render(request,'admin_module/adminindex.html')

def add_doctor(request):

    if request.method == "POST":
        dn =request.POST['textfield']
        a = request.POST['textfield2']
        g = request.POST['gender']
        p = request.POST['textfield3']
        e =request.POST['textfield4']
        q = request.POST.getlist('Qualification')
        print(q)
        qua=','.join(q)
        ph = request.FILES['fileField']
        date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        fs = FileSystemStorage()
        fs.save(r"C:\Users\LENOVO\PycharmProjects\MM_hospital\hospital_modules\static\pic\\"+date+'.jpg',ph)
        path = "/static/pic/" + date + '.jpg'
        res=login.objects.filter(username = e)

        if res.exists():
            return HttpResponse('<script>alert("user already exist");window.location="/addddoctorr"</script>')


        obj2 = login()
        obj2.username = e
        obj2.password = '123'
        obj2.user_type = 'doctor'

        obj2.save()

        obj = doctor()
        obj.d_name = dn
        obj.age = a
        obj.gender = g
        obj.phone = p
        obj.email = e
        obj.qualification = qua
        obj.photo = path
        obj.login_id = obj2
        obj.save()




        return HttpResponse('<script>alert("ok");window.location="/adminnhome"</script>')

    else:
        return render(request,'admin_module/doctor.html')

def deletedoctor(request,id):
    doctor.objects.filter(id=id).delete()
    return HttpResponse('<script>alert("deleted");window.location="/viewwdoctor"</script>')



def updatedoctor(request,id):
    if request.method == "POST":
        try:
            dn = request.POST['textfield']
            a = request.POST['textfield2']
            g = request.POST['gender']
            p = request.POST['textfield3']
            e = request.POST['textfield4']
            q = request.POST.getlist('Qualification')
            qua = ','.join(q)
            ph = request.FILES['fileField']
            date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            fs = FileSystemStorage()
            fs.save(r"C:\Users\LENOVO\PycharmProjects\MM_hospital\hospital_modules\static\pic\\" + date + '.jpg', ph)
            path = "/static/pic/" + date + '.jpg'

            doctor.objects.filter(id=id).update(d_name=dn,age=a,gender=g,phone=p,email=e,qualification=qua,photo=path)
            login.objects.filter(id=request.session['lid']).update(username=e)

            return HttpResponse("ok")
        except Exception as e:
            dn = request.POST['textfield']
            a = request.POST['textfield2']
            g = request.POST['gender']
            p = request.POST['textfield3']
            e = request.POST['textfield4']
            q = request.POST.getlist('Qualification')
            qua = ','.join(q)
            doctor.objects.filter(id=id).update(d_name=dn, age=a, gender=g, phone=p, email=e, qualification=qua)
            login.objects.filter(id=request.session['lid']).update(username=e)
            return HttpResponse('<script>alert("Updated");window.location="/adminnhome"</script>')



    else:
        res = doctor.objects.get(id=id)
        qual=res.qualification.split(',')
        return render(request, 'admin_module/update_doctor.html', {'data': res,'quali':qual})


def add_schedule(request,id):

    if request.method =="POST":
        d = request.POST['textfield']
        st = request.POST['textfield2']
        et = request.POST['textfield3']
        tt = request.POST['textfield4']
        res = schedule.objects.filter(date=d,doctor =id)

        if res.exists():
            return HttpResponse('<script>alert("already have schedule today");window.location="/viewwdoctor"</script>')

        obj = schedule()
        obj.date = d
        obj.starting_time = st
        obj.ending_time = et
        obj.total_token = tt
        obj.doctor_id = id

        obj.save()

        return HttpResponse('<script>alert("Schedule Added");window.location="/adminnhome"</script>')


    else:
        return render(request,'admin_module/Add_schedule.html')

def delete_schedule(request,id):
    schedule.objects.filter(id=id).delete()
    return HttpResponse('<script>alert("deleted");window.location="/viewwschedule"</script>')


def update_schedule1(request,id):

    if request.method =="POST":
        d = request.POST['textfield']
        st = request.POST['textfield2']
        et = request.POST['textfield3']
        tt = request.POST['textfield4']
        schedule.objects.filter(id=id).update(date = d,starting_time = st,ending_time = et,total_token =tt)
        return HttpResponse("ok")


    else:
        res = schedule.objects.get(id=id)
        return render(request,'admin_module/update_schedule.html',{'data': res})


def view_doctor1(request):
    res=doctor.objects.all()
    return render(request,'admin_module/view_doctor.html',{'data':res})

def view_patient1(request):

    res = patient.objects.all()
    return render(request,'admin_module/view_patient.html',{'data':res})
def deletepatient1(request,id):
    patient.objects.filter(id=id).delete()
    return HttpResponse('<script>alert("deleted");window.location="/viewwpatient"</script>')


def view_rating1(request):
    average_ratings = doctor_rating.objects.all().values('doctor_id__d_name').annotate(avg_rating=Avg('rating'))
    print(average_ratings)
    return render(request, 'admin_module/view_rating.html', {'data': average_ratings})

def view_schedule1(request):

    qry = schedule.objects.all()


    return render(request,'admin_module/view_schedule.html',{'data':qry} )

def viewAppointedPatientad(request,id):
    qry = appointment.objects.filter(Schedule=id)
    return render(request, 'admin_module/admin_view_appointed_patient.html', {'data': qry})

def adminPatientDetails(request,id):
    # aid=appointment.objects.get(patient=id)
    qry = patient.objects.get(id=id)
    print(qry)

    return render(request,'admin_module/adminviewpatient_details.html',{'data':qry})



#------------------------------------ Doctor ----------------------------------------------------------------#


def doctorhome(request):

    return render(request,'doctor_module/doctorindex.html')


def updatedoctord(request):
    if request.method == "POST":
        try:
            dn = request.POST['textfield']
            a = request.POST['textfield2']
            g = request.POST['gender']
            p = request.POST['textfield3']
            e = request.POST['textfield4']
            q = request.POST.getlist('Qualification')
            qua = ','.join(q)
            ph = request.FILES['fileField']
            date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            fs = FileSystemStorage()
            fs.save(r"C:\Users\LENOVO\PycharmProjects\MM_hospital\hospital_modules\static\pic\\" + date + '.jpg', ph)
            path = "/static/pic/" + date + '.jpg'

            doctor.objects.filter(login_id=request.session['lid']).update(d_name=dn,age=a,gender=g,phone=p,email=e,qualification=qua,photo=path)
            login.objects.filter(id=request.session['lid']).update(username=e)

            return HttpResponse('<script>alert("updated successfully");window.location="doctorrhome"</script>')
        except Exception as e:
            dn = request.POST['textfield']
            a = request.POST['textfield2']
            g = request.POST['gender']
            p = request.POST['textfield3']
            e = request.POST['textfield4']
            q = request.POST.getlist('Qualification')
            qua = ','.join(q)
            doctor.objects.filter(login_id=request.session['lid']).update(d_name=dn, age=a, gender=g, phone=p, email=e, qualification=qua)
            login.objects.filter(id=request.session['lid']).update(username=e)
            return HttpResponse('<script>alert("updated successfully");window.location="doctorrhome"</script>')



    else:
        res = doctor.objects.get(login_id=request.session['lid'])
        qual=res.qualification.split(',')
        return render(request, 'doctor_module/update_doctor.html', {'data': res,'quali':qual})


def view_scheduledoc(request):
    did=doctor.objects.get(login_id=request.session['lid'])
    qry = schedule.objects.filter(doctor=did)


    return render(request, 'doctor_module/view_scheduledoc.html', {'data': qry})



def view_appointed_patient(request,id):
    qry = appointment.objects.filter(Schedule=id)
    return render(request,'doctor_module/view_appointed_patient.html',{'data': qry})

def add_prescription(request,id):
    return render(request,'doctor_module/add_prescription.html',{'id':id})

def add_prescription_post(request,id):
    if request.method == "POST":
        dn = request.POST['textfield']
        du = request.POST['textfield2']
        do = request.POST['textfield3']
        r = request.POST['textfield4']
        ins = request.POST['textfield5']


        obj = prescription()

        obj.drug_name = dn
        obj.duration = du
        obj.dosage = do
        obj.route = r
        obj.instruction = ins
        obj.appointment_id = id
        obj.save()

        return HttpResponse('<script>alert("added");window.location="/addprescription/'+id+'"</script>')

def view_prescription(request,id):
    qry = prescription.objects.filter(appointment=id)

    return render(request, 'doctor_module/view_prescription.html',{'data':qry})

def deletedrug(request,id):
    prescription.objects.filter(id=id).delete()
    return HttpResponse('<script>alert("deleted");window.location="/viewscedulefrdoc"</script>')

def updatedrug(request,id):
    if request.method == "POST":
        dn = request.POST['textfield']
        du = request.POST['textfield2']
        do = request.POST['textfield3']
        r = request.POST['textfield4']
        ins = request.POST['textfield5']

        prescription.objects.filter(id=id).update(drug_name = dn,duration = du,dosage = do,route = r,instruction = ins)
        return HttpResponse('<script>alert("updated successfully");window.location="/viewscedulefrdoc"</script>')

    else:
        res = prescription.objects.get(id=id)
        return render(request, 'doctor_module/update_prescription.html', {'data': res})

def deletepatientappointment(request,id):
    appointment.objects.filter(id=id).delete()
    return HttpResponse('<script>alert("deleted");window.location="/view_appointed_patientt/"</script>')

def patientDetails(request,id):
    # aid=appointment.objects.get(patient=id)
    qry = patient.objects.get(id=id)
    print(qry)

    return render(request,'doctor_module/patient_details.html',{'data':qry})

def changePass(request):

    if request.method == "POST":
        cp =request.POST['textfield']
        np =request.POST['textfield2']
        rp = request.POST['textfield3']

        res = login.objects.filter(password = cp)

        if res.exists():
            if np == rp:
                login.objects.filter(id=request.session['lid']).update(password=rp)
                return HttpResponse('<script>alert(" password changed");window.location="/doctorrhome"</script>')
            elif np!=rp:
                return HttpResponse('<script>alert(" password mismatch");window.location="/changepassword"</script>')
        else:
            return HttpResponse('<script>alert("incorrect current password");window.location="/changepassword"</script>')
    else:
        return render(request,'doctor_module/change_password.html')

def viewRating(request):
    did = doctor.objects.get(login_id=request.session['lid'])

    res = doctor_rating.objects.filter(doctor_id=did)
    ar_rt = []


    for im in range(0, len(res)):
        print(im)
        val = str(res[im].rating)
        print(val)
        ar_rt.append(val)
    fs = "/static/star/full.jpg"
    hs = "/static/star/half.jpg"
    es = "/static/star/empty.jpg"
    arr = []

    for rt in ar_rt:
        print(rt)
        a = float(rt)

        if a >= 0.0 and a < 0.4:
            print("eeeee")
            ar = [es, es, es, es, es]
            arr.append(ar)

        elif a >= 0.4 and a < 0.8:
            print("heeee")
            ar = [hs, es, es, es, es]
            arr.append(ar)

        elif a >= 0.8 and a < 1.4:
            print("feeee")
            ar = [fs, es, es, es, es]
            arr.append(ar)

        elif a >= 1.4 and a < 1.8:
            print("fheee")
            ar = [fs, hs, es, es, es]
            arr.append(ar)

        elif a >= 1.8 and a < 2.4:
            print("ffeee")
            ar = [fs, fs, es, es, es]
            arr.append(ar)

        elif a >= 2.4 and a < 2.8:
            print("ffhee")
            ar = [fs, fs, hs, es, es]
            arr.append(ar)

        elif a >= 2.8 and a < 3.4:
            print("fffee")
            ar = [fs, fs, fs, es, es]
            arr.append(ar)

        elif a >= 3.4 and a < 3.8:
            print("fffhe")
            ar = [fs, fs, fs, hs, es]
            arr.append(ar)

        elif a >= 3.8 and a < 4.4:
            print("ffffe")
            ar = [fs, fs, fs, fs, es]
            arr.append(ar)

        elif a >= 4.4 and a < 4.8:
            print("ffffh")
            ar = [fs, fs, fs, fs, hs]
            arr.append(ar)

        elif a >= 4.8 and a <= 5.0:
            print("fffff")
            ar = [fs, fs, fs, fs, fs]
            arr.append(ar)
    return render(request,'doctor_module/viewrating.html',{'data':res ,'r1':arr,'ln':len(arr),'d':range(0,len(arr))})
def chatdocget(request,id):
    did = doctor.objects.get(login_id=request.session['lid'])
    qry = chat.objects.filter(sender_id=did.id,receiver_id=id)
    return render(request,'doctor_module/chatdoc.html',{'data':qry,'id':id})

def chatdoc(request,id):
    # if request.method == "POST":
        ct = request.POST['textfield']
        date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        did = doctor.objects.get(login_id=request.session['lid'])
        print(did)

        obj = chat()

        obj.sender_id=did.id
        obj.receiver_id = id
        obj.chat = ct
        obj.date = date
        obj.type = "doctor"
        obj.save()
        return redirect("/chatdocget/"+id)
        # return HttpResponse('<script>alert("updated successfully");window.location="/chatdocget/'+id+'"</script>')
#

#---------------------------  patient ------------------------------------------------------------#

def patientHome(request):

    return render(request,'patient_module/patientindex.html')

def regPatient(request):
    if request.method == "POST":
        n = request.POST['textfield']
        ag = request.POST['textfield2']
        dob = request.POST['dateofbirth']
        s = request.POST['sex']
        ph = request.POST['textfield3']
        pl = request.POST['textfield4']
        po = request.POST['textfield5']
        pin = request.POST['textfield6']
        em = request.POST['textfield7']
        pho = request.FILES['fileField']
        passw = request.POST['textfield8']
        date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        fs = FileSystemStorage()
        fs.save(r"C:\Users\LENOVO\PycharmProjects\MM_hospital\hospital_modules\static\pic\\" + date + '.jpg', pho)
        path = "/static/pic/" + date + '.jpg'
        res = login.objects.filter(username=em)

        if res.exists():
            return HttpResponse('<script>alert("user already exist");window.location="/registerrpatient"</script>')

        obj2 = login()

        obj2.username = em
        obj2.password = passw
        obj2.user_type = 'patient'

        obj2.save()

        obj = patient()

        obj.p_name = n
        obj.age = ag
        obj.dob = dob
        obj.gender = s
        obj.phone = ph
        obj.place = pl
        obj.post = po
        obj.pin = pin
        obj.email = em
        obj.photo = path
        obj.login_id = obj2
        obj.save()

        return HttpResponse('<script>alert("User Registered");window.location="/"</script>')





    else:
        return render(request,'patient_module/register.html')


def viewUpdatePatient(request):
    if request.method == "POST":
        try:
            n = request.POST['textfield']
            ag = request.POST['textfield2']
            dob = request.POST['dateofbirth']
            s = request.POST['sex']
            ph = request.POST['textfield3']
            pl = request.POST['textfield4']
            po = request.POST['textfield5']
            pin = request.POST['textfield6']
            em = request.POST['textfield7']
            pho = request.FILES['fileField']

            date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            fs = FileSystemStorage()
            fs.save(r"C:\Users\LENOVO\PycharmProjects\MM_hospital\hospital_modules\static\pic\\" + date + '.jpg', pho)
            path = "/static/pic/" + date + '.jpg'

            patient.objects.filter(login_id=request.session['lid']).update(p_name = n,age = ag,dob = dob,gender = s,phone = ph,place = pl,post = po,pin = pin,email = em,photo = path)
            login.objects.filter(id=request.session['lid']).update(username = em)
            return HttpResponse("ok")
        except Exception as e:
            n = request.POST['textfield']
            ag = request.POST['textfield2']
            dob = request.POST['dateofbirth']
            s = request.POST['sex']
            ph = request.POST['textfield3']
            pl = request.POST['textfield4']
            po = request.POST['textfield5']
            pin = request.POST['textfield6']
            em = request.POST['textfield7']

            patient.objects.filter(login_id=request.session['lid']).update(p_name=n, age=ag, dob=dob, gender=s,phone=ph, place=pl, post=po, pin=pin, email=em)
            login.objects.filter(id=request.session['lid']).update(username=em)
            return HttpResponse('<script>alert("Updated");window.location="/patientthome"</script>')

    else:
        res = patient.objects.get(login_id=request.session['lid'])
        return render(request, 'patient_module/view_update_profile.html',{'data' : res})


def pViewDoc(request):

    res = doctor.objects.all()
    average_ratings = doctor_rating.objects.all().values('doctor_id__d_name').annotate(avg_rating=Avg('rating'))

    return render(request,'patient_module/View_doctor.html',{'data':res,'rate':average_ratings})
def pViewSchedule(request):
    res = schedule.objects.all()
    return render(request,'patient_module/view_schedule.html',{'data':res})

def bookappointment(request,id):
    p = patient.objects.get(login_id=request.session['lid'])
    d = schedule.objects.get(id=id)
    da = datetime.datetime.now().strftime("%Y-%m-%d")
    res=appointment.objects.filter(Schedule=d)
    res1=appointment.objects.filter(Schedule=id,patient=p)

    if res1.exists():
        return HttpResponse('<script>alert("already taken");window.location="/viewschedulepp"</script>')

    print(p)
    print(res)
    print(res1)

    if res.exists():
        # t=res.count()
        # token = d.total_token
        # print(token)
        # obj = appointment()
        # obj.date = da
        # obj.patient = p
        # obj.Schedule = d
        # obj.token = t+1
        # obj.save()
        t = res.aggregate(Max('token'))
        print(t)
        token = d.total_token
        print(token)
        obj = appointment()
        obj.date = da
        obj.patient = p
        obj.Schedule = d
        obj.token = int(t['id__max']) + 1
        obj.save()
        return HttpResponse('<script>alert("Appointment Taken!");window.location="/viewschedulepp"</script>')
    else:
        obj = appointment()
        obj.date = da
        obj.patient = p
        obj.Schedule = d
        obj.token = 1
        obj.save()
        return HttpResponse('<script>alert("Appointment Taken");window.location="/viewschedulepp"</script>')


def ViewDocProfile(request,id):
    qry = doctor.objects.get(id=id)
    return render(request, 'patient_module/viewDocProfile.html', {'data': qry})

def viewbooked(request):
    pid=patient.objects.get(login_id=request.session['lid'])
    qry = appointment.objects.filter(patient_id=pid)

    return render(request, 'patient_module/view_booking.html', {'data': qry})

def pViewPrescription(request,id):

    qry = prescription.objects.filter(appointment=id)

    return render(request,'patient_module/view_prescriptionPatient.html',{'data':qry})
def rate(request,id):
    if request.method == "POST":
        p = patient.objects.get(login_id=request.session['lid'])
        d = doctor.objects.get(id=id)
        r = request.POST['textfield']
        da = datetime.datetime.now().strftime("%Y-%m-%d")

        res = doctor_rating.objects.filter(patient_id=p,doctor_id=d)
        print(res)
        if res.exists():
            doctor_rating.objects.filter(patient_id=p,doctor_id=id).update(rating=r)
            return HttpResponse('<script>alert("updated");window.location="/viewbooked"</script>')

        else:


            obj = doctor_rating()

            obj.date = da
            obj.rating = r
            obj.patient_id = p
            obj.doctor_id = d
            obj.save()
            print(id)

            return HttpResponse('<script>alert("done");window.location="/viewbooked"</script>')



    else:
        return  render(request,'patient_module/rate.html')

def changePassPatient(request):

    if request.method == "POST":
        cp =request.POST['textfield']
        np =request.POST['textfield2']
        rp = request.POST['textfield3']

        res = login.objects.filter(password = cp)

        if res.exists():
            if np == rp:
                login.objects.filter(id=request.session['lid']).update(password=rp)
                return HttpResponse('<script>alert(" password changed");window.location="/patientthome"</script>')
            elif np!=rp:
                return HttpResponse('<script>alert(" password mismatch");window.location="/chgpasspatient"</script>')
        else:
            return HttpResponse('<script>alert("incorrect current password");window.location="/chgpasspatient"</script>')
    else:
        return render(request,'patient_module/change_passwordpatient.html')

def chatpatget(request, id):
    print(request.session['lid'])
    res= patient.objects.get(login_id=request.session['lid'])
    qry = chat.objects.filter(sender_id=res.id, receiver_id=id)
    return render(request, 'patient_module/chatpatient.html', {'data': qry, 'id': id})

def chatpat(request, id):
        # if request.method == "POST":
    ct = request.POST['textfield']
    date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
    pid = patient.objects.get(login_id=request.session['lid'])
    print(pid)
    obj = chat()

    obj.sender_id = pid.id
    obj.receiver_id = id
    obj.chat = ct
    obj.date = date
    obj.type = "patient"
    obj.save()
    return redirect("/chatpatientget/"+id)
    # return HttpResponse('<script>alert("updated successfully");window.location="/chatdocget/' + id + '"</script>')



#------------------------------------------------- android ---------------------------------------------------------#

def loginnn(request):
    if request.method == "POST":
        u = request.POST['u']
        p = request.POST['p']
        res=login.objects.filter(username = u,password = p)
        # res=res[0]
        if res.exists():
        # if res.user_type == 'patient':
            lid = res[0].id
            logininstance=login.objects.get(id=lid)
            qry = patient.objects.get(login_id=logininstance)

            type=res[0].user_type
            p_name = qry.p_name
            photo=qry.photo

            print(qry)

            return JsonResponse({'status':"ok","lid":lid,"type":type,"p_name":p_name,"photo":photo,"email":u})
        else:
            return JsonResponse({'status':"no"})



def reggandroid(request):
    if request.method == "POST":
        n = request.POST['na']
        ag = request.POST['a']
        dob = request.POST['db']
        s = request.POST['gender']
        ph = request.POST['phon']
        pl = request.POST['pla']
        po = request.POST['pos']
        pin = request.POST['pin']
        em = request.POST['em']
        pho = request.FILES['pic']
        passw = request.POST['p']
        date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        fs = FileSystemStorage()
        fs.save(r"C:\Users\LENOVO\PycharmProjects\MM_hospital\hospital_modules\static\pic\\" + date + '.jpg', pho)
        path = "/static/pic/" + date + '.jpg'
        res = login.objects.filter(username=em)

        if res.exists():
            return JsonResponse({"status": "no"})

        obj2 = login()

        obj2.username = em
        obj2.password = passw
        obj2.user_type = 'patient'

        obj2.save()

        obj = patient()

        obj.p_name = n
        obj.age = ag
        obj.dob = dob
        obj.gender = s
        obj.phone = ph
        obj.place = pl
        obj.post = po
        obj.pin = pin
        obj.email = em
        obj.photo = path
        obj.login_id = obj2
        obj.save()

        return JsonResponse({"status":"ok"})





def updprof(request):

        try:
            n = request.POST['na']
            ag = request.POST['a']
            dob = request.POST['do']
            s = request.POST['gender']
            ph = request.POST['phon']
            pl = request.POST['pla']
            po = request.POST['pos']
            pin = request.POST['pin']
            em = request.POST['em']
            pho = request.FILES['pic']
            id = request.POST['login']
            print(pho)
            import time
            date = time.strftime("%y%m%d_%H%M%S")
            fs = FileSystemStorage()
            print("hello")
            # fs.save(date + '.jpg', pho)
            print("hii")
            fs.save(r"C:\Users\LENOVO\PycharmProjects\MM_hospital\hospital_modules\static\pic\\" + date + '.jpg', pho)
            path = "/static/pic/" + date + '.jpg'
            print("ppppppppppppp",path)

            patient.objects.filter(login_id=id).update(p_name=n, age=ag, dob=dob, gender=s,phone=ph, place=pl, post=po, pin=pin,email=em, photo=str(path))
            login.objects.filter(id=request.session['lid']).update(username=em)
            return JsonResponse({'status':"ok"})
        except Exception as e:
            id = request.POST['login']
            n = request.POST['na']
            ag = request.POST['a']
            dob = request.POST['do']
            s = request.POST['gender']
            ph = request.POST['phon']
            pl = request.POST['pla']
            po = request.POST['pos']
            pin = request.POST['pin']
            em = request.POST['em']

            patient.objects.filter(login_id=id).update(p_name=n, age=ag, dob=dob, gender=s,phone=ph, place=pl, post=po, pin=pin, email=em)
            login.objects.filter(id=id).update(username=em)
            return JsonResponse({'status':"done"})



def viewprof(request):
    id=request.POST['login']

    res=patient.objects.get(login_id=id)
    data={'gender':res.gender,'p_name':res.p_name,'age':res.age,'dob':res.dob,'phone':res.phone,'place':res.place,'post':res.post,'pin':res.pin,'email':res.email,'photo':res.photo}
    return JsonResponse({'status': "ok",'data':data})

def viewscheduleand(request):

    res=schedule.objects.all()

    ar=[]
    for i in res:
        ar.append({
              'id':i.id,
              'date':i.date,
              'd_name':i.doctor.d_name,
              'qualification':i.doctor.qualification,
              'starting_time':i.starting_time,
              'ending_time':i.ending_time,
              'total_token':i.total_token})
        print(ar)

    return JsonResponse({'status': "ok", 'data': ar})




def ratte(request):
    if request.method == "POST":
        id = request.POST['id']
        did= request.POST['did']
        print(did)

        p = patient.objects.get(login_id=id)
        # d = doctor.objects.filter(id=did)

        r = request.POST['rate']
        print(r,"jjjjjjjjjjjjj")
        if float(r) < 1.0:
            return JsonResponse({'status': "null"})
        else:
            da = datetime.datetime.now().strftime("%Y-%m-%d")

            res = doctor_rating.objects.filter(patient_id=p, doctor_id=did)
            print(res)
            if res.exists():
                doctor_rating.objects.filter(patient_id=p,doctor_id=did).update(rating=r)
                return JsonResponse({'status':"update"})

            else:

                obj = doctor_rating()

                obj.date = da
                obj.rating = r
                obj.patient_id = p
                obj.doctor_id = doctor.objects.get(id=did)
                obj.save()
                print(id)


                return JsonResponse({'status': "ok"})


def bookappointmentand(request):
    if request.method == "POST":
        id = request.POST['id']
        sid = request.POST['sid']
        print(id,"iiiiiiiiiii")
        print(sid,"sssssssss")
        p = patient.objects.get(login_id=id)
        d = schedule.objects.get(id=sid)
        da = datetime.datetime.now().strftime("%Y-%m-%d")
        res = appointment.objects.filter(Schedule=d)
        res1 = appointment.objects.filter(Schedule=d, patient=p)

        if res1.exists():
            return JsonResponse({'status': "no"})


        print(res)
        print(res1)

        if res.exists():
            # t=res.count()
            # token = d.total_token
            # print(token)
            # obj = appointment()
            # obj.date = da
            # obj.patient = p
            # obj.Schedule = d
            # obj.token = t+1
            # obj.save()
            t = res.aggregate(Max('token'))
            print(t)
            token = d.total_token
            print(token)
            obj = appointment()
            obj.date = da
            obj.patient = p
            obj.Schedule = d
            obj.token = int(t['token__max']) + 1
            # obj.token=int(token)+1
            obj.save()
            return JsonResponse({'status': "ok"})
        else:
            obj = appointment()
            obj.date = da
            obj.patient = p
            obj.Schedule = d
            obj.token = 1
            obj.save()
            return JsonResponse({'status': "ok"})

def viewbookedand(request):
    id=request.POST['id']
    pid = patient.objects.get(login_id=id)
    qry = appointment.objects.filter(patient_id=pid)

    ar = []
    for i in qry:
        ar.append({
            'id': i.id,
            'token': i.token,
            'd_name': i.Schedule.doctor.d_name,
            'Schedule': i.Schedule.starting_time,
            'doctor':i.Schedule.doctor.id,
            'date':i.date})
        print(i.Schedule.doctor.id)

    return JsonResponse({'status': "ok", 'data': ar})

def viewprescriptionand(request):
    id = request.POST['aid']
    qry = prescription.objects.filter(appointment=id)
    if qry.exists():

        ar = []
        for i in qry:
            ar.append({
                'id': i.id,
                'drug_name': i.drug_name,
                'duration': i.duration,
                'dosage': i.dosage,
                'route': i.route,
                'instruction':i.instruction})

        return JsonResponse({'status': "ok", 'data': ar})
    else:
        return JsonResponse({'status': "no"})


def viewdoctorand(request):
    res = doctor.objects.all()
    average_ratings = doctor_rating.objects.all().values('doctor_id_id','doctor_id__d_name','doctor_id__qualification',).annotate(avg_rating=Avg('rating'))

    ar = []
    for i in res:
        average_ratings = doctor_rating.objects.filter(doctor_id=i.id).values('doctor_id_id', 'doctor_id__d_name',
                                                             'doctor_id__qualification', ).annotate(
            avg_rating=Avg('rating'))
        if average_ratings.exists():
            ar.append({
                        'id':i.id,
                       'd_name':i.d_name,
                       'qualification':i.qualification,
                       'rating':average_ratings[0]['avg_rating'],
                       })

        else:
            # print("kkkkkkkkkkkkkk"+i.d_name)
            ar.append({
                'id': i.id,
                'd_name': i.d_name,
                'qualification': i.qualification,
                'rating': '0',
            })
    return JsonResponse({'status': "ok", 'data': ar})

def viewdocprofand(request):
    id = request.POST['did']
    qry = doctor.objects.get(id=id)
    print(qry,"iddddddd")
    return JsonResponse({'status': "ok", 'd_name': qry.d_name,'age':qry.age,'gender':qry.gender,'qualification':qry.qualification,'phone':qry.phone,'photo':qry.photo})


def changepassand(request):
    if request.method == "POST":
        id=request.POST['id']
        cp = request.POST['cur']
        np = request.POST['new']
        rp = request.POST['rp']

        res = login.objects.filter(password=cp)
        ee =  len(np)
        print(ee,"lenth")

        if res.exists():
            if np == rp:
                if ee == 0:
                    print("helo")
                    return JsonResponse({'status': "em"})
                login.objects.filter(id=id).update(password=rp)
                return JsonResponse({'status': "ok"})
            elif np != rp:
                return JsonResponse({'status': "inc"})

        else:
            return JsonResponse({'status': "no"})

def chatandget(request):
    id = request.POST['id']
    did = request.POST['did']
    res = patient.objects.get(login_id=id)
    qry = chat.objects.filter(sender_id=res.id, receiver_id=did)
    print(res,"senderr")
    print(did,"ddddr")

    ar = []

    for i in qry:
        ar.append({'id':i.id,
                    'sender_id':i.sender_id,
                    'receiver_id':i.receiver_id,
                    'chat':i.chat,
                    'type':i.type
                   })
    print(ar)

    return JsonResponse({'status': "ok",'data':ar})

def chatandpost(request):
    did = request.POST['did']
    ct = request.POST['msg']
    id = request.POST['id']
    date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
    pid = patient.objects.get(login_id=id)
    print(pid)
    chatlen = len(ct)
    if chatlen == 0:
        return JsonResponse({'status:"no"'})
    else:
        obj = chat()

        obj.sender_id = pid.id
        obj.receiver_id = did
        obj.chat = ct
        obj.date = date
        obj.type = "patient"
        obj.save()

        return JsonResponse({'status': "ok"})