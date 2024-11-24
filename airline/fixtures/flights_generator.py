# this was used to generate the flights fixture

from datetime import datetime, timedelta
import pytz
import json

my_data = []
pk = 1
weeks = 52

# ------------------------------------------------------------------------------

# dairy flats to sydney, starting 31 may 2024, 210 minutes. 1 to 2.
leaves = datetime(2024, 5, 30, 22, 0, 0, tzinfo=pytz.utc)
arrives = datetime(2024, 5, 31, 1, 30, 0, tzinfo=pytz.utc)
for week in range(weeks):
    new_dict = {}
    fields_dict = {}
    new_dict["model"] = "airline.Flight"
    new_dict["pk"] = str(pk)

    fields_dict["direction"] = "O"
    fields_dict["flight_num"] = "DFA011"
    fields_dict["route"] = str(1)
    fields_dict["plane"] = str(1)
    fields_dict["leaving_time_utc"] = str(leaves.time())
    fields_dict["leaving_date_utc"] = str(leaves.date())
    fields_dict["arrival_time_utc"] = str(arrives.time())
    fields_dict["arrival_date_utc"] = str(arrives.date())
    fields_dict["duration"] = str(210)
    # fields_dict["price"] = str(160.00)
    fields_dict["price"] = f"{160.00:.2f}"
    fields_dict["seats_available"] = str(6)

    new_dict["fields"] = fields_dict
    my_data.append(new_dict)

    # print(leaves.astimezone(pytz.timezone("Pacific/Auckland")).time())
    # print(leaves.astimezone(pytz.timezone("Pacific/Auckland")).date())
    # print(arrives.astimezone(pytz.timezone("Australia/Sydney")).time())
    # print(arrives.astimezone(pytz.timezone("Australia/Sydney")).date())

    leaves += timedelta(weeks=1)
    arrives += timedelta(weeks=1)
    pk += 1


# sydney to dairy flats, starting 2 jun 2024, leaves sunday afternoon their time. 2 to 1.
leaves = datetime(2024, 6, 2, 5, 0, 0, tzinfo=pytz.utc)
arrives = datetime(2024, 6, 2, 8, 0, 0, tzinfo=pytz.utc)
for week in range(weeks):
    new_dict = {}
    fields_dict = {}
    new_dict["model"] = "airline.Flight"
    new_dict["pk"] = str(pk)

    fields_dict["direction"] = "I"
    fields_dict["flight_num"] = "DFA012"
    fields_dict["route"] = str(2)
    fields_dict["plane"] = str(1)
    fields_dict["leaving_time_utc"] = str(leaves.time())
    fields_dict["leaving_date_utc"] = str(leaves.date())
    fields_dict["arrival_time_utc"] = str(arrives.time())
    fields_dict["arrival_date_utc"] = str(arrives.date())
    fields_dict["duration"] = str(180)
    # fields_dict["price"] = str(240.00)
    fields_dict["price"] = f"{240.00:.2f}"
    fields_dict["seats_available"] = str(6)

    new_dict["fields"] = fields_dict
    my_data.append(new_dict)

    # print(leaves.astimezone(pytz.timezone("Australia/Sydney")).time())
    # print(leaves.astimezone(pytz.timezone("Australia/Sydney")).date())
    # print(arrives.astimezone(pytz.timezone("Pacific/Auckland")).time())
    # print(arrives.astimezone(pytz.timezone("Pacific/Auckland")).date())

    leaves += timedelta(weeks=1)
    arrives += timedelta(weeks=1)
    pk += 1


