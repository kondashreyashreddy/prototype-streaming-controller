from var import shows, u1, site, jujutsukaisen, demonslayer, onepiece, sakamotodays, spyxfamily, frieren, chainsawman, rezero, rampartsofice, deathnote, vinlandsaga, jojosbizarreadventure, bluebox
def lin():
    return "-----------------------------------------------"
    
def jujutsu_kaisen():
    print(lin())
    print("Jujutsu Kaisen")
    u1 = 0
    for item in jujutsukaisen:
        u1 += 1
        print(f"{u1}. {item}")
        
def demon_slayer():
    print(lin())
    print("Demon Slayer: Kimetsu no Yaiba")
    u1 = 0
    for item in demonslayer:
        u1 += 1
        print(f"{u1}. {item}")
        
def one_piece():
    print(lin())
    print("One Piece")
    print(f"Choose Between Episode {onepiece[0]} and Episode {onepiece[1]}")

def sakamoto_days():
    print(lin())
    print("Sakamoto Days")
    u1 = 0
    for item in sakamotodays:
        u1 += 1
        print(f"{u1}. {item}")

def spy_x_family():
    print(lin())
    print("Spy X Family")
    u1 = 0
    for item in spyxfamily:
        u1 += 1
        print(f"{u1}. {item}")
        
def FRIEREN():
    print(lin())
    print("Frieren: Beyond Journey's End")
    u1 = 0
    for item in frieren:
        u1 += 1
        print(f"{u1}. {item}")
        
def chainsaw_man():
    print(lin())
    print("Chainsaw Man")
    u1 = 0
    for item in chainsawman:
        u1 += 1
        print(f"{u1}. {item}")
        
def ReZero():
    print(lin())
    print("Re:Zero")
    u1 = 0
    for item in rezero:
        u1 += 1
        print(f"{u1}. {item}")
        
def ramparts_of_ice():
    print(lin())
    print("Ramparts of Ice")
    u1 = 0
    for item in rampartsofice:
        u1 += 1
        print(f"{u1}. {item}")
        
def death_note():
    print(lin())
    print("Death Note")
    print(f"Choose Between Episode {deathnote[0]} and Episode {deathnote[1]}")

def vinland_saga():
    print(lin())
    print("Vinland Saga")
    u1 = 0
    for item in vinlandsaga:
        u1 += 1
        print(f"{u1}. {item}")
        
def jojos_bizarre_adventure():
    print(lin())
    print("Jojo's Bizarre Adventure")
    u1 = 0
    for item in jojosbizarreadventure:
        u1 += 1
        print(f"{u1}. {item}")
        
def blue_box():
    print(lin())
    print("Blue Box")
    u1 = 0
    for item in bluebox:
        u1 += 1
        print(f"{u1}. {item}")
        
def sys_check1(user_input):
    if user_input in site:
        chosen_list = site[user_input]
        return chosen_list
    else:
        service_input = input("\n[Previous Attempt Failed] Enter Name Of Streaming Service Of Choice: ")
        return sys_check1(service_input)
        
def sys_check2(user_input, chose):
    if user_input in chose:
        sys_log(user_input)
        return user_input
    else:
        show_input = input("\n[Previous Attempt Failed] Enter Name Of Show Of Choice: ")
        return sys_check1(show_input, chose)
        
def sys_check3(user_input, show):
    show_options = shows[show]
    if user_input in show_options:
        print(lin())
        print(f"Now watching {show} {user_input}")
        print(lin())
        return user_input
    elif show in ["One Piece","Death Note"]:
            print(lin())
            print(f"Now watching {show} Episode {user_input}")
            print(lin())
            return user_input
    else:
        episode_input = input("\n[Previous Attempt Failed] Enter Episode Of Show Of Choice: ")
        return sys_check3(episode_input, show)
    
def sys_log(anime_name):
    if anime_name == "Jujutsu Kaisen":
        jujutsu_kaisen()
    elif anime_name == "Demon Slayer: Kimetsu no Yaiba":
        demon_slayer()
    elif anime_name == "One Piece":
        one_piece()
    elif anime_name == "Sakamoto Days":
        sakamoto_days()
    elif anime_name == "Spy X Family":
        spy_x_family()
    elif anime_name == "Frieren: Beyond Journey's End":
        FRIEREN()
    elif anime_name == "Chainsaw Man":
        chainsaw_man()
    elif anime_name == "Re:Zero":
        ReZero()
    elif anime_name == "Ramparts of Ice":
        ramparts_of_ice()
    elif anime_name == "Death Note":
        death_note()
    elif anime_name == "Vinland Saga":
        vinland_saga()
    elif anime_name == "Jojo's Bizarre Adventure":
        jojos_bizarre_adventure()
    elif anime_name == "Blue Box":
        blue_box()
