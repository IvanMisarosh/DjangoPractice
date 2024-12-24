from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .forms import ReviewForm

# Create your views here.
class ReviewView(View):
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect('/thank_you')
        return render(request, 'reviews/review.html', {
            'form': form
        })

    def get(self, request):
        form = ReviewForm()
        return render(request, 'reviews/review.html', {
            'form': form
        })


def thank_you(request):
    return render(request, 'reviews/thank_you.html')
