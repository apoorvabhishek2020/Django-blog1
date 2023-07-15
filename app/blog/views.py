from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Apoorv",
        "date": date(2023, 7, 15),
        "title": "Mountain Hiking",
        "excerpt": '''
            There's nothing like a mountain hiking.
            It's really awesome and a fun moment for anyone who wants to travel.
            I love travelling to mountains and I do that very often.
            I have visited many and many hill stations.
        ''',
        "content": '''
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia perspiciatis ipsam
            iusto vel aliquam debitis ipsa neque omnis temporibus?
            Deleniti blanditiis impedit quam voluptates sunt aut necessitatibus eos reiciendis non!
        '''
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Apoorv",
        "date": date(2023, 7, 15),
        "title": "Mountain Hiking",
        "excerpt": '''
            There's nothing like a mountain hiking.
            It's really awesome and a fun moment for anyone who wants to travel.
            I love travelling to mountains and I do that very often.
            I have visited many and many hill stations.
        ''',
        "content": '''
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia perspiciatis ipsam
            iusto vel aliquam debitis ipsa neque omnis temporibus?
            Deleniti blanditiis impedit quam voluptates sunt aut necessitatibus eos reiciendis non!
        '''
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Apoorv",
        "date": date(2023, 7, 15),
        "title": "Mountain Hiking",
        "excerpt": '''
            There's nothing like a mountain hiking.
            It's really awesome and a fun moment for anyone who wants to travel.
            I love travelling to mountains and I do that very often.
            I have visited many and many hill stations.
        ''',
        "content": '''
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia perspiciatis ipsam
            iusto vel aliquam debitis ipsa neque omnis temporibus?
            Deleniti blanditiis impedit quam voluptates sunt aut necessitatibus eos reiciendis non!
        '''
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Apoorv",
        "date": date(2023, 7, 15),
        "title": "Mountain Hiking",
        "excerpt": '''
            There's nothing like a mountain hiking.
            It's really awesome and a fun moment for anyone who wants to travel.
            I love travelling to mountains and I do that very often.
            I have visited many and many hill stations.
        ''',
        "content": '''
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia perspiciatis ipsam
            iusto vel aliquam debitis ipsa neque omnis temporibus?
            Deleniti blanditiis impedit quam voluptates sunt aut necessitatibus eos reiciendis non!
        '''
    },
]

def starting_page(request):
    sorted_posts = sorted(all_posts, key=lambda post: post['date'])
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {"posts": latest_posts})

def posts(request):
    return render(request, 'blog/all-posts.html', {"all_posts": all_posts})

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {"post": identified_post})
