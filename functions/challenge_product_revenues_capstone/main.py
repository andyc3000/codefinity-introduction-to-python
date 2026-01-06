# Task 1: Define a function to calculate the revenue for each product
def calculate_revenue(prices, quantities_sold):
    revenue = []
    for i in range(len(prices)):
        revenue.append(prices[i] * quantities_sold[i])
    return revenue

# Task 2: Define a function to format and display the sorted revenues
def formatted_output(revenues):
    for product, rev in sorted(revenues):
        print(f"{product} has total revenue of ${rev}")

# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]
quantities_sold = [150, 200, 100, 50]

# Task 3 & 4: Calculate revenue and pair with product names
revenue = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenue))

# Task 5: Display the sorted revenues
formatted_output(revenue_per_product)

Task
Completed
Follow these step-by-step instructions to complete the task:
Initialize a list named products that contains the product names;
Initialize a list named prices that contains the price per item for each product;
Initialize a list named quantities_sold that contains the number of items sold for each product;
Calculate the revenue for each product by multiplying the price by the quantity sold, and store all results in a new list called revenue;
Use the zip() function to combine the products and revenue lists into a list of tuples named revenue_per_product, where each tuple contains a product name and its corresponding revenue;
Sort the revenue_per_product list alphabetically by product name;
Print each product and its revenue using this format: <product_name> has total revenue of $<revenue>.
You must define the following functions:
calculate_revenue(prices, quantities_sold): This function should multiply each price by its corresponding quantity sold, store the results in a list, and return this list of revenues.
formatted_output(revenues): This function should take a list of (product_name, revenue) tuples, sort them alphabetically by product name, and print each in the specified format.
After defining these functions, use the provided lists to call them and display the results as described above.
