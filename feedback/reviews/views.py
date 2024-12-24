from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.http import HttpResponseRedirect

from .forms import ReviewForm
from .models import Review

# Create your views here.
class ReviewView(CreateView):
    template_name = 'reviews/review.html'
    model = Review
    form_class = ReviewForm
    success_url = '/thank_you'


class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'This works!'
        return context
    
class ReviewListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data
    
class ReviewDetailView(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review
    context_object_name = 'review'
  
