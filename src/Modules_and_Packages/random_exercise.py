import random

def generate_tickets(ticket_count, max_number):
    nums = [x for x in range(max_number)]
    fi_el = random.sample(nums, ticket_count)
    se_el = random.choice(fi_el)
    return (fi_el, se_el)
