from flask.views import View
from flask.views import MethodView

class get_request(View):

	method = ['GET', 'POST'] 
	def dispatch_request(self):
		return '<h1> class base view </h1>'


class GetPostRequest(MethodView):

	def get(self):
		bar = request.args.get('foo', 'bar')
		return 'A simple Flask request where foo is %s' % bar

	def post(self):
		bar = request.form.get('foo', 'bar')
		return 'A simple Flask request where foo is %s' % bar
