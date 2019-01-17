from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from django.http import HttpResponse
def test(request, *args, **kwargs):
	return HttpResponse('OK\n')


def post_list_all(request):
  questions = Question.objects.new()
  limit = request.GET.get('limit', 10)
  page = request.GET.get('page', 1)
  paginator = Paginator(questions, limit)
  paginator.baseurl = '/?page='
  page = paginator.page(page)
  return render(request, 'qa/question.html', {
    'questions': page.object_list,
    'paginator': paginator, 'page': page,  
  })
