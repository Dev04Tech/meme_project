from django.shortcuts import render,redirect
from django.http import HttpResponse
from .utils import registerUser,loginUser
from django.contrib.sessions.backends.db import SessionStore #for sessions store

import psycopg2
import requests


# URL :https://api.imgflip.com/get_memes
# use GET requests for this



s=SessionStore()
#connect to database
try:
      connection=psycopg2.connect(
            host="127.0.0.1",
            port="5432",
            database="memestore",
            user="postgres",
            password="Radhika"
            )
      
      print("connected database :")
except Exception as e:
      print("Error :",e)
      print("database connection failed")


 
connection.autocommit=True  #'autocommmit' set to TRUE , so you do not have to commit your queries
cursor=connection.cursor()


# Create your views here.
def home(request):
      return render(request,'home.html')

#middleware
def checkSession():
      try:
            email=s['email']
            return True
      except Exception as e:
            print("ERROR ",e)
            return False


def login(request):
      sessionExist=checkSession()


      if sessionExist==False:
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
                  response=loginUser(userData,cursor)

                  #to debugg this 
                  # print("users :")
                  # print(users)

                  if response['statuscode'] ==200:
                        #session store
                        s['email']=userData['email']
                        s['password']=userData['password']

                        print("session ",s)
                        return redirect('/memes/')
                        # return render(request,'login.html',{'message':'successfully logged in'})
                  elif response['statuscode']==503 and response['message']=='passworderror':
                        return render(request,'login.html',{'message':'password not found'})
                  else:
                        return render(request,'login.html',{'message':'not register'})



            elif request.method=='GET':
                  return render(request,'login.html')
            else:
                  render(request,'login.html')
      else:
            return redirect('/memes/')

            
      # else:
      #       return HttpResponse('ERROR')






def register(request):





      sessionExist=checkSession()
      #we can pass html_string by decleration 
      #i.e. html_string =''' html code'''
      #return Httprespone(html_string)

      if sessionExist==False:
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
                  response=registerUser(userData,cursor)



                  #print user data
                  # print('Users:')
                  # print(response['total_users'])

                  if response['statuscode'] == 200:
                        #sesssion store
                        s['email']=userData['email']
                        s['password']=userData['password']

                        print("session ",s)

                        # return render(request,'register.html',{'message':'successful'})
                        return redirect('/memes/')
                  else:
                        return render(request,'register.html',{'message':'already register'})
                  # return render(request,'register.html',{'message':'succesful'})
            elif request.method=='GET':
                  return render(request,'register.html')
            else:
                  return render(request,'register.html')
            #
            # return HttpResponse("<h1>hello lund  world</h1>")
      else:
            return redirect('/memes/')


def getmemes(request):
      sessionExist=checkSession()
      r=requests.get('https://api.imgflip.com/get_memes')
      meme_data=r.json()
      if sessionExist==False:
            return redirect('/login/')
      else: 
            
            
            context={
                  'meme_metadata':r.json()['data']['memes']
            }

            return render(request,'meme.html',context=context)
      
def editmeme(request):
      sessionStatus=checkSession()
      if sessionStatus:
            #display update page 
            template_id=request.GET['id']
            context={
                  'meme_id':template_id
            }
            return render(request,'editmeme.html',context=context)
      else:
            return redirect('/login/') 

def logout(request):
      try:
            s.clear()
            return redirect('/login/')
      except:
            return redirect('/memes/')
      


def memedetails(request):
      sessionStatus=checkSession()

      if sessionStatus:
            if request.method=='POST':
                  template_id=request.POST['id']
                  text0=request.POST['text1']
                  text1=request.POST['text2']

                  #post request meme api
                  payload={
                        'template_id':template_id,
                        'username':'Ramesh23',
                        'password':'Suraj@2000',
                        'text0':text0,
                        'text1':text1
                  }
                  response=requests.request('POST','https://api.imgflip.com/caption_image',params=payload).json()

                  print("response :",response)

                  html_str=f'''
                              <h1>Response</h1>
                              <img src="{response['data']['url']}">
                              <a href="{response['data']['url']}">view Image</a>'''
                  return HttpResponse(html_str)

      else:
            return redirect('/login/')
