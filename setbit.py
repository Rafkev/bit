def set_bit(number, position):
    """Set the bit at the given position to 1."""
    return number | (1 << position)

def clear_bit(number, position):
    """Clear the bit at the given position to 0."""
    return number & ~(1 << position)

def toggle_bit(number, position):
    """Toggle the bit at the given position."""
    return number ^ (1 << position)

def check_bit(number, position):
    """Check if the bit at the given position is set (1)."""
    return (number >> position) & 1

def update_bit(number, position, value):
    """Update the bit at the given position with the given value (0 or 1)."""
    mask = ~(1 << position)
    return (number & mask) | (value << position)

# Example usage
num = 10  # 1010 in binary

print("Original number:", num)
print("Setting bit at position 2:", set_bit(num, 2))
print("Clearing bit at position 1:", clear_bit(num, 1))
print("Toggling bit at position 3:", toggle_bit(num, 3))
print("Checking bit at position 0:", check_bit(num, 0))
print("Updating bit at position 1 with 1:", update_bit(num, 1, 1))
