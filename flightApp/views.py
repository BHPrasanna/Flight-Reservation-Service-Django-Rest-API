from django.shortcuts import render
from rest_framework import viewsets
from flightApp.models import Flight, Passenger, Reservation
from flightApp.serializers import FlightSerializer,PassengerSerializer,ReservationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.
@api_view(['POST'])
def findFlights(request):
    departing_city = request.data.get('departingCity')
    arriving_city = request.data.get('arrivingCity')
    date_of_departure = request.data.get('dateOfDeparture')

    flights = Flight.objects.filter(
        departingCity=departing_city,
        arrivingCity=arriving_city,
        dateOfDeparture=date_of_departure
    )

    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def saveReservation(request):
    flight_id = request.data.get('flightId')
    passenger_data = {
        'firstName': request.data.get('firstName'),
        'lastName': request.data.get('lastName'),
        'middleName': request.data.get('middleName'),
        'mobile': request.data.get('mobile'),
        'email': request.data.get('email')
    }

    passenger_serializer = PassengerSerializer(data=passenger_data)
    if passenger_serializer.is_valid():
        passenger = passenger_serializer.save()

        flight = Flight.objects.get(id=flight_id)
        reservation = Reservation(flight=flight, passenger=passenger)
        reservation.save()

        return Response(passenger_serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(passenger_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FlightViewset(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer
    permission_classes=(IsAuthenticated,)
class PassengerViewset(viewsets.ModelViewSet):
    queryset=Passenger.objects.all()
    serializer_class=PassengerSerializer
    permission_classes=(IsAuthenticated,)
class ReservationViewset(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer
    permission_classes=(IsAuthenticated,)
       