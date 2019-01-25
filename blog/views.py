from django.shortcuts import render

# all supporting views
def post_list(request):
    return render(request, 'blog/post_list.html', {})