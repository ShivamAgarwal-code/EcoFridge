from werkzeug.security import generate_password_hash
from app.models import db, User, GroceryType, Grocery, FreezerGroceryType, FreezerGrocery, PantryGroceryType, PantryGrocery

# Adds a demo user, you can add other users here if you want
def seed_users():

    demo = [
           User(first_name='Demo', 
                last_name='User', 
                email='demo@aa.io',
                password='password', 
                city='Chicago',
                country='USA', 
                avatar='https://images.unsplash.com/photo-1486739985386-d4fae04ca6f7?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxzZWFyY2h8MjF8fHJ1bm5pbmd8ZW58MHx8MHw%3D&auto=format&fit=crop&w=500&q=60'),
           User(
                first_name='David',
                last_name='Jensen',
                email='david@david.com',
                password="password5",
                city="Detroit",
                country="USA",
                avatar='https://images.unsplash.com/photo-1560073743-0a45c01b68c4?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mjd8fHJ1bm5pbmd8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'),
           User(
                first_name='Tom',
                last_name='Mayfield',
                email='tom@tom.com',
                password="password2",
                city="Los Angeles",
                country="USA",
                avatar='https://images.unsplash.com/photo-1475274110913-480c45d0e873?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NDB8fHJ1bm5pbmd8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'),
           User(
                first_name='Sally',
                last_name='Choi',
                email='sally@sally.com',
                password="password3",
                city="Seoul",
                country="South Korea",
                avatar='https://images.unsplash.com/photo-1509010636466-2292663e132f?ixid=MXwxMjA3fDB8MHxzZWFyY2h8OTV8fHJ1bm5pbmd8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'),
           User(
                first_name='Eric',
                last_name='Mandy',
                email='eric@eric.com',
                password="password4",
                city="Berlin",
                country="Germany",
                avatar='https://images.unsplash.com/photo-1512299286776-c18be8ed6a1a?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTA1fHxydW5uaW5nfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'),
    ]

    db.session.add_all(demo)

    db.session.commit()

