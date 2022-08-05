from django.http import JsonResponse
def roomsPage(request):
    return JsonResponse({'foo':'bar'})
