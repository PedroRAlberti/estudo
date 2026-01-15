from pulp import *

# Create the problem
prob = LpProblem("Universal_Aviation_Aircraft_Selection", LpMaximize)

# Decision variables: number of each aircraft type to purchase
A = LpVariable("Aircraft_A", lowBound=0, cat='Integer')
B = LpVariable("Aircraft_B", lowBound=0, cat='Integer')
C = LpVariable("Aircraft_C", lowBound=0, cat='Integer')
S = LpVariable("Subcontracted_TonMiles", lowBound=0)  # ton-miles subcontracted

# Aircraft parameters
cost_A = 80000
cost_B = 130000
cost_C = 150000

payload_A = 10  # tons
payload_B = 20  # tons
payload_C = 18  # tons

speed_A = 350   # knots (miles/hour)
speed_B = 300   # knots (miles/hour)
speed_C = 300   # knots (miles/hour)

hours_A = 18    # hours/day
hours_B = 18    # hours/day
hours_C = 21    # hours/day

contribution_A = 1     # $ per ton-mile
contribution_B = 8     # $ per ton-mile
contribution_C = 120   # $ per ton-mile
contribution_sub = 0.20  # $ per ton-mile subcontracted

# Calculate daily ton-mile capacity for each aircraft
capacity_A = payload_A * speed_A * hours_A  # ton-miles/day
capacity_B = payload_B * speed_B * hours_B  # ton-miles/day
capacity_C = payload_C * speed_C * hours_C  # ton-miles/day

# Objective function: maximize total contribution
prob += (contribution_A * capacity_A * A + 
         contribution_B * capacity_B * B + 
         contribution_C * capacity_C * C + 
         contribution_sub * S), "Total_Contribution"

# Constraints

# 1. Budget constraint: $4,000,000 available
prob += cost_A * A + cost_B * B + cost_C * C <= 4000000, "Budget_Constraint"

# 2. Maintenance constraint: no more than 30 planes
prob += A + B + C <= 30, "Maintenance_Constraint"

# 3. Pilot-shift constraint: 150 pilot-shifts available per day
# Plane A: 1 pilot × 3 shifts = 3 pilot-shifts/day
# Plane B: 2 pilots × 3 shifts = 6 pilot-shifts/day  
# Plane C: 2 pilots × 3 shifts = 6 pilot-shifts/day
prob += 3*A + 6*B + 6*C <= 150, "Pilot_Shift_Constraint"

# 4. Shipping requirement: 3,500,000 ton-miles must be completed
# Total capacity + subcontracted = required ton-miles
prob += capacity_A * A + capacity_B * B + capacity_C * C + S == 3500000, "Shipping_Requirement"

# Solve the problem
prob.solve()

# Print results
print("Status:", LpStatus[prob.status])
print("\nOptimal Aircraft Mix:")
print(f"Aircraft A: {A.varValue} planes")
print(f"Aircraft B: {B.varValue} planes") 
print(f"Aircraft C: {C.varValue} planes")
print(f"Subcontracted ton-miles: {S.varValue:,.0f}")

print(f"\nTotal contribution per day: ${value(prob.objective):,.2f}")

# Calculate and display constraint usage
print("\nConstraint Usage:")
print(f"Budget used: ${cost_A*A.varValue + cost_B*B.varValue + cost_C*C.varValue:,.0f} / $4,000,000")
print(f"Planes purchased: {A.varValue + B.varValue + C.varValue} / 30")
print(f"Pilot-shifts used: {3*A.varValue + 6*B.varValue + 6*C.varValue} / 150")
print(f"Ton-miles handled internally: {capacity_A*A.varValue + capacity_B*B.varValue + capacity_C*C.varValue:,.0f} / 3,500,000")

# Calculate individual contributions
print("\nIndividual Contributions:")
if A.varValue > 0:
    print(f"Aircraft A: ${contribution_A * capacity_A * A.varValue:,.2f}")
if B.varValue > 0:
    print(f"Aircraft B: ${contribution_B * capacity_B * B.varValue:,.2f}")
if C.varValue > 0:
    print(f"Aircraft C: ${contribution_C * capacity_C * C.varValue:,.2f}")
if S.varValue > 0:
    print(f"Subcontracted: ${contribution_sub * S.varValue:,.2f}")