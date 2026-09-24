def calculate_discount(price, discount):
    """
    Calculate the final price of a product after applying a percentage discount.
    
    Parameters:
        price (int or float): The original price of the product.
        discount (int or float): The discount percentage to apply.
    
    Returns:
        float: The final price after applying the discount.
    
    Example:
        >>> calculate_discount(100, 20)
        80.0
        >>> calculate_discount(50, 10)
        45.0
    """
    final_price = price - (price * discount / 100)
    return final_price
