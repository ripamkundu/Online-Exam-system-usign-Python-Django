from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Question,Question_s1
end_q_no = 10
def index(request):
    return render(request,"index.html")

    
def login(request):
    return render(request,"login.html")
def startexam(request):
    allquestions = Question.objects.all()[0]
    print(allquestions)
    # total_questions = len(allquestions)
    # actual_ans = []
    # for answer in range(total_questions):
    #     actual_ans.append(allquestions[answer]['ans'])
        #print(allquestions[answer]['ans'])
    #print(actual_ans)
    # qid = []
    # ques = []
    # for i in q:
    #     qid.append(i['q_id'])
    #     ques.append(i['question'])
    para = {'item':allquestions}
    return render(request,"basic.html",para)

# def SaveAns(request):
#     userans = request.POST.get("userans","not found")
#     userans_qno = request.POST.get("qId","not found")
#     print(userans,userans_qno)
#     # saveans.save()
#     return HttpResponseRedirect('/mocktest/login/startexam/')

def endexam(request):
    user_ans = request.POST.get("userans",'Error')
    print(user_ans)
    return render(request,'endpage.html')
def basic(request,q_id):
    question = Question.objects.all()
    item = Question.objects.get(q_id = q_id)
    params = {'questions':question,'item':item,'end_q_no':range(2,end_q_no+1)}       
    return render(request,"basic.html",params)
def saveans(request,q_id):
    user_ans = request.POST.get("userans",'Error')
    try:
        saveans = Question.objects.get(q_id = q_id)
        saveans.user_ans = user_ans
        saveans.save()
        qid = int(q_id)+1
        end_q_id = end_q_no + 1
        if (qid == end_q_id):
            return HttpResponseRedirect('/mocktest/login/startexam/'+str(qid)+'/endpage/')
        return HttpResponseRedirect('/mocktest/login/startexam/'+str(qid)+'/')
    except Question.DoesNotExist:
        return HttpResponseRedirect('/mocktest/login/startexam/1/')

def travelAns(request,q_id):
    try:
        return HttpResponseRedirect('/mocktest/login/startexam/'+str(q_id)+'/')
    except Question.DoesNotExist:
        return HttpResponseRedirect('/mocktest/login/startexam/1/')

def endpage(request,q_id):
    all_questions = Question.objects.all()
    marks = 0
    for question in all_questions:
        if question.ans == question.user_ans:
            marks += 1
    params = {'marks':marks}
    return render(request,"endpage.html",params)


