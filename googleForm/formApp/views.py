from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from models import Questions, Answers, FormHeader, FormList
# Create your views here.
# @login_required(login_url="login/")
# def home(request):
#     return render(request,"home.html")

def login_check(request):
    return render(request, "login.html")

def login_success(request):
     #return render(request, "home.html")

    if request.method == 'POST':
      usname = request.POST['username']
      pwd = request.POST['password']

      user = authenticate(username=usname, password=pwd)

      if user is not None:
          login(request, user)
            #return render(request,"login.html",{'invalid':1})
          return render(request,"home.html", {'user':user})
      else:
          return render(request,"login.html",{'invalid':1,'invalidu':1})


def preview(request):


    #if request.method == 'POST':

    print request.POST.getlist('answersssss')
    formName= FormList()
    formName.save()

    header = FormHeader()
    header.form_title = request.POST['formTitle']
    header.form_description = request.POST['formDescription']
    header.formNo = formName
    header.save()

    fieldTypeVal = request.POST.getlist('fieldTypes')
    QuestionList = request.POST.getlist('questions')
    ac=1
    for i in range(len(QuestionList)):
        quest = Questions()
        quest.ques = QuestionList[i]
        quest.formNo = formName
        quest.save()
        ansName='answers'+str(ac)
        answerList=0
        while True:
            #print i,ac
            answerList = request.POST.getlist(ansName)
            ac+=1
            print ansName,answerList
            if len(answerList)!=0:
                break
            else:
                ansName='answers'+str(ac)
        for j in answerList:
            answ=Answers()
            answ.ans=j
            answ.fieldType=fieldTypeVal[i]
            answ.question = quest
            answ.save()

    #Q=Questions.objects.all()

    formName=formName.id
    formID = FormList.objects.filter(pk=formName)
    H = FormHeader.objects.filter(formNo=formName)
    q = Questions.objects.filter(formNo=formName)
    a = Answers.objects.all()
    f = FormList.objects.filter(pk=formID)
    # print f
    return render(request, "preview.html", {'h': H, 'q': q, 'f': f[0], 'a': a})
    #return render(request,"home.html")


def show(request):
   forms= FormList.objects.all()
   return render(request,"showForms.html",{'formsList':forms})

def viewForm(request):
    #formID=request.POST['formID']
    formID=FormList.objects.filter(pk=21)
    H=FormHeader.objects.filter(formNo=formID)
    q=Questions.objects.filter(formNo=formID)
    a=Answers.objects.all()
    f=FormList.objects.filter(pk=formID)
    #print f
    return render(request,"preview.html",{'h':H,'q':q,'f':f[0],'a':a})