from django.shortcuts import render, get_object_or_404
from .models import Destination, TourPackage, Booking
from django.http import HttpResponse

# View to display a list of destinations
def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'travel/destination_list.html', {'destinations': destinations})

# View to show details of a specific tour package
def tour_package_detail(request, package_id):
    tour_package = get_object_or_404(TourPackage, id=package_id)
    return render(request, 'travel/tour_package_detail.html', {'tour_package': tour_package})

# View to handle bookings
def book_tour(request, package_id):
    tour_package = get_object_or_404(TourPackage, id=package_id)
    
    if request.method == 'POST':
        user_name = request.POST['user_name']
        email = request.POST['email']
        number_of_people = int(request.POST['number_of_people'])
        total_price = tour_package.price * number_of_people
        
        # Save booking to the database
        booking = Booking(user_name=user_name, email=email, tour_package=tour_package, 
                          number_of_people=number_of_people, total_price=total_price)
        booking.save()
        
        return HttpResponse("Booking successful!")
    
    return render(request, 'travel/book_tour.html', {'tour_package': tour_package})
