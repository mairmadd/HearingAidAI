print("Welcome to the Hearing Aid Troubleshooting AI!")

problem = input("What problem are you experiencing? ").lower()

if "no sound" in problem: print("Recommendation: Check the battery, charge the hearing aid, and check the wax filter.")
elif "weak" in problem or "muffled" in problem: print("Recommendation: Check the wax filter and microphone openings.")
elif "whistling" in problem or "feedback" in problem: print("Recommendation: Check the hearing aid fit and make sure it is inserted correctly.")
elif "bluetooth" in problem: print("Recommendation: Make sure Bluetooth is on and reconnect the hearing aid.")
elif "cutting out" in problem or "static" in problem: print("Recommendation: Check the battery and moisture exposure.")
elif "pain" in problem or "uncomfortable" in problem: print("Recommendation: Stop wearing the hearing aid and schedule a fit check.")
else: print("Problem not recognized. Please contact a hearing care professional.")

