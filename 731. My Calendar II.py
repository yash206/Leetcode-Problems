''' 
Question -
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.
A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).
The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.
Implement the MyCalendarTwo class:
MyCalendarTwo() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
'''

'''
Difficulty - Medium
'''


class MyCalendarTwo:

    def __init__(self):
        self.single = []  # Stores single booked intervals
        self.double_booked = []  # Stores double booked intervals

    def book(self, start: int, end: int) -> bool:
        # Check if the event overlaps with any double booking, which would cause a triple booking
        for s, e in self.double_booked:
            if max(start, s) < min(end, e):
                return False  # Triple booking found
        
        # Add the overlapping parts to double bookings
        for s, e in self.single:
            if max(start, s) < min(end, e):
                self.double_booked.append((max(start, s), min(end, e)))
        
        # Add the event to single bookings
        self.single.append((start, end))
        return True


'''
Time Complexity - O(n)
'''
