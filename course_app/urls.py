from django.urls import path, include

from . import views

app_name = 'course_app'

urlpatterns = [
    # Leave as empty string for base url
    path('', views.index, name="index"),
    path('courses/', views.courses, name="courses"),
    path('about/', views.about, name="about"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('category_detail/<int:pk>/', views.category_detail, name="category_detail"),
    path('course_detail/<int:pk>/', views.course_detail, name="course_detail"),
    path('user_course/', views.user_course, name="user_course"),
    path('checkout/<int:pk>/', views.checkout, name="checkout"),
    path('paypal', include('paypal.standard.ipn.urls')),
    path('payment_completed/<int:pk>/', views.payment_completed, name="payment_completed"),
    path('payment_failed/', views.payment_failed, name="payment_failed"),
    path('watch_course/<int:pk>/', views.watch_course, name="watch_course"),
    path('ajax_add_review/<int:pk>/', views.ajax_add_review, name="ajax_add_review"),
    path('get_email/', views.get_email, name="get_email"),
    path('shipping_address/', views.shipping_address, name="shipping_address"),
    path('get_contact/', views.get_contact, name="get_contact"),

]
