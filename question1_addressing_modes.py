
# Question 1: Effective Address Calculation
# Computer Architecture - Group 2

# Given values
address_field = 200
R1 = 40

# Memory locations and their values
memory = {
    200: 500,
    240: 900
}

print("EFFECTIVE ADDRESS CALCULATION")
print("--------------------------------")

# a) Immediate Addressing
operand = 25

print("\na) Immediate Addressing")
print("Rule: Operand is directly given")
print("Operand =", operand)

# b) Direct Addressing
effective_address = address_field
operand = memory[effective_address]

print("\nb) Direct Addressing")
print("Rule: EA = Address Field")
print("Effective Address =", effective_address)
print("Operand =", operand)

# c) Indirect Addressing
effective_address = memory[address_field]

print("\nc) Indirect Addressing")
print("Rule: EA = Memory[Address Field]")
print("Effective Address =", effective_address)

if effective_address in memory:
    print("Operand =", memory[effective_address])
else:
    print("Operand = Not provided in the question")

# d) Indexed Addressing
effective_address = address_field + R1
operand = memory[effective_address]

print("\nd) Indexed Addressing")
print("Rule: EA = Address Field + R1")
print("Effective Address =", effective_address)
print("Operand =", operand)
