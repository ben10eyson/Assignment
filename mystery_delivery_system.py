
import json
import math
import csv
import random

def euclidean_distance(point1, point2):
    """
    Calculate Euclidean distance between two points.
    point format: [x, y]
    """
    return math.sqrt(
        (point1[0] - point2[0]) ** 2 +
        (point1[1] - point2[1]) ** 2
    )


def nearest_agent(warehouse_location, agents):
    """
    Find the nearest agent to a warehouse.
    Returns agent_id and distance.
    """
    closest_agent = None
    shortest_distance = float("inf")

    for agent_id, agent_location in agents.items():
        distance = euclidean_distance(agent_location, warehouse_location)

        if distance < shortest_distance:
            shortest_distance = distance
            closest_agent = agent_id

    return closest_agent, shortest_distance


with open("base_case.json", "r") as file:
    data = json.load(file)

warehouses = data["warehouses"]
agents = data["agents"]
packages = data["packages"]

report = {}

for agent_id in agents:
    print(agents)
    print(type(agents))
    report[agent_id] = {
        "packages_delivered": 0,
        "total_distance": 0.0,
        "efficiency": 0.0
    }


print("\n===== DELIVERY SIMULATION =====\n")

for package in packages:

    package_id = package["id"]
    warehouse_id = package["warehouse"]
    destination = package["destination"]

    warehouse_location = warehouses[warehouse_id]

    # Find nearest agent
    agent_id, distance_to_warehouse = nearest_agent(
        warehouse_location,
        agents
    )

    agent_location = agents[agent_id]

    # Distance from warehouse to destination
    distance_to_destination = euclidean_distance(
        warehouse_location,
        destination
    )

    # Total trip distance
    total_trip_distance = (
        distance_to_warehouse +
        distance_to_destination
    )

    delay = random.choice([0, 2, 5])

    # Update report
    report[agent_id]["packages_delivered"] += 1
    report[agent_id]["total_distance"] += total_trip_distance

    agents[agent_id] = destination

    print(f"Package {package_id}")
    print(f"Warehouse : {warehouse_id}")
    print(f"Assigned Agent : {agent_id}")
    print(f"Distance to Warehouse : {distance_to_warehouse:.2f}")
    print(f"Distance to Destination : {distance_to_destination:.2f}")
    print(f"Total Distance : {total_trip_distance:.2f}")
    print(f"Delay : {delay} mins")
    print("-" * 40)


best_agent = None
best_efficiency = float("inf")

for agent_id, stats in report.items():

    delivered = stats["packages_delivered"]

    if delivered > 0:
        stats["efficiency"] = round(
            stats["total_distance"] / delivered,
            2
        )

    stats["total_distance"] = round(
        stats["total_distance"],
        2
    )

    if stats["efficiency"] < best_efficiency:
        best_efficiency = stats["efficiency"]
        best_agent = agent_id

report["best_agent"] = best_agent



with open("report.json", "w") as outfile:
    json.dump(report, outfile, indent=4)

print("\nReport saved to report.json")



with open("top_performer.csv", "w", newline="") as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow([
        "Agent",
        "Packages Delivered",
        "Total Distance",
        "Efficiency"
    ])

    writer.writerow([
        best_agent,
        report[best_agent]["packages_delivered"],
        report[best_agent]["total_distance"],
        report[best_agent]["efficiency"]
    ])

print("Top performer exported to top_performer.csv")



print("\n===== ASCII ROUTE VISUALIZATION =====")

for package in packages:
    print(
        f"{package['warehouse']} ---> {package['destination']}"
    )

print("\nSimulation Completed.")