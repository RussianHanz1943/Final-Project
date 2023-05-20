program_name = "Resistor Color Value Converter"
build = "Build 1.18.61"
t = 1
t_1 = 0
t_2 = 0
t_3 = 0
tries = 0
credentials = {"user": "Student", "password": "Password"}
count = 0
VV = 0
VA = 0
small_battery = {"Voltage": 5, "Amperage": 1}
medium_battery = {"Voltage": 9, "Amperage": 2.1}
large_battery = {"Voltage": 12, "Amperage": 10}
power_supply = {"Voltage": VV, "Amperage": VA}
power_sources = ["5V Battery", "9V Battery" ,"12V Battery" ,"Power Supply"]
small_motor = 2500
medium_motor = 4900
large_motor = 8300
motors = ["Small Motor", "Medium Motor", "Large Motor"]
print ()
print (program_name)
print (build)
while (t > 0):
    print ()
    user_input = input("Login, Signup or Exit: ")
    if user_input == "Signup":
        print ()
        print (user_input)
        sign_user = input("Enter Username: ")
        sign_password = input("Enter Password: ")
        credentials.update({"user": sign_user})
        credentials.update({"password": sign_password})
    elif user_input == "Login":
        tries = 0
        print ()
        print (user_input)
        while tries <= 3:
            print ()
            user = input("Enter Username: ")
            password = input ("Enter Password: ")
            t -= 1
            tries += 1
            if user == credentials.get("user") and password == credentials.get("password"):
                print ()
                print ("Welcome", user)
                tries += 3
                t_1 = 1
                while (t_1 > 0):
                    print ()
                    print ("Select what you want to do.", "\n1. Resistor Color Codes", "\n2. Circuit Builder", "\n3. Display Previous Build","\n4. Exit","\n5. Debug: Show Memory", "\n6. Program Info")
                    choice = input("Enter your selection here (Number): ")
                    if choice == "1":
                        t_2 = 1
                        resistor_values = {"Black": {"Value": 0, "Multiplier": 1, "Tolerance": 0 ,"Temperature Coefficient": 250, "Fail Rate": 0},
                        "Brown": {"Value": 1, "Multiplier": 10, "Tolerance": 1,"Temperature Coefficient": 100, "Fail Rate": 1},
                        "Red": {"Value": 2, "Multiplier": 100, "Tolerance": 2,"Temperature Coefficient": 50, "Fail Rate": 0.1},
                        "Orange": {"Value": 3, "Multiplier": 1e3, "Tolerance": 0,"Temperature Coefficient": 15, "Fail Rate": 0.01},
                        "Yellow": {"Value": 4, "Multiplier": 1e4, "Tolerance": 0,"Temperature Coefficient": 25, "Fail Rate": 0.001},
                        "Green": {"Value": 5, "Multiplier": 1e5, "Tolerance": 0.5,"Temperature Coefficient": 20, "Fail Rate": 0},
                        "Blue": {"Value": 6, "Multiplier": 1e6, "Tolerance": 0.25,"Temperature Coefficient": 10, "Fail Rate": 0},
                        "Violet": {"Value": 7, "Multiplier": 1e7, "Tolerance": 0.1,"Temperature Coefficient": 5, "Fail Rate": 0},
                        "Gray": {"Value": 8, "Multiplier": 1e8, "Tolerance": 0.05,"Temperature Coefficient": 1, "Fail Rate": 0},
                        "White": {"Value": 9, "Multiplier": 1e9, "Tolerance": 0,"Temperature Coefficient": 0, "Fail Rate": 0},
                        "Gold": {"Value": 0, "Multiplier": 0.1, "Tolerance": 5,"Temperature Coefficient": 0, "Fail Rate": 0},
                        "Silver": {"Value": 0, "Multiplier": 0.01, "Tolerance": 10,"Temperature Coefficient": 0, "Fail Rate": 0},
                        "None": {"Value": 0, "Multiplier": 0, "Tolerance": 20,"Temperature Coefficient": 0, "Fail Rate": 0}}
                        resistor_type = ["4 Band", "5 Band", "6 Band"]
                        resistor_color = ["Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", "Violet", "Gray", "White", "Gold", "Silver", "None"]
                        r_band_1 = ""
                        r_band_2 = ""
                        r_band_3 = ""
                        r_band_4 = ""
                        r_band_5 = ""
                        r_band_6 = ""
                        ban_list = ["Gold", "Silver", "None"]
                        multiplier = ""
                        tolerance = ""
                        temperature_coefficient = ""
                        print ()
                        print ("Resistor Color Code Converter")
                        while (t_2 > 0):
                            print ()
                            print ("Select what to do:", "\n1. Color Code -> Resistance Value", "\n2. Resistance Value -> Color Code", "\n3. Exit")
                            choice_2 = input("Select Mode (Number): ")
                            if choice_2 == "1":
                                print (resistor_type)
                                choice_3 = input("Select type: ")
                                if choice_3 == resistor_type[0]:
                                    print (resistor_type[0])
                                    print (resistor_color)
                                    print ("Select Color Combination: ")
                                    i_band_1 = input("Assign Color for the 1st Band: ")
                                    i_band_2 = input("Assign Color for the 2nd Band: ")
                                    i_band_3 = input("Assign Color for the 3rd Band: ")
                                    i_band_4 = input("Assign Color for the 4th Band: ")
                                    band_1 = i_band_1.capitalize()
                                    band_2 = i_band_2.capitalize()
                                    band_3 = i_band_3.capitalize()
                                    band_4 = i_band_4.capitalize()
                                    ohms = ((resistor_values[band_1]["Value"] * 10 + resistor_values[band_2]["Value"]) * (resistor_values[band_3]["Multiplier"]))
                                    print ()
                                    print("Select displayed output:", "\n1. Ohms(Ω)", "\n2. Kilo ohms(K Ω)", "\n3. Mega ohms(M Ω)")
                                    choice_4 = input("Input choice here: ")
                                    if choice_4 == "1":
                                        print ("Result:", ohms, "Ω", "±", str(resistor_values[band_4]["Tolerance"])+"%", "Tolerance")
                                    elif choice_4 == "2":
                                        print ("Result:", ohms/1e3, "kΩ", "±", str(resistor_values[band_4]["Tolerance"])+"%", "Tolerance")
                                    elif choice_4 == "3":
                                        print ("Result:", ohms/1e6, "MΩ", "±", str(resistor_values[band_4]["Tolerance"])+"%", "Tolerance")
                                elif choice_3 == resistor_type[1]:
                                    print (resistor_type[1])
                                    print (resistor_color)
                                    print ("Select Color Combination: ")
                                    i_band_1 = input("Assign Color for the 1st Band: ")
                                    i_band_2 = input("Assign Color for the 2nd Band: ")
                                    i_band_3 = input("Assign Color for the 3rd Band: ")
                                    i_band_4 = input("Assign Color for the 4th Band: ")
                                    i_band_5 = input("Assign Color for the 5th Band: ")
                                    band_1 = i_band_1.capitalize()
                                    band_2 = i_band_2.capitalize()
                                    band_3 = i_band_3.capitalize()
                                    band_4 = i_band_4.capitalize()
                                    band_5 = i_band_5.capitalize()
                                    ohms = ((resistor_values[band_1]["Value"] * 100 + resistor_values[band_2]["Value"] * 10 + resistor_values[band_3]["Value"]) * (resistor_values[band_4]["Multiplier"]))
                                    print ()
                                    print("Select displayed output:", "\n1. Ohms(Ω)", "\n2. Kilo ohms(K Ω)", "\n3. Mega ohms(M Ω)")
                                    choice_4 = input("Input choice here: ")
                                    if choice_4 == "1":
                                        print ("Result:", ohms, "Ω", "±", str(resistor_values[band_5]["Tolerance"])+"%", "Tolerance")
                                    elif choice_4 == "2":
                                        print ("Result:", ohms/1e3, "kΩ", "±", str(resistor_values[band_5]["Tolerance"])+"%", "Tolerance")
                                    elif choice_4 == "3":
                                        print ("Result:", ohms/1e6, "MΩ", "±", str(resistor_values[band_5]["Tolerance"])+"%", "Tolerance")
                                elif choice_3 == resistor_type[2]:
                                    print (resistor_type[2])
                                    print (resistor_color)
                                    print ("Select Color Combination: ")
                                    i_band_1 = input("Assign Color for the 1st Band: ")
                                    i_band_2 = input("Assign Color for the 2nd Band: ")
                                    i_band_3 = input("Assign Color for the 3rd Band: ")
                                    i_band_4 = input("Assign Color for the 4th Band: ")
                                    i_band_5 = input("Assign Color for the 5th Band: ")
                                    i_band_6 = input("Assign Color for the 6th Band: ")
                                    band_1 = i_band_1.capitalize()
                                    band_2 = i_band_2.capitalize()
                                    band_3 = i_band_3.capitalize()
                                    band_4 = i_band_4.capitalize()
                                    band_5 = i_band_5.capitalize()
                                    band_6 = i_band_6.capitalize()
                                    ohms = ((resistor_values[band_1]["Value"] * 100 + resistor_values[band_2]["Value"] * 10 + resistor_values[band_3]["Value"]) * (resistor_values[band_4]["Multiplier"]))
                                    print ()
                                    print("Select displayed output:", "\n1. Ohms(Ω)", "\n2. Kilo ohms(K Ω)", "\n3. Mega ohms(M Ω)")
                                    choice_4 = input("Input choice here: ")
                                    if choice_4 == "1":
                                        print ("Result:", ohms, "Ω", "±", str(resistor_values[band_5]["Tolerance"])+"%", "Tolerance"+",", str(resistor_values[band_6]["Temperature Coefficient"]), "ppm/K", str(resistor_values[band_5]["Fail Rate"])+"%", "Fail Rate")
                                    elif choice_4 == "2":
                                        print ("Result:", ohms/1e3, "kΩ", "±", str(resistor_values[band_5]["Tolerance"])+"%", "Tolerance"+",", str(resistor_values[band_6]["Temperature Coefficient"]), "ppm/K", str(resistor_values[band_5]["Fail Rate"])+"%", "Fail Rate")
                                    elif choice_4 == "3":
                                        print ("Result:", ohms/1e6, "MΩ", "±", str(resistor_values[band_5]["Tolerance"])+"%", "Tolerance"+",", str(resistor_values[band_6]["Temperature Coefficient"]), "ppm/K", str(resistor_values[band_5]["Fail Rate"])+"%", "Fail Rate")
                                else:
                                    print ()
                                    print ("Invalid Choice. Try Again.")
                            elif choice_2 == "2":
                                print ()
                                print (resistor_type)
                                choice_4 = input("Select type: ")
                                if choice_4 == resistor_type[0]:
                                    ohms_1 = input("Resistance Value (0-9): ")
                                    ohms_2 = input("Resistance Value (0-9): ")
                                    print ()
                                    print ("0.01, 0.1, 0, 1, 10, 100, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9")
                                    multiplier = str(input("Multiplier Value: "))
                                    if multiplier == "0.01":
                                        r_band_3 = "Silver"
                                    elif multiplier == "0.1":
                                        r_band_3 = "Gold"
                                    elif multiplier == "0":
                                        r_band_3 = "None"
                                    elif multiplier == "1":
                                        r_band_3 = "Black"
                                    elif multiplier == "10":
                                        r_band_3 = "Brown"
                                    elif multiplier == "100":
                                        r_band_3 = "Red"
                                    elif multiplier == "1e3":
                                        r_band_3 = "Orange"
                                    elif multiplier == "1e4":
                                        r_band_3 = "Yellow"
                                    elif multiplier == "1e5":
                                        r_band_3 = "Green"
                                    elif multiplier == "1e6":
                                        r_band_3 = "Blue"
                                    elif multiplier == "1e7":
                                        r_band_3 = "Violet"
                                    elif multiplier == "1e8":
                                        r_band_3 = "Gray"
                                    elif multiplier == "1e9":
                                        r_band_3 = "White"
                                    print ()
                                    print ("0, 0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10, 20")
                                    tolerance = input("Tolerance Value: ")
                                    if tolerance == "0":
                                        r_band_4 = "Orange, Yellow or White"
                                    elif tolerance == "0.05":
                                        r_band_4 = "Gray"
                                    elif tolerance == "0.1":
                                        r_band_4 = "Violet"
                                    elif tolerance == "0.25":
                                        r_band_4 = "Blue"
                                    elif tolerance == "0.5":
                                        r_band_4 = "Green"
                                    elif tolerance == "1":
                                        r_band_4 = "Brown"
                                    elif tolerance == "2":
                                        r_band_4 = "Red"
                                    elif tolerance == "5":
                                        r_band_4 = "Gold"
                                    elif tolerance == "10":
                                        r_band_4 = "Silver"
                                    elif tolerance == "20":
                                        r_band_4 = "None"
                                    for band_1 in resistor_values:
                                        for values in str(resistor_values[band_1]["Value"]):
                                            if ohms_1 != values:
                                                pass
                                            elif ohms_1 == values:
                                                if r_band_1 in ban_list:
                                                    pass
                                                else:
                                                    r_band_1 = band_1
                                    for band_2 in resistor_values:
                                        for values in str(resistor_values[band_2]["Value"]):
                                            if ohms_2 != values:
                                                pass
                                            elif ohms_2 == values:
                                                if band_2 in ban_list:
                                                    pass
                                                else:
                                                    r_band_2 = band_2
                                    print ("Results:")
                                    print ("Band 1:", r_band_1,",", "Band 2:", r_band_2,",", "Band 3:", r_band_3,",", "Band 4:", r_band_4)
                                if choice_4 == resistor_type[1]:
                                    ohms_1 = input("Resistance Value (0-9): ")
                                    ohms_2 = input("Resistance Value (0-9): ")
                                    ohms_3 = input("Resistance Value (0-9): ")
                                    print ()
                                    print ("0.01, 0.1, 0, 1, 10, 100, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9")
                                    multiplier = str(input("Multiplier Value: "))
                                    if multiplier == "0.01":
                                        r_band_4 = "Silver"
                                    elif multiplier == "0.1":
                                        r_band_4 = "Gold"
                                    elif multiplier == "0":
                                        r_band_4 = "None"
                                    elif multiplier == "1":
                                        r_band_4 = "Black"
                                    elif multiplier == "10":
                                        r_band_4 = "Brown"
                                    elif multiplier == "100":
                                        r_band_4 = "Red"
                                    elif multiplier == "1e3":
                                        r_band_4 = "Orange"
                                    elif multiplier == "1e4":
                                        r_band_4 = "Yellow"
                                    elif multiplier == "1e5":
                                        r_band_4 = "Green"
                                    elif multiplier == "1e6":
                                        r_band_4 = "Blue"
                                    elif multiplier == "1e7":
                                        r_band_4 = "Violet"
                                    elif multiplier == "1e8":
                                        r_band_4 = "Gray"
                                    elif multiplier == "1e9":
                                        r_band_4 = "White"
                                    print ()
                                    print ("0, 0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10, 20")
                                    tolerance = input("Tolerance Value: ")
                                    if tolerance == "0":
                                        r_band_5 = "Orange, Yellow or White"
                                    elif tolerance == "0.05":
                                        r_band_5 = "Gray"
                                    elif tolerance == "0.1":
                                        r_band_5 = "Violet"
                                    elif tolerance == "0.25":
                                        r_band_5 = "Blue"
                                    elif tolerance == "0.5":
                                        r_band_5 = "Green"
                                    elif tolerance == "1":
                                        r_band_5 = "Brown"
                                    elif tolerance == "2":
                                        r_band_5 = "Red"
                                    elif tolerance == "5":
                                        r_band_5 = "Gold"
                                    elif tolerance == "10":
                                        r_band_5 = "Silver"
                                    elif tolerance == "20":
                                        r_band_5 = "None"
                                    for band_1 in resistor_values:
                                        for values in str(resistor_values[band_1]["Value"]):
                                            if ohms_1 != values:
                                                pass
                                            elif ohms_1 == values:
                                                if r_band_1 in ban_list:
                                                    pass
                                                else:
                                                    r_band_1 = band_1
                                    for band_2 in resistor_values:
                                        for values in str(resistor_values[band_2]["Value"]):
                                            if ohms_2 != values:
                                                pass
                                            elif ohms_2 == values:
                                                if band_2 in ban_list:
                                                    pass
                                                else:
                                                    r_band_2 = band_2
                                    for band_3 in resistor_values:
                                        for values in str(resistor_values[band_3]["Value"]):
                                            if ohms_3 != values:
                                                pass
                                            elif ohms_3 == values:
                                                if band_3 in ban_list:
                                                    pass
                                                else:
                                                    r_band_3 = band_3
                                    print ("Results:")
                                    print ("Band 1:", r_band_1,",", "Band 2:", r_band_2,",", "Band 3:", r_band_3,",", "Band 4:", r_band_4,",", "Band 5:", r_band_5)
                                if choice_4 == resistor_type[2]:
                                    ohms_1 = input("Resistance Value (0-9): ")
                                    ohms_2 = input("Resistance Value (0-9): ")
                                    ohms_3 = input("Resistance Value (0-9): ")
                                    print ()
                                    print ("0.01, 0.1, 0, 1, 10, 100, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9")
                                    multiplier = str(input("Multiplier Value: "))
                                    if multiplier == "0.01":
                                        r_band_4 = "Silver"
                                    elif multiplier == "0.1":
                                        r_band_4 = "Gold"
                                    elif multiplier == "0":
                                        r_band_4 = "None"
                                    elif multiplier == "1":
                                        r_band_4 = "Black"
                                    elif multiplier == "10":
                                        r_band_4 = "Brown"
                                    elif multiplier == "100":
                                        r_band_4 = "Red"
                                    elif multiplier == "1e3":
                                        r_band_4 = "Orange"
                                    elif multiplier == "1e4":
                                        r_band_4 = "Yellow"
                                    elif multiplier == "1e5":
                                        r_band_4 = "Green"
                                    elif multiplier == "1e6":
                                        r_band_4 = "Blue"
                                    elif multiplier == "1e7":
                                        r_band_4 = "Violet"
                                    elif multiplier == "1e8":
                                        r_band_4 = "Gray"
                                    elif multiplier == "1e9":
                                        r_band_4 = "White"
                                    print ()
                                    print ("0, 0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10, 20")
                                    tolerance = input("Tolerance Value: ")
                                    if tolerance == "0":
                                        r_band_5 = "Orange, Yellow or White"
                                    elif tolerance == "0.05":
                                        r_band_5 = "Gray"
                                    elif tolerance == "0.1":
                                        r_band_5 = "Violet"
                                    elif tolerance == "0.25":
                                        r_band_5 = "Blue"
                                    elif tolerance == "0.5":
                                        r_band_5 = "Green"
                                    elif tolerance == "1":
                                        r_band_5 = "Brown"
                                    elif tolerance == "2":
                                        r_band_5 = "Red"
                                    elif tolerance == "5":
                                        r_band_5 = "Gold"
                                    elif tolerance == "10":
                                        r_band_5 = "Silver"
                                    elif tolerance == "20":
                                        r_band_5 = "None"
                                    print ()
                                    print ("0, 1, 5, 10, 15, 20, 25, 50, 100, 250")
                                    temperature_coefficient = input("Temperature Coefficient Value (ppm/K): ")
                                    if temperature_coefficient == "0":
                                        r_band_6 = "None, Silver, Gold or White"
                                    elif temperature_coefficient == "1":
                                        r_band_6 = "Gray"
                                    elif temperature_coefficient == "5":
                                        r_band_6 = "Violet"
                                    elif temperature_coefficient == "10":
                                        r_band_6 = "Blue"
                                    elif temperature_coefficient == "15":
                                        r_band_6 = "Orange"
                                    elif temperature_coefficient == "20":
                                        r_band_6 = "Green"
                                    elif temperature_coefficient == "25":
                                        r_band_6 = "Yellow"
                                    elif temperature_coefficient == "50":
                                        r_band_6 = "Red"
                                    elif temperature_coefficient == "100":
                                        r_band_6 = "Brown"
                                    elif temperature_coefficient == "250":
                                        r_band_6 = "Black"
                                    for band_1 in resistor_values:
                                        for values in str(resistor_values[band_1]["Value"]):
                                            if ohms_1 != values:
                                                pass
                                            elif ohms_1 == values:
                                                if r_band_1 in ban_list:
                                                    pass
                                                else:
                                                    r_band_1 = band_1
                                    for band_2 in resistor_values:
                                        for values in str(resistor_values[band_2]["Value"]):
                                            if ohms_2 != values:
                                                pass
                                            elif ohms_2 == values:
                                                if band_2 in ban_list:
                                                    pass
                                                else:
                                                    r_band_2 = band_2
                                    for band_3 in resistor_values:
                                        for values in str(resistor_values[band_3]["Value"]):
                                            if ohms_3 != values:
                                                pass
                                            elif ohms_3 == values:
                                                if band_3 in ban_list:
                                                    pass
                                                else:
                                                    r_band_3 = band_3
                                    print ("Results:")
                                    print ("Band 1:", r_band_1,",", "Band 2:", r_band_2,",", "Band 3:", r_band_3,",", "Band 4:", r_band_4,",", "Band 5:", r_band_5,",","Band 6:", r_band_6)
                            elif choice_2 == "3":
                                t_2 = 0
                            else:
                                print ("Invalid Value. Try Again.")
                    elif choice == "2":
                        count += 1
                        t_3 = 1
                        print ()
                        print ("Circuit Builder")
                        while (t_3 > 0):
                            print (power_sources)
                            name = input("Select power source: ")
                            if name in power_sources:
                                print ()
                                if name == power_sources[0]:
                                    power_source = small_battery
                                    print (power_source)
                                elif name == power_sources[1]:
                                    power_source = medium_battery
                                    print (power_source)
                                elif name == power_sources[2]:
                                    power_source = large_battery
                                    print (power_source)
                                elif name == power_sources[3]:
                                    f_VV = float(input("Enter Voltage Value: "))
                                    f_VA = float(input("Enter Amperage Value: "))
                                    power_supply.update({"Voltage": f_VV})
                                    power_supply.update({"Amperage": f_VA})
                                    power_source = power_supply
                                    print (power_source)
                                print ()
                                print ("Choose load: Motor or Light")
                                choice_1 = input("Enter choice here: ")
                                if choice_1 == "Motor":
                                    print ()
                                    print (motors)
                                    motor_choice = input("Selected motor: ")
                                    if motor_choice == motors[0]:
                                        rpm = power_source.get("Voltage") * power_source.get("Amperage") * 120
                                        if rpm < small_motor:
                                            print ("Motor RPM =", rpm, "RPM")
                                        else:
                                            rpm = small_motor
                                            print ()
                                            print ("High power detected. Running motor in safe mode.")
                                            print ("Motor RPM =", rpm, "RPM")
                                        t_3 = 0
                                    elif motor_choice == motors[1]:
                                        rpm = power_source.get("Voltage") * power_source.get("Amperage") * 120
                                        if rpm < medium_motor:
                                            print ("Motor RPM =", rpm, "RPM")
                                        else:
                                            rpm = medium_motor
                                            print ()
                                            print ("High power detected. Running motor in safe mode.")
                                            print ("Motor RPM =", rpm, "RPM")
                                        t_3 = 0
                                    elif motor_choice == motors[2]:
                                        rpm = power_source.get("Voltage") * power_source.get("Amperage") * 120
                                        if rpm < large_motor:
                                            print ("Motor RPM =", rpm, "RPM")
                                        else:
                                            rpm = large_motor
                                            print ()
                                            print ("High power detected. Running motor in safe mode.")
                                            print ("Motor RPM =", rpm, "RPM")
                                        t_3 = 0
                                    else:
                                        print (motor_choice, "is not present. Select only from the options above.")
                                        pass
                                elif choice_1 == "Light":
                                    light_power = power_source.get("Voltage") * power_source.get("Amperage")
                                    print ()
                                    print ("Light Power =", light_power, "W")
                                    t_3 = 0
                                else:
                                    print ("Invalid Choice, Try Again.")
                            else:
                                print ("Choice is not present. Try again.")
                    elif choice == "3":
                        if count == 0:
                            print ()
                            print ("Error 404. No previous circuit built detected.")
                            pass
                        elif count > 0:
                            print ()
                            print ("Last Circuit Built:")
                            print (name, ":", power_source.get("Voltage"), "V", "@", power_source.get("Amperage"), "A")
                            if choice_1 == "Motor":
                                print(motor_choice, "@", rpm, "RPM")
                            elif choice_1 =="Light":
                                print ("Light Power =", light_power, "W")
                    elif choice == "4":
                        print ()
                        print ("Are you sure you want to leave?")
                        escape = input("Yes or No? ")
                        escape_0 = escape.casefold()
                        if escape_0 == "yes":
                            print ()
                            print (program_name)
                            print (build)
                            t_1 = 0
                            t = 1
                        elif escape_0 =="no":
                            pass
                    elif choice == "5":
                        print (count)
                        print (credentials)
                        print (tries)
                        print (t)
                        print (t_1)
                        print (t_2)
                        print (t_3)
                    elif choice == "6":
                        print ()
                        print ("Program Information")
                        print ()
                        print (program_name)
                        print (build)
                        print ("Developed by: The Group 6 Development Trio")
                    else:
                        print ()
                        print ("Invalid value. Try Again!")
            elif tries == 3:
                print ()
                print ("You have reached the maximum amount of tries. Try again next time.")
                break
            else:
                print ("Invalid Username or Password. Try Again.")
                pass
    elif user_input == "Exit":
        print ()
        print ("Thank you for using the program. Bye o/")
        print ()
        print (program_name)
        print (build)
        t = 0
    else:
        print ("Invalid Option. Try Again.")