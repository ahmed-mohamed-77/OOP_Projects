import json

class TravelPlanning:
    def __init__(self, country: str, month: str, trip_type: str) -> None:
        # Initialize the attributes with the provided arguments
        self.country = country
        self.month = month.lower()  # Normalize the month to lowercase for case insensitivity
        self.trip_type = trip_type
        
        # Define the list of months in lowercase
        self.MONTH = [
            "january", "february", "march", "april", "may", 
            "june", "july", "august", "september", "october", 
            "november", "december"
        ]
        
    def trip_info(self):
        # Define the months categorized as winter trips
        WINTER_TRIP = self.MONTH[9:] + self.MONTH[:3]
        # Define the months categorized as summer trips
        SUMMER_TRIP = self.MONTH[3:9]
        
        # Check if the provided month is in the winter trip months
        if self.month in WINTER_TRIP:
            # Print the travel information indicating it's a winter trip
            print(f"The country: {self.country}\nTrip type: {self.trip_type}\nSeason: Winter")
        # Check if the provided month is in the summer trip months
        elif self.month in SUMMER_TRIP:
            # Print the travel information indicating it's a summer trip
            print(f"The country: {self.country}\nTrip type: {self.trip_type}\nSeason: Summer")
        else:
            # Print an error message if the month is not recognized
            print("Please write the correct spelling of the month.")
    
    def calc_cost(self, cost: int):
        """:parm : cost => the flight cost of the trip""" 
        total = 0
        print("Calculate the additional costs for the travel")
        print("to quit additional costs, press Q".upper())
        
        additional_cost= {}
        
        while True:
            activity = input("activity name: ").strip()
            
            if 'q' in activity.lower():
                break
            
            price = int(input("activity price: ").strip())
            additional_cost[activity] = price
        
        print(json.dumps(additional_cost, indent=2))
        
        for price in additional_cost.values():
            total += price
        
        total += cost
        
        if 500 <= total <= 1500:
            print(f"trip cost: {total}\nit's low budget trip")
        elif total > 1500:
            print(f"trip cost: {total}\nit's luxury trip")
            
            

# Main block to test the TravelPlanning class
if __name__ == "__main__":
    # Create an instance of TravelPlanning with given arguments
    travel = TravelPlanning('Egypt', "May", "business")
    # Call the trip_info method to print the travel details
    travel.trip_info()
    travel.calc_cost(350)
