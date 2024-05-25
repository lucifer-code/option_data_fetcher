from datetime import datetime, time

def is_within_business_hours(now=None):
    # Get the current date and time
    # now = 
    
    # Define the start and end time
    start_time = time(9, 15)  # 9:15 AM
    end_time = time(15, 30)   # 3:30 PM
    
    # Get the current time
    current_time = now.time()
    
    # Check if current day is between Monday (0) and Friday (4)
    if now.weekday() >= 0 and now.weekday() <= 4:
        # Check if current time is between start_time and end_time
        if start_time <= current_time <= end_time:
            return True
    
    return False

# Example usage
# print (is_within_business_hours(datetime.now()))