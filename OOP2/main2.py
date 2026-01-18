# class User:
#     def view_hotels(self): 
#         pass

import pandas as pd
from abc import ABC, abstractmethod

df = pd.read_csv('hotels.csv', dtype={'id':str})


class Hotel: 
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id,'name'].squeeze()

    def book(self):
        df.loc[df['id'] == self.hotel_id,'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        availability = df.loc[df['id'] == self.hotel_id,'available'].squeeze()
        if  availability == 'yes':
            return True
        else: 
            return False
    
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

# this class is going to be used as a remidner for other developers that any class that inherits Ticket
# class should have the generate method within, otherwsie the class would have an error
class Ticket(ABC):
    @abstractmethod
    def generate(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self): 
        content = f"""
        Thank you for reservation!
        here is your booking information
        Name :{self.the_customer_name}
        Hotel Name: {self.hotel.name}"""
        return content
    
    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name
    
    @staticmethod
    def convert(amount):
        return amount * 2
    
    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else: 
            return False


hotel1 = Hotel(hotel_id='188')
hotel2 = Hotel(hotel_id='134')

ticket = ReservationTicket(customer_name='john miiiikasa', hotel_object=hotel1)
print(ticket.the_customer_name)


