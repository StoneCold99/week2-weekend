# Class Methods
# Your Parking Garage class should implement the following methods:

# - take_ticket:
#   - Decrease the number of available tickets and parking spaces by 1.
 
# - pay_for_parking:
#   - Show an input prompt asking for the payment amount.
#   - If the payment variable is not empty, display a message that the ticket has been paid and they have 15 minutes to leave.
#   - Update the `current_ticket` dictionary, setting the key "paid" to True.
 
# - leave_garage:
#   - If the ticket has been paid, display a "Thank You, have a nice day" message.
#   - If not, prompt for payment.
#   - Once paid, update the parking spaces and tickets lists to increase by 1.

# Attributes
# You will need the following attributes:
# - `tickets` (list)
# - `parking_spaces` (list)
# - `current_ticket` (dictionary)


class ParkingGarage:
    
    def __init__(self, tickets, parking_spaces, current_ticket):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = current_ticket
        
    def takeTicket(self):
        self.tickets = self.tickets - 1
        print(f'There are {self.tickets}/10 tickets available')
        self.parking_spaces = self.parking_spaces - 1
        print(f'There are {self.parking_spaces}/10 parking spaces available')
    
    def payForParking(self):
        pay_ticket = input ("please input payment and enter [purchase] ").lower()
        if pay_ticket == 'purchase':
            self.current_ticket["Paid"] = True
        print(self.current_ticket)
        print('Thank you for your purchase')
    
    def leaveGarage(self):
        if self.current_ticket['Paid'] == False:
          print('Balance is unpaid, redirecting to payment...')
          my_ticket.payForParking()
        elif self.current_ticket['Paid'] == True:
          self.tickets = self.tickets + 1
          self.parking_spaces = self.parking_spaces + 1
          print("Thank You, have a nice day!")
    
    def viewTicket(self):
        print(self.current_ticket)
        
        
def driver():
    while True:
            while True:
             response = input("Pay, Enter, View, or exit? ")
        
             if response.lower() == 'view':
               my_ticket.viewTicket()
             elif response.lower() == 'pay':
               my_ticket.payForParking()
             elif response.lower() == 'enter':
               my_ticket.takeTicket()
             elif response.lower() == 'exit':
               my_ticket.leaveGarage()
            
my_ticket = ParkingGarage(10, 10, {'Paid': False})

driver()

