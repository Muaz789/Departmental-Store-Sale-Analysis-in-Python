import csv
import matplotlib.pyplot as plt

# Load the CSV file


def load_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

# Save filtered data to a new CSV file


def save_filtered_data(data, output_file, filter_function):
    with open(output_file, 'w', newline='') as file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            if filter_function(row):
                writer.writerow(row)

# Write a summary to a text file


def write_summary(output_file, summary_data):
    with open(output_file, 'w') as file:
        file.write("Analysis Summary\n")
        file.write("================\n")
        for key, value in summary_data.items():
            file.write(f"{key}: {value}\n")

# Question 1: Total Sales


def total_sales(data):
    return sum(float(row['Total sale']) for row in data)

# Question 2: Average Sales


def average_sales(data):
    return total_sales(data) / len(data)

# Question 3: Branch with Highest Sales


def highest_sales_branch(data):
    branch_sales = {}
    for row in data:
        branch_sales[row['Branch']] = branch_sales.get(row['Branch'], 0) + float(row['Total sale'])
    return max(branch_sales, key=branch_sales.get)

# Question 4: Top Product Line by Revenue


def top_product_line(data):
    product_sales = {}
    for row in data:
        product_sales[row['Product line']] = product_sales.get(row['Product line'], 0) + float(row['Total sale'])
    return max(product_sales, key=product_sales.get)

# Question 5: Proportion of Member vs. Normal Customers


def customer_type_proportion(data):
    types = {'Member': 0, 'Normal': 0}
    for row in data:
        types[row['Customer type']] += 1
    total = sum(types.values())
    return {key: value / total * 100 for key, value in types.items()}

# Question 6: Total Revenue by Gender


def revenue_by_gender(data):
    gender_revenue = {'Male': 0, 'Female': 0}
    for row in data:
        gender_revenue[row['Gender']] += float(row['Total sale'])
    return gender_revenue

# Question 7: Most Frequently Used Payment Method


def most_used_payment_method(data):
    payment_methods = {}
    for row in data:
        payment_methods[row['Payment']] = payment_methods.get(row['Payment'], 0) + 1
    return max(payment_methods, key=payment_methods.get)

# Question 8: Average Gross Margin Percentage


def average_gross_margin(data):
    return sum(float(row['gross margin percentage']) for row in data) / len(data)

# Question 9: City with Highest Sales


def city_with_highest_sales(data):
    city_sales = {}
    for row in data:
        city_sales[row['City']] = city_sales.get(row['City'], 0) + float(row['Total sale'])
    return max(city_sales, key=city_sales.get)


# Question 10: Average Quantity Sold per Product Line
def avg_quantity_by_product_line(data):
    product_quantities = {}
    product_counts = {}
    for row in data:
        line = row['Product line']
        product_quantities[line] = product_quantities.get(line, 0) + int(row['Quantity'])
        product_counts[line] = product_counts.get(line, 0) + 1
    return {line: product_quantities[line] / product_counts[line] for line in product_quantities}

# Question 11: Average Sales Value of High-Rating Transactions


def avg_high_rating_sales(data, rating_threshold=8.0):
    high_rating_sales = [float(row['Total sale']) for row in data if float(row['Rating']) > rating_threshold]
    return sum(high_rating_sales) / len(high_rating_sales) if high_rating_sales else 0

# Question 12: Sales by Branch


def sales_by_branch(data):
    branch_sales = {}
    for row in data:
        branch_sales[row['Branch']] = branch_sales.get(row['Branch'], 0) + float(row['Total sale'])
    return branch_sales

# Question 13: Peak Transaction Hours


def peak_transaction_hours(data):
    hours = {}
    for row in data:
        hour = int(row['Time'].split(':')[0])
        hours[hour] = hours.get(hour, 0) + 1
    return max(hours, key=hours.get)

# Question 14: Tax-to-Sales Ratio


def tax_to_sales_ratio(data):
    return sum(float(row['Tax 5%']) for row in data) / total_sales(data)

# Question 15: Revenue Above Unit Price Threshold


def revenue_above_threshold(data, threshold):
    return sum(float(row['Total sale']) for row in data if float(row['Unit price']) > threshold)


# Data Visualization: Line Graph for Branch Sales


def plot_branch_sales(branch_sales):
    branches = list(branch_sales.keys())
    sales = list(branch_sales.values())
    plt.figure(figsize=(8, 5))
    plt.plot(branches, sales, marker='o', color='blue', label='Branch Sales')
    plt.title('Total Sales by Branch')
    plt.xlabel('Branch')
    plt.ylabel('Total Sales')
    plt.grid()
    plt.legend()
    plt.show()

    # Data Visualization: Line Graph for Gender Revenue