# dairy flat to rotorua, mon to fri, morning. route 3 = 1 to 3.
leaves = datetime(2024, 6, 2, 18, 0, 0, tzinfo=pytz.utc)
arrives = datetime(2024, 6, 2, 18, 45, 0, tzinfo=pytz.utc)
for week in range(weeks):
    for j in range(5):
        new_dict = {}
        fields_dict = {}
        new_dict["model"] = "airline.Flight"
        new_dict["pk"] = str(pk)

        fields_dict["direction"] = "O"
        fields_dict["flight_num"] = "DFA021"
        fields_dict["route"] = str(3)
        fields_dict["plane"] = str(2)
        fields_dict["leaving_time_utc"] = str(leaves.time())
        fields_dict["leaving_date_utc"] = str(leaves.date())
        fields_dict["arrival_time_utc"] = str(arrives.time())
        fields_dict["arrival_date_utc"] = str(arrives.date())
        fields_dict["duration"] = str(45)
        # fields_dict["price"] = str(70.00)
        fields_dict["price"] = f"{70.00:.2f}"
        fields_dict["seats_available"] = str(4)

        new_dict["fields"] = fields_dict
        my_data.append(new_dict)

        # print(leaves.astimezone(pytz.timezone("Pacific/Auckland")).time())
        # print(leaves.astimezone(pytz.timezone("Pacific/Auckland")).date())
        # print(arrives.astimezone(pytz.timezone("Pacific/Auckland")).time())
        # print(arrives.astimezone(pytz.timezone("Pacific/Auckland")).date())

        leaves += timedelta(days=1)
        arrives += timedelta(days=1)
        pk += 1

    arrives += timedelta(days=2)
    leaves += timedelta(days=2)


# rotorua to dairy flat, mon to fri, morning. route 4 = 3 to 1
leaves = datetime(2024, 6, 2, 19, 15, 0, tzinfo=pytz.utc)
arrives = datetime(2024, 6, 2, 20, 00, 0, tzinfo=pytz.utc)
for week in range(weeks):
    for j in range(5):
        new_dict = {}
        fields_dict = {}
        new_dict["model"] = "airline.Flight"
        new_dict["pk"] = str(pk)

        fields_dict["direction"] = "I"
        fields_dict["flight_num"] = "DFA022"
        fields_dict["route"] = str(4)
        fields_dict["plane"] = str(2)
        fields_dict["leaving_time_utc"] = str(leaves.time())
        fields_dict["leaving_date_utc"] = str(leaves.date())
        fields_dict["arrival_time_utc"] = str(arrives.time())
        fields_dict["arrival_date_utc"] = str(arrives.date())
        fields_dict["duration"] = str(45)
        # fields_dict["price"] = str(70.00)
        fields_dict["price"] = f"{70.00:.2f}"
        fields_dict["seats_available"] = str(4)

        new_dict["fields"] = fields_dict
        my_data.append(new_dict)

        # print(leaves.astimezone(pytz.timezone("Pacific/Auckland")).time())
        # print(leaves.astimezone(pytz.timezone("Pacific/Auckland")).date())
        # print(arrives.astimezone(pytz.timezone("Pacific/Auckland")).time())
        # print(arrives.astimezone(pytz.timezone("Pacific/Auckland")).date())

        leaves += timedelta(days=1)
        arrives += timedelta(days=1)
        pk += 1

    arrives += timedelta(days=2)
    leaves += timedelta(days=2)

# dairy flat to rotorua, afternoon
leaves = datetime(2024, 6, 3, 4, 00, 0, tzinfo=pytz.utc)
arrives = datetime(2024, 6, 3, 4, 45, 0, tzinfo=pytz.utc)
for week in range(weeks):
    for j in range(5):
        new_dict = {}
        fields_dict = {}
        new_dict["model"] = "airline.Flight"
        new_dict["pk"] = str(pk)

        fields_dict["direction"] = "O"
        fields_dict["flight_num"] = "DFA031"
        fields_dict["route"] = str(3)
        fields_dict["plane"] = str(2)
        fields_dict["leaving_time_utc"] = str(leaves.time())
        fields_dict["leaving_date_utc"] = str(leaves.date())
        fields_dict["arrival_time_utc"] = str(arrives.time())
        fields_dict["arrival_date_utc"] = str(arrives.date())
        fields_dict["duration"] = str(45)
        # fields_dict["price"] = str(70.00)
        fields_dict["price"] = f"{70.00:.2f}"
        fields_dict["seats_available"] = str(4)

        new_dict["fields"] = fields_dict
        my_data.append(new_dict)

        # print(leaves.astimezone(pytz.timezone("Pacific/Auckland")).time())
        # print(leaves.astimezone(pytz.timezone("Pacific/Auckland")).date())
        # print(arrives.astimezone(pytz.timezone("Pacific/Auckland")).time())
        # print(arrives.astimezone(pytz.timezone("Pacific/Auckland")).date())

        leaves += timedelta(days=1)
        arrives += timedelta(days=1)
        pk += 1

    arrives += timedelta(days=2)
    leaves += timedelta(days=2)

