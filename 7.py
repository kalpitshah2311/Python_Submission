from forms import WorkForm
from django.core.mail import send_mail, EmailMessage
def work(request): 
template = 'other/work.html'
if request.method == 'POST':
form = WorkForm(request.POST, request.FILES)
if form.is_valid():
name = form.cleaned_data['name'] 
nick = form.cleaned_data['nick'] 
email = form.cleaned_data['email'] 
subject = 'Work' text = form.cleaned_data['text'] 
image1 = request.FILES['image1'] 
image2 = request.FILES['image2'] 
image3 = request.FILES['image3'] 

try:
mail = EmailMessage(subject, text, ['EMAIL_ADDRESS'], [email])
mail.attach(image1.name, attach.read(), attach.content_type) 
mail.attach(image2.name, attach.read(), attach.content_type)
mail.attach(image3.name, attach.read(), attach.content_type)
mail.send()
template = 'other/mail_sent.html' 
except:
return "Attachment error"
return render_to_response(template, {'form':form},
context_instance=RequestContext(request))
else: 
form = WorkForm()
return render_to_response(template, {'form':form},
context_instance=RequestContext(request))
