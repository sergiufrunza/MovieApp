from django.urls import path

urlpatterns = [
    path('logout/' ,log_out_user ,name='logout') ,
    path('' ,MainViewHome.as_view() ,name='main_page') ,
    path('movie/<slug:slug_movie>/' ,MovieView.as_view() ,name='movie') ,
    path('genre/<slug:slug_cat>/' ,CategoriesView.as_view() ,name='categories') ,
    path('favorite/<int:pk>/' ,FavoriteView.as_view() ,name='favorite') ,
    path('user/<int:pk>/' ,ProfileUser.as_view() ,name="user_profile") ,
    path('login/' ,LoginUser.as_view() ,name="login") ,
    path('register/' ,RegisterUser.as_view() ,name="registrate"),
    path('editprofile/<int:pk>/', EditUserProfile.as_view(), name="edit_profile")
]
