
🚀 Mars-lander Game | Squad Leader Thisun + Cadet Dulnath
import time

print("🚀 MARS LANDING SIMULATOR ACTIVATED 🚀")
print("👨‍🚀 Squad Leader: Thisun | 🫡 Cadet: Dulnath")
print("-" * 40)

altitude = 1000  # meters
fuel = 500       # liters  
velocity = 50    # m/s falling down

print(f"START: Altitude {altitude}m | Fuel {fuel}L | Velocity {velocity}m/s")
print("-" * 40)
time.sleep(1)

while altitude > 0:
    print(f"\nAltitude: {altitude}m | Fuel: {fuel}L | Speed: {velocity}m/s")
    
    try:
        thrust = int(input("Thrust දාන්න 0-50: "))
    except:
        thrust = 0
    
    if thrust > fuel:
        thrust = fuel
        print("⚠️ Fuel මදි! Thrust auto-adjust කළා")
    
    fuel -= thrust
    velocity = velocity - thrust + 10  # Gravity pulls down
    altitude -= velocity
    
    if velocity < 0: velocity = 0
    if altitude < 0: altitude = 0
    time.sleep(0.5)

print("\n" + "=" * 40)
print("🛬 LANDING COMPLETE!")
print(f"Final Speed: {velocity}m/s")

if velocity <= 5:
    print("🏆 PERFECT LANDING! NASA APPROVED! Squad Leader Wins!")
elif velocity <= 15:
    print("✅ Safe Landing! Good job Cadet!")
else:
    print("💥 CRASH! Lander destroyed. Try again malli!")

print("=" * 40)