def seed_grocery_types():

    grocery_type = [
        GroceryType(type='Apples', image='https://i.imgur.com/FVf9I61.jpg', days_to_expiry=28),
        GroceryType(type='Avocados', image='https://i.imgur.com/xjimeYz.jpg', days_to_expiry=21),
        GroceryType(type='Bananas', image='https://i.imgur.com/qAVaqDE.jpg', days_to_expiry=21),
        GroceryType(type='Blueberries', image='https://i.imgur.com/sHMxtTP.jpg', days_to_expiry=7), 
        GroceryType(type='Citrus fruits - orange, grapefruit, clementines, etc.', image='https://i.imgur.com/BaZbcWZ.jpg', days_to_expiry=10),
        GroceryType(type='Dried fruit', image='https://i.imgur.com/zCtmoN7.jpg', days_to_expiry=180), 
        GroceryType(type='Grapes', image='https://i.imgur.com/VnAIH5y.jpg', days_to_expiry=7),
        GroceryType(type='Melons', image='https://i.imgur.com/ZKwZ23R.jpg', days_to_expiry=14),
        GroceryType(type='Peaches, nectarines, plums or pears', image='https://i.imgur.com/Q0TbeAA.jpg', days_to_expiry=3), 
        GroceryType(type='Pineapple', image='https://i.imgur.com/Yj0940Q.jpg', days_to_expiry=5),
        GroceryType(type='Strawberries', image='https://i.imgur.com/OaEx0gn.jpg', days_to_expiry=2),
        GroceryType(type='Asparagus', image='https://i.imgur.com/y8vfLyN.jpg', days_to_expiry=3), 
        GroceryType(type='Bagged greens', image='https://i.imgur.com/KBIpQqb.jpg', days_to_expiry=3), 
        GroceryType(type='Broccoli', image='https://i.imgur.com/bggYZTe.jpg', days_to_expiry=3), 
        GroceryType(type='Brussels sprouts', image='https://i.imgur.com/qaENyle.jpg', days_to_expiry=3), 
        GroceryType(type='Cabbage', image='https://i.imgur.com/hL3gJqV.jpg', days_to_expiry=7), 
        GroceryType(type='Carrots', image='https://i.imgur.com/p5gSJPI.jpg', days_to_expiry=14), 
        GroceryType(type='Cauliflower', image='https://i.imgur.com/4mH7X54.jpg', days_to_expiry=3), 
        GroceryType(type='Celery', image='https://i.imgur.com/J1elfV9.jpg', days_to_expiry=7), 
        GroceryType(type='Corn on the cob', image='https://i.imgur.com/YkOTg4M.jpg', days_to_expiry=1), 
        GroceryType(type='Cucumbers', image='https://i.imgur.com/XR3S8Q0.jpg', days_to_expiry=4), 
        GroceryType(type='Dried beans, lentils or split peas (cooked)', image='https://i.imgur.com/YGdwkaO.jpg', days_to_expiry=3),
        GroceryType(type='Onions', image='https://i.imgur.com/bxCp4pa.jpg', days_to_expiry=60),
        GroceryType(type='Potatoes', image='https://i.imgur.com/XHIFEmZ.jpg', days_to_expiry=300),
        GroceryType(type='Spinach or leaf lettuce', image='https://i.imgur.com/Ixv3b6v.jpg', days_to_expiry=3),
        GroceryType(type='Summer squash or zucchini', image='https://i.imgur.com/RKRRBFj.jpg', days_to_expiry=4), 
        GroceryType(type='Tomatoes', image='https://i.imgur.com/dJ0Zk0E.jpg', days_to_expiry=1), 
        GroceryType(type='Winter squash', image='https://i.imgur.com/heOHlqy.jpg', days_to_expiry=7), 
        GroceryType(type='Butter', image='https://i.imgur.com/1cMcWdJ.jpg', days_to_expiry=31),
        GroceryType(type='Cheese, hard - Cheddar, Swiss, block Parmesan, etc.', image='https://i.imgur.com/KNNx37B.jpg', days_to_expiry=28), 
        GroceryType(type='Cheese, processed', image='https://i.imgur.com/cZz1Nl3.jpg', days_to_expiry=21),
        GroceryType(type='Cheese, shredded - Cheddar, Mozzarella, etc.', image='https://i.imgur.com/L8z4MRr.jpg', days_to_expiry=31), 
        GroceryType(type='Cheese, soft - Brie, Bel paese, etc.', image='https://i.imgur.com/2VIoLjm.jpg', days_to_expiry=7),
        GroceryType(type='Cottage or ricotta cheese', image='https://i.imgur.com/ZYHnbJ3.jpg', days_to_expiry=7), 
        GroceryType(type='Cream cheese', image='https://i.imgur.com/ZYHnbJ3.jpg', days_to_expiry=14),
        GroceryType(type='Margarine', image='https://i.imgur.com/1cMcWdJ.jpg', days_to_expiry=180),
        GroceryType(type='Milk', image='https://i.imgur.com/BdzPlv3.jpg', days_to_expiry=7),  
        GroceryType(type='Milk - canned evaporated or condensed', image='https://i.imgur.com/BdzPlv3.jpg', days_to_expiry=4), 
        GroceryType(type='Non-dairy milk alternates - almond, soy, rice, etc.', image='https://i.imgur.com/BdzPlv3.jpg', days_to_expiry=7), 
        GroceryType(type='Sour cream', image='https://i.imgur.com/ZYHnbJ3.jpg', days_to_expiry=7), 
        GroceryType(type='Fresh beef, veal, lamb or pork (steaks, chops or roasts)', image='https://i.imgur.com/rt7BERZ.jpg', days_to_expiry=3), 
        GroceryType(type='Ground beef, turkey, veal, pork or lamb, stew meat', image='https://i.imgur.com/wxfmWMg.jpg', days_to_expiry=1), 
        GroceryType(type='Bacon', image='https://i.imgur.com/oL9teA8.jpg', days_to_expiry=7), 
        GroceryType(type='Bacon, fully cooked and shelf stable', image='https://i.imgur.com/oL9teA8.jpg', days_to_expiry=5), 
        GroceryType(type='Sausage, raw from chicken, turkey, pork or beef', image='https://i.imgur.com/Y69uwRB.jpg', days_to_expiry=1), 
        GroceryType(type='Sausage, fully cooked, from chicken, turkey, pork or beef', image='https://i.imgur.com/Y69uwRB.jpg', days_to_expiry=7), 
        GroceryType(type='Ham, canned, labeled "Keep Refrigerated"', image='https://i.imgur.com/hzRsvEl.jpg', days_to_expiry=3), 
        GroceryType(type='Ham, fully cooked, store-wrapped, slices, half or spiral cut', image='https://i.imgur.com/hzRsvEl.jpg', days_to_expiry=3), 
        GroceryType(type='Ham, fully cooked, store-wrapped, whole', image='https://i.imgur.com/hzRsvEl.jpg', days_to_expiry=7), 
        GroceryType(type='Hot dogs', image='https://i.imgur.com/sOPIuql.jpg', days_to_expiry=7), 
        GroceryType(type='Lunch meats; sliced at store or deli', image='https://i.imgur.com/qz1wFAK.jpg', days_to_expiry=3), 
        GroceryType(type='Lunch meats; prepackaged', image='https://i.imgur.com/qz1wFAK.jpg', days_to_expiry=7), 
        GroceryType(type='Venison', image='https://i.imgur.com/rt7BERZ.jpg', days_to_expiry=2), 
        GroceryType(type='Chicken or turkey', image='https://i.imgur.com/V5yF8aX.jpg', days_to_expiry=1), 
        GroceryType(type='Commercially canned meat, poultry or fish', image='https://i.imgur.com/V5yF8aX.jpg', days_to_expiry=3), 
        GroceryType(type='Fresh fish or shellfish', image='https://i.imgur.com/cWS2n2V.jpg', days_to_expiry=1), 
        GroceryType(type='Eggs, raw in shell', image='https://i.imgur.com/aDMneVr.jpg', days_to_expiry=21), 
        GroceryType(type='Raw egg yolks, whites', image='https://i.imgur.com/aDMneVr.jpg', days_to_expiry=7), 
        GroceryType(type='Hard cooked eggs', image='https://i.imgur.com/aDMneVr.jpg', days_to_expiry=2), 
        GroceryType(type='Liquid pasteurized eggs or egg substitutes (unopened)', image='https://i.imgur.com/aDMneVr.jpg', days_to_expiry=10), 
        GroceryType(type='Liquid pasteurized eggs or egg substitutes (opened)', image='https://i.imgur.com/aDMneVr.jpg', days_to_expiry=3), 
        GroceryType(type='Leftovers with meat, fish, poultry or egg', image='https://i.imgur.com/V5yF8aX.jpg', days_to_expiry=3), 
        GroceryType(type='Bread', image='https://i.imgur.com/pNyGInN.jpg', days_to_expiry=14), 
        GroceryType(type='Cakes and muffins, baked commercially', image='https://i.imgur.com/pNyGInN.jpg', days_to_expiry=3), 
        GroceryType(type='Tortillas, flour', image='https://i.imgur.com/i0W3PUM.jpg', days_to_expiry=7), 
        GroceryType(type='Pickles', image='https://i.imgur.com/1W0nwbe.jpg', days_to_expiry=30), 
        GroceryType(type='Spaghetti or pizza sauce in jars', image='https://i.imgur.com/TVpAKUq.jpg', days_to_expiry=4), 
        GroceryType(type='Salsa, picante and taco sauces', image='https://i.imgur.com/TVpAKUq.jpg', days_to_expiry=30), 
        GroceryType(type='Hummus (traditional - no preservatives, not pasteurized)', image='https://i.imgur.com/TVpAKUq.jpg', days_to_expiry=7), 
        GroceryType(type='Mayonnaise (commercial)', image='https://i.imgur.com/TVpAKUq.jpg', days_to_expiry=60),
        GroceryType(type='Salad dressings (commercial, bottled)', image='https://i.imgur.com/TVpAKUq.jpg', days_to_expiry=30),
        GroceryType(type='Custom: 1 week', days_to_expiry=7),
        GroceryType(type='Custom: 2 weeks', days_to_expiry=14),
        GroceryType(type='Custom: 1 month', days_to_expiry=30),
        GroceryType(type='Custom: 3 months', days_to_expiry=90),
        GroceryType(type='Custom: 6 months', days_to_expiry=180),
        GroceryType(type='Custom: 1 year', days_to_expiry=365),
        GroceryType(type='Kimchi', image='https://i.imgur.com/K4IeJTA.jpg', days_to_expiry=180),
        GroceryType(type='Pesto', image='https://i.imgur.com/TVpAKUq.jpg', days_to_expiry=7),

    ]

    db.session.add_all(grocery_type)

    db.session.commit()

