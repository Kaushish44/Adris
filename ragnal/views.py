from django.shortcuts import render, redirect
from .models import City, Site
from django.http.response import JsonResponse

def Index(request):
    template = 'ragnal/index.html'
    return render(request, template)

def city(request):
    query = request.GET.get('q')
    if query:
        results = City.objects.get(name__iexact=query)
        all_sites = Site.objects.filter(city=results)
        return render(request, 'ragnal/city.html', {'results': results, 'all_sites': all_sites})
    return redirect('ragnal:index')

def autocomplete(request):
    if request.is_ajax():
        search_qs = City.objects.filter(name__startswith=request.GET.get('q',None))
        results = []
        for r in search_qs:
            results.append(r.name)
        data = {'results':results }
        return JsonResponse(data)

# class IndexView(generic.ListView):
#     template_name = 'ragnal/index.html'
#     context_object_name = 'all_sites'
#     def get_queryset(self):
#         return City.objects.all()