import Ferrer_script_1_stat  as sc
import Ferrer_script_2_ev as ec
print("Type and choose the number below")
print("1. Stat Calc")
print("2. EV Calc")

pokemon_nature_Attack = 1
pokemon_nature_Defense = 1
pokemon_nature_SPAttack = 1
pokemon_nature_SPDefense = 1
pokemon_nature_Speed = 1

choice = int(input("Enter: "))


if choice == 1:
    print("Stats")

    Pokemon = str(input("Enter Pokemon: "))

    Pokemon_Level = int(input("Enter Pokemon level: "))

    Pok_Nat = str.lower(input("Enter Pokemon's Nature: "))

    Pokemon_Base = int(input("Enter Pokemon's Base: "))

    Pokemon_IV = int(input("Enter Pokemn's IV: "))

    Pokemon_EV = int(input("Enter Pokemon's EV: "))

    #for pokemon neutral nature
    if Pok_Nat in ['quirky','bashful','serious','docile','hardy']:
        pokemon_nature_Attack = 1
        pokemon_nature_Defense = 1
        pokemon_nature_SPAttack = 1
        pokemon_nature_SPDefense = 1
        pokemon_nature_Speed = 1
    #for pokemon attack nature
    elif Pok_Nat in ['lonely','brave','adamant','naughty']:
        pokemon_nature_Attack = 1.1
        if Pok_Nat in ['lonely']:
            pokemon_nature_Defense = 0.9
        elif Pok_Nat in ['brave']:
            pokemon_nature_Speed = 0.9
        elif Pok_Nat in ['adamant']:
            pokemon_nature_SPAttack = 0.9
        elif Pok_Nat in ['naughty']:
            pokemon_nature_SPDefense = 0.9
    #for pokemon defense nature
    elif Pok_Nat in ['bold','relaxed','impish','lax']:
        pokemon_nature_Defense = 1.1
        if Pok_Nat in ['bold']:
            pokemon_nature_Attack = 0.9
        elif Pok_Nat in ['relaxed']:
            pokemon_nature_Speed = 0.9
        elif Pok_Nat in ['impish']:
            pokemon_nature_SPAttack = 0.9
        elif Pok_Nat in ['lax']:
            pokemon_nature_SPDefense = 0.9
    #for pokemon speed nature
    elif Pok_Nat in ['timid','hasty','jolly','naive']:
        pokemon_nature_Speed = 1.1
        if Pok_Nat in ['timid']:
            pokemon_nature_Attack = 0.9
        elif Pok_Nat in ['hasty']:
            pokemon_nature_Defense = 0.9
        elif Pok_Nat in ['jolly']:
            pokemon_nature_SPAttack = 0.9
        elif Pok_Nat in ['naive']:
            pokemon_nature_SPDefense = 0.9
    #for pokemon special attack nature
    elif Pok_Nat in ['modest','mild','quiet','rash']:
        pokemon_nature_SPAttack = 1.1
        if Pok_Nat in ['modest']:
            pokemon_nature_Attack = 0.9
        elif Pok_Nat in ['mild']:
            pokemon_nature_Defense = 0.9
        elif Pok_Nat in ['quiet']:
            pokemon_nature_Speed = 0.9
        elif Pok_Nat in ['rash']:
            pokemon_nature_SPDefense = 0.9
    #for pokemon special defense nature
    elif Pok_Nat in ['calm','gentle','sassy','careful']:
        pokemon_nature_SPDefense = 1.1
        if Pok_Nat in ['calm']:
            pokemon_nature_Attack = 0.9
        elif Pok_Nat in ['gentle']:
            pokemon_nature_Defense = 0.9
        elif Pok_Nat in ['sassy']:
            pokemon_nature_Speed = 0.9
        elif Pok_Nat in ['careful']:
            pokemon_nature_SPAttack = 0.9
    
    print("1. HP")
    print("2. Attack")
    print("3. Defense")
    print("4. Special Attack")
    print("5. Special Defense")
    print("6. Speed")
    
    opt = int(input("Choose from 1-6: "))

    if opt == 1:
        Pokemon_Base_HP = int(input("Enter Base HP: "))
        Pokemon_Iv = int(input("Enter IV: "))
        Pokemon_Ev = int(input("Enter EV: "))
        print("Total HP: ", sc.Ferrer_script_1_stat.Stat_Calc_HP(Pokemon_Base_HP,Pokemon_Iv,Pokemon_Ev,Pokemon_Level),"\n")
    if opt == 2:
        Pokemon_Base_Attack = int(input("Enter Base Attack Points: "))
        Pokemon_Iv = int(input("Enter IV: "))
        Pokemon_Ev = int(input("Enter EV: "))
        print("Total Attack Points: ", sc.Ferrer_script_1_stat.Other_Stat_Attack(Pokemon_Base_Attack,Pokemon_Iv,Pokemon_Ev,Pokemon_Level,pokemon_nature_Attack),"\n")
    if opt == 3:
        Pokemon_Base_Defense = int(input("Enter Base Defense Points: "))
        Pokemon_Iv = int(input("Enter IV: "))
        Pokemon_Ev = int(input("Enter EV: "))
        print("Total Defense Points: ", sc.Ferrer_script_1_stat.Other_Stat_Defense(Pokemon_Base_Defense,Pokemon_Iv,Pokemon_Ev,Pokemon_Level,pokemon_nature_Defense),"\n")    
    if opt == 4:
        Pokemon_Base_SPAttack = int(input("Enter Base Special Attack Points: "))
        Pokemon_Iv = int(input("Enter IV: "))
        Pokemon_Ev = int(input("Enter EV: "))
        print("Total Special Attack Points: ", sc.Ferrer_script_1_stat.Other_Stat_SPAttack(Pokemon_Base_SPAttack,Pokemon_Iv,Pokemon_Ev,Pokemon_Level,pokemon_nature_SPAttack),"\n")
    if opt == 5:
        Pokemon_Base_SPDefense = int(input("Enter Base Special Defense Points: "))
        Pokemon_Iv = int(input("Enter IV: "))
        Pokemon_Ev = int(input("Enter EV: "))
        print("Total Special Defenes Points: ", sc.Ferrer_script_1_stat.Other_Stat_SPDefense(Pokemon_Base_SPDefense,Pokemon_Iv,Pokemon_Ev,Pokemon_Level,pokemon_nature_SPDefense),"\n")
    if opt == 6:
        Pokemon_Base_Speed = int(input("Enter Base Speed Points: "))
        Pokemon_Iv = int(input("Enter IV: "))
        Pokemon_Ev = int(input("Enter EV: "))
        print("Total Speed Points: ", sc.Ferrer_script_1_stat.Other_Stat_Speed(Pokemon_Base_Speed,Pokemon_Iv,Pokemon_Ev,Pokemon_Level,pokemon_nature_Speed),"\n")

