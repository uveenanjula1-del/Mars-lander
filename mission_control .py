#NASA MISSION CONTROL SYSTEM - FINAL BOSS
print("=== NASA MISSION CONTROL ===")

nasa_team = [
    {
        "name": "Neil Armstrong", 
        "role": "Commander",
        "missions": 2,
        "moon_ready": True
    },
    {
        "name": "Buzz Aldrin",
        "role": "Pilot", 
        "missions": 2,
        "moon_ready": True
    },
    {
        "name": "thisun",
        "role": "Engineer",
        "missions": 0,
        "moon_ready": True
    }
]

print("\n--- ASTRONAUT ROSTER ---")
total_moon_ready = 0

for astronaut in nasa_team:
    print(f"\nName: {astronaut['name']}")
    print(f"Role: {astronaut['role']}")
    print(f"Missions: {astronaut['missions']}")
    
    if astronaut['moon_ready'] == True:
        print("Status: MOON READY ✅")
        total_moon_ready = total_moon_ready + 1
    else:
        print("Status: TRAINING NEEDED ❌")

print(f"\n--- MISSION STATUS ---")
print(f"Moon Ready Astronauts: {total_moon_ready}/3")

if total_moon_ready == 3:
    print("\n[LAUNCH APPROVED] 🚀🌕")
    print("[FINAL MISSION COMPLETE]")
    print("YOU ARE NOW NASA SPACE APPS READY!")
else:
    print("\n[LAUNCH DELAYED] Complete training first")