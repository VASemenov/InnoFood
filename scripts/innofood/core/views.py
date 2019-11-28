from logging import log

from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from collections import Counter
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from .forms import RegistrationForm, ComplaintForm
from .models import Cafe, Dish, Order, OrderDetail, Complaint
from django.views.generic.list import ListView
from django.contrib.auth import login, logout, authenticate
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings


# === CUSTOMER PART

# VIEWS


# this function is connected to use case  015 Resolve complaint
def deleteOrder(request, id):
    order = Order.objects.get(id=id)
    order.visible = False
    order.save()
    return redirect('customer_orders')


def myOrders(request):
    order_list = Order.objects.filter(visible=True)
    return render(request, 'core/myOrders.html', {'order_list': order_list})


# this function is connected to use case  015 Resolve complaint
def managerComplainsResolve(request, id):
    complain = Complaint.objects.get(id=id)
    complain.complaint_resolved = True
    complain.save()
    return redirect('managerComplains')


# this function is connected to use case  015 Resolve complaint
def managerComplains(request):
    complain_list = Complaint.objects.filter(complaint_resolved=False)
    return render(request, 'core/managerComplain.html', {'complain_list': complain_list})


# this function is connected to use case  014 create complaint
def complaints(request):
    return render(request, 'core/complaints.html', None)


# this function is connected to use case  014 create complaint
def complaintsCreated(request):
    if request.method == "POST":
        subject = request.POST["title_field"]
        description = request.POST["complain_field"]
        orderNumber = request.POST["order_field"]
        contact = request.POST["contact_field"]

        if description == '' or subject == '' or orderNumber == '' or contact == '':
            return HttpResponse('<h1>Do not leave any field empty 😡<h1>')
        complain = Complaint(description=description, complaint_title=subject, complaint_order_number=orderNumber,
                             complaint_contact=contact)
        complain.save()
    return render(request, 'core/complaintsCreated.html', None)


# this function is connected to use case  014 create complaint
def complaintsCompleted(request):
    return redirect('cafes')


class CafeListView(ListView):
    """Displaying list of all cafe accessible for the customer
    """

    model = Cafe
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return redirect('manager_orders')

        return super(CafeListView, self).dispatch(request, *args, **kwargs)


class DishListView(ListView):
    """List all of the available dishes for Customer to order
    """

    model = Dish
    template_name = 'core/dishes.html'

    def get_queryset(self):
        print(self.kwargs)
        context = Dish.objects.filter(cafe=self.kwargs['id'])
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(DishListView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return DishListView.as_view()(request)


class CartListView(ListView):
    """Customer's shopping cart
    """

    model = Dish
    template_name = 'core/cart.html'

    def get_queryset(self):
        print(self.kwargs)
        context = Dish.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        ids = request.POST.getlist('dish_cart')
        print(ids)
        qs = Dish.objects.filter(id__in=ids)
        # print(self.qs, qs)
        # stuff = Dish.filter(id__in=stuff)
        return render(request, self.template_name, {'objects_list': qs})


def user_account_change(request):
    """
    DROPPED FROM MVP
    Customer account manipulation
    """
    return render(request, 'core/user_page.html')


# this function is connected to use case  016 signup
# this function is connected to use case  017 sign in
def registration_view(request):
    """
    Login and registration page
    """

    context = {}
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('name')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, passwors=raw_password)
            login(request, user)

            # if request.user.is_staff:
            #     return redirect('manager_orders')

        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'registration/register.html', context)


# this function is connected to use case  016 Sign up
class SignUp(CreateView):
    form_class = UserCreationForm
    # model = settings.AUTH_USER_MODEL
    success_url = '/cafes/'
    template_name = 'registration/register.html'
    # fields = ['name', 'email', 'password']


# CONTROLLERS


def index(request):
    """
    Handling redirections for logged in users
    """

    if request.user.is_authenticated:

        # Go to main administrator page
        if request.user.is_superuser:
            return redirect('/admin/')

        # Go to main manager page
        if request.user.is_staff:
            return redirect('manager_orders')

        # Go to cafe list for customer to start ordering if user is not manager or admin
        return redirect('cafes')

    # Go here if not authenticated
    return redirect('login')


