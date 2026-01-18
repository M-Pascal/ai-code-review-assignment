# Calculating the average of non-cancelled orders
def calculate_average_order_value(orders):
    """
    Calculate the average order value for non-cancelled orders.
    
    Args:
        orders: A list of order dictionaries, each containing 'status' and 'amount' keys.
    
    Returns:
        float: The average order value, or 0 if there are no non-cancelled orders.
    """
    total = 0  # Sum of all non-cancelled order amounts
    count = 0  # Count of non-cancelled orders

    # Iterate through all orders
    for order in orders:
        # Only include non-cancelled orders in the calculation
        if order["status"] != "cancelled":
            total += order["amount"]
            count += 1

    # Return the average, avoiding division by zero
    return total / count if count > 0 else 0