# rotorua to dairy flat, afternoon
leaves = datetime(2024, 6, 3, 4, 00, 0, tzinfo=pytz.utc)
arrives = datetime(2024, 6, 3, 4, 45, 0, tzinfo=pytz.utc)
for week in range(weeks):
    for j in range(5):
        new_dict = {}
        fields_dict = {}
        new_dict["model"] = "airline.Flight"
        new_dict["pk"] = str(pk)

        fields_dict["direction"] = "I"
        fields_dict["flight_num"] = "DFA032"
        fields_dict["route"] = str(4)
        fields_dict["plane"] = str(2)
        fields_dict["leaving_time_utc"] = str(leaves.time())
        fields_dict["leaving_date_utc"] = str(leaves.date())
        fields_dict["arrival_time_utc"] = str(arrives.time())
        fields_dict["arrival_date_utc"] = str(arrives.date())
        fields_dict["duration"] = str(45)
        # fields_dict["price"] = str(70.00)
        fields_dict["price"] = f"{70.00:.2f}"
        fields_dict["seats_available"] = str(4)

        new_dict["fields"] = fields_dict
        my_data.append(new_dict)

        # print(leaves.astimezone(pytz.timezone("Pacific/Auckland")).time())
        # print(leaves.astimezone(pytz.timezone("Pacific/Auckland")).date())
        # print(arrives.astimezone(pytz.timezone("Pacific/Auckland")).time())
        # print(arrives.astimezone(pytz.timezone("Pacific/Auckland")).date())

        leaves += timedelta(days=1)
        arrives += timedelta(days=1)
        pk += 1

    arrives += timedelta(days=2)
    leaves += timedelta(days=2)


# dairy flat to claris, morning, mon-wed-fri, duration 30
leaves = datetime(2024, 6, 2, 21, 0, 0, tzinfo=pytz.utc)
arrives = datetime(2024, 6, 2, 21, 30, 0, tzinfo=pytz.utc)
for week in range(weeks):
    for j in range(3):
        new_dict = {}
        fields_dict = {}
        new_dict["model"] = "airline.Flight"
        new_dict["pk"] = str(pk)

        fields_dict["direction"] = "O"
        fields_dict["flight_num"] = "DFA041"
        fields_dict["route"] = str(5)
        fields_dict["plane"] = str(3)
        fields_dict["leaving_time_utc"] = str(leaves.time())
        fields_dict["leaving_date_utc"] = str(leaves.date())
        fields_dict["arrival_time_utc"] = str(arrives.time())
        fields_dict["arrival_date_utc"] = str(arrives.date())
        fields_dict["duration"] = str(25)
        # fields_dict["price"] = str(200.00)
        fields_dict["price"] = f"{200.00:.2f}"
        fields_dict["seats_available"] = str(4)

        new_dict["fields"] = fields_dict
        my_data.append(new_dict)

        # print(leaves.astimezone(pytz.timezone("Pacific/Auckland")).time())
        # print(leaves.astimezone(pytz.timezone("Pacific/Auckland")).date())
        # print(arrives.astimezone(pytz.timezone("Pacific/Auckland")).time())
        # print(arrives.astimezone(pytz.timezone("Pacific/Auckland")).date())

        leaves += timedelta(days=2)
        arrives += timedelta(days=2)
        pk += 1

    arrives += timedelta(days=1)
    leaves += timedelta(days=1)

