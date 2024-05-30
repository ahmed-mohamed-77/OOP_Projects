import json

class Guest:
    def __init__(self, lastname: str, firstname: str, age: int, rank_title: str = 'Un-ranked') -> None:
        """
        Initialize a new guest with their last name, first name, rank, and age.

        This ensures rank and age are stored as integers for calculations

        :param lastname: Last name of the guest
        :param firstname: First name of the guest
        :param rank: Rank of the guest, expected to be convertible to an integer
        :param age: Age of the guest, expected to be convertible to an integer
        """
        self.lastname = lastname
        self.firstname = firstname
        self.age = int(age)
        self._rank = rank_title
    
    @property
    def rank(self):
        return self._rank
    
    # setter
    @rank.setter
    def rank(self, rank_title):
        if rank_title not in ['Platinum', 'Gold', 'Silver', 'Bronze', 'Un-ranked']:
            raise ValueError("Invalid Rank")
        self._rank = rank_title
    
    
    def __repr__(self) -> str:
        """Return a string representation of the Guest object"""
        return f"Guest(lastname='{self.lastname}', firstname='{self.firstname}', rank='{self.rank}', age={self.age})"

class GuestManagement:
    def __init__(self) -> None:
        """Initialize the GuestManagement class with an empty list of guests"""
        self.guests = []

    def add_guest(self, lastname, firstname, age, points):
        """Add a guest to the guest list and assign rank based on points"""
        rank_title = self.guest_point(points)  # Determine the rank based on points
        guest = Guest(lastname, firstname, age, rank_title)  # Create a new Guest object
        self.guests.append(guest)  # Add the guest to the guests list

    def guest_point(self, points):
        """Determine the overall rank based on points"""
        if points >= 1000:
            overall_rank = 'Platinum'
        elif points >= 500:
            overall_rank = 'Gold'
        elif points >= 200:
            overall_rank = 'Silver'
        elif points >= 10:
            overall_rank = 'Bronze'
        else:
            overall_rank = 'Un-ranked'
        
        return overall_rank
    
    def calc_cost(self, guest_name: str):
        """
        Calculate the total cost and points for a guest
        :param guest_name: The name of the guest
        """
        total_cost = 0
        total_points = 0
        print(f"Calculate the cost for the guest {guest_name}")
        print("To quit, press Q")

        additional_cost = {}
        
        while True:
            activity = input("Activity: ").strip()  # Get activity from user
            
            if 'q' in activity.lower():  # Exit loop if 'q' is entered
                break
            
            try:
                price = int(input("Price: ").strip())  # Get price for the activity
                points = int(input("Points: ").strip())  # Get points for the activity
            except ValueError:
                print("Invalid input. Please enter numeric values for price and points.")
                continue
            
            additional_cost[activity] = [price, points]  # Store activity details in dictionary
        
        """testing code"""
        print(json.dumps(additional_cost, indent=2))  # Print the activity details in JSON format
        
        for cost, points in additional_cost.values():
            total_cost += cost  # Sum up the total cost
            total_points += points  # Sum up the total points

        return total_cost, total_points  # Return the total cost and points
    
    def calc_points(self, guest_name: str):
        """
        Calculate and return the rank and points for a guest based on their name
        :param guest_name: The name of the guest in "Firstname Lastname" format
        """
        for guest in self.guests:
            if f"{guest.firstname} {guest.lastname}" == guest_name:
                _, points = self.calc_cost(guest_name)  # Calculate cost and points for the guest
                rank_title = self.guest_point(points)  # Determine the rank based on points
                return rank_title, points  # Return the rank and points
        else:
            rank_title = 'Un-ranked'
            return rank_title, print(f"Guest named {guest_name} not found.")
    
    def guest_info(self, rank_title: str):
        """
        Display information for all guests with a specific rank title
        :param rank_title: The rank title to filter guests by
        """
        for guest in self.guests:
            if guest.rank == rank_title:
                print(guest)  # Print guest information if their rank matches the rank_title
    
if __name__ == '__main__':
    user_one = GuestManagement()
    # Example of adding guests without interactive input
    user_one.add_guest("Doe", "John", 30, 600)
    user_one.add_guest("Smith", "Jane", 25, 300)
    
    # Example of calculating points and displaying guest info
    rank, points = user_one.calc_points("John Doe")
    print(f"John Doe: Rank - {rank}, Points - {points}")
    
    user_one.guest_info("Silver")
