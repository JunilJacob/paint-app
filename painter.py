import webapp2
from google.appengine.ext import db
from google.appengine.ext.webapp import template

class Image(db.Model):
	data = db.TextProperty()
class MainPage(webapp2.RequestHandler):
	def post(self):
		imgname=self.request.get('pname')
		imgdata=self.request.get('pdata')
		image=Image(key_name=imgname,data=imgdata)
		image.put();
		
        def get(self):
                imgname=self.request.get('imagename')
                self.response.headers['content-Type'] = 'html'
                
                if imgname:
                	key=db.Key.from_path('Image',imgname)
                	obj=db.get(key)
               		if obj:
                		json=obj.data
                		self.response.out.write("<script>var data=JSON.parse('"+json+"'); </script>")
	                	self.response.out.write(template.render("painter.html",{}));

	                else:	
	                	self.response.out.write("""<script> alert("Image not found");	document.location.href="/" </script>""")
	        else:
			self.response.out.write("""<script>var data=[]; </script>""")
			self.response.out.write(template.render("painter.html",{}));

app = webapp2.WSGIApplication([('/.*',MainPage)], debug=True)