# claris to dairy flat, morning, tue-thu-sat, duration 30
leaves = datetime(2024, 6, 3, 22, 0, 0, tzinfo=pytz.utc)
arrives = datetime(2024, 6, 3, 22, 30, 0, tzinfo=pytz.utc)
for week in range(weeks):
    for j in range(3):
        new_dict = {}
        fields_dict = {}
        new_dict["model"] = "airline.Flight"
        new_dict["pk"] = str(pk)

        fields_dict["direction"] = "I"
        fields_dict["flight_num"] = "DFA042"
        fields_dict["route"] = str(6)
        fields_dict["plane"] = str(3)
        fields_dict["leaving_time_utc"] = str(leaves.time())
        fields_dict["leaving_date_utc"] = str(leaves.date())
        fields_dict["arrival_time_utc"] = str(arrives.time())
        fields_dict["arrival_date_utc"] = str(arrives.date())
        fields_dict["duration"] = str(30)
        # fields_dict["price"] = str(200.00)
        fields_dict["price"] = f"{200.00:.2f}"
        fields_dict["seats_available"] = str(4)

        new_dict["fields"] = fields_dict
        my_data.append(new_dict)

        # print(leaves.astimezone(pytz.timezone("Pacific/Auckland")).time())
        # print(leaves.astimezone(pytz.timezone("Pacific/Auckland")).date())
        # print(arrives.astimezone(pytz.timezone("Pacific/Auckland")).time())
        # print(arrives.astimezone(pytz.timezone("Pacific/Auckland")).date())

        leaves += timedelta(days=2)
        arrives += timedelta(days=2)
        pk += 1

    arrives += timedelta(days=1)
    leaves += timedelta(days=1)


# dairy flat to chatham island, tue and fri
leaves = datetime(2024, 6, 3, 19, 0, 0, tzinfo=pytz.utc)
arrives = datetime(2024, 6, 3, 21, 15, 0, tzinfo=pytz.utc)
for week in range(weeks):
    for j in range(2):
        new_dict = {}
        fields_dict = {}
        new_dict["model"] = "airline.Flight"
        new_dict["pk"] = str(pk)

        fields_dict["direction"] = "O"
        fields_dict["flight_num"] = "DFA051"
        fields_dict["route"] = str(7)
        fields_dict["plane"] = str(4)
        fields_dict["leaving_time_utc"] = str(leaves.time())
        fields_dict["leaving_date_utc"] = str(leaves.date())
        fields_dict["arrival_time_utc"] = str(arrives.time())
        fields_dict["arrival_date_utc"] = str(arrives.date())
        fields_dict["duration"] = str(120)
        # fields_dict["price"] = str(600.00)
        fields_dict["price"] = f"{600.00:.2f}"
        fields_dict["seats_available"] = str(5)

        new_dict["fields"] = fields_dict
        my_data.append(new_dict)

        # print(leaves.astimezone(pytz.timezone("Pacific/Auckland")).time())
        # print(leaves.astimezone(pytz.timezone("Pacific/Auckland")).date())
        # print(arrives.astimezone(pytz.timezone("Pacific/Chatham")).time())
        # print(arrives.astimezone(pytz.timezone("Pacific/Chatham")).date())

        leaves += timedelta(days=3)
        arrives += timedelta(days=3)
        pk += 1

    arrives += timedelta(days=1)
    leaves += timedelta(days=1)

# chatham island to dairy flat, wed and sat
leaves = datetime(2024, 6, 5, 1, 15, 0, tzinfo=pytz.utc)
arrives = datetime(2024, 6, 5, 3, 30, 0, tzinfo=pytz.utc)
for week in range(weeks):
    for j in range(2):
        new_dict = {}
        fields_dict = {}
        new_dict["model"] = "airline.Flight"
        new_dict["pk"] = str(pk)

        fields_dict["direction"] = "I"
        fields_dict["flight_num"] = "DFA052"
        fields_dict["route"] = str(8)
        fields_dict["plane"] = str(4)
        fields_dict["leaving_time_utc"] = str(leaves.time())
        fields_dict["leaving_date_utc"] = str(leaves.date())
        fields_dict["arrival_time_utc"] = str(arrives.time())
        fields_dict["arrival_date_utc"] = str(arrives.date())
        fields_dict["duration"] = str(135)
        # fields_dict["price"] = str(600.00)
        fields_dict["price"] = f"{600.00:.2f}"
        fields_dict["seats_available"] = str(5)

        new_dict["fields"] = fields_dict
        my_data.append(new_dict)

        # print(leaves.astimezone(pytz.timezone("Pacific/Chatham")).time())
        # print(leaves.astimezone(pytz.timezone("Pacific/Chatham")).date())
        # print(arrives.astimezone(pytz.timezone("Pacific/Auckland")).time())
        # print(arrives.astimezone(pytz.timezone("Pacific/Auckland")).date())

        leaves += timedelta(days=3)
        arrives += timedelta(days=3)
        pk += 1

    arrives += timedelta(days=1)
    leaves += timedelta(days=1)


