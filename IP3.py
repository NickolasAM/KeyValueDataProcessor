# Author: Nickolas Marquez
# Assignment: Individual Project 3 - Key-Value MapReduce Simulation
# Description: This script demonstrates basic key-value operations in Python using a dictionary.
#              It also includes logic to simulate part of a MapReduce concept.

# --------------------------
# Create a dictionary of 50 US states and their capitals
# --------------------------
us_states = {
    1: "Montgomery", 2: "Juneau", 3: "Phoenix", 4: "Little Rock", 5: "Sacramento",
    6: "Denver", 7: "Hartford", 8: "Dover", 9: "Tallahassee", 10: "Atlanta",
    11: "Honolulu", 12: "Boise", 13: "Springfield", 14: "Indianapolis", 15: "Des Moines",
    16: "Topeka", 17: "Frankfort", 18: "Baton Rouge", 19: "Augusta", 20: "Annapolis",
    21: "Boston", 22: "Lansing", 23: "St. Paul", 24: "Jackson", 25: "Jefferson City",
    26: "Helena", 27: "Lincoln", 28: "Carson City", 29: "Concord", 30: "Trenton",
    31: "Santa Fe", 32: "Albany", 33: "Raleigh", 34: "Bismarck", 35: "Columbus",
    36: "Oklahoma City", 37: "Salem", 38: "Harrisburg", 39: "Providence", 40: "Columbia",
    41: "Pierre", 42: "Nashville", 43: "Austin", 44: "Salt Lake City", 45: "Montpelier",
    46: "Richmond", 47: "Olympia", 48: "Charleston", 49: "Madison", 50: "Cheyenne"
}

# --------------------------
# 1. Enumerate key-value pairs
# --------------------------
print("Enumerated key-value pairs:")
for key, value in us_states.items():
    print(f"{key}: {value}")

# --------------------------
# 2. List all keys in the dictionary
# --------------------------
print("\nAll keys:")
print(list(us_states.keys()))

# --------------------------
# 3. List all values in the dictionary
# --------------------------
print("\nAll values:")
print(list(us_states.values()))

# --------------------------
# 4. Replace value at key 1
# --------------------------
us_states[1] = "New Montgomery"  # Simulating an update in a key-value system
print(f"\nUpdated value at key 1: {us_states[1]}")

