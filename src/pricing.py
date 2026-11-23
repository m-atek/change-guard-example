"""Order pricing for the demo shop. Demo project, no real data."""


def line_total(unit_price_cents, quantity):
    """Price of one order line in cents."""
    if quantity < 0:
        raise ValueError("quantity must not be negative")
    return unit_price_cents * quantity


def order_total(lines):
    """Sum of all lines, each given as (unit_price_cents, quantity)."""
    return sum(line_total(price, qty) for price, qty in lines)
