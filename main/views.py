from django.shortcuts import render
from django.http import HttpResponse

from .utils import registerUser,loginUser

# Create your views here.
def home(request):
      return HttpResponse('<h1>hello  world</h1>')


def login(request):

      if request.method =='POST':#we are checking the type of request,GET or POST
            email=request.POST['email']
            password=request.POST['password']
            # name=request.POST['name']

            #print
            print('Email :')
            print(email)

            print("password :")
            print(password)

            # print("name :")
            # print(name)
            userData={
                  'email':email,
                  'password':password

            }
            response=loginUser(userData)

            if response['statuscode'] ==200:
                  return render(request,'login.html',{'message':'successfully logged in'})
            elif response['statuscode']==503 and response['message']=='passworderror':
                  return render(request,'login.html',{'message':'password not found'})
            else:
                  return render(request,'login.html',{'message':'not register'})



      elif request.method=='GET':
            return render(request,'login.html')
      else:
            render(request,'login.html')


            
      # else:
      #       return HttpResponse('ERROR')






def register(request):
      #we can pass html_string by decleration 
      #i.e. html_string =''' html code'''
      #return Httprespone(html_string)
      if request.method=='POST':
            #collect data from client
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['password']

            #print data in terminal
            print(f'name:{name}')
            print(f'Email:{email}')
            print(f'password:{password}')

            #create user Dictionary
            userData={
                  'name':name,
                  'email':email,
                  'password':password
            }
            #register User
            response=registerUser(userData)
            #print user data
            print('Users:')
            print(response['total_users'])

            if response['statuscode'] == 200:
                  return render(request,'register.html',{'message':'successful'})
            else:
                  return render(request,'register.html',{'message':'already register'})
            # return render(request,'register.html',{'message':'succesful'})
      elif request.method=='GET':
            return render(request,'register.html')
      else:
            return render(request,'register.html')
      #
      # return HttpResponse("<h1>hello lund  world</h1>")