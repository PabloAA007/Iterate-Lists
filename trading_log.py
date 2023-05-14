# -*- coding: utf-8 -*-
"""
Student Do: Trading Log.

This script demonstrates how to perform basic analysis of trading profits/losses
over the course of a month (20 business days).
"""

# @TODO: Initialize the metric variables
total = 0
count = 0
average = 0
minimum = 0
maximum = 0

# @TODO: Initialize lists to hold profitable and unprofitable day profits/losses
profitable_days = []
unprofitable_days = []

# List of trading profits/losses
trading_pnl = [ -224,  352, 252, 354, -544,
                -650,   56, 123, -43,  254,
                 325, -123,  47, 321,  123,
                 133, -151, 613, 232, -311 ]

# @TODO: Iterate over each element of the list
for x in trading_pnl:

    # @TODO: Cumulatively sum up the total and count
    total += x
    count += 1 

    # @TODO: Write logic to determine minimum and maximum values
    if minimum == 0:
        minimum = x
    elif minimum > x:
        minimum = x
    elif maximum < x:
        maximum = x
        
    # @TODO: Write logic to determine profitable vs. unprofitable days
    if x > 0:
        profitable_days.append(x)
    if x < 0:
        unprofitable_days.append(x)
# @TODO: Calculate the average
average = total / count

# @TODO: Calculate count metrics
unprofitable_count = len(unprofitable_days)
profitable_count = len(profitable_days)

# @TODO: Calculate percentage metrics
percent_profitable_days = profitable_count / count * 100
percent_unprofitable_days = unprofitable_count / count * 100

# @TODO: Print out the summary statistics
print("----------Summary Statistics----------")
print(f"Number of Total Days: {count}")
print(f"Number of Profitable Days: {profitable_count}")
print(f"Number of Unprofitable Days: {unprofitable_count}")
print(f"Percent of Profitable Days: {percent_profitable_days}%")
print(f"Percent of Unprofitable Days: {percent_unprofitable_days}%")
print("--------------------------------------")
print(f"Profitable Days: {profitable_days}")
print(f"Unprofitable Days: {unprofitable_days}")
print("--------------------------------------")
print(f"Total Profits/Lossess: {total}")
print(f"Daily Average: {average}")
print(f"Worst Loss: {minimum}")
print(f"Best Gain: {maximum}")