def seed_freezer_grocery_types():

    freezer_grocery_type = [
        FreezerGroceryType(type='Custom: 1 week', days_to_expiry=7),
        FreezerGroceryType(type='Custom: 2 weeks', days_to_expiry=14),
        FreezerGroceryType(type='Custom: 1 month', days_to_expiry=30),
        FreezerGroceryType(type='Custom: 3 months', days_to_expiry=90),
        FreezerGroceryType(type='Custom: 6 months', days_to_expiry=180),
        FreezerGroceryType(type='Custom: 1 year', days_to_expiry=365), 
        FreezerGroceryType(type='Fresh beef, veal, lamb or pork (steaks, chops or roasts)', image='https://i.imgur.com/rt7BERZ.jpg', days_to_expiry=120), 
        FreezerGroceryType(type='Ground beef, turkey, veal, pork or lamb, stew meat', image='https://i.imgur.com/wxfmWMg.jpg', days_to_expiry=90), 
        FreezerGroceryType(type='Bacon', image='https://i.imgur.com/oL9teA8.jpg', days_to_expiry=30), 
        FreezerGroceryType(type='Bacon, fully cooked and shelf stable', image='https://i.imgur.com/oL9teA8.jpg', days_to_expiry=90), 
        FreezerGroceryType(type='Sausage, raw from chicken, turkey, pork or beef', image='https://i.imgur.com/Y69uwRB.jpg', days_to_expiry=90), 
        FreezerGroceryType(type='Sausage, fully cooked, from chicken, turkey, pork or beef', image='https://i.imgur.com/Y69uwRB.jpg', days_to_expiry=30), 
        FreezerGroceryType(type='Ham, canned, labeled "Keep Refrigerated"', image='https://i.imgur.com/hzRsvEl.jpg', days_to_expiry=30), 
        FreezerGroceryType(type='Ham, fully cooked, store-wrapped, slices, half or spiral cut', image='https://i.imgur.com/hzRsvEl.jpg', days_to_expiry=30), 
        FreezerGroceryType(type='Ham, fully cooked, store-wrapped, whole', image='https://i.imgur.com/hzRsvEl.jpg', days_to_expiry=30), 
        FreezerGroceryType(type='Hot dogs', image='https://i.imgur.com/sOPIuql.jpg', days_to_expiry=30), 
        FreezerGroceryType(type='Lunch meats; sliced at store or deli', image='https://i.imgur.com/qz1wFAK.jpg', days_to_expiry=30), 
        FreezerGroceryType(type='Lunch meats; prepackaged', image='https://i.imgur.com/qz1wFAK.jpg', days_to_expiry=30), 
        FreezerGroceryType(type='Venison', image='https://i.imgur.com/rt7BERZ.jpg', days_to_expiry=60), 
        FreezerGroceryType(type='Chicken or turkey', image='https://i.imgur.com/V5yF8aX.jpg', days_to_expiry=365), 
        FreezerGroceryType(type='Fresh fish or shellfish', image='https://i.imgur.com/cWS2n2V.jpg', days_to_expiry=90), 
        FreezerGroceryType(type='Raw egg yolks, whites', image='https://i.imgur.com/aDMneVr.jpg', days_to_expiry=365), 
        FreezerGroceryType(type='Liquid pasteurized eggs or egg substitutes (unopened)', image='https://i.imgur.com/aDMneVr.jpg', days_to_expiry=365), 
        FreezerGroceryType(type='Leftovers with meat, fish, poultry or egg', image='https://i.imgur.com/V5yF8aX.jpg', days_to_expiry=60),
        FreezerGroceryType(type='Ice cream', image='https://i.imgur.com/lK8QykQ.jpg', days_to_expiry=60), 
        
    ]

    db.session.add_all(freezer_grocery_type)

    db.session.commit()

