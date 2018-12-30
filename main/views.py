from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.shortcuts import render
from django.http import HttpResponse
from main.weather import Weather
from main.forms import TimeForm


obj=Weather()
obj.create_wiew_of_weather()

#def state_(self):
 #   """ Return the text of the state rather than an integer """
  #  return self.STATE[self.state]


def main_view(request):
    # template = Template(
    #     'Hello {{ name }}'
    # )
    # context = Context({
    #     'name': 'Anton'
    # })
    # response_string = template.render(context)

    # template = get_template('main/index.html')

    # context = {
    #     'title': 'This is a main page',
    #     'subtitle': 'First django page',
    #     'username': request.user,
    # }

    # response_string = template.render(context)

    response_string = render_to_string(
        'main/index.html',
        {
            'title': 'This is a main page',
            'subtitle': 'First django page',
            'username': request.user,
            'is_active': True
        }
    )

    # return render(request, 'main/index.html')
    return HttpResponse(response_string)


def contacts_view(request):
    return render(
        request,
        'main/contacts.html',
        {
            'contacts': [
                'Почта : taytds10@gmail.com',

            ]
        }
    )


def about_view(request):
    return render(
        request,
        'main/about.html',
        {
            'text': 'Проектируем...'
        }
    )


def weather_view(request):
    form = TimeForm(request.GET or None)
    if form.is_valid():
        from_= form.cleaned_data['from_']
        to_= form.cleaned_data['to_']
        obj.change_time(from_,to_)
        obj.create_wiew_of_weather()
    if 'refresh' in request.GET:
        obj.refresh_weather()

    else:
        pass

    return render(
        request,
        'main/weather.html',
        {
            'погода': obj.list_of_weathers,

            'form':form,

        },

    )

