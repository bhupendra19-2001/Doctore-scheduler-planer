from django.shortcuts import render
from django.http import JsonResponse 
from myapp.models import Events 

# Create your views here.
def index(request):  
    all_events = Events.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'index.html',context)

# def all_events(request):                                                                                                 
#     all_events = Events.objects.all()                                                                                    
#     out = []                                                                                                             
#     for event in all_events:                                                                                             
#         out.append({                                                                                                     
#             'title': event.name,                                                                                         
#             'id': event.id,                                                                                              
#             'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
#             'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),                                                             
#         })                                                                                                               
                                                                                                                     
#     return JsonResponse(out, safe=False) 

def all_events(request):
    all_events = Events.objects.all()
    out = []
    for event in all_events:
        start_time = event.start.strftime("%m/%d/%Y, %H:%M:%S") if event.start else None
        end_time = event.end.strftime("%m/%d/%Y, %H:%M:%S") if event.end else None
        out.append({
            'title': event.name,
            'id': event.id,
            'start': start_time,
            'end': end_time,
        })

    return JsonResponse(out, safe=False)

def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)

def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)

def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)