# BCoT TOURNAMENT MANAGEMENT SYSTEM
# Name: Arjun J
# Assignment 4.2 - Programming

import os

# --- SECTION 1: TOURNAMENT RULES & DATA ---

MAX_TEAMS = 4
MAX_INDIVIDUALS = 20
TOTAL_EVENTS = 5

DEFAULT_EVENTS = {
    "1": {"name": "100m Sprint", "type": "Sporting", "scope": "Individual"},
    "2": {"name": "Maths Quiz", "type": "Academic", "scope": "Individual"},
    "3": {"name": "Coding Challenge", "type": "Academic", "scope": "Team"},
    "4": {"name": "Tug of War", "type": "Sporting", "scope": "Team"},
    "5": {"name": "Chess Grand Prix", "type": "Academic", "scope": "Individual"}
}

POINT_MATRIX = [10, 8, 6, 4, 2]

db = {
    "teams": {},
    "individuals": {},
}

# --- SECTION 2: REGISTRATION FUNCTIONS (IMPROVED) ---

def register_competitor():
    print("\n--- Competitor Registration ---")
    print("What type of competitor are you registering?")
    print("1. Team")
    print("2. Individual")
    
    comp_type = input("Choice (1-2): ").strip()
    
    if comp_type == "1":
        register_team()
    elif comp_type == "2":
        register_individual()
    else:
        print("Invalid choice. Returning to main menu.")

def register_team():
    if len(db["teams"]) >= MAX_TEAMS:
        print("Error: Tournament is full (Max 4 teams).")
        return
    
    t_name = input("Enter Team Name: ").strip().lower()
    if not t_name:
        print("Error: Name cannot be empty.")
        return

    if t_name in db["teams"]:
        print("Error: Team name already exists.")
        return

    members = []
    print(f"Enter the 5 member names for team {t_name}:")
    for i in range(1, 6):
        m_name = input(f"  Member {i}: ").strip().lower()
        if not m_name:
            print("Error: Member name cannot be empty. Using 'Unknown'.")
            m_name = "unknown"
        members.append(m_name)
        
    db["teams"][t_name] = {"members": members, "total_points": 0}
    print(f"Success: {t_name} is registered with {len(members)} members.")

def register_individual():
    if len(db["individuals"]) >= MAX_INDIVIDUALS:
        print("Error: No individual spots left (Max 20).")
        return
    
    name = input("Enter Competitor Name: ").strip().lower()
    
    if not name:
        print("Error: Name cannot be empty.")
        return
    
    if name in db["individuals"]:
        print("Error: Individual name already exists.")
        return
    
    single_event = input("Is this a ONE-EVENT only entry? (y/n): ").lower() == 'y'
    
    db["individuals"][name] = {"total_points": 0, "single_event": single_event}
    print(f"Success: {name} is registered.")

# --- SECTION 3: SCORING LOGIC ---

def record_scores():
    print("\n--- Select Event to Score ---")
    for key, event in DEFAULT_EVENTS.items():
        print(f"{key}. {event['name']} ({event['type']})")
    
    event_id = input("Select Event (1-5): ")
    if event_id not in DEFAULT_EVENTS:
        print("Invalid Choice.")
        return
    
    print(f"\nRecording scores for: {DEFAULT_EVENTS[event_id]['name']}")
    target = input("Enter name of Participant to score: ").strip().lower()
    
    try:
        points = float(input("Enter Points earned: "))
        
        if target in db["teams"]:
            db["teams"][target]["total_points"] += points
            print(f"Points saved for Team: {target}")
        elif target in db["individuals"]:
            db["individuals"][target]["total_points"] += points
            print(f"Points saved for Individual: {target}")
        else:
            print("Error: Name not found!")
    except ValueError:
        print("Error: You must type a number.")

# --- SECTION 4: LEADERBOARD & OUTPUT ---

def view_leaderboard():
    print("\n" + "="*40)
    print("      BCoT TOURNAMENT LEADERBOARD")
    print("="*40)
    
    all_results = []
    for name, data in db["teams"].items():
        all_results.append({"name": name, "points": data["total_points"], "type": "Team"})
    for name, data in db["individuals"].items():
        all_results.append({"name": name, "points": data["total_points"], "type": "Indiv"})

    if not all_results:
        print("No competitors registered yet.")
        return

    sorted_list = sorted(all_results, key=lambda x: x['points'], reverse=True)

    print(f"{'RANK':<5} | {'NAME':<20} | {'TYPE':<8} | {'POINTS'}")
    print("-" * 50)
    for i, entry in enumerate(sorted_list):
        print(f"{i+1:<5} | {entry['name']:<20} | {entry['type']:<8} | {entry['points']}")

# --- SECTION 5: MAIN MENU LOOP ---

def main():
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Register Competitor")
        print("2. Input Event Scores")
        print("3. View Leaderboard")
        print("4. Exit")
        
        choice = input("Choice (1-4): ")
        
        if choice == "1": register_competitor()
        elif choice == "2": record_scores()
        elif choice == "3": view_leaderboard()
        elif choice == "4": 
            print("Closing system. Good luck with the tournament!")
            break
        else: 
            print("Try again, 1-4 only.")

if __name__ == "__main__":
    main()