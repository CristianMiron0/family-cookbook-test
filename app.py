import os
from flask import Flask, jsonify, render_template, abort
import random

app = Flask(__name__)

# Data structure to hold categories and recipes
data = {
    "mainDish": [
        {"id": "lentil_burger", "name": "Lentil and Cauliflower Meatballs in a Burger", "img": "lentil_burger.png"},
        {"id": "beouf_salad", "name": "Beouf Salad", "img": "salata_beouf.png"},
        {"id": "sarmele", "name": "Sarmale", "img": "sarmale.jpg"},
        {"id": "meatballs_mushrooms", "name": "Meatballs with mushrooms", "img": "meatballs_with_mush.png"},
        {"id": "eggplant_mushrooms", "name": "Eggplant stuffed with mushrooms", "img": "vinete_umplute_cu_ciuperci.png"},
        {"id": "spinach_rice", "name": "Spinach with rice", "img": "spinach_with_rice.jpg"}
    ],

    "mainDishPage2": [
        {"id": "stuffed_tomatoes_rice", "name": "Tomatoes stuffed with potatoes and rice in the oven", "img": "rosii_umplute.png"},
        {"id": "cheese_and_onion_pasties", "name": "Cheese and Onion Pasties", "img": "cheese_pastry.jpeg"},
        {"id": "tvp_meatballs", "name": "TVP Meatballs", "img": "vegan_tvp.jpg"}
    ],

    "appetizer": [
        {"id": "sweet_potatoes_garlic", "name": "Sweet potatoes with garlic and thyme", "img": "sweet_potatoes_garlic.jpg"},
        {"id": "sage_onion_stuffing", "name": "Sage and onion stuffing", "img": "sage_onion_stuffing.jpg"},
        {"id": "pizza_chec", "name": "Appetizer cake with olives", "img": "pizza_chec.png"}
    ],

    "soup": [
        {"id": "leek_onion_bechamel", "name": "Leek and onion bechamel sauce", "img": "leek_onion_bechamel.jpg"},
        {"id": "fideo_con_garbanzos", "name": "Quick garbanzos and fideos soup", "img": "fideo_con_garbanzos.png"},
        {"id": "mancarica_cartofi", "name": "Peas with Potatoes", "img": "mancarica_cartofi.jpg"}
    ],

    "salad": [
        {"id": "apple_yogurt", "name": "Apple yogurt salad", "img": "apple_yogurt.jpg"},
        {"id": "grape_walnut", "name": "Grape and walnut salad", "img": "grape_walnut.jpg"},
        {"id": "asian_cucumber", "name": "Asian cucumber salad", "img": "asian_cucumber.jpg"},
        {"id": "veggies_feta", "name": "Baked veggies with feta cheese", "img": "veggies_feta.jpg"},
        {"id": "ensaladilla_rusa", "name": "Ensaladilla rusa", "img": "ensaladilla_rusa.jpg"},
        {"id": "tomato_avocado", "name": "Tomato and avocado salad", "img": "tomato_avocado.jpg"}
    ],

    "saladPage2": [
        {"id": "lentil_salad", "name": "Cold lentil salad", "img": "lentil_salad.jpg"},
        {"id": "radish_rocket", "name": "Radish and rockett salad", "img": "radish_rocket.jpg"},
        {"id": "tortellini_salad", "name": "Tortellini Salad", "img": "tortellini_salad.jpg"}
    ],

    "dessert": [
        {"id": "banana_bread", "name": "Banana Bread", "img": "banana_bread.jpg"},
        {"id": "pretzels", "name": "Pretzels in syrup", "img": "pretzels.jpg"},
        {"id": "negreasa", "name": "Chocolate glazed negreasa", "img": "negreasa.jpg"},
        {"id": "chocolate_mug_cake", "name": "Chocolate Mug Cake", "img": "chocolate_mug_cake.png"},
        {"id": "cookies", "name": "Peanut Butter Cookies", "img": "cookies.jpg"}
    ],

    "snack": [
        {"id": "honey_parsnips", "name": "Honey-roasted parsnips", "img": "honey_parsnips.jpg"},
        {"id": "zucchini_oregano", "name": "Baked zucchini with oil and oregano", "img": "zucchini_oregano.jpg"},
        {"id": "tofu_peach", "name": "Grilled Sesame Peach Tofu", "img": "tofu_peach.jpg"},
        {"id": "mamaliga", "name": "Mamaliga", "img": "mamaliga.jpg"}
    ],

    "details": {
        "lentil_burger": {
            "name": "Lentil and Cauliflower Meatballs in a Burger",
            "prep": "20 mins",
            "cook": "20 mins",
            "yields": "10 Servings",
            "ingredients": [
                "300 grams of red lentils",
                "600 grams of cauliflower",
                "1 large onion",
                "2 cloves of garlic",
                "1 teaspoon ground cumin",
                "4 tablespoons of olive oil",
                "2 tablespoons of quinoa, chickpea or pea flour",
                "Salt and pepper",
                "To assemble: 6 buns, sauces of your choice, green salad, tomatoes, onions, etc"
            ],
            "steps": [
                "Preheat the oven to 180°C.",
                "Put the cauliflower on the grater with large holes and spread it on a baking paper in as even a layer as possible. Place in the preheated oven and bake for 5-6 minutes, until traces of browning appear from place to place (especially on the edges).",
                "Wash the lentils under running water in a colander, then boil them in 1 L of water, together with the chopped garlic and a pinch of salt. After it boils, reduce the heat to minimum and continue boiling for about 15 minutes), until the liquid is absorbed and the lentils begin to crumble.",
                "Add the grated onion, cauliflower flakes, flour, ground cumin, 1 tablespoon of olive oil and salt and pepper to taste over the lentils (other spices can be added, according to everyone's preferences). Mix well and, with wet hands, form the meatballs that sit on a tray covered with baking paper, then sprinkle with 1 tablespoon of olive oil.",
                "Bake the meatballs in a preheated oven at 180 degrees Celsius for 15-20 minutes, possibly turning them with a spatula halfway through the baking time (it's not mandatory, though). They can also be made in the air fryer at 180 degrees for 15-20 minutes."
            ]
        },

        "beouf_salad": {
            "name": "Beouf Salad",
            "prep": "1 hour",
            "cook": "2 hours",
            "yields": "10+ Servings",
            "ingredients": [
                "1 kg steak and/or thigh meat",
                "1-1.5 kg boiled potatoes in their skins",
                "Approx. 1 kg of home made mayonnaise (for composition and decoration)",
                "500 g marcov (or according to taste)",
                "250 g celery root",
                "250 g parsley root",
                "1.5 pickled red peppers (or pimientos de piquillo)",
                "300 g or 5-6 pieces of pickled cucumbers",
                "1-2 teaspoons of salt, or to taste",
                "6 eggs (3 raw and 3 boiled, only the yolk from the boiled and raw ones) (for mayonnaise)",
                "1 spoon of mustard (for mayonnaise)",
                "750 ml or 1 L of oil (for mayonnaise)",
                "Olives (for decoration)",
                "Egg white from boiled eggs (for decoration)"
            ],
            "steps": [
                "Put the washed potatoes to boil in cold water with a spoonful of salt on medium heat for about one hour or until a knife goes in and out easily.",
                "If using meat, boil it for a short time to remove all the blood. The meat will be cooked more with vegetables later.",
                "Cut the cucumbers lengthwise into slices, then into sticks and small cubes. Cut the peppers the same way.",
                "In a pot, add celery root, parsley root, and carrots. Add bay leaves, peppercorns, and the meat (if using) with the vegetables, covering everything with water. Boil until all the vegetables are soft (about 1-1.5 hours).",
                "Peel the boiled potatoes (this may take time, so prepare something to watch).",
                "Once all the vegetables are cooked, start cutting them, using the same technique as for cucumbers and peppers. Add everything to a large bowl.",
                "For the mayonnaise, place the eggs in a bowl, add mustard, and mix with a whisk. Gradually add oil until incorporated with the eggs. You can use a mixer after adding a little oil, but be careful not to add too much oil at once.",
                "After adding all ingredients to the large bowl, add salt and mix with your hands. Then add the mayonnaise and mix again with a spoon.",
                "The salad is ready to be shaped as desired."
            ]
        },

        "sarmele": {
            "name": "Sarmale",
            "prep": "1-2 hours",
            "cook": "3-4 hours",
            "yields": "10+ Servings",
            "ingredients": [
                "200 ml olive oil",
                "500 g finely chopped onion",
                "1 tablespoon salt",
                "1 grated carrot (250 g)",
                "50-60 g finely chopped walnut kernel (or 500 g finely chopped mushrooms or soya or a combination)",
                "40-50 g tomato paste",
                "1-2 finely chopped Kabia peppers",
                "300 g washed and soaked rice",
                "200 ml tomato juice + 50-100 ml water if needed",
                "1/2 teaspoon pepper",
                "6 g dried thyme",
                "1 good bunch of dill",
                "1 good bunch of fresh parsley",
                "50 g cornmeal (malai) (optional)",
                "Leaves from one pickled cabbage for the sarmale and some leftover for under and above the sarmale in the pot",
                "1 garlic head",
                "4-5 springs of dill",
                "100 ml olive oil for boiling",
                "+/- 250 ml water, to cover the cabbage rolls",
                "For the tomato sauce: 600 ml tomato juice, 2-3 cups of water, pepper, bay leaves, 1 level tablespoon of salt, 3 g dried thyme"
            ],
            "steps": [
                "Add the oil to a pot, then add the chopped onion and salt. Sauté and stir for about 10 minutes until the onion is slightly caramelized.",
                "Add the grated carrot and cook for another 4-5 minutes, stirring constantly.",
                "After 4-5 minutes, add the walnut or mushrooms with soy (following the instructions on the bag) and cook for another minute. Add the tomato paste and stir for another minute, then cook for an additional 2 minutes after adding the peppers.",
                "Add the rice and cook for about 5 minutes, adding a little water or tomato juice to prevent burning.",
                "Add pepper, thyme, chopped dill and parsley over the mixture. If desired, add cornmeal to help bind the sarmale. Mix for the last time.",
                "As the mixture cools, prepare the sauce by adding thyme, salt, pepper, bay leaves to the tomato juice and water.",
                "Start forming the sarmale. Take the leaves, cut them in half, and assemble by adding about a spoonful of the filling and rolling.",
                "Place some chopped cabbage at the bottom of a pot, add garlic cloves and dill springs if available, then start stacking the sarmale in the pot.",
                "Add 100 ml of oil and the tomato sauce, then add a little water until the sarmale are covered. Place some cabbage leaves on top and cover with baking paper or aluminum foil to prevent burning.",
                "Put the pot on low heat and simmer for about 3 hours. After 3 hours, check one sarmale to see if it's cooked. If not, continue to cook as needed."
            ]
        },

        "meatballs_mushrooms": {
            "name": "Meatballs with Mushrooms",
            "prep": "20 minutes",
            "cook": "30 minutes",
            "yields": "8 Servings",
            "ingredients": [
                "600 g mixed mushrooms (frozen or fresh)",
                "2 boiled potatoes in their skins",
                "2 slices of bread",
                "1 onion",
                "2 cloves of garlic",
                "1 teaspoon chopped dill",
                "2 tablespoons flour",
                "2 tablespoons breadcrumbs",
                "Salt (to taste)",
                "Pepper (to taste)",
                "Oil for frying",
                "Flour for coating"
            ],
            "steps": [
                "Peel the two potatoes.",
                "Mash the peeled potatoes until you achieve a smooth puree.",
                "Wash the mushrooms, onion, and garlic.",
                "Finely chop the mushrooms, onion, and garlic.",
                "Soak the bread in water and squeeze it well to remove excess moisture.",
                "Sauté the mushrooms, onion, and garlic in two tablespoons of oil until all the moisture evaporates.",
                "Blend the sautéed mushrooms with the onion and garlic in a blender until you achieve a creamy paste.",
                "Mix the mushroom paste with the potato puree, soaked bread, flour, and breadcrumbs.",
                "Add dill, salt, and pepper to taste.",
                "Mix all the ingredients well until you achieve a homogeneous mixture.",
                "Form round or flat meatballs from the mixture.",
                "Coat the meatballs in flour.",
                "Fry the meatballs in hot oil until golden or fully cooked.",
                "Drain the fried meatballs on a paper towel to remove excess oil.",
                "Let the meatballs cool for a few minutes."
            ]
        },

        "eggplant_mushrooms": {
            "name": "Eggplant Stuffed with Mushrooms",
            "prep": "20 minutes",
            "cook": "30 minutes",
            "yields": "5 Servings",
            "ingredients": [
                "1 kg not too big, long, even eggplants",
                "500 g mushrooms",
                "1 small onion",
                "1 small carrot",
                "2-3 cloves of garlic",
                "2 fleshy tomatoes",
                "Salt (to taste)",
                "Pepper (to taste)",
                "50 ml oil",
                "Chopped dill and parsley (to taste)",
                "50 ml white wine (optional)"
            ],
            "steps": [
                "Wash the eggplants, wipe them, and cut them lengthwise in half. Partially scoop out the core with a spoon.",
                "Sprinkle the inside of the eggplants with a little salt and place them on a napkin, hollow side down, to drain the bitter juice.",
                "In a pan, heat half of the oil, then add the onion, mushrooms, and diced eggplant. If the mushrooms are small, they can be cut into slices. Add the grated or diced carrot, as desired.",
                "Add 1 teaspoon of grated salt, mix everything, and cover with a lid. The salt will make the mushrooms release water, allowing everything to steam rather than fry.",
                "Mix occasionally, ensuring the heat is moderate to prevent burning.",
                "Once the water is gone, add pepper and crushed garlic, diced tomatoes, and wine (if using), then mix. Cook for another 10 minutes, stirring often.",
                "Turn off the heat and add ¾ of the chopped greens, mixing well.",
                "Fill the eggplants with the mushroom mixture, then place them in a baking pan.",
                "Drizzle the stuffed eggplants with the remaining oil, cover the pan with a lid, and bake at 220°C.",
                "After 20 minutes, remove the lid and allow them to brown a little more."
            ]
        },

        "spinach_rice": {
            "name": "Spinach with Rice",
            "prep": "20 minutes",
            "cook": "20 minutes",
            "yields": "6 Servings",
            "ingredients": [
                "600-700 g spinach, cleaned of tails (or 1 kg with tails)",
                "1 bunch of green onion (or 1 dry onion)",
                "1 clove of green garlic (or 1 clove of dry garlic)",
                "100 g long-grain rice",
                "3-4 tablespoons oil",
                "300 g fresh tomatoes (or 3-4 tablespoons tomato juice)",
                "1 bunch of dill",
                "1 bunch of parsley",
                "2-3 slices of lemon",
                "Salt (to taste)",
                "Pepper (to taste)"
            ],
            "steps": [
                "Boil 2-3 liters of water with a little salt. When the water boils, add the cleaned spinach.",
                "Let the water boil briefly, then immediately remove the spinach with a sieve and allow it to cool. Once cooled, chop it with a knife into larger pieces. (If using frozen spinach, just boil briefly and add them as they are.)",
                "In a saucepan, heat the oil and add the finely chopped onion and garlic. If using green onion and garlic, they will cook quickly. If using dry onion, let it soften well.",
                "Do not fry the vegetables; let them soften for only 2-3 minutes, then add a little of the water used to boil the spinach. We want to steam, not fry the onion.",
                "Add the tomatoes, washed rice, spinach, and half of the dill and parsley.",
                "Pour in the water used to boil the spinach, using four times the amount of rice (like pilaf).",
                "Add salt and pepper, stir, and place the lemon slices on top. Cover with a lid and let everything simmer on low heat for 10 minutes.",
                "After 10 minutes, turn off the heat without mixing. Sprinkle the remaining dill and parsley on top, cover again, and leave on the stove.",
                "During this time, the rice will swell and remain fluffy, with each grain separate."
            ]
        },

         "stuffed_tomatoes_rice": {
            "name": "Tomatoes Stuffed with Potatoes and Rice in the Oven",
            "prep": "20 minutes",
            "cook": "60 minutes",
            "yields": "10 Servings",
            "ingredients": [
                "10 tomatoes",
                "10 tablespoons rice",
                "700 g potatoes",
                "Basil leaves (to taste)",
                "Oregano (to taste)",
                "Extra virgin olive oil (to taste)",
                "Salt (to taste)",
                "Pepper (to taste)",
                "Parsley for decoration"
            ],
            "steps": [
                "Wash the tomatoes well, then cut the tops off to create lids.",
                "Scoop out the insides of each tomato with a teaspoon, then place the tomato pulp in a food processor with 5-6 basil leaves, the cleaned and washed garlic clove, salt, pepper to taste, and 2 tablespoons of olive oil.",
                "Allow the tomatoes to drain with the hollow side down.",
                "Put the washed rice in a bowl and pour the mixed tomato juice over it. Cover with plastic wrap and refrigerate for about an hour.",
                "Meanwhile, wash and peel the potatoes, cutting them into thicker slices or cubes. Wash them again, pat them dry with kitchen paper to absorb all the water, then sprinkle with a pinch of salt, oregano, and 2 tablespoons of oil. Mix and set aside.",
                "After about an hour, remove the rice mixture, which should have absorbed the tomato juice, and fill each tomato with the mixture.",
                "Cover the stuffed tomatoes with their lids and place them in a baking pan lined with baking paper. Arrange the potatoes between the tomatoes.",
                "Place the tray in a preheated oven at 200°C for about an hour."
            ]
        },

        "tvp_meatballs": {
            "name": "TVP Meatballs",
            "prep": "15 minutes",
            "cook": "15 minutes",
            "yields": "8 Servings",
            "ingredients": [
                "1 cup textured vegetable protein (TVP)",
                "1 cup vegetable broth",
                "1 medium sweet onion, diced",
                "1 teaspoon garlic powder",
                "1 ½ teaspoon Italian seasoning",
                "1 teaspoon dried parsley, roughly chopped (about 3-4 big leaves or 6-8 smaller ones)",
                "1 teaspoon smoked paprika",
                "1 tablespoon soy sauce (or alternative)",
                "1 tablespoon nutritional yeast",
                "5 tablespoons panko bread crumbs",
                "2 tablespoons oat flour (or other flours)",
                "Salt (to taste)",
                "Black pepper (to taste)"
            ],
            "steps": [
                "Preheat the oven to 200°C.",
                "In a small saucepan, bring the vegetable stock to a boil. Place the TVP in a bowl and pour the boiling stock over it. Cover and let it sit for 5-10 minutes until fully soaked.",
                "Add all the remaining ingredients to the bowl with the TVP. Using a handheld mixer, mix evenly until the mixture can stick together.",
                "If the mixture is too loose, add extra breadcrumbs one tablespoon at a time to help it bind.",
                "Using a tablespoon scoop out the mixture and shape it into balls.",
                "Bake for about 12-15 minutes until browned.",
                "Alternatively, cook in an air fryer at 200°C for 10-15 minutes.",
                "Or, add a few tablespoons of oil to a skillet over medium heat, then fry for 5-8 minutes, or until all sides are browned."
            ]
        },

        "cheese_and_onion_pasties": {
            "name": "Cheese and Onion Pasties",
            "prep": "10 minutes",
            "cook": "40 minutes",
            "yields": "8 Servings",
            "ingredients": [
                "800 g potatoes, peeled and cut into small cubes",
                "60 g salted butter",
                "4 large onions, peeled and finely chopped",
                "250 g strong cheddar, grated",
                "750 g puff pastry",
                "Salt (to taste)",
                "Freshly ground black pepper (to taste)"
            ],
            "steps": [
                "Boil the potatoes in a large pan of salted water for 15-20 minutes until soft.",
                "While the potatoes are cooking, melt the butter in a small frying pan and gently fry the onions for 5-10 minutes until soft and transparent, avoiding browning.",
                "Preheat the oven to 200°C.",
                "Once the potatoes are cooked, drain them and add the onions (along with any remaining butter), cheese, and plenty of salt and pepper. Mash well and allow to cool.",
                "Roll out the puff pastry and cut it into 8 rectangles.",
                "Share the potato mixture across 4 rectangles. Brush around the edges with beaten egg and place the other 4 rectangles on top as lids.",
                "Seal the edges using a fork and brush the top with the remaining egg.",
                "Place on a baking sheet lined with baking paper or parchment.",
                "Bake for 15-20 minutes until very golden."
            ]
        },

        "pizza_chec": {
            "name": "Appetizer Cake with Olives",
            "prep": "15 minutes",
            "cook": "40 minutes",
            "yields": "10 Servings",
            "ingredients": [
                "200 g sliced olives",
                "200 g grated cheese",
                "200 g meat/sausage (optional)",
                "100 g peas",
                "100 g corn",
                "150 g pickled red peppers (or pimientos de piquillo)",
                "150 g flour",
                "6 eggs",
                "4 tablespoons oil",
                "1 1/2 teaspoons baking powder"
            ],
            "steps": [
                "Put the 6 eggs in a large bowl and beat them with a mixer until they double in volume.",
                "Add the flour little by little, mixing well to incorporate.",
                "Add the baking powder and mix.",
                "Add the oil and all the remaining ingredients to the mixture.",
                "Once everything is well mixed, set the composition aside.",
                "In a long baking tray, spread a little oil in all corners and walls. Then dust with flour to prevent sticking.",
                "Pour the composition into the tray and bake in a preheated oven at 200°C for 30-40 minutes, or until a toothpick comes out clean from the center."
            ]
        },

        "sage_onion_stuffing": {
            "name": "Sage and Onion Stuffing",
            "prep": "10 mins",
            "cook": "45 mins",
            "yields": "12 balls",
            "ingredients": [
                "1 tbsp butter",
                "1 tbsp oil",
                "1 large onion, finely chopped",
                "1 bay leaf",
                "1 garlic clove, crushed",
                "1 1/2 tbsp dried or fresh sage, finely chopped",
                "180 g fresh breadcrumbs",
                "1 large egg, lightly beaten"
            ],
            "steps": [
                "Heat the butter and oil in a frying pan. Fry the onion, bay leaf, and a pinch of salt gently for 15 mins over low heat until the onions are softened and translucent.",
                "Add the garlic and sage, and fry for 1 min. Leave to cool for 10 mins.",
                "Heat the oven to 180°C (160°C fan) or gas mark 4.",
                "Stir the breadcrumbs and beaten egg through the onion mixture. Season to taste.",
                "Divide into 12 balls, weighing for accuracy, if you like.",
                "Bake on a flat baking sheet lined with parchment for 25-30 mins or until golden brown. Serve as part of a roast dinner."
            ]
        },

        "sweet_potatoes_garlic": {
            "name": "Sweet Potatoes with Garlic and Thyme",
            "prep": "15 mins",
            "cook": "30 mins",
            "yields": "10+ Servings",
            "ingredients": [
                "2 sweet potatoes",
                "3-4 tablespoons olive oil",
                "1/2 teaspoon garlic powder",
                "1 teaspoon thyme",
                "Salt and pepper to taste"
            ],
            "steps": [
                "Peel the potatoes and cut them into one-centimeter-thick slices.",
                "In a bowl, mix the olive oil, garlic powder, thyme, salt, and pepper to taste.",
                "Toss the potato rings in this mixture until all slices are well seasoned.",
                "Place the potato slices on a pan lined with baking paper and bake at 180°C for about 25-30 minutes.",
                "Serve the potatoes warm. You can also prepare a sauce or serve them as a side dish with a steak."
            ]
        },

        "leek_onion_bechamel": {
            "name": "Leek and Onion Bechamel Sauce",
            "prep": "15 mins",
            "cook": "30 mins",
            "yields": "6 Servings",
            "ingredients": [
                "1/2 litre unsweetened soy milk",
                "5 tablespoons butter",
                "3 tablespoons flour",
                "Pinch of nutmeg",
                "Salt to taste",
                "Pepper to taste",
                "Pinch of turmeric",
                "3 leeks, chopped",
                "1 large onion, chopped",
                "3 tablespoons olive oil",
                "6 tablespoons nutritional yeast"
            ],
            "steps": [
                "Cut the onion and leek into small pieces.",
                "Fry the onion and leek in a pan with olive oil until soft.",
                "Melt the butter in a large saucepan over medium heat. Add the flour and mix with the butter until smooth. Cook until the mixture turns light golden, about 7 minutes.",
                "Increase the heat to medium-high and gradually stir in the soy milk until the mixture thickens. Bring to a gentle boil, then reduce to medium-low and simmer for 10-20 minutes, until the flour flavor disappears.",
                "Season with salt, pepper, nutmeg, and turmeric.",
                "Add the nutritional yeast and the fried leek and onion mixture. Stir to combine while heating.",
                "Optionally, add your preferred protein to the sauce."
            ]
        },

        "fideo_con_garbanzos": {
            "name": "Quick Garbanzos and Fideos Soup",
            "prep": "5 mins",
            "cook": "20 mins",
            "yields": "4 Servings",
            "ingredients": [
                "2 tablespoons vegetable oil",
                "Fideos (amount as preferred)",
                "1 teaspoon salt",
                "1 teaspoon pepper",
                "1 small carrot, diced (optional)",
                "1/2 small onion, sliced",
                "1/2 teaspoon garlic salt",
                "2 cups chicken broth or vegetable broth",
                "1 can garbanzo beans, drained and rinsed"
            ],
            "steps": [
                "Heat oil in a saucepan over medium-high heat.",
                "Add the fideos and fry until browned, stirring occasionally.",
                "Add diced carrots, onion, salt, pepper, and garlic salt. Cook for an additional minute while stirring.",
                "Stir in the chicken or vegetable broth. Bring to a boil, then reduce heat to a simmer. Cook for 15 minutes, or until the fideo is tender.",
                "Add garbanzo beans and continue simmering for about 2 minutes, until the beans are heated through.",
                "Remove from heat, taste, and adjust seasoning with additional salt and pepper if needed.",
                "Serve warm."
            ]
        },

        "mancarica_cartofi": {
            "name": "Peas with Potatoes",
            "prep": "15 mins",
            "cook": "40 mins",
            "yields": "6 Servings",
            "ingredients": [
                "1 kg peas",
                "2 dried onions, chopped",
                "2 bell peppers, chopped",
                "1 carrot, halved and sliced",
                "2-3 potatoes, cubed",
                "1-2 broth cubes",
                "100 ml oil",
                "400 ml tomato juice",
                "Salt, to taste",
                "Pepper, to taste",
                "Paprika, to taste"
            ],
            "steps": [
                "Heat oil in a pot over medium heat and cook the chopped onions until they become glassy.",
                "Add the chopped bell peppers and cook for another 1-2 minutes.",
                "Add the carrot, peas, and cubed potatoes. Pour enough water to cover the vegetables.",
                "Add the broth cubes, salt, pepper, and paprika to taste.",
                "Once the water boils, reduce the heat to low and simmer for at least 30 minutes.",
                "After half an hour, add the tomato juice and cook for another 10 minutes.",
                "Taste and adjust seasoning. If the dish is too soupy, mash some of the potatoes to thicken the sauce."
            ]
        },

        "apple_yogurt": {
            "name": "Apple Yogurt Salad",
            "prep": "15 mins",
            "cook": "0 mins",
            "yields": "2-4 Servings",
            "ingredients": [
                "1 medium apple, diced",
                "½ cucumber, cubed",
                "2 cloves garlic, minced",
                "1 tbsp apple cider vinegar",
                "1 large carrot, grated",
                "5 tbsp Greek yogurt",
                "2 tbsp yellow mustard",
                "2 tbsp honey",
                "1 tbsp extra virgin olive oil",
                "Salt, to taste",
                "Pepper, to taste"
            ],
            "steps": [
                "Score the washed cucumber with a fork, cut into small cubes, and add salt generously. Refrigerate for at least 1 hour to allow the cucumber to release water.",
                "Dice the apple and grate the carrot.",
                "After an hour, discard the cucumber water and add the cucumber to the apple and carrot.",
                "In a bowl, mix the Greek yogurt, mustard, honey, olive oil, garlic, vinegar, salt, and pepper to make the dressing.",
                "Pour the dressing over the salad and toss well."
            ]
        },

        "grape_walnut": {
            "name": "Grape and Walnut Salad",
            "prep": "10 mins",
            "cook": "0 mins",
            "yields": "2-4 Servings",
            "ingredients": [
                "Mixed salad leaves",
                "Handful of grapes, halved",
                "Handful of walnuts, toasted and crushed (or substitute with cashews)",
                "3 tbsp extra virgin olive oil",
                "2 tbsp Modena vinegar",
                "1 tbsp honey",
                "1 tsp dried oregano",
                "Salt, to taste",
                "Pepper, to taste"
            ],
            "steps": [
                "Halve the grapes and set aside.",
                "Toast the walnuts in a pan or air fryer for 5 minutes, then crush them into medium-sized pieces.",
                "In a large bowl, combine the halved grapes, toasted walnuts, and mixed salad leaves.",
                "In a separate bowl, whisk together the olive oil, Modena vinegar, honey, oregano, salt, and pepper to create the dressing.",
                "Pour the dressing over the salad and toss well to combine."
            ]
        },

        "asian_cucumber": {
            "name": "Asian Cucumber Salad",
            "prep": "15 mins + 1h Rest",
            "cook": "0 mins",
            "yields": "2-4 Servings",
            "ingredients": [
                "1 large cucumber",
                "2 medium carrots, grated",
                "¼ cabbage, grated",
                "1 tbsp rice vinegar",
                "2 tbsp toasted sesame oil",
                "2 tbsp soy sauce",
                "1 tbsp agave syrup or honey",
                "1 tsp grated ginger",
                "Sesame seeds",
                "Salt, to taste"
            ],
            "steps": [
                "Score the washed cucumber with a fork, cut into preferred size, and generously salt. Let it rest in the fridge for at least 1 hour to release water.",
                "Grate the carrots and cabbage while the cucumber rests.",
                "Once the cucumber has released its water, discard the excess water and combine the cucumber with the carrots and cabbage in a large bowl.",
                "In a separate bowl, mix the rice vinegar, sesame oil, soy sauce, agave syrup (or honey), and ginger to create the dressing.",
                "Pour the dressing over the veggies and toss to coat evenly.",
                "Sprinkle with sesame seeds before serving."
            ]
        },

        "veggies_feta": {
            "name": "Baked Veggies with Feta Cheese",
            "prep": "15 mins",
            "cook": "30-45 mins",
            "yields": "4 servings",
            "ingredients": [
                "2 medium potatoes, cubed",
                "2 medium beetroots, cubed",
                "2 medium carrots, sliced (¼ inch thick)",
                "2 medium onions, cut into eighths",
                "½ small butternut squash, cubed",
                "5 garlic cloves, peeled",
                "Fresh or dried rosemary and thyme",
                "Extra virgin olive oil",
                "400 g feta cheese, crumbled into large chunks",
                "Salt and pepper, to taste"
            ],
            "steps": [
                "Preheat the oven to 180°C.",
                "Cut the potatoes, beetroot, and butternut squash into cubes. Slice the carrots and onions.",
                "Toss the veggies and garlic with olive oil, rosemary, thyme, salt, and pepper in a large bowl.",
                "Spread the veggies in a single layer on a baking tray.",
                "Crumble the feta cheese in large chunks over the top.",
                "Bake for 30-45 minutes, until the potatoes are tender and the veggies are lightly caramelized.",
                "Serve warm."
            ]
        },

        "ensaladilla_rusa": {
            "name": "Ensaladilla Rusa",
            "prep": "15 mins",
            "cook": "20 mins",
            "yields": "4 servings",
            "ingredients": [
                "3 large carrots, cut into ½ inch cubes",
                "2 medium potatoes, cut into ½ inch cubes",
                "1 cup peas",
                "1 cup green beans",
                "1/3 can black olives, halved",
                "3 whole pickled red peppers, cut into strips",
                "Lettuce leaves, for serving",
                "Mayonnaise, to taste",
                "Salt and pepper, to taste"
            ],
            "steps": [
                "Boil the carrots, potatoes, peas, and green beans in salted water until tender, about 10-15 minutes.",
                "While the veggies are cooling, cut the olives in half and slice the pickled peppers into strips.",
                "Once the boiled vegetables are cool, combine them with the olives, peppers, and chopped lettuce in a large bowl.",
                "Dress with mayonnaise and season with salt and pepper to taste.",
                "Mix well and serve chilled or at room temperature."
            ]
        },

        "tomato_avocado": {
            "name": "Tomato and Avocado Salad",
            "prep": "10 mins",
            "cook": "0 mins",
            "yields": "2-4 servings",
            "ingredients": [
                "1 large tomato or 2 medium tomatoes, cut into inch-wide pieces",
                "1 avocado, cut into inch-wide pieces",
                "3 whole pickled red peppers, cut into strips",
                "1 small onion (sweet or purple), thinly sliced",
                "Extra virgin olive oil, to taste",
                "Apple cider vinegar (optional), to taste",
                "Salt, to taste"
            ],
            "steps": [
                "Cut the tomatoes and avocado into inch-wide pieces.",
                "Cut the pickled peppers into stripes and slice the onion thinly.",
                "In a large bowl, toss the tomatoes, avocado, peppers, and onion generously with olive oil.",
                "Sprinkle with salt and mix well.",
                "Add apple cider vinegar if desired, and toss again before serving."
            ]
        },

        "lentil_salad": {
            "name": "Cold Lentil Salad",
            "prep": "10 mins",
            "cook": "30 mins",
            "yields": "2-4 servings",
            "ingredients": [
                "½ cup dry brown lentils (or 1 cup cooked)",
                "1 medium yellow onion, diced",
                "1 red bell pepper, diced",
                "1 green bell pepper, diced",
                "½ cucumber, diced",
                "1 large tomato, diced",
                "Extra virgin olive oil, to taste",
                "Juice of 2 lemons",
                "A bunch of fresh parsley, chopped",
                "Salt and pepper, to taste"
            ],
            "steps": [
                "If using dry lentils, cook them according to package instructions and allow to cool.",
                "Dice the onion, cucumber, red and green peppers, and tomato into small pieces.",
                "Chop the fresh parsley.",
                "In a large bowl, combine the cooked lentils, diced vegetables, and parsley.",
                "Dress the salad with lemon juice and olive oil, and mix well.",
                "Season with salt and pepper to taste before serving."
            ]
        },

        "radish_rocket": {
            "name": "Radish and Rocket Salad",
            "prep": "5 mins",
            "cook": "0 mins",
            "yields": "2 servings",
            "ingredients": [
                "5 small radishes, cut into fourths",
                "A handful of rocket leaves",
                "100 g feta cheese, crumbled",
                "Extra virgin olive oil, to taste"
            ],
            "steps": [
                "Cut the radishes into fourths.",
                "In a bowl, combine the radishes with the rocket leaves.",
                "Crumble feta cheese on top.",
                "Drizzle with extra virgin olive oil and toss gently to combine."
            ]
        },

        "tortellini_salad": {
            "name": "Tortellini Salad",
            "prep": "15 mins",
            "cook": "10 mins",
            "yields": "6 servings",
            "ingredients": [
                "18 ounces cheese tortellini or vegan tortellini",
                "Italian dressing (to taste)",
                "2 cups halved cherry tomatoes",
                "1 (14-ounce) can artichoke hearts, drained and chopped",
                "1 cup cooked white beans, drained and rinsed",
                "½ cup thinly sliced red onion",
                "5 pepperoncini, stemmed and chopped",
                "2 cups fresh arugula",
                "1 cup fresh basil, torn, plus more for garnish",
                "Parmesan or pecorino cheese, optional",
                "Red pepper flakes, optional"
            ],
            "steps": [
                "Cook the tortellini according to the package directions until al dente. Drain and let cool.",
                "Prepare the dressing according to the instructions in the recipe.",
                "In a large bowl, combine the cooled tortellini, cherry tomatoes, artichokes, white beans, red onion, and pepperoncini.",
                "Add half of the dressing and toss to combine.",
                "Add the arugula and torn basil, then toss again.",
                "Season to taste with salt and pepper, and add Parmesan, red pepper flakes, and more dressing if desired.",
                "Garnish with additional fresh basil and serve right away or store in the fridge for up to 4 days."
            ]
        },

        "banana_bread": {
            "name": "Banana Bread",
            "prep": "20 mins",
            "cook": "60 mins",
            "yields": "1 loaf (about 10 servings)",
            "ingredients": [
                "3 very ripe bananas (medium/large)",
                "½ cup unsalted butter (8 Tbsp) at room temperature",
                "¾ cup granulated sugar",
                "2 large eggs, lightly beaten",
                "1½ cups all-purpose flour",
                "1 tsp baking soda",
                "½ tsp salt",
                "½ tsp vanilla extract",
                "1 cup walnuts, coarsely chopped",
                "½ cup raisins (optional)"
            ],
            "steps": [
                "Preheat the oven to 180°C. Grease and flour a bread loaf pan.",
                "In a skillet, lightly roast the walnuts while continuously stirring to prevent burning. Coarsely chop and let them cool to room temperature.",
                "In a mixing bowl, cream together the softened butter and granulated sugar (or honey if using).",
                "Mash the bananas with a fork until they have a chunky applesauce consistency and add them to the butter mixture along with the lightly beaten eggs. Mix until well blended.",
                "In a separate bowl, whisk together the flour, baking soda, and salt. Gradually add this dry mixture to the batter.",
                "Add the vanilla extract and mix in the chopped walnuts and raisins (if using).",
                "Pour the batter into the prepared loaf pan and bake in the preheated oven for 45-60 minutes, or until a toothpick inserted into the center comes out clean.",
                "Let the banana bread rest for 10 minutes in the pan before transferring it to a wire rack to cool completely."
            ]
        },

        "pretzels": {
            "name": "Pretzels in Syrup",
            "prep": "30 mins",
            "cook": "40 mins",
            "yields": "Approximately 15 pretzels",
            "ingredients": [
                "600 g flour",
                "3 eggs",
                "10 g dry yeast",
                "50 g powdered sugar",
                "a little salt",
                "50 g melted butter",
                "1 tablespoon vanilla essence",
                "100 g soft butter",
                "250 ml milk",
                "200 g sugar",
                "300 ml water",
                "100 g honey",
                "2 tablespoons vanilla essence",
                "50 g coconut"
            ],
            "steps": [
                "In a bowl, combine flour, dry yeast, salt, powdered sugar, eggs, melted butter, milk, and vanilla essence.",
                "Mix all the ingredients and knead until the dough is no longer sticky, using either your hands or a mixer.",
                "Place the dough in a bowl coated with a little oil, cover it, and let it rise in a warm place until it doubles in size.",
                "In a pot, combine water, sugar, honey, and vanilla essence to make the syrup.",
                "Boil the mixture for 5 minutes to dissolve the sugar and honey. Set it aside to cool.",
                "Once the dough has risen, roll it out and spread soft butter over the surface. Fold the dough and refrigerate it for half an hour.",
                "After chilling, roll out the dough again and cut it into 3 cm wide strips, then cut each strip in half without cutting all the way through.",
                "Braid the two pieces, roll them slightly, and form them into pretzel shapes.",
                "Repeat the braiding and shaping process until all the dough is used.",
                "Preheat the oven to 180°C and bake the pretzels for 20 minutes until golden.",
                "While the pretzels are still warm, dip them in the cooled syrup for no more than 1 minute.",
                "Sprinkle the pretzels with coconut, and they are ready to eat!"
            ]
        },

        "negreasa": {
            "name": "Chocolate Glazed Negreasa",
            "prep": "15 mins",
            "cook": "50 mins",
            "yields": "Approximately 10 servings",
            "ingredients": [
                "250 ml milk",
                "250 g flour",
                "200 g brown sugar",
                "100 g melted butter",
                "50 g cocoa",
                "5 g baking powder",
                "3 eggs",
                "1 teaspoon vanilla essence",
                "a little salt",
                "200 g milk chocolate",
                "100 ml sweet cream",
                "50 g dark chocolate"
            ],
            "steps": [
                "In a large bowl, mix the dry ingredients: flour, brown sugar, cocoa, salt, and baking powder until well combined.",
                "In a separate bowl, whisk together the wet ingredients: milk, eggs, and melted butter until smooth.",
                "Gradually combine the dry and wet mixtures, stirring until fully incorporated.",
                "Line a baking tray with parchment paper and pour the batter into the tray, leveling it out evenly.",
                "Preheat the oven to 150°C and bake for 40-50 minutes or until a toothpick inserted into the center comes out clean.",
                "To prepare the glaze, place a bowl over a pot of simmering water and add the chocolate and cream.",
                "Gently melt the chocolate while stirring continuously until smooth. Set aside to cool slightly.",
                "Once the cake is done, remove it from the oven and allow it to cool completely.",
                "Pour the cooled glaze over the cake, spreading it evenly. Refrigerate the cake until the glaze is set."
            ]
        },


        "chocolate_mug_cake": {
            "name": "Chocolate Mug Cake",
            "prep": "5 mins",
            "cook": "1.5 mins",
            "yields": "1 serving",
            "ingredients": [
                "6 Tbsp all-purpose flour",
                "4 Tbsp granulated sugar",
                "2 Tbsp unsweetened cocoa powder",
                "0.5 tsp baking powder",
                "dash of salt",
                "6 Tbsp milk (any kind of milk)",
                "2 Tbsp canola oil (or melted butter)",
                "0.25 tsp vanilla extract",
                "2 tsp chocolate chips (or any type of chocolate you like)"
            ],
            "steps": [
                "In a microwave-safe mug, combine the flour, sugar, cocoa powder, baking powder, and salt. Stir together until well mixed.",
                "Add the milk, canola oil (or melted butter), and vanilla extract. Mix until smooth, making sure to scrape the bottom of the mug to incorporate all ingredients.",
                "Stir in the chocolate chips or sprinkle them on top of the batter.",
                "Microwave the mug on high for 70-90 seconds, until the cake is just set but still slightly shiny on top.",
                "Allow the mug cake to rest in the microwave for 1 minute before consuming. Enjoy!"
            ]
        },

        "cookies": {
            "name": "Peanut Butter Cookies",
            "prep": "20 mins",
            "cook": "8 mins per cookie",
            "yields": "Approximately 24 cookies",
            "ingredients": [
                "1 1/2 cup (180g) all-purpose flour",
                "1/2 cup (113g) unsalted butter, room temperature",
                "1 cup (250g) peanut butter",
                "1/2 cup (100g) brown sugar, lightly packed",
                "1/2 cup (100g) granulated sugar",
                "1 tsp (5mL) vanilla extract",
                "1 large egg, room temperature",
                "3/4 tsp (3g) baking powder",
                "optional: 1/4-1/2 tsp sea salt"
            ],
            "steps": [
                "Preheat the oven to 180°C.",
                "Sift the flour and baking powder together, then whisk to combine.",
                "In a stand mixer fitted with a paddle attachment, cream the butter and sugars together until light and fluffy. (Alternatively, do this by hand.) You can add an optional 1/4-1/2 tsp of sea salt at this stage.",
                "Add the peanut butter and mix until well incorporated.",
                "Mix in the egg and vanilla extract, then add the flour mixture and beat until fully incorporated.",
                "Roll the dough into 1-inch balls and place them on a baking sheet lined with parchment paper.",
                "Flatten each cookie with a fork in a criss-cross pattern.",
                "Optional: Add chocolate bits on top of the cookies for extra flavor.",
                "Bake the cookies for about 8 minutes.",
                "Allow the cookies to cool completely on the baking sheet; they need to set up before being transferred to a wire rack."
            ]
        },

        "honey_parsnips": {
            "name": "Honey-roasted Parsnips",
            "prep": "10 mins",
            "cook": "40 mins",
            "yields": "5 servings",
            "ingredients": [
                "500g parsnips",
                "1 tbsp flour",
                "1 tbsp honey",
                "2 tbsp sunflower oil",
                "2 tbsp butter",
                "Salt to taste",
                "Pepper to taste (optional)"
            ],
            "steps": [
                "Preheat the oven to 190°C.",
                "Top and tail the parsnips, cutting any larger ones in half lengthways.",
                "Place the parsnips in a large saucepan, cover with salted water, and bring to a boil. Cook for 5 minutes.",
                "Drain the parsnips in a colander and let them steam-dry for a few minutes.",
                "Sprinkle the flour and honey over the parsnips and toss to coat.",
                "Place the parsnips in a roasting tin with sunflower oil, butter, and seasoning.",
                "Roast the parsnips for 40 minutes, turning them halfway through cooking, until golden."
            ]
        },

        "zucchini_oregano": {
            "name": "Baked Zucchini with Oil and Oregano",
            "prep": "10 mins",
            "cook": "45-50 mins",
            "yields": "6 servings",
            "ingredients": [
                "3 zucchini (or as many as fit in the baking pan)",
                "Olive oil, for greasing and brushing",
                "Salt, to taste",
                "Pepper, to taste",
                "Oregano, to taste"
            ],
            "steps": [
                "Preheat the oven to 180°C.",
                "Wash the zucchini, dry them with a napkin, cut off the ends, and slice them into 1 cm thick rounds.",
                "Season the zucchini slices with salt and pepper.",
                "Line a baking tray with parchment paper and grease it with olive oil.",
                "Arrange the zucchini slices on the tray and brush the tops with more olive oil.",
                "Sprinkle oregano evenly over the zucchini.",
                "Bake for 45-50 minutes, until the zucchini softens and browns on top."
            ]
        },

        "tofu_peach": {
            "name": "Grilled Sesame Peach Tofu",
            "prep": "30 mins (longer if making peach preserves)",
            "cook": "15-25 mins for peach preserves, 10 mins for grilling",
            "yields": "6 servings",
            "ingredients": [
                "1 block super firm tofu, cut into strips",
                "3-4 cloves garlic, minced",
                "3 tbsp rice wine vinegar",
                "2 tbsp soy sauce",
                "1 ½ tsp sesame seeds, more for garnish",
                "½ tsp onion powder",
                "½ tsp smoked paprika",
                "½ tsp cumin",
                "½ tsp cinnamon",
                "2 tbsp avocado oil (or another high heat oil)",
                "Wooden skewers, for grilling",
                "Omit the next part if using jarred peach preserves",
                "1 lb fresh peaches, peeled and pitted, cut into cubes",
                "1 lemon, juiced",
                "1 ½ cups cane sugar (add more if desired)"
                ],
            "steps": [
                "In a medium saucepan over medium-high heat, add peaches and lemon juice. Stir to combine. (omit this step if using jarred peach preserves)",
                "Bring the mixture to a boil, then mash the peaches to your desired consistency with a spatula or masher. (omit this step if using jarred peach preserves)",
                "Reduce heat to medium and add sugar, stirring frequently. Allow the mixture to boil until it coats the back of a spoon (about 15-25 minutes). (omit this step if using jarred peach preserves)",
                "Remove from heat and let it cool. Set aside ½ cup for the sauce (omit this step if using jarred peach preserves)."
                "Preheat the grill to medium-medium high heat (170-180°C).",
                "In a small bowl, whisk together ½ cup peach preserves, minced garlic, rice vinegar, soy sauce, sesame seeds, onion powder, smoked paprika, cumin, and cinnamon.",
                "Thread each strip of tofu onto a wooden skewer. Lightly brush or spray the tofu with avocado oil.",
                "Place the tofu skewers on the grill and grill each side for 1-2 minutes, flipping until all four sides are done.",
                "Once back to the original side, brush on the peach sauce and rotate every 30 seconds, continuing to brush on the sauce.",
                "Remove from heat and serve with extra sauce on the side, garnishing with more sesame seeds if desired."
            ]
        },

        "mamaliga": {
            "name": "Mamaliga",
            "prep": "5 mins",
            "cook": "15 mins",
            "yields": "Servings depending on water-to-malay ratio",
            "ingredients": [
                "Malay (cornmeal)",
                "Water (1 cup per person)",
                "1 teaspoon salt",
                "Butter or margarine (1 spoonful)"
            ],
            "steps": [
                "In a pot, add 1 cup of water per person, ensuring there's enough for everyone, and a handful of malay (cornmeal).",
                "Add 1 teaspoon of salt to the water and bring it to a boil over high heat.",
                "Once the water boils, reduce the heat to low and slowly start adding the malay while constantly stirring.",
                "Keep stirring until the mixture reaches the desired consistency, whether you prefer a thicker or thinner texture.",
                "Once the mamaliga reaches the right texture, add a spoonful of butter or margarine and mix well until fully incorporated."
            ]
        }
    }
}

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")


