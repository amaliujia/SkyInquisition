from django.http import HttpResponse
from django import template

'''
login logic

return login page
'''
def user_login(request):
    with open('templates/user/login.html', 'r') as reader:
        render_engine = template.Template(reader.read())
    context = template.Context()
    return HttpResponse(render_engine.render(context));
