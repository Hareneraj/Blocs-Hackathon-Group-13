from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary data storage for recipes
recipes = [
    {
        "id": 1,
        "title": "Blackforest Cake",
        "category": "Cakes",
        "image": "images/blackforest_cake.jpg",
        "description": "A delicious chocolate and cherry delight.",
        "ingredients": ["Flour", "Sugar", "Cocoa", "Cherries", "Cream"],
        "instructions": "Bake the cake layers and layer with cream and cherries."
    },
    {
        "id": 2,
        "title": "Chocolate Orange Baked Cheesecake",
        "category": "Cakes",
        "image": "images/choclate_orange_bakes_cheesecake.jpeg",
        "description": "A creamy baked cheesecake with a hint of orange and rich chocolate topping.",
        "ingredients": ["200g cream cheese", "150g sugar", "3 eggs", "Zest of 1 orange", "100g dark chocolate"],
        "instructions": "1. Preheat the oven to 170°C. Grease a springform pan.<br> 2. Mix cream cheese, sugar, and orange zest. Add eggs one at a time.<br> 3. Pour into the pan and bake for 40 minutes.<br> 4. Melt chocolate and drizzle on top after cooling."
    },
    {
        "id": 3,
        "title": "Sticky Toffee Pudding",
        "category": "Cakes",
        "image": "images/sticky_toffee_pudding.jpeg",
        "description": "A moist sponge dessert with finely chopped dates and a rich toffee sauce.",
        "ingredients": ["Flour", "Sugar", "Eggs", "Butter", "Dates", "Baking Soda", "Toffee Sauce"],
        "instructions": "1. Mix the ingredients and bake the sponge.<br> 2. Prepare the toffee sauce.<br> 3. Pour over the cake and serve."
    },
    {
        "id": 4,
        "title": "Gingerbread Cookies",
        "category": "Cookies",
        "image": "images/gingerbread.jpeg",
        "description": "Classic Christmas gingerbread cookies.",
        "ingredients": ["Flour", "Ginger", "Sugar", "Butter", "Molasses"],
        "instructions": "Mix, roll, cut shapes, and bake."
    },
    {
        "id": 5,
        "title": "Raspberry Cheesecake",
        "category": "Cakes",
        "image": "images/raspberry_cheesecake.jpeg",
        "description": "A rich and creamy cheesecake topped with fresh raspberries.",
        "ingredients": ["Cream cheese", "Sugar", "Eggs", "Raspberries", "Graham crackers"],
        "instructions": "Prepare the crust, mix the filling, bake, and top with fresh raspberries."
    },
    {
        "id": 6,
        "title": "Minced Pie",
        "category": "Cakes",
        "image": "images/Minced_Pie.jpeg",
        "description": "A sweet pie filled with mincemeat, perfect for the holidays.",
        "ingredients": ["Mincemeat", "Butter", "Sugar", "Flour", "Egg"],
        "instructions": "Prepare the crust, fill with mincemeat, bake until golden brown."
    },
    {
        "id": 7,
        "title": "Turkey With Stuffing",
        "category": "Meals",
        "image": "images/Turkey_With_Stuffing.jpeg",
        "description": "A classic holiday turkey with delicious stuffing.",
        "ingredients": ["Whole turkey", "Breadcrumbs", "Onions", "Celery", "Sage", "Butter"],
        "instructions": "Stuff the turkey with the prepared stuffing, roast until golden and cooked through."
    },
    {
        "id": 8,
        "title": "Roast Potatoes",
        "category": "Meals",
        "image": "images/Roast Potatoes.jpeg",
        "description": "Crispy golden roast potatoes, the perfect side dish.",
        "ingredients": ["Potatoes", "Olive oil", "Garlic", "Rosemary", "Salt"],
        "instructions": "Peel and chop potatoes, season, and roast in a hot oven until crispy."
    },
    {
        "id": 9,
        "title": "EggNog",
        "category": "Drinks",
        "image": "images/EggNog.jpeg",
        "description": "A creamy, spiced holiday drink made with eggs, milk, and nutmeg.",
        "ingredients": ["Eggs", "Sugar", "Milk", "Nutmeg", "Vanilla extract", "Rum (optional)"],
        "instructions": "Whisk eggs and sugar, add milk, and heat gently. Stir in nutmeg and vanilla, then chill."
    }
]

# Route: Homepage (this will display the homepage first)
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/reviews")
def reviews_page():
    return render_template("reviewspage.html")


# Route: Homepage displaying recipes (main.html page)
@app.route("/recipes")
def recipes_page():
    categories = {
        "Cakes": [],
        "Cookies": [],
        "Meals": [],
        "Drinks": [],
    }

    for recipe in recipes:
        categories[recipe['category']].append(recipe)

    return render_template("main.html", categories=categories)

# Route: Add a New Recipe
@app.route("/add", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        title = request.form["title"]
        category = request.form["category"]
        image = request.form["image"]  # Ensure this is the correct path
        description = request.form["description"]
        ingredients = request.form["ingredients"].split(",")  # Expecting comma-separated ingredients
        instructions = request.form["instructions"]

        # Add new recipe
        new_recipe = {
            "id": len(recipes) + 1,
            "title": title,
            "category": category,
            "image": image,  # Ensure this path works correctly in your static folder
            "description": description,
            "ingredients": ingredients,
            "instructions": instructions,
        }
        recipes.append(new_recipe)
        return redirect(url_for("recipes_page"))
    
    return render_template("add_recipe.html")

# Route: Recipe Details
@app.route("/recipe/<int:recipe_id>")
def recipe_details(recipe_id):
    recipe = next((r for r in recipes if r["id"] == recipe_id), None)
    if not recipe:
        return "Recipe not found!", 404
    return render_template("recipe_details.html", recipe=recipe)

if __name__ == "__main__":
    app.run(debug=True)