#2. Implement Function Tools
# @function_tool: get_order_status(order_id): Simulates fetching order status.

# Use is_enabled to toggle the tool (e.g., only enabled for "order" queries).
# Use error_function to return a friendly error if order_id not found. 

from agents import  function_tool

# Tool 1: Check if query is about an order
@function_tool
def is_enabled(query: str) -> bool:
    """Enable this tool only for queries related to orders."""
    # print("<<<<<<<<<<<<<<<< Get Order Status Tool Enabled >>>>>>>>>>>>>>>>>")
    return "order" in query.lower()

# Tool 2: Get order status
@function_tool
def get_order_status(order_id: str):
    """Fetch the status of an order given its ID."""
    # print("<<<<<<<<<<<<<<<< Get Order Status Called >>>>>>>>>>>>>>>>>")
    orders = {
         "01": "Shipped - Expected delivery in 24 hours",
         "02": "Processing - Will ship in tomorrow morning",
         "03": "Delivered - delivery has completed successfully",
    }
    if order_id in orders:
        return {"order_id": order_id, "status": orders[order_id]}
    else:
        return error_function(order_id)

# Tool 3: error function
@function_tool
def error_function(order_id: str):
    """Return a friendly error message."""
    # print("<<<<<<<<<<<<<<<< Get Order Status Error Function Called >>>>>>>>>>>>>>>>>>>>")
    return {"error": f"Sorry, we couldn't find any details for Order ID {order_id}."}
