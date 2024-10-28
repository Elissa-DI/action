from django.views import View
from django.http import HttpResponse
import asyncio
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt 
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class GetView(View):
    message = "Hello Elissa from CBV"
    def get(self, request):
        # return HttpResponse("Hello Elissa 1")
        return HttpResponse(self.message) 
    
    
class AsyncView(View):
    message = "Hello Elissa from CBV"
    async def get(self, request):
        # return HttpResponse("Hello Elissa 1")
        await asyncio.sleep(1)
        return HttpResponse(self.message)  
    

@method_decorator(csrf_exempt, name="dispatch")    
class GetPostView(View):
    message = "Hello Elissa getpostview"
    template = "index.html"
    name = "Elissa DUSABE"
        
    def get(self, request):
        # return HttpResponse(self.message)
        data = {
            "name": self.name
        }
        return render(request, self.template, data)
        
    
    def post(self, request, *args, **kwargs):
        # print(request.data.dict())
        return HttpResponse("Hello Elissa POST")

      
      
class IndexView(TemplateView, LoginRequiredMixin):
    template_name = "index.html"