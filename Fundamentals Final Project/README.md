# CHOICE
Fantasy Adventure / RPG

# SCRIBBLE
- Navigation
* Should most likely have a menu, and ask the user what it wants to do.
* So there will be a select amount of actions.

- Character, with Attributes: 
* Level - Not a visible parameter, default value should be 1.
* Equipment/Storage - Should be some sort of collection, starting empty and will be limited to an already decided length.

Should be able to get some statistics about what they have.

- Enemy (baseclass, with subclasses varying):
* BasicEnemy
* WeirdEnemy
* GreatEnemy
(Will probably be a bit too overkill to have a boss, because I am not sure what it would have to distinguish it from all the others)
(And it probably won't make sense in a terminal-based system unless it ACTUALLY has a meaningful quirk.)

!! Based on what level the user is, a certain difficulty will be applied.

#IDK if it is overkill to have a JSON file with everything, so you could load it in IF there is anything, and DELETE it if you so choose.

# LOGIC
- Stepping
* I guess you could have some sort of command to do this logic. 
* step()
* For each step, there is a 1/4 chance that you meet a basic enemy.
* Utilize random(), which takes this relation into account.
* At every decided milestone, you get a heal/refresh of everything.

# ITEMS
- One item might regen a tiny bit of HP back.
- Another might also double turn.
- And another may reduce damage taken.

!! Should probably have very low chance of drops.

# COMBAT
- Take turns. 
- Attack: Do damage
- Defend: Have damage done by enemy reduced.  

# EXTRAS
Would be fun to just make it a bit more decorative, e.g. using kaomoji/emoticons.

# CONSIDERATIONS
There is an incredibly great risk that this could become way too packed. 
I guess the best way for this to work is to have it some Dragon Quest-like fashion. 