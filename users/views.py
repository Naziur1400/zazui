from django.shortcuts import render

# Create your views here.


def home_view(request):
    # category = Category.objects.all()[:6].annotate(lists_count=Count('project'))
    # projects = Project.objects.order_by('-list_date').filter(is_published=True)[:3]
    # carousel = Carousel.objects.all()

    # context = {
    #     'category': category,
    #     'projects': projects,
    #     'carousel' : carousel,
    # }

    # if request.user.is_authenticated:
    #     return HttpResponseRedirect('afterlogin')
    return render(request,'pages/index.html')
