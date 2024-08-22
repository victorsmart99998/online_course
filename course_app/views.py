from django.shortcuts import render, redirect
from django.db.models import Count, Avg
from django.urls import reverse
from django.conf import settings
from django.http import JsonResponse
from paypal.standard.forms import PayPalPaymentsForm
from django.contrib import messages
from django.db.models import Sum
from .form import ProductReviewForm
from .models import *


def index(request):
    categorys = Category.objects.all()
    courses = Course.objects.all()
    context = {'courses': courses, 'categorys': categorys}
    return render(request, 'course_app/index.html', context)


def about(request):
    return render(request, 'course_app/about.html')


def contact_us(request):
    return render(request, 'course_app/contact.html')


def courses(request):
    courses = Course.objects.all()
    categorys = Category.objects.all()
    context = {'courses': courses, 'categorys': categorys}
    return render(request, 'course_app/course.html', context)


def category_detail(request, pk):
    category = Category.objects.get(id=pk)
    courses = Course.objects.filter(category=category)
    context = {'courses': courses}
    return render(request, 'course_app/category_detail.html', context)


def course_detail(request, pk):
    course = Course.objects.get(id=pk)
    reviews = ProductReview.objects.filter(course=course).order_by("date_created")
    related_courses = Course.objects.filter(category=course.category).exclude(id=course.id)[:4]
    time_duration = Video.objects.filter(course__id=pk).aggregate(sum=Sum('time_duration'))
    average_rating = ProductReview.objects.filter(course=course).aggregate(rating=Avg('rating'))
    review_form = ProductReviewForm()
    make_review = True

    if request.user.is_authenticated:
        user_review_count = ProductReview.objects.filter(user=request.user, course=course).count()
        user = request.user

        if user_review_count > 0:
            make_review = False
    else:
        user = None

    try:
        check_enroll = User_course.objects.get(user=user, course=course)
    except User_course.DoesNotExist:
        check_enroll = None

    context = {'course': course, 'time_duration': time_duration, 'related_courses': related_courses,
               'check_enroll': check_enroll, 'reviews': reviews,
               'review_form': review_form,
               'make_review': make_review}

    print(user)
    return render(request, 'course_app/course_detail.html', context)


def ajax_add_review(request, pk):
    course = Course.objects.get(id=pk)
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None

    review = ProductReview.objects.create(
        user=user,
        course=course,
        review=request.POST['review'],
        rating=request.POST['rating'],
    )
    context = {
        'user': user.username,
        'review': request.POST['review'],
        'rating': request.POST['rating'],
    }
    return JsonResponse(
        {
            'bool': True,
            'context': context,
        }
    )


def user_course(request):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    courses = User_course.objects.filter(user=user)
    context = {'courses': courses}
    print(courses)
    return render(request, 'course_app/user_course.html', context)


def checkout(request, pk):
    host = request.get_host()
    action = request.GET.get('action')
    course = Course.objects.get(id=pk)
    amount = course.price
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': amount,
        'item_name': 'Order-Item-No-' + str(course.id),
        'invoice': 'INVOICE_NO-' + str(course.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse("course_app:paypal-ipn")),
        'return_url': 'http://{}{}'.format(host, reverse("course_app:payment_completed", args=[pk])),
        'cancel_url': 'http://{}{}'.format(host, reverse("course_app:payment_failed")),
    }
    paypal_payment_button = PayPalPaymentsForm(initial=paypal_dict)

    course = Course.objects.get(id=pk)
    total = (course.price + 10)

    if request.user.is_authenticated:
        user = request.user
    else:
        user = None

    if course.price == 0:
        course = User_course(
            user=user,
            course=course,
        )
        course.save()
        return redirect("course_app:user_course")
    elif action == "create_payment":
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            address = request.POST.get('address')
            country = request.POST.get('country')
            city = request.POST.get('city')
            state = request.POST.get('state')

            payment = Payment(
                user=user,
                course=course,
            )

            payment.save()

    context = {'paypal_payment_button': paypal_payment_button, 'course': course, 'total': total}
    return render(request, 'course_app/checkout.html', context)


def payment_completed(request, pk):
    course = Course.objects.get(id=pk)

    if course:
        course = User_course(
            user=request.user,
            course=course,
        )
        course.save()
    return render(request, 'course_app/payment_completed.html')


def payment_failed(request):
    return render(request, 'course_app/payment_failed.html')


def watch_course(request, pk):
    video_id = request.GET.get('lecture')
    print("id =")
    print(video_id)

    try:
        course = Course.objects.get(id=pk)
    except Course.DoesNotExist:
        course = None


    try:
        video = Video.objects.get(id=video_id)
    except Video.DoesNotExist:
        video = course

    context = {'course': course, 'video': video}
    return render(request, 'course_app/watch_course.html', context)


def get_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        email = NewsletterSubscribers(
            email=email,
        )
        email.save()

    context = {
        'email': request.POST.get('email'),
    }
    return JsonResponse(
        {
            'context': context,
        }
    )


def shipping_address(request):
    if request.method == 'POST':

        shippingaddress = ShippingAddress(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            address=request.POST.get('address'),
            country=request.POST.get('country'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
        )

        shippingaddress.save()

    context = {}
    return JsonResponse(
        {
            'context': context,
        }
    )


def get_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(
            name=request.POST.get('name'),
            subject=request.POST.get('subject'),
            email=request.POST.get('email'),
            message=request.POST.get('message'),
        )

        contact.save()

    context = {
        'name': request.POST.get('name'),
        'subject': request.POST.get('subject'),
        'email': request.POST.get('email'),
        'message': request.POST.get('message'),
    }
    return JsonResponse(
        {
            'context': context,
        }
    )
