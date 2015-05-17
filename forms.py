from django.forms import ModelForm
from models import Query
from django.template import Template,Context
from django.core.mail import send_mail

class QueryForm(ModelForm):
	class Meta:
		model = Query
		fields = ['name','email','phone','body','prefered_reply']
		exclude =['created']

	def save(self):
		query = super().save(commit=False)
		body = Template("{{query.name}} {{query.email}} {{query.body}}")
		send_mail("Brainjack query",
			body.render(Context({"query":query})),
			"admin@brainjack.com",
			["chinmaykousik1@gmail.com",],
			fail_silently=False)
		super().save()