# ===== MANAGER PART

# VIEWS

# this function is connected to use case  007 Create Order
class ManagerOrders(ListView):
    """
    List of all of the active orders that manager can manipulate
    """

    model = Order
    template_name = 'core/managerActiveOrders.html'

    def get_queryset(self):
        cafe_id = Cafe.objects.get(manager=self.request.user)
        qs = Order.objects.filter(visible=True).filter(confirmed=False).filter(cafe=cafe_id)
        return qs


# this function is connected to use case  009 confirm order
class ManagerOrdersConfirmed(ListView):
    """
    List of all of the confirmed orders
    """

    model = Order
    template_name = 'core/managerConfirmedOrders.html'

    def get_queryset(self):
        cafe_id = Cafe.objects.get(manager=self.request.user)
        qs = Order.objects.filter(confirmed=True).filter(cafe=cafe_id)
        return qs


# this function is connected to use case  010 Decline order
class ManagerOrdersDeclined(ListView):
    model = Order
    template_name = 'core/managerDeclinedOrders.html'

    def get_queryset(self):
        cafe_id = Cafe.objects.get(manager=self.request.user)
        qs = Order.objects.filter(visible=False).filter(cafe=cafe_id)
        return qs


class ManagerCafe(ListView):
    model = Dish
    template_name = 'core/cafeMenuEdit.html'

    def get_queryset(self):
        cafe_id = Cafe.objects.get(manager=self.request.user)
        qs = Dish.objects.filter(visible=True).filter(cafe=cafe_id)
        return qs


# this function is connected to use case  012 Edit dish
class ManagerDish(CreateView):
    model = Dish
    template_name = 'core/dishManager.html'
    fields = ['name', 'price']

    def form_valid(self, form):
        cafe = Cafe.objects.get(manager=self.request.user)
        form.instance.cafe = cafe
        return super(ManagerDish, self).form_valid(form)

    def get_success_url(self):
        return reverse('manager_cafe')


# this function is connected to use case  012 Edit dish
class ManagerDishUpdate(UpdateView):
    model = Dish
    template_name = 'core/dishManagerUpdate.html'
    fields = ['name', 'price', 'in_menu']

    def get_success_url(self):
        return reverse('manager_cafe')


# CONTROLLERS

# this function is connected to use case  007 Create Order
# this function is connected to use case  009 confirm Order
# this function is connected to use case  010 decline Order
def switch_order(request, id, status):
    order = Order.objects.get(id=id)
    if status == 2:
        order.confirmed = True
        order.visible = True
    elif status == 0:
        order.confirmed = False
        order.visible = False
    elif status == 1:
        order.confirmed = False
        order.visible = True

    order.save()
    return redirect('manager_orders')


# this function is connected to use case  007 Create Order
@login_required
def create_order(request, id):
    # dishes = request.POST.getlist('dish_cart')
    dishes = request.POST.getlist('dish_listed')
    address = request.POST.get('destination')
    idCafe = id

    dictOfDishs = Counter()
    for id in dishes:
        dictOfDishs[id] += 1
    dictOfDishs = dict(dictOfDishs)
    print(dictOfDishs)
    # zipbObj = zip(dishesIDs, dishes)
    # dictOfDishs = dict(zipbObj)
    # Dictionary of item purchases

    new_order = Order()
    new_order.destination = address
    new_order.cafe = Cafe.objects.filter(id=idCafe)[0]
    new_order.customer = request.user
    new_order.confirmed = False
    new_order.visible = True
    new_order.save()

    for k in dictOfDishs:
        order_det = OrderDetail()
        order_det.dishes = Dish.objects.filter(id=k)[0]
        order_det.quantity = dictOfDishs[k]
        order_det.order = new_order  # Order.objects.filter(id=1)[0]
        order_det.save()

    return render(request, 'core/order_approved.html')


def showhide_dish(request, id):
    dish = Dish.objects.get(id=id)
    if dish.in_menu:
        dish.in_menu = False
    else:
        dish.in_menu = True

    dish.save()
    return redirect('manager_cafe')


def delete_dish(request, id):
    dish = Dish.objects.get(id=id)
    dish.visible = False
    dish.save()

    return redirect('manager_cafe')
