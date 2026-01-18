# Average of valid measurements
def average_valid_measurements(values):
    """
    Calculate the average of valid (non-None) measurements.
    
    Args:
        values: List of numeric values or None
        
    Returns:
        float: Average of valid measurements
        
    Raises:
        ValueError: If no valid measurements are found
    """
    # Initialize accumulator for sum and counter for valid values
    total = 0
    valid_count = 0

    # Iterate through all values in the list
    for v in values:
        # Only process non-None values (filter out invalid measurements)
        if v is not None:
            # Add the numeric value to our running total
            total += float(v)
            # Increment the count of valid measurements
            valid_count += 1

    # Check if we have any valid measurements before dividing
    if valid_count == 0:
        raise ValueError("No valid measurements to average")
    
    # Calculate and return the average (sum / count)
    return total / valid_count
