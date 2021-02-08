import  falcon

class  TestResource(object):
    def on_get(self,req,res):
        """Handles all GET requests."""
        res.status = falcon.HTTP_200 #THis is the default status
        res.body =("This is me ,falcon,serving a resource!")
# Lunch@12:30!

        #CReate the falcon appplication object
app =falcon.API()


#instantiate the TestResource class

test_resource = TestResource()

#add route to the  reosurce
# app.add_route('/test',test_resource)
if __name__ == '__main__':
    app.add_route('/test',test_resource)

