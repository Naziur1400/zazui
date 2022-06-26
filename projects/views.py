from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required,user_passes_test

# from .models import  Project





def projects(request):
    # projects = Project.objects.order_by('-list_date').filter(is_published=True)
    
    # paginator = Paginator(projects, 6)
    # page = request.GET.get('page')
    # paged_listings = paginator.get_page(page)
    # context = {
    #     'projects': paged_listings
    # }
    return render(request, 'listings/projects.html')



def project(request, project_id):
    # project = get_object_or_404(Project, pk=project_id)
    # context = {
    #     'project': project,
    # }

    return render(request, 'project/project.html')