def seed_pantry_grocery_types():

    pantry_grocery_type = [
        PantryGroceryType(type='Baking Powder', image='https://i.imgur.com/zML4B4u.jpg', days_to_expiry=90),
        PantryGroceryType(type='Baking Soda', image='https://i.imgur.com/zML4B4u.jpg', days_to_expiry=180),
        PantryGroceryType(type='Bouillon cubes or granules', image='https://i.imgur.com/t5VjnqZ.jpg', days_to_expiry=365),
        PantryGroceryType(type='Cereals, ready-to-eat', image='https://i.imgur.com/2OYWLTh.jpg', days_to_expiry=60),
        PantryGroceryType(type='Cornmeal', image='https://i.imgur.com/t5VjnqZ.jpg', days_to_expiry=180),
        PantryGroceryType(type='Flour, white', image='https://i.imgur.com/t5VjnqZ.jpg', days_to_expiry=180),
        PantryGroceryType(type='Flour, whole wheat', image='https://i.imgur.com/t5VjnqZ.jpg', days_to_expiry=90),
        PantryGroceryType(type='Herbs, dried', image='https://i.imgur.com/3McAtJ9.jpg', days_to_expiry=365),
        PantryGroceryType(type='Oatmeal', image='https://i.imgur.com/0ks0edA.jpg', days_to_expiry=180),
        PantryGroceryType(type='Oil - vegetable or olive', image='https://i.imgur.com/HijTAe5.jpg', days_to_expiry=180),
        PantryGroceryType(type='Pasta', image='https://i.imgur.com/TnFNKIz.jpg', days_to_expiry=365),
        PantryGroceryType(type='Peanut butter', image='https://i.imgur.com/TVpAKUq.jpg', days_to_expiry=60),  
        PantryGroceryType(type='Popcorn - dry kernels in a jar', image='https://i.imgur.com/w77pjsY.jpg', days_to_expiry=365),
        PantryGroceryType(type='Popcorn - microwave packets', image='https://i.imgur.com/w77pjsY.jpg', days_to_expiry=60),
        PantryGroceryType(type='Quinoa', image='https://i.imgur.com/w77pjsY.jpg', days_to_expiry=730),
        PantryGroceryType(type='Rice, brown', image='https://i.imgur.com/bvrKGdZ.jpg', days_to_expiry=365),
        PantryGroceryType(type='Rice, white or wild', image='https://i.imgur.com/bvrKGdZ.jpg', days_to_expiry=730),
        PantryGroceryType(type='Spices, ground', image='https://i.imgur.com/3McAtJ9.jpg', days_to_expiry=730), 
        PantryGroceryType(type='Spices, whole', image='https://i.imgur.com/3McAtJ9.jpg', days_to_expiry=1000),
        PantryGroceryType(type='Sugar - brown, powdered, granulated', image='https://i.imgur.com/t5VjnqZ.jpg', days_to_expiry=550),
        PantryGroceryType(type='Yeast', image='https://i.imgur.com/pNyGInN.jpg', days_to_expiry=730),
        PantryGroceryType(type='Custom: 1 week', days_to_expiry=7),
        PantryGroceryType(type='Custom: 2 weeks', days_to_expiry=14),
        PantryGroceryType(type='Custom: 1 month', days_to_expiry=30),
        PantryGroceryType(type='Custom: 3 months', days_to_expiry=90),
        PantryGroceryType(type='Custom: 6 months', days_to_expiry=180),
        PantryGroceryType(type='Custom: 1 year', days_to_expiry=365), 
        PantryGroceryType(type='Bread', image='https://i.imgur.com/pNyGInN.jpg', days_to_expiry=3), 
        PantryGroceryType(type='Bread products, baked commercially such as bread, flat breads, rolls, buns, etc.', image='https://i.imgur.com/pNyGInN.jpg', days_to_expiry=14), 
        PantryGroceryType(type='Cakes and muffins, baked commercially', image='https://i.imgur.com/pNyGInN.jpg', days_to_expiry=7), 
        PantryGroceryType(type='Apples', image='https://i.imgur.com/FVf9I61.jpg', days_to_expiry=21),
        PantryGroceryType(type='Avocados', image='https://i.imgur.com/xjimeYz.jpg', days_to_expiry=3),
        PantryGroceryType(type='Bananas', image='https://i.imgur.com/qAVaqDE.jpg', days_to_expiry=3),
        PantryGroceryType(type='Citrus fruits - orange, grapefruit, clementines, etc.', image='https://i.imgur.com/BaZbcWZ.jpg', days_to_expiry=10),
        PantryGroceryType(type='Grapes', image='https://i.imgur.com/VnAIH5y.jpg', days_to_expiry=1),
        PantryGroceryType(type='Melons', image='https://i.imgur.com/ZKwZ23R.jpg', days_to_expiry=3),
        PantryGroceryType(type='Peaches, nectarines, plums or pears', image='https://i.imgur.com/Q0TbeAA.jpg', days_to_expiry=3), 
        PantryGroceryType(type='Pineapple', image='https://i.imgur.com/Yj0940Q.jpg', days_to_expiry=5),
        PantryGroceryType(type='Strawberries', image='https://i.imgur.com/OaEx0gn.jpg', days_to_expiry=2),
        PantryGroceryType(type='Onions', image='https://i.imgur.com/bxCp4pa.jpg', days_to_expiry=30),
        PantryGroceryType(type='Potatoes', image='https://i.imgur.com/XHIFEmZ.jpg', days_to_expiry=30),
        PantryGroceryType(type='Dried beans, lentils or split peas', image='https://i.imgur.com/YGdwkaO.jpg', days_to_expiry=365),
        PantryGroceryType(type='Summer squash or zucchini', image='https://i.imgur.com/RKRRBFj.jpg', days_to_expiry=1), 
        PantryGroceryType(type='Tomatoes', image='https://i.imgur.com/dJ0Zk0E.jpg', days_to_expiry=7), 
        PantryGroceryType(type='Winter squash', image='https://i.imgur.com/heOHlqy.jpg', days_to_expiry=30), 


    ]

    db.session.add_all(pantry_grocery_type)

    db.session.commit()

