
# Sample space for a die roll
sample_space_die = {1, 2, 3, 4, 5, 6}

# Event B: Rolling an even number
event_B = {2, 4, 6}

# P(B): Probability of rolling an even number
p_B = len(event_B) / len(sample_space_die)

print("--- Rolling a six-sided die ---")
print(f"Sample space: {sample_space_die}")
print(f"Event B (Rolling an even number): {event_B}")
print(f"P(B) = {p_B}")

# Event C: Rolling a number greater than 4
event_C = {5, 6}

# P(C): Probability of rolling a number greater than 4
p_C = len(event_C) / len(sample_space_die)

print(f"\nEvent C (Rolling a number > 4): {event_C}")
print(f"P(C) = {p_C}")

# --- New Events ---

# Event D: Rolling a number less than 3
# The event set is {1, 2}.
event_D = {1, 2}
p_D = len(event_D) / len(sample_space_die)
print(f"\nEvent D (Rolling a number < 3): {event_D}")
print(f"P(D) = {p_D}")

# Event E: Rolling a prime number
# The event set is {2, 3, 5}.
event_E = {2, 3, 5}
p_E = len(event_E) / len(sample_space_die)
print(f"\nEvent E (Rolling a prime number): {event_E}")
print(f"P(E) = {p_E}")