# Route to get a random recipe
@app.route('/randomRecipe')
def randomRecipe():
    allRecipes = []
    for category in data:
        allRecipes.extend(data[category])

    randomRecipe = random.choice(allRecipes)

    return jsonify({"recipe_id": randomRecipe['id']})

# Dynamic route for categories
@app.route("/mainDish")
def mainDish():
    return render_template("mainDish.html", recipes=data["mainDish"])

@app.route("/mainDishPage2")
def mainDishPage2():
    return render_template("mainDishPage2.html", recipes=data["mainDishPage2"])

@app.route("/appetizer")
def appetizer():
    return render_template("appetizer.html", recipes=data["appetizer"])

@app.route("/soup")
def soup():
    return render_template("soup.html", recipes=data["soup"])

@app.route("/salad")
def salad():
    return render_template("salad.html", recipes=data["salad"])

@app.route("/saladPage2")
def saladPage2():
    return render_template("saladPage2.html", recipes=data["saladPage2"])

@app.route("/dessert")
def dessert():
    return render_template("dessert.html", recipes=data["dessert"])

@app.route("/snack")
def snack():
    return render_template("snack.html", recipes=data["snack"])

@app.route("/recipes/<recipe_id>")
def recipe_details(recipe_id):
    recipe = data['details'].get(recipe_id)
    if recipe is None:
        abort(404)
    return render_template("recipes/recipeDetail.html", recipe=recipe)