def seed_groceries():

    grocery = [
        Grocery(user_id=1, item_name='Aparagus', grocery_types_id=12),
        Grocery(user_id=1, item_name='Apples', grocery_types_id=1),
        Grocery(user_id=1, item_name='Avocados', grocery_types_id=2),
        Grocery(user_id=1, item_name='Bananas', grocery_types_id=3),
        Grocery(user_id=1, item_name='Blueberries', grocery_types_id=4),
   
    ]

    db.session.add_all(grocery)

    db.session.commit()

def seed_freezer_groceries():

    grocery = [
        FreezerGrocery(user_id=1, item_name='Veal', freezer_grocery_types_id=7),
        FreezerGrocery(user_id=1, item_name='Hot dogs', freezer_grocery_types_id=16),
        FreezerGrocery(user_id=1, item_name='chicken', freezer_grocery_types_id=20),
        FreezerGrocery(user_id=1, item_name='bacon', freezer_grocery_types_id=9),
        FreezerGrocery(user_id=1, item_name='venison', freezer_grocery_types_id=19),
   
    ]

    db.session.add_all(grocery)

    db.session.commit()

def seed_pantry_groceries():

    grocery = [
        PantryGrocery(user_id=1, item_name='pasta', pantry_grocery_types_id=11),
        PantryGrocery(user_id=1, item_name='peanut butter', pantry_grocery_types_id=12),
        PantryGrocery(user_id=1, item_name='quinoa', pantry_grocery_types_id=15),
        PantryGrocery(user_id=1, item_name='oatmeal', pantry_grocery_types_id=9),
        PantryGrocery(user_id=1, item_name='cornmeal', pantry_grocery_types_id=5),
        PantryGrocery(user_id=1, item_name='cereal', pantry_grocery_types_id=4),
   
    ]

    db.session.add_all(grocery)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_users():
    db.session.execute('TRUNCATE users;')
    db.session.commit()

def undo_grocery_types():
    db.session.execute('TRUNCATE grocery_types;')
    db.session.commit()

def undo_groceries():
    db.session.execute('TRUNCATE groceries;')
    db.session.commit()
# new models for v2---------------------------------------
def undo_freezer_grocery_types():
    db.session.execute('TRUNCATE freezer_grocery_types;')
    db.session.commit()

def undo_freezer_groceries():
    db.session.execute('TRUNCATE freezer_groceries;')
    db.session.commit()

def undo_pantry_grocery_types():
    db.session.execute('TRUNCATE pantry_grocery_types;')
    db.session.commit()

def undo_pantry_groceries():
    db.session.execute('TRUNCATE pantry_groceries;')
    db.session.commit()
