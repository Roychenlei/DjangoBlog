from django.shortcuts import render,get_object_or_404
from .models  import Post
from django.http import Http404



def index(request):
	latest_list = Post.objects.order_by('updated')[:5]
	context={
	'latest_list': latest_list
	}
	return render(request,'posts/index.html',context)

def detail(request,post_id):
	post = get_object_or_404(Post,pk=post_id)
	return render(request,'posts/detail.html',{'post':post})


def results(request,post_id):
	return HttpResponse("posts %s" % post_id)

def vote(request,post_id):
	return HttpResponse("posts %s" % post_id)


