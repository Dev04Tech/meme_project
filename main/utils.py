
'''
userDetails={
'id','name','email','password'
}'''


users=[]

#users.append(usrDetails)
def userExists(userData):
      '''
      @berif:
      '''
      email=userData['email']#collect users email

      #handel first user
      # if len(user)==0:
      #       return False
      for user in users:
            if user['email']==email:
                  #email found
                  return True#{'response':True,'user':user}
      
      #email not found
      return False   #{'response':False,'user':{}}

def loginUser(userData):
      checkUser=userExists(userData)

      if checkUser['response']:
            #user exists amd now check from passsword with the stored password
            if userData['password']==checkUser['user']['password']:
                  #return respose dicts.
                  return {'statuscode':200,'message':'loggedin','total_users':users}
            else:
                  #if passsword not matched
                  return {'statuscode':503,'message':'passworderror','total_users':users}
      else:
            #return responce dicts
            return {'statuscode':503,'message':'alreadyregistered','total_users':users}



def registerUser(userData):
      '''
      @brief:
      @param:
      @return:
      '''
      #check whether email id is register or not !
      checkUser=userExists(userData)
      if(checkUser):
            #user exixts !
            #return response dict.
            return {'statuscode':503,'message':'alreadyregistered','total_users':users}
      else:
            #store the data
            users.append(userData)

            #return response dictionary
            return {'statuscode':200,'message':'registered','total_users':users}


    