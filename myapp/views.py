from django.shortcuts import render, redirect, get_object_or_404
from .models import Membership, Addbook, sign1, Car
from .forms import MembershipForm, CarForm, AddbookForm, SignupForm
from django.contrib import messages
from django.http import HttpResponseRedirect


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_admin_statistics():
    """Get statistics for admin dashboard"""
    return {
        'total_cars': Car.objects.count(),
        'total_memberships': Membership.objects.count(),
        'total_users': sign1.objects.count(),
    }

def handle_form_submit(request, form_class, success_message, redirect_url, template_name, context=None):
    """Generic form handling helper"""
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, success_message)
            return redirect(redirect_url)
    else:
        form = form_class()
    
    render_context = {'form': form}
    if context:
        render_context.update(context)
    
    return render(request, template_name, render_context)


# ============================================================================
# ADMIN VIEWS
# ============================================================================

def admin_dashboard(request):
    """Admin dashboard with overview statistics"""
    stats = get_admin_statistics()
    return render(request, 'myapp/admin/dashboard.html', {'stats': stats})

def admin_car_manage(request):
    """Manage all cars - CRUD dashboard"""
    cars = Car.objects.all()
    return render(request, 'myapp/admin/car_manage.html', {'cars': cars})

def admin_car_create(request):
    """Create new car"""
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Car added successfully!')
            return redirect('admin_car_manage')
    else:
        form = CarForm()
    return render(request, 'myapp/admin/car_create.html', {'form': form})

def admin_car_update(request, pk):
    """Update existing car"""
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            messages.success(request, 'Car updated successfully!')
            return redirect('admin_car_manage')
    else:
        form = CarForm(instance=car)
    return render(request, 'myapp/admin/car_update.html', {'form': form, 'car': car})

def admin_car_delete(request, pk):
    """Delete car"""
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        car.delete()
        messages.success(request, 'Car deleted successfully!')
        return redirect('admin_car_manage')
    return render(request, 'myapp/admin/car_delete.html', {'car': car})


# ============================================================================
# PUBLIC VIEWS - CAR RELATED
# ============================================================================

def cartest(request):
    """List all cars (Read) - Public view"""
    context = {
       'all_cars': Car.objects.all()
    }
    return render(request, 'cartest.html', context)  

def car_detail(request, pk):
    """View car details - Public view"""
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'car_detail.html', {'car': car})


# ============================================================================
# PUBLIC VIEWS - FORMS
# ============================================================================

def homepage(request):
    """Add book form"""
    return handle_form_submit(
        request, 
        AddbookForm, 
        'Book added successfully!', 
        'm',
        'm.html'
    )

def s(request):
    """Signup form"""
    return handle_form_submit(
        request,
        SignupForm,
        'Account created successfully!',
        'sign',
        'sign.html'
    )

def mem(request):
    """Membership form"""
    return handle_form_submit(
        request,
        MembershipForm,
        'Membership registered successfully!',
        'membership',
        'membership.html'
    )


# ============================================================================
# PUBLIC VIEWS - STATIC PAGES
# ============================================================================

def m(request):
    return render(request, 'm.html')

def about(request):
    return render(request, 'about.html')

def hello(request):
    return render(request, 'hello.html')

def home(request):
    return render(request, 'home.html')

def rentcar(request):
    context = {
       'all_cars': Car.objects.all()
    }
    return render(request, 'rentcar.html', context)

def user_profile(request):
    return render(request, 'user.html')

def news(request):
    return render(request, 'news.html')

def return_instructions(request):
    return render(request, 'return.html')

def blog(request):
    return render(request, 'blog.html')

def customer_support(request):
    return render(request, 'customer.html')

def buycar(request):
    context = {
       'all_cars': Car.objects.all()
    }
    return render(request, 'buycar.html', context)

def delivery(request):
    return render(request, 'delivery.html')

def reviews(request):
    return render(request, 'reviews.html')

def reservation(request):
    return render(request, 'reservation.html')

def terms(request):
    return render(request, 'terms.html')

def membership(request):
    return render(request, 'membership.html')

def car_description(request):
    return render(request, 'car_description.html')

def promotional(request):
    return render(request, 'promotional.html')

def sign(request):
    return render(request, 'sign.html')