# weekly service to lake tekapo. departs DF monday.
leaves = datetime(2024, 6, 3, 0, 0, 0, tzinfo=pytz.utc)
arrives = datetime(2024, 6, 3, 1, 30, 0, tzinfo=pytz.utc)
for week in range(weeks):
    new_dict = {}
    fields_dict = {}
    new_dict["model"] = "airline.Flight"
    new_dict["pk"] = str(pk)

    fields_dict["direction"] = "O"
    fields_dict["flight_num"] = "DFA061"
    fields_dict["route"] = str(9)
    fields_dict["plane"] = str(5)
    fields_dict["leaving_time_utc"] = str(leaves.time())
    fields_dict["leaving_date_utc"] = str(leaves.date())
    fields_dict["arrival_time_utc"] = str(arrives.time())
    fields_dict["arrival_date_utc"] = str(arrives.date())
    fields_dict["duration"] = str(90)
    # fields_dict["price"] = str(270.00)
    fields_dict["price"] = f"{270.00:.2f}"
    fields_dict["seats_available"] = str(5)

    new_dict["fields"] = fields_dict
    my_data.append(new_dict)

    # print(leaves.astimezone(pytz.timezone("Pacific/Auckland")).time())
    # print(leaves.astimezone(pytz.timezone("Pacific/Auckland")).date())
    # print(arrives.astimezone(pytz.timezone("Pacific/Auckland")).time())
    # print(arrives.astimezone(pytz.timezone("Pacific/Auckland")).date())

    leaves += timedelta(weeks=1)
    arrives += timedelta(weeks=1)
    pk += 1


# weekly service to lake tekapo. departs lake tekapo tuesday
leaves = datetime(2024, 6, 4, 0, 30, 0, tzinfo=pytz.utc)
arrives = datetime(2024, 6, 4, 2, 0, 0, tzinfo=pytz.utc)
for week in range(weeks):
    new_dict = {}
    fields_dict = {}
    new_dict["model"] = "airline.Flight"
    new_dict["pk"] = str(pk)

    fields_dict["direction"] = "I"
    fields_dict["flight_num"] = "DFA062"
    fields_dict["route"] = str(10)
    fields_dict["plane"] = str(5)
    fields_dict["leaving_time_utc"] = str(leaves.time())
    fields_dict["leaving_date_utc"] = str(leaves.date())
    fields_dict["arrival_time_utc"] = str(arrives.time())
    fields_dict["arrival_date_utc"] = str(arrives.date())
    fields_dict["duration"] = str(90)
    # fields_dict["price"] = str(270.00)
    fields_dict["price"] = f"{270.00:.2f}"
    fields_dict["seats_available"] = str(5)

    new_dict["fields"] = fields_dict
    my_data.append(new_dict)

    # print(leaves.astimezone(pytz.timezone("Pacific/Auckland")).time())
    # print(leaves.astimezone(pytz.timezone("Pacific/Auckland")).date())
    # print(arrives.astimezone(pytz.timezone("Pacific/Auckland")).time())
    # print(arrives.astimezone(pytz.timezone("Pacific/Auckland")).date())

    leaves += timedelta(weeks=1)
    arrives += timedelta(weeks=1)
    pk += 1

# ------------------------------------------------------------------------------

json_str = json.dumps(my_data)
with open("flights.json", "w") as fw:
    fw.write(json_str)
