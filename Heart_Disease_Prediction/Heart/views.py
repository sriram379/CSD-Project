from django.shortcuts import render
import pandas as pd
import pickle


# Create your views here.
def index(request):
    return render(request, 'index.html')

def predict(request):
    if request.method=='POST':
        age=request.POST['age']
        sex=request.POST['sex']
        chest_pain_type=request.POST['cpt']
        blood_pressure=request.POST['bp']
        cholesterol=request.POST['cholesterol']
        fbs_over=request.POST['fbs']
        if int(fbs_over)>=120:
            fbs_over=1
        else:
            fbs_over=0
        ekg_results=request.POST['ekg']
        max_hr=request.POST['max_hr']
        exercise_angina=request.POST['EA']
        st_depression=request.POST['st']
        slope_of_st=request.POST['slopeofst']
        number_of_vessels_fluro=request.POST['nvf']
        thallium=request.POST['thallium']
        data={'Age':age,'Sex':sex,'Chest pain type':chest_pain_type,'BP':blood_pressure,'Cholesterol':cholesterol,'FBS over 120':fbs_over,'EKG results':ekg_results,'Max HR':max_hr,'Exercise angina':exercise_angina,'ST depression':st_depression,'Slope of ST':slope_of_st,'Number of vessels fluro':number_of_vessels_fluro,'Thallium':thallium}
        df=pd.DataFrame(data,index=[0])
        model=pickle.load(open("model.sav","rb"))
        output=model.predict(df)
        if output[0] == 'presence':
            output = 'The patient has heart disease'
        else:
            output = 'The patient doesnt have heart disease'
        return render(request, 'result.html', {'message': output} )