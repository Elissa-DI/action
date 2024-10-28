from .models import Post
from django.http import JsonResponse


# Read data operation
def index(request):
    queryset = Post.objects.all()
    # queryset = Post.objects.filter(id=2)
    extra_processing = list(queryset.values())

    # obj = Post.objects.values().get(id=1)

    # return JsonResponse(obj, safe=False)
    return JsonResponse(extra_processing, safe=False)


#Create data operation
def create_data(request):
    Post.objects.create(
        title="New blog",
        slug="new-blog",
        content=(
            "This blog is about machine learning. It will cover some basic concepts in machine learning like supervised and unsupervised learning, regression, classification, clustering, etc. It will also cover some advanced concepts like neural networks, deep learning, transfer learning, etc."
        ),
        owner_id=1,
    )

    return JsonResponse({"message": "Successfully submitted the data."})


# Update data operation
def update_data(request):
    id = 1
    # obj = Post.objects.filter(id=id).update(title="Update title")
    obj = Post.objects.filter(id=id).first()
    obj.title = "Update title"
    obj.save()
    
    return JsonResponse({
        "message": "Data updated successfully!"
    })
    
def remove_data(request):
    id = 2
    Post.objects.filter(id=id).delete()
    
    return JsonResponse({
        "message": "Data removed successfully!"
    })