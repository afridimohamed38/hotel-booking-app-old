import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here is your booking details
        Name:{self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content


class CreditCard:

    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration, "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False


# this below is the programming main loop
print(df)
hotel_ID = input("Enter a hotel id: ")
hotel = Hotel(hotel_ID)
# print(hotel)
if hotel.available():
    # card_number = input("Enter your card number: ")
    # expiration_date = input("Enter expiration date: ")
    # holder_name = input("Enter card holder name: ")
    # cvc_code = input("Enter cvc number: ")

    credit_card = CreditCard(number="123456780123456")
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        name = input("Enter your name: ")
        hotel.book()
        reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
        print(reservation_ticket.generate())
    else:
        print("There is a problem with your payment")
else:
    print("Hotel is not free")
