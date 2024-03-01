"""
    Program Purpose: create a versatile reservation system for ABC Hotel, facilitating users to make room reservations
    with customizable options. It first defines room types and their respective nightly rates, then prompts users to
    input check-in and check-out dates. Upon selection of room type, number of rooms, and duration of stay, the program
    calculates the total cost of the reservation, considering additional services like breakfast, WiFi, or parking if
    opted for. It displays a confirmation message with detailed reservation information, enabling users to view and
    confirm their reservation before finalizing it
    Programmer: Muhammad Muqry Bin Razaly
    Date 1 March 2024

"""

# Define room types and their nightly rates using lists
room_types = ["Single Room", "Double Room", "Suite"]
nightly_rates = [100, 150, 250]

# Define additional services and their costs
additional_services = {
    "Breakfast": 20,
    "Wifi": 10,
    "Parking": 15
}


# Function to display available room types and their rates
def display_room_types():
    print("\nAvailable Room Types:")
    for i, room_type in enumerate(room_types, start=1):
        print(f"{i}. {room_type} - RM{nightly_rates[i - 1]} per night")


# Function to calculate the total cost of reservation
def calculate_total_cost(room_type_index, num_rooms, check_in, check_out, services):
    nightly_rate = nightly_rates[room_type_index]
    total_nights = (check_out - check_in).days
    subtotal = nightly_rate * total_nights * num_rooms

    additional_costs = sum(services.values()) * num_rooms
    total_cost = subtotal + additional_costs
    return total_cost


# Main function to run the hotel reservation system
def main():
    print("Welcome to Muqry's Hotel Reservation System")

    # Display available room types
    display_room_types()

    # Select room type
    room_type_index = int(input("\nPlease select a room type (1/2/3): ")) - 1
    if room_type_index < 0 or room_type_index >= len(room_types):
        print("Error: Invalid room type selection.")
        return

    # Input number of rooms
    num_rooms = int(input("\nEnter the number of rooms: "))
    if num_rooms <= 0:
        print("Error: Number of rooms must be greater than zero.")
        return

    # Input check-in and check-out dates
    check_in_str = input("\nEnter your check-in date (DD-MM-YYYY): ")
    check_out_str = input("Enter your check-out date (DD-MM-YYYY): ")
    try:
        from datetime import datetime
        check_in = datetime.strptime(check_in_str, "%d-%m-%Y")
        check_out = datetime.strptime(check_out_str, "%d-%m-%Y")
        if check_out <= check_in:
            print("Error: Check-out date must be after check-in date.")
            return
    except ValueError:
        print("Error: Invalid date format.")
        return

    # Additional services
    add_services = input("\nWould you like to add any additional services? (Yes/No): ").lower()
    selected_services = {}
    if add_services == 'yes':
        print("\nAdditional Services:")
        for i, (service, cost) in enumerate(additional_services.items(), start=1):
            print(f"{i}. {service} - RM{cost} per {service.lower()}")
        services_choice = input("Please select additional services (separated by commas, e.g., 1,2): ")
        for choice in services_choice.split(','):
            try:
                index = int(choice.strip()) - 1
                if 0 <= index < len(additional_services):
                    service, cost = list(additional_services.items())[index]
                    selected_services[service] = cost
                else:
                    print("Error: Invalid additional service selection.")
                    return
            except ValueError:
                print("Error: Invalid additional service selection.")
                return

    # Calculate total cost
    total_cost = calculate_total_cost(room_type_index, num_rooms, check_in, check_out, selected_services)

    # Display reservation details
    print("\nThank you for your reservation.\n")
    print("Reservation details:")
    print(f"Room Type: {room_types[room_type_index]}")
    print(f"Number of Rooms: {num_rooms}")
    print(f"Check-in Date: {check_in.strftime('%d-%m-%Y')}")
    print(f"Check-out Date: {check_out.strftime('%d-%m-%Y')}")
    print("\nAdditional Services:")
    for service, cost in selected_services.items():
        print(f"- {service} ({num_rooms} {service.lower()}): RM{cost * num_rooms}")
    print(f"\nTotal cost: RM{total_cost}")

    # Confirm reservation
    confirm = input("\nWould you like to confirm your reservation? (Yes/No): ").lower()
    if confirm == 'yes':
        print("Reservation confirmed. Thank you for choosing Muqry's Hotel. Enjoy your stay with Style.")
    else:
        print("Reservation canceled.")


if __name__ == "__main__":
    main()
