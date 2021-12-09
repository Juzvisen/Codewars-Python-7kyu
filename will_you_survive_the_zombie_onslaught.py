# https://www.codewars.com/kata/5deeb1cc0d5bc9000f70aa74/python


def zombie_shootout(zombies, distance, ammo, shot=0):
    
    if not zombies:
        return f'You shot all {shot} zombies.'
    
    if distance <= 0:
        return f'You shot {shot} zombies before being eaten: overwhelmed.'
    
    if not ammo:
        return f'You shot {shot} zombies before being eaten: ran out of ammo.'
    
    return zombie_shootout(zombies - 1, distance - 0.5, ammo - 1, shot + 1)

