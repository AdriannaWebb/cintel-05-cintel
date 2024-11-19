############################
# Imports
############################

from collections import deque


############################
# Create a deque
############################

# create a deque by calling the deque() constructor and passing in a list of values.

# Create an empty deque
empty_deque = deque()
print(empty_deque) 

# Create a deque by passing in a list with values
temp_deque_F = deque( [56, 58, 47, 54, 55] )
print(temp_deque_F)  

# Create a deque by passing in a list variable
temp_list_C = [5, 6, 8, 4, 3, 2]
temp_deque_C = deque( temp_list_C )
print(temp_deque_C )


############################
# Append Elements
############################

# append() method is for adding new data points to the end 
# appendleft() method is used to append the front but isn't commonly used with live data
temp_deque_F.append(60)
temp_deque_F.append(62)
temp_deque_F.append(64)
temp_deque_F.append(61)

# check results
print(temp_deque_F)


############################
# Remove Elements
############################

# use the pop() method to remove the end of the deque right to left
# use popleft() method to remove from left to right 
temp_deque_F.pop()  
temp_deque_F.popleft()  

# check results
print(temp_deque_F)


############################
# Get Length of List (Count)
############################

#use python's built in len() function
len(temp_deque_F)  


############################
# Clear the Deque
############################

#call the clear() method on the deque.
temp_deque_F.clear()  



############################
# Limit Deque Size
############################

# Initialize deque with a max length of 3 to store last 3 stock prices
msft_prices = deque(maxlen=3)

# Clear the deque (we might call this at the start of a new day)
msft_prices.clear()

# Simulate updating the stock price with new values
msft_prices.append(310.35)
print("MSFT stock prices:", list(msft_prices))

msft_prices.append(312.31)
print("MSFT stock prices:", list(msft_prices))

msft_prices.append(315.25)
print("MSFT stock prices:", list(msft_prices))

msft_prices.append(317.41)
print("MSFT stock prices:", list(msft_prices))




