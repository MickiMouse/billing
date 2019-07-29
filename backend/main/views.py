from django.http.response import JsonResponse


def test(request):
    print({'message': 'OK!'})
    if request.method == 'OPTIONS':
        return JsonResponse({'message': 'WORKING!', 'method': 'OPTIONS'})
    return JsonResponse({'message': 'WORKING!'})
