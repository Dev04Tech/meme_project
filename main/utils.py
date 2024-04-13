
'''
userDetails={
'id','name','email','password'
}'''


# users=[] in memory storage

#users.append(usrDetails)
def userExists(userData,cursor):
      '''
      @berif:
      '''
      sql_query=f'''
                  select * from users;
                  '''
      try:
            cursor.execute(sql_query)
            users=cursor.fetchall()
      except Exception as e:
            print("Error :",e)

      print("users: ")
      print(users)

      email=userData['email']#collect users email

      # if email in users:
      #       return {'response':True,'user':user}

      #handel first user
      # if len(user)==0:
      #       return False
      for user in users:
            if user[2]==email:
                  #email found
                  return {'response':True,'user':user}
      
      #email not found
      return {'response':False,'user':{}}

def loginUser(userData,cursor):
      checkUser=userExists(userData,cursor)

      if checkUser['response']:
            #user exists amd now check from passsword with the stored password
            if userData['password']==checkUser['user'][3]:
                  #return respose dicts.
                  return {'statuscode':200,'message':'loggedin'}
            else:
                  #if passsword not matched
                  return {'statuscode':503,'message':'passworderror'}
      else:
            #return responce dicts
            return {'statuscode':503,'message':'alreadyregistered'}



def registerUser(userData,cursor):
      '''
      @brief:
      @param:
      @return:
      '''
      #check whether email id is register or not !
      checkUser=userExists(userData,cursor)
      if checkUser['response']:
            #user exixts !
            #return response dict.
            return {'statuscode':503,'message':'alreadyregistered'}
      else:
            #store the data
            # users.append(userData) in memory storage

            sql_query=f'''
                              insert into users(name,email,password) values('{userData['name']}','{userData['email']}','{userData['password']}');
                              '''
            try:
            #execute sql queries
                  cursor.execute(sql_query)
            except Exception as e:
                  print("Error ",e)
            #return response dictionary
            return {'statuscode':200,'message':'registered'}


    