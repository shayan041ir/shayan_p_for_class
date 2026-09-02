from django.shortcuts import render


def blogs_list(request):

    blog_lists = [
        {
            "id": 1,
            "title": "blog1",
            "content": "this is blog1 content",
        },
        {
            "id": 2,
            "title": "blog2",
            "content": "this is blog2 content",
        },
        {
            "id": 3,
            "title": "blog3",
            "content": "this is blog3 content",
        },
    ]

    return render(request, "blog/blog_list.html", {"blog_lists": blog_lists})


def blog_detail(request, id):

    blog = {
        "id": id,
        "title": f"Blog {id}",
        "content": f"This is the content of blog {id}",
    }

    return render(request, "blog/blog_detail.html", {"blog": blog})
