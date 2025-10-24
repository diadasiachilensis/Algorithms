# Club members data (preloaded founders)
club = {
    1: {"name": "Alice Johnson", "join_date": "17/03/2009", "membership": "Premium", "status": "Up to date"},
    2: {"name": "Brian Smith", "join_date": "17/03/2009", "membership": "Standard", "status": "Up to date"},
    3: {"name": "Charlie Evans", "join_date": "17/03/2009", "membership": "Basic", "status": "Up to date"},
    4: {"name": "Diana Roberts", "join_date": "13/03/2018", "membership": "Standard", "status": "Pending"},
    5: {"name": "Edward Brown", "join_date": "13/03/2018", "membership": "Premium", "status": "Pending"},
    6: {"name": "Fiona Clark", "join_date": "12/03/2018", "membership": "Basic", "status": "Up to date"},
}

# Show all members
def show_members():
    print("\n=== Club Members List ===")
    for num, info in club.items():
        print(f"#{num}: {info['name']} | Joined: {info['join_date']} | Plan: {info['membership']} | Status: {info['status']}")
    print()

# Add a new member
def add_member():
    num = max(club.keys()) + 1
    name = input("Enter member full name: ").title()
    join_date = input("Enter join date (dd/mm/yyyy): ")
    membership = input("Enter membership type (Basic / Standard / Premium): ").capitalize()
    status = input("Is the payment up to date? (y/n): ").lower()
    status = "Up to date" if status == "y" else "Pending"
    club[num] = {"name": name, "join_date": join_date, "membership": membership, "status": status}
    print(f"✅ Member added successfully with number #{num}.\n")

# Count members
def count_members():
    print(f"\n📊 Total members: {len(club)}\n")

# Update payment status
def update_payment():
    try:
        num = int(input("Enter member number to update payment: "))
        if num in club:
            club[num]["status"] = "Up to date"
            print(f"✅ {club[num]['name']} is now up to date with payments.\n")
        else:
            print("❌ Member number not found.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")

# Correct join dates (13/03/2018 → 14/03/2018)
def fix_join_dates():
    count = 0
    for info in club.values():
        if info["join_date"] == "13/03/2018":
            info["join_date"] = "14/03/2018"
            count += 1
    print(f"🗓️ Updated join date for {count} members.\n")

# Remove a member by name
def remove_member():
    name = input("Enter full name of the member to remove: ").title()
    for num, info in list(club.items()):
        if info["name"] == name:
            del club[num]
            print(f"❎ {name} has been removed from the club.\n")
            return
    print("❌ Member not found.\n")

# Main menu
def menu():
    while True:
        print("=== CLUB MANAGEMENT MENU ===")
        print("1. Show total members")
        print("2. Add a new member")
        print("3. Update payment status")
        print("4. Fix join dates (13/03/2018 → 14/03/2018)")
        print("5. Remove a member")
        print("6. Show all members")
        print("7. Exit")

        option = input("Select an option (1-7): ")

        if option == "1":
            count_members()
        elif option == "2":
            add_member()
        elif option == "3":
            update_payment()
        elif option == "4":
            fix_join_dates()
        elif option == "5":
            remove_member()
        elif option == "6":
            show_members()
        elif option == "7":
            print("👋 Exiting program...")
            break
        else:
            print("⚠️ Invalid option, please try again.\n")

# Run program
menu()
