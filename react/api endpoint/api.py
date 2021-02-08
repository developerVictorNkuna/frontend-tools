import  requests
from flask import Flask
# from requests.models import Response 
from flask_restful import Resource ,Api



app = Flask(__name__)
api =Api(app) #we are creating a flask instance object and pass that to the API object

class  Hello(Resource):
            #flask class Hello extends the class from Resource
            #restful api modules

    def get(self,name):
        """this a get request method that returns 'Hello name
        This method telss what kind of REST ops to be used by our api  call'"""

        return {"Hello":name}

api.add_resource(Hello,"/hello/")

if __name__ == '__main__':
    app.run(debug=True)




        




# global resp
# try:
#     resp = requests.get("https://jsonplaceholder.typicode.com/todos/1")
#     if resp.status_code == 200:

#         """this means soemthing  went wrong maybe the server couldnt send back a response bodyd"""

# except  requests.ConnectionError as err:

#     print(('The error is:{}'.format({err}),"GET/tasks/ {}".format(resp.status_code)))
# finally:
#     # print(resp.json())

#     for key in resp.:
#         print()
        
    
