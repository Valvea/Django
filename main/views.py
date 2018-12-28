from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.shortcuts import render
from django.http import HttpResponse
from main.weather import Weather
obj=Weather()
obj.get_wiew_of_weather()

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
                '8900007500',
                '8900007501',
                '8900007502',
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

    time_from=request.GET.get('from', None)
    time_to = request.GET.get('to', None)
    if time_to or time_from:
        #temp_str=str.split(temp_str," ")
        obj.change_time(time_from,time_to)
        obj.get_weather()
    else:
        pass
    return render(
        request,
        'main/weather.html',
        {
            'погода': obj.list_of_weathers
        },

    )


