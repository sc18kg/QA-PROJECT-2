from flask import Flask, Response, request
import random

from application import app

magic = ['Alteration', 'Conjuration', 'Destruction']
combat = ['One-handed', 'Archery', 'Two Handed']
stealth = ['Lockpicking', 'Pickpocket', 'Sneak']
combat_val = []
magic_val = []
stealth_val = []


random_number = random.randint(4,8)
random_number2 = random.randint(4,8)
random_number3 = random.randint(4,8)

for item in range(len(magic)):
    magic_val.append(random_number)

for item in range(len(combat)):
    combat_val.append(random_number2)

for item in range(len(stealth)):
    stealth_val.append(random_number3)


@app.route('/skills', methods=['GET', 'POST'])
def skills():
    data = request.get_json()
    race = data['race']
    gender = data['gender']

    if gender == 'Male':
        combat_val = [x+5 for x in combat_val]

    else:
        stealth_val = [x+5 for x in stealth_val]
    

    if race == 'Altmer':
        stealth_val = [x+2 for x in stealth_val]
        magic_val = [x+2 for x in magic_val]
        combat_val = [x-2 for x in combat_stat]

    elif race == 'Argonian':
        stealth_val = [x+1 for x in stealth_val]
        magic_val = [x-2 for x in magic_val]
        combat_val = [x+3 for x in combat_stat]
        
    elif race == 'Bosmer':
        stealth_val = [x-1 for x in stealth_val]
        magic_val = [x+1 for x in magic_val]
        combat_val = [x+2 for x in combat_stat]

    elif race == 'Breton':
        stealth_val = [x-1 for x in stealth_val]
        magic_val = [x-1 for x in magic_val]
        combat_val = [x+4 for x in combat_stat]
        
    elif race == 'Dunmer':
        stealth_val = [x-4 for x in stealth_val]
        magic_val = [x-1 for x in magic_val]
        combat_val = [x-1 for x in combat_stat]

    elif race == 'Imperial':
        stealth_val = [x+1 for x in stealth_val]
        magic_val = [x-1 for x in magic_val]
        combat_val = [x+2 for x in combat_stat]

    elif race == 'Khajiit':
        stealth_val = [x-2 for x in stealth_val]
        magic_val = [x-2 for x in magic_val]
        combat_val = [x+2 for x in combat_stat]

    elif race == 'Nord':
        stealth_val = [x-1 for x in stealth_val]
        magic_val = [x+0 for x in magic_val]
        combat_val = [x+3 for x in combat_stat]

    elif race == 'Orc':
        stealth_val = [x-3 for x in stealth_val]
        magic_val = [x-2 for x in magic_val]
        combat_val = [x+7 for x in combat_stat]

    else:
        stealth_val = [x-1 for x in stealth_val]
        magic_val = [x-1 for x in magic_val]
        combat_val = [x+4 for x in combat_stat]

    magic_stat = (f"{magic} values are {magic_val}")
    combat_stat = (f"{combat} values are {combat_val}")
    stealth_stat = (f"{stealth} values are {stealth_val}")

    final_char = (combat_stat + magic_stat + stealth_stat)
    db.session.add(skills)
    dbsession.commit()

    return redirect(url_for("index"))