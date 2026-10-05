#Part D

# -----1-----
names = ["Lizbeth", "Karen", "Tomi"]
scores = [80, 90, 100]

for name, score in zip(names, scores):
    print(f"{name}: {score} points")

# -----2-----
athlete_names = ["Yoshimoto", "Takashi", "Alfons"]
lengths = [1.60, 1.85, 1.85]

athletes = dict(zip(athlete_names, lengths))

#Proof
print(athletes)

# -----3-----
p_name = ["scottie toilet paper", "nissin ramen", "kikkoman soy sauce"] 
p_price = [3.99, 0.99, 6.99]
p_stock = [50, 20, 15]

products = [(a, b, c) for a, b, c in zip(p_name, p_price, p_stock)]

#Proof
print(products)

# -----4-----
brands = ["ben&jerry", "sia", "häagen-dasz", "triumph"]
flavors = ["vanilla", "chocolate", "strawberry"]

brands_with_flavors = [(a, b) for a, b in zip(brands, flavors)]

#Proof
print(brands_with_flavors)

#It cuts off at the point / length that is shortest, so everything after (in this case) the 3rd item is ignored.

# -----5-----
element_data = ["Water", "Life", "Spell Magic"]
tribe_data = ["Monster", "Human", "Sorcerer Orc"]
zipped_data = [(e,t) for e,t in zip(element_data, tribe_data)]

for data in zipped_data:
    e, t = data
    print(f"Element: {e}, Tribe: {t}")

# -----6-----
p, m = ("Minus", "Plus")
p, m = m, p

#Proof
print(f"Plus={p}, Minus={m}")
