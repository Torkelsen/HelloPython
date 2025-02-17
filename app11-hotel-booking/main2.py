import pandas
from abc import ABC, abstractmethod

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    #Class variable (class attribute)
    watermark = "Roger's hotels"

    #Instance method (instance attribute)
    def __init__(self, hotel_id):
        #Instance variable (instance attribute)
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

    #Class method (class attribute)
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    #Override magic method (==)
    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False

#Abstract class
class Ticket(ABC):
    @abstractmethod
    def generate(self):
        pass


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.the_customer_name}
        Hotel name: {self.hotel.name}
        """
        return content

    #Property
    @property
    def the_customer_name(self):
        return self.customer_name.strip().title()

    #Static method ("utility functions", compared to class methods)
    @staticmethod
    def convert(amount):
        return amount * 1.2

class DigitalTicket(Ticket):
    def generate(self):
        print("This is your digital ticket")

    def download(self):
        pass