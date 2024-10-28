from django.http import JsonResponse

def create_data(request):
    # print(request.POST.dict())
    # return JsonResponse({ "message": "Successfully submitted the data." })
    
    if request.method == "POST":
        print(request.POST.dict())
        name = request.POST.dict()["name"]
        return JsonResponse({ "message": f"Successfully submitted the data, {name}" })
    return JsonResponse({ "message": "Please submit the data." })