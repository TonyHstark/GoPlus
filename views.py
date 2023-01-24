from django.shortcuts import render
from .models import Feedback

def update_feedback(request):
    feedback = Feedback.objects.get(id=1)
    if request.method == 'POST':
        if request.POST.get('like_btn'):
            feedback.like_count += 1
        elif request.POST.get('dislike_btn'):
            feedback.dislike_count += 1
        feedback.save()
    return render(request, "template.html", {'feedback': feedback})