flag = True
Pokemon_Level =0
Pokemon_Stat = ["HP","Attack","Defense","Special Attack","Special Defenes","Speed"]
Pokemon_Base = [6]
Pokemon_IV = [6]
Pokemon_EV = [6]

if choice == 2:
    print("Evs")

    while flag:
        Pokemon_Level = int(input("Enter Pokemon level: "))
        if Pokemon_Level > 0 and Pokemon_Level < 101:
            flag = False
    
    
    Pok_Nat1 = str.lower(input("Enter Pokemon's Nature: "))

    print("Enter Base Stats")   
    for x in range(1, 6):
        Pokemon_Base.append(int(input("Enter "+ Pokemon_Stat[x] + ": ")))
    
    print("Enter IV on each Stat")    
    i = 1
    while i < 7:
        Pokemon_IV.append(int(input("Enter "+Pokemon_Stat[i]+" IV: ")))
        if (Pokemon_IV[i] < 0 or Pokemon_IV[i] > 31):
            i = i - 1
            print("must be between 0 and 31")
        i = i + 1

            

    print("Enter EV on each Stat")
    j = 1
    while j < 7:
        Pokemon_EV.append(int(input("Enter "+Pokemon_Stat[j]+" EV: ")))
        if (Pokemon_EV[j] < 0 or Pokemon_EV[j] > 255):
            j = j - 1
            print("must be between 0 and 255")
        j = j + 1    

    #for pokemon neutral nature
    if Pok_Nat in ['quirky','bashful','serious','docile','hardy']:
        pokemon_nature_Attack = 1
        pokemon_nature_Defense = 1
        pokemon_nature_SPAttack = 1
        pokemon_nature_SPDefense = 1
        pokemon_nature_Speed = 1
    #for pokemon attack nature
    elif Pok_Nat in ['lonely','brave','adamant','naughty']:
        pokemon_nature_Attack = 1.1
        if Pok_Nat in ['lonely']:
            pokemon_nature_Defense = 0.9
        elif Pok_Nat in ['brave']:
            pokemon_nature_Speed = 0.9
        elif Pok_Nat in ['adamant']:
            pokemon_nature_SPAttack = 0.9
        elif Pok_Nat in ['naughty']:
            pokemon_nature_SPDefense = 0.9
    #for pokemon defense nature
    elif Pok_Nat in ['bold','relaxed','impish','lax']:
        pokemon_nature_Defense = 1.1
        if Pok_Nat in ['bold']:
            pokemon_nature_Attack = 0.9
        elif Pok_Nat in ['relaxed']:
            pokemon_nature_Speed = 0.9
        elif Pok_Nat in ['impish']:
            pokemon_nature_SPAttack = 0.9
        elif Pok_Nat in ['lax']:
            pokemon_nature_SPDefense = 0.9
    #for pokemon speed nature
    elif Pok_Nat in ['timid','hasty','jolly','naive']:
        pokemon_nature_Speed = 1.1
        if Pok_Nat in ['timid']:
            pokemon_nature_Attack = 0.9
        elif Pok_Nat in ['hasty']:
            pokemon_nature_Defense = 0.9
        elif Pok_Nat in ['jolly']:
            pokemon_nature_SPAttack = 0.9
        elif Pok_Nat in ['naive']:
            pokemon_nature_SPDefense = 0.9
    #for pokemon special attack nature
    elif Pok_Nat in ['modest','mild','quiet','rash']:
        pokemon_nature_SPAttack = 1.1
        if Pok_Nat in ['modest']:
            pokemon_nature_Attack = 0.9
        elif Pok_Nat in ['mild']:
            pokemon_nature_Defense = 0.9
        elif Pok_Nat in ['quiet']:
            pokemon_nature_Speed = 0.9
        elif Pok_Nat in ['rash']:
            pokemon_nature_SPDefense = 0.9
    #for pokemon special defense nature
    elif Pok_Nat in ['calm','gentle','sassy','careful']:
        pokemon_nature_SPDefense = 1.1
        if Pok_Nat in ['calm']:
            pokemon_nature_Attack = 0.9
        elif Pok_Nat in ['gentle']:
            pokemon_nature_Defense = 0.9
        elif Pok_Nat in ['sassy']:
            pokemon_nature_Speed = 0.9
        elif Pok_Nat in ['careful']:
            pokemon_nature_SPAttack = 0.9

    
    print("1. Attack")
    print("2. Defense")
    print("3. Special Attack")
    print("4. Special Defense")
    print("5. Speed")
    
    opt = int(input("Choose from 1-5: "))

    if opt == 1:
        Modifier = pokemon_nature_Attack
    if opt == 2:
        Modifier = pokemon_nature_Defense
    if opt == 3:
        Modifier = pokemon_nature_SPAttack
    if opt == 4:
        Modifier = pokemon_nature_SPDefense
    if opt == 5:
        Modifier = pokemon_nature_Speed

    Desired_Increase = int(input("Enter Desired Increase: "))

    D = ec.Ferrer_script_2_ev.Ev_Calc_D( Pokemon_Base[opt+1],Pokemon_IV[opt+1],Pokemon_EV[opt+1],Pokemon_Level)

    EVs_needed = ec.Ferrer_script_2_ev.Ev_Calc_EV_Needed( Desired_Increase,Modifier,D,Pokemon_Level)

    print("The total amount of Evs needed for your pokemon ", EVs_needed)