def plot_gender_revenue(gender_revenue):
    genders = list(gender_revenue.keys())
    revenue = list(gender_revenue.values())
    plt.figure(figsize=(8, 5))
    plt.plot(genders, revenue, marker='o', color='green', label='Revenue by Gender')
    plt.title('Revenue by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Revenue')
    plt.grid()
    plt.legend()
    plt.show()

# Data Visualization: Bar Graph for Product Line Quantities


def plot_product_line_quantities(product_quantities):
    lines = list(product_quantities.keys())
    quantities = list(product_quantities.values())
    plt.bar(lines, quantities, color='orange')
    plt.title('Average Quantity Sold by Product Line')
    plt.xlabel('Product Line')
    plt.ylabel('Average Quantity')
    plt.show()

# Data Visualization: Bar Graph for Payment Methods


def plot_payment_methods(data):
    payment_counts = {}
    for row in data:
        payment_counts[row['Payment']] = payment_counts.get(row['Payment'], 0) + 1
    methods = list(payment_counts.keys())
    counts = list(payment_counts.values())
    plt.figure(figsize=(8, 5))
    plt.bar(methods, counts, color='purple')
    plt.title('Payment Method Frequency')
    plt.xlabel('Payment Method')
    plt.ylabel('Frequency')
    plt.show()
# Main Execution


data = load_csv('data.csv')

# User Input for Filtered Data
print("Select a filter for saving data:")
print("1. Total Sale above a threshold")
print("2. Sales Rating above a threshold")
filter_choice = input("Enter your choice (1 or 2): ")

if filter_choice == "1":
    threshold = float(input("Enter the Total Sale threshold: "))
    save_filtered_data(data, 'filtered_data.csv', lambda row: float(row['Total sale']) > threshold)
    print(f"Filtered data saved to 'filtered_data.csv' for Total Sale > {threshold}.")
elif filter_choice == "2":
    threshold = float(input("Enter the Sales Rating threshold: "))
    save_filtered_data(data, 'filtered_data.csv', lambda row: float(row['Rating']) > threshold)
    print(f"Filtered data saved to 'filtered_data.csv' for Rating > {threshold}.")
else:
    print("Invalid choice. No data saved.")

print("Total Sales:", total_sales(data))
print("Average Sales:", average_sales(data))
print("Highest Sales Branch:", highest_sales_branch(data))
print("Top Product Line:", top_product_line(data))
print("Customer Type Proportion:", customer_type_proportion(data))
print("Revenue by Gender:", revenue_by_gender(data))
print("Most Used Payment Method:", most_used_payment_method(data))
print("Average Gross Margin:", average_gross_margin(data))
print("City with Highest Sales:", city_with_highest_sales(data))
print("Average Quantity by Product Line:", avg_quantity_by_product_line(data))
print("Average High Rating Sales:", avg_high_rating_sales(data))

branch_sales = sales_by_branch(data)
# Generate Summary
summary = {
    "Total Sales": total_sales(data),
    "Average Sales": average_sales(data),
    "Highest Sales Branch": highest_sales_branch(data),
    "Top Product Line": top_product_line(data),
    "Customer Type Proportion": customer_type_proportion(data),
    "Revenue by Gender": revenue_by_gender(data),
    "Most Used Payment Method": most_used_payment_method(data),
    "Average Gross Margin": average_gross_margin(data),
    "City with Highest Sales": city_with_highest_sales(data),
    "Average Quantity by Product Line": avg_quantity_by_product_line(data),
    "Average High Rating Sales": avg_high_rating_sales(data),
    "Branch Sale:": branch_sales,
    "Peak Transaction Hour": peak_transaction_hours(data),
    "Tax-to-Sales Ratio": tax_to_sales_ratio(data),
    "Revenue Above Threshold": revenue_above_threshold(data, threshold=50)
}

# Write summary to a file
write_summary('summary.txt', summary)

# Plot the trend
print("Branch Sale:", branch_sales)
print("Peak Transaction Hour:", peak_transaction_hours(data))
print("Tax-to-Sales Ratio:", tax_to_sales_ratio(data))
print("Revenue Above Threshold:", revenue_above_threshold(data, threshold=50))

plot_branch_sales(branch_sales)
gender_revenue = revenue_by_gender(data)
plot_gender_revenue(gender_revenue)

product_quantities = avg_quantity_by_product_line(data)
plot_product_line_quantities(product_quantities)

plot_payment_methods(data)
