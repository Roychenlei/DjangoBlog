from django.shortcuts import render,get_object_or_404,redirect
from .models  import Post
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
from .forms import PostForm
from django.contrib import messages


def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		print (form.cleaned_data.get("title"))
		print (form.cleaned_data.get("content"))

		instance.save()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request,"Not successfully created")
	context={
		"form":form,
	}



	return render(request,"post_form.html",context)





def post_detail(request,id=None): #retrieve

	instance = Post.objects.get(id=id)

	context = {
		"title": instance.title,
		"instance":instance,
	}
	return render(request, "post_detail.html", context)



def post_list(request): #list items

	queryset = Post.objects.all()
	
	context={
			"object_list": queryset,
			"title":"List"
	}


	return render(request,"post_list.html",context)

def post_update(request,id=None):

	instance = get_object_or_404(Post,id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())
	context={
		"title":instance.title,
		"instance":instance,
		"form":form,
	}
	return render(request,"post_form.html",context)


def post_delete(request,id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("posts:list")


