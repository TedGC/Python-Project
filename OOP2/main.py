# class User:
#     def view_hotels(self): 
#         pass

import pandas as pd

df = pd.read_csv('hotels.csv', dtype={'id':str})
df_card = pd.read_csv('cards.csv', dtype=str).to_dict(orient="records")
df_password = pd.read_csv('card_security.csv', dtype=str)


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
    


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self): 
        content = f"""
        Thank you for reservation!
        here is your booking information
        Name :{self.customer_name}
        Hotel Name: {self.hotel.name}"""
        return content
    

class CreditCard:
    def __init__(self, number):
        self.number = number
    
    def validate(self, expiration, holder, cvc): 
        card_data = {"number":self.number, "expiration":expiration, 
                     "holder":holder, "cvc":cvc}
        if card_data in df_card:
            return True
        else:
            return f"{card_data} not found. Try differnet cards"
        
        
class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_password.loc[df_password['number'] == self.number, 'password'].squeeze()
        if password == given_password:
            return True
        else:
            return False



print(df)
print(df_card)


hotel_ID = input('enter the id of the hotel: ')
hotel = Hotel(hotel_ID)

if hotel.available():
    credit_card = SecureCreditCard(number='1234')
    if credit_card.validate( holder='JOHN SMITH', expiration='12/26', cvc='123'): 
        given_password = input("Enter your password here: ")
        if credit_card.authenticate(given_password):
            hotel.book()
            name = input('enter your name: ')
            reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            print(reservation_ticket.generate())
        else: 
            print("Wrong password, try a different password")
    else:
        print('there was an issue with your payment')
else: 
    print('hotel is not available at the moment')