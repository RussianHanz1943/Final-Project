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
while (1):
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
        break
    else:
        print ()
        print ("Invalid Value. Try Again.")
        pass