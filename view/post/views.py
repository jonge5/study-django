import math

from django.db import transaction
from django.db.models import F
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member
from post.models import Post, PostFile


class PostWriteView(View):
    def get(self, request):
        return render(request, 'post/write.html')

    @transaction.atomic
    def post(self, request):
        data = request.POST
        # input 태그 하나 당 파일 1개일 때
        # file = request.FILES

        # input 태그 하나에 여러 파일일 때(multiple), getlist('{input태그 name값}')
        files = request.FILES.getlist('upload-file')

        member = Member(**request.session['member'])

        data = {
            'post_title': data['post-title'],
            'post_content': data['post-content'],
            'member': member
        }
        post = Post.objects.create(**data)

        for file in files:
            PostFile.objects.create(post=post, path=file)

        # for key in file:
        #     PostFile.objects.create(post=post, path=file[key])

        return redirect(post.get_absolute_url())


class PostDetailView(View):
    def get(self, request):
        post = Post.objects.get(id=request.GET['id'])

        post.post_view_count += 1
        post.save(update_fields=['post_view_count'])

        context = {
            'post': post,
            'post_files': list(post.postfile_set.all())
        }
        return render(request, 'post/detail.html', context)


class PostUpdateView(View):
    def get(self, request):
        post = Post.objects.get(id=request.GET['id'])
        return render(request, "post/update.html", {'post': post})

    def post(self, request):
        data = request.POST

        post_id = data['id']
        post = Post.objects.get(id=post_id)

        post.post_title = data['post-title']
        post.post_content = data['post-content']
        post.save(update_fields=['post_title', 'post_content'])

        return redirect(post.get_absolute_url())


class PostDeleteView(View):
    def get(self, request):
        Post.objects.filter(id=request.GET['id']).update(post_status=False)
        # post = Post.objects.get(id=request.GET['id'])
        # post.status = False
        # post.save(update_fields=['status'])
        return redirect('/post/list')


class PostListView(View):
    def get(self, request):
        return render(request, 'post/list.html')


class PostListAPI(APIView):
    def get(self, request, page):
        row_count = 5

        offset = (page - 1) * row_count
        limit = page * row_count
        columns = [
            'id',
            'post_title',
            'post_content',
            'post_view_count',
            'member_name'
        ]
        posts = Post.enabled_objects\
                    .annotate(member_name=F('member__member_name'))\
                    .values(*columns)[offset:limit]

        has_next = Post.enabled_objects.filter()[limit:limit + 1].exists()

        post_info = {
            'posts': posts,
            'hasNext': has_next
        }

        return Response(post_info)



