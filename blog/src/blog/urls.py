from django.urls import path
from . import views, view_post, view_cbv, view_orm, view_form

urlpatterns = [
    path("blogs/", views.index, name="index"),
    path("blogs/<int:id>/", views.index_id, name="index_id"),
    path("blogs/<str:title>/", views.index_title, name="index_title"),
    
    path("first", views.first, name="first"),
    path("second", views.second, name="second"),
    path("third", views.third, name="third"),
    path("create_data/", view_post.create_data, name="create_data"),
    
    path("get-view/", view_cbv.GetView.as_view(), name="get-view"),
    path("get-async-view/", view_cbv.AsyncView.as_view(), name="get-async-view"),
    path("get-post-view/", view_cbv.GetPostView.as_view(), name="get--post-view"),
    path("index-view/", view_cbv.IndexView.as_view(), name="index-view"),
    
    path("orm-index/", view_orm.index, name="orm-index"),
    path("orm-create-data/", view_orm.create_data, name="orm-create-data"),
    path("orm-update-data/", view_orm.update_data, name="orm-update-data"),
    path("orm-remove-data/", view_orm.remove_data, name="orm-remove-data"),
    
    
    path("form-index/", view_form.index, name="form-index"),
]
