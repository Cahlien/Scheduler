#!/usr/bin/env python

def main():
    # 1) add people to their set shifts, if applicable
    # 2) fill empty manager shifts
    # 3) fill empty part-timer shifts
    # 4) print schedule
    pass

class day:
    def __init__(self, name, start, end):
        self.name = name
        self.shifts = []
        self.start = start
        self.end = end
    
    def add_shift(self, shift):
        self.shifts.append(shift)

class shift:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

class employee:
    def __init__(self, name, shift):
        self.name = name
        self.shift = shift

def print_schedule(week):
    for day in week:
        print(day.name)
        for shift in day.shifts:
            print(shift.name, "-", shift.start, shift.end)

sunday, monday, tuesday, wednesday, thursday, friday, saturday = day("Sunday", 1000, 1900), day("Monday", 1000, 1900), day("Tuesday", 1000, 1900), day("Wednesday", 1000, 1900), day("Thursday", 1000, 1900), day("Friday", 1000, 1900), day("Saturday", 1000, 1900)

rotation_A = shift("Shift A", 1000, 1900)
rotation_B = shift("Shift B", 1000,1900)

sunday.add_shift(rotation_A)
monday.add_shift(rotation_A)
tuesday.add_shift(rotation_A)
wednesday.add_shift(rotation_A)
wednesday.add_shift(rotation_B)
thursday.add_shift(rotation_B)
friday.add_shift(rotation_B)
saturday.add_shift(rotation_B)

emp1 = employee("A", rotation_A)
emp2 = employee("B", rotation_B)
week1 = [sunday, monday, tuesday, wednesday, thursday, friday, saturday]

print_schedule(week1)
