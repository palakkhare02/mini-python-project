#input  from user :
#total persons,total rent ,total food ordered for snacking ,electricity units spend,charge per unit 


## output :total amount according per person that you have to pay

# simple way to solve this problem

Total_persons=int(input("Enter the number of persons living in room/flat:"))
Rent = int(input("Enter your room rent :"))
food=int(input("Enter the amount of food ordered :"))
electricity_spend= int(input("Enter the total of electricity spend units :"))
per_unit_electricity=int(input("Enter the charge per unit of electricity:"))

Total_bill= electricity_spend*per_unit_electricity
output =(food+Rent+Total_bill)//Total_persons

print("Each persons will pay eqaul to",output,"rs")


#  using function
# Function to calculate the bill per person
def calculate_bill_per_person():
    """
    Calculates the total amount each person has to pay based on rent,
    food, and electricity costs.
    """
    try:
        # Taking input from the user
        total_persons = int(input("Enter the total number of persons: "))
        total_rent = int(input("Enter the total rent: "))
        food_cost = int(input("Enter the total food ordered for snacking: "))
        electricity_units_spent = int(input("Enter the total electricity units spent: "))
        charge_per_unit = int(input("Enter the charge per unit of electricity: "))

        # Calculate the total electricity bill
        total_electricity_bill = electricity_units_spent * charge_per_unit

        # Calculate the total expenses
        total_expenses = total_rent + food_cost + total_electricity_bill

        # Calculate the amount each person needs to pay
        amount_per_person = total_expenses // total_persons

        # Print the final output
        print(f"\nEach person will pay an equal amount of {amount_per_person} rs.")

    except ValueError:
        print("\nInvalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("\nError: The number of persons cannot be zero.")

# Call the function to run the program
if __name__ == "__main__":
    calculate_bill_per_person()





