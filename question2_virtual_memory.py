
# Question 2: Virtual to Physical Address Translation
# Computer Architecture - Group 2

# Given page size
page_size = 1024

# Page table
page_table = {
    0: 5,
    1: 2,
    2: None,
    3: 7
}

# Virtual addresses
virtual_addresses = [500, 1500, 2500, 3500]

print("VIRTUAL TO PHYSICAL ADDRESS TRANSLATION")
print("------------------------------------------------")

print("Virtual Address | Page No | Offset | Frame | Physical Address")
print("------------------------------------------------")

# Process each virtual address
for va in virtual_addresses:

    # Calculate page number
    page_number = va // page_size

    # Calculate offset
    offset = va % page_size

    # Check page table
    frame = page_table[page_number]

    if frame is not None:

        # Calculate physical address
        physical_address = frame * page_size + offset

        print(va, "|", page_number, "|", offset,
              "|", frame, "|", physical_address)

    else:
        print(va, "|", page_number, "|", offset,
              "| Not Present | Page fault")
