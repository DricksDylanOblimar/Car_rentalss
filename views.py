# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
# from .models import Car
# from .Forms import CarForm

# class CarListView(ListView):
#     template_name = 'index.html'
#     model = Car
#     context_object_name = 'cars_list'

# class CarRentDetailView(DetailView):
#     template_name = 'car_detail.html'
#     model = Car
#     context_object_name = 'car'

# class CarCreateView(CreateView):
#     template_name = 'car_create.html'
#     form_class = CarForm
#     success_url = reverse_lazy('list-view-car')

# class CarUpdateView(UpdateView):
#     template_name = 'car_update.html'
#     model = Car
#     form_class = CarForm
#     success_url = reverse_lazy('list-view-car')

# class CarDeleteView(DeleteView):
#     template_name = 'car_confirm_delete.html'
#     model = Car
#     success_url = reverse_lazy('list-view-car')



























# # from django.shortcuts import render
# # from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# # from django.urls import reverse_lazy  # Import reverse_lazy for success_url
# # from CarRent.models import Car
# # from CarRent.forms import CarForm

# # class CarListView(ListView):
# #     template_name = 'index.html'
# #     model = Car
# #     context_object_name = 'cars_list'

# # class CarRentDetailView(DetailView):
# #     template_name = 'car_detail.html'
# #     model = Car
# #     context_object_name = 'car'

# # class CarCreateView(CreateView):
# #     template_name = 'car_create.html'
# #     form_class = CarForm
# #     success_url = reverse_lazy('list-view-car')  # Use reverse_lazy to avoid issues with URL resolution

# # class CarUpdateView(UpdateView):
# #     template_name = 'car_update.html'
# #     model = Car
# #     form_class = CarForm
# #     context_object_name = 'car'
# #     success_url = reverse_lazy('list-view-car')  # Use reverse_lazy to avoid issues with URL resolution

# # class CarDeleteView(DeleteView):
# #     template_name = 'car_confirm_delete.html'
# #     model = Car
# #     context_object_name = 'car'
# #     success_url = reverse_lazy('list-view-car')  # Use reverse_lazy to avoid issues with URL resolution




































# # # from django.shortcuts import render
# # # from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# # # from CarRent.models import Car
# # # from CarRent.forms import CarForm


# # # class CarListView(ListView):
# # #     template_name = 'index.html'
# # #     model = Car
# # #     queryset = Car.objects.all()
# # #     context_object_name = 'cars_list'

# # # class CarRentDetailView(DetailView):
# # #     template_name = 'car_detail.html'
# # #     model = Car
# # #     context_object_name = 'car_detail'

# # # class CarCreateView(CreateView):
# # #     form_class = CarForm
# # #     template_name = 'car_create.html'
# # #     success_url = '/CarRent/'

# # # class CarUpdateView(UpdateView):
# # #     model = Car
# # #     form_class = CarForm
# # #     template_name = 'car_update.html'
# # #     context_object_name = 'CarRent'
# # #     success_url = '/CarRent/'

# # # class CarDeleteView(DeleteView):
# # #     template_name = 'car_confirm_delete.html'
# # #     context_object_name = 'CarRent'
# # #     model = Car
# # #     success_url = '/CarRent/'

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Car
from car.Forms import CarForm
from django.shortcuts import render, redirect

class CarListView(ListView):
    template_name = 'index.html'
    model = Car
    context_object_name = 'cars_list'

class CarRentDetailView(DetailView):
    template_name = 'car_detail.html'
    model = Car
    context_object_name = 'car'

class CarCreateView(CreateView):
    template_name = 'car_create.html'
    form_class = CarForm
    success_url = reverse_lazy('list-view-car')

class CarUpdateView(UpdateView):
    template_name = 'car_update.html'
    model = Car
    form_class = CarForm
    success_url = reverse_lazy('list-view-car')

class CarDeleteView(DeleteView):
    template_name = 'car_confirm_delete.html'
    model = Car
    success_url = reverse_lazy('list-view-car')

def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success-url')  # Replace 'success-url' with the URL you want to redirect to after successful form submission
    else:
        form = CarForm()
    return render(request, 'car_create.html', {'form': form})


