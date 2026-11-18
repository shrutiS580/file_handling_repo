
# def analyse(orders):

#     revenue = {}
#     products = {}
#     customer_status = {}

#     for order in orders:

#         customer = order['customer']
#         status = order['status']

#         if customer not in customer_status:
#             customer_status[customer] = []

#         customer_status[customer].append(status)

#         if status != 'CANCELLED':

#             if customer not in revenue:
#                 revenue[customer] = 0

#             for item in order['items']:

#                 name = item[0]
#                 quantity = item[1]
#                 price = item[2]

#                 revenue[customer] += quantity * price

#                 if name not in products:
#                     products[name] = 0

#                 products[name] += quantity

#     top_products = sorted(
#         products.items(),
#         key=lambda x: (-x[1], x[0])
#     )[:2]

#     fully_delivered = sorted([
#         customer
#         for customer in customer_status
#         if all(status == 'DELIVERED'
#                for status in customer_status[customer])
#     ])

#     return {
#         'revenue': revenue,
#         'top_products': top_products,
#         'fully_delivered': fully_delivered
#     }


# orders = [
#     {'id': 101, 'customer': 'Asha', 'status': 'DELIVERED',
#      'items': [('keyboard', 2, 1499.0), ('mouse', 1, 599.0)]},

#     {'id': 102, 'customer': 'Ravi', 'status': 'CANCELLED',
#      'items': [('monitor', 1, 10999.0)]},

#     {'id': 103, 'customer': 'Asha', 'status': 'DELIVERED',
#      'items': [('cable', 5, 199.0)]},

#     {'id': 104, 'customer': 'Meera', 'status': 'SHIPPED',
#      'items': [('keyboard', 1, 1499.0), ('monitor', 1, 10999.0)]},

#     {'id': 105, 'customer': 'Ravi', 'status': 'DELIVERED',
#      'items': [('mouse', 3, 599.0)]}
# ]

# result = analyse(orders)
# print(result)








def clean_customer(raw):

    fields = raw.split(';')

    if len(fields) != 4:
        return None

    name = fields[0].strip().title()
    email = fields[1].strip().lower()
    phone = fields[2].strip()
    city = fields[3].strip().title()

    words = name.split()

    if len(words) == 0:
        return None

    for word in words:
        if not word.isalpha():
            return None

    if city == "":
        return None

    if email.count('@') != 1:
        return None

    parts = email.split('@')

    username = parts[0]
    domain = parts[1]

    if username == "":
        return None

    if '.' not in domain:
        return None

    if domain[0] == '.' or domain[-1] == '.':
        return None

    phone = phone.replace(" ", "")
    phone = phone.replace("-", "")

    if phone.startswith("+91"):
        phone = phone[3:]

    elif len(phone) == 12 and phone.startswith("91"):
        phone = phone[2:]

    if len(phone) != 10:
        return None

    if not phone.isdigit():
        return None

    if phone[0] not in "6789":
        return None

    return {
        'name': name,
        'email': email,
        'phone': phone,
        'city': city
    }


lines = [
    ' asha VERMA ; ASHA.V@Example.COM ; +91 98765-43210 ;pune ',
    'ravi kumar;ravi@@corp.in;9123456780;Mumbai',
    'meera;meera@mail;9123456780;Delhi',
    'john doe; john@x.org ;12345; Goa',
    'Neha Rao;neha.rao@firm.co.in;919876501234;nashik',
    'amit;amit@site.com;9876543210'
]

rejected = 0

for record in lines:

    result = clean_customer(record)

    if result is not None:
        print(result)

    else:
        rejected += 1

print("Rejected:", rejected)
