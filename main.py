# Imports the 'requests' library for making HTTP requests
import requests

# Function to get recipes from Edamam API based on ingredient
def get_recipes(ingredient):
    try:
        # API credentials and URL construction
        app_id = '9e8e2d3f'
        app_key = '860c66f5e85ea75f0e0e045f19063202'
        url = f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}'

        # Making a GET request to the Edamam API
        response = requests.get(url)

        # Handling successful response or error
        if response.status_code == 200:
            # Return list of recipes from the response JSON
            return response.json().get('hits', [])
        else:
            print("Oops! Couldn't get the recipes for this ingredient. Status code:", response.status_code)
        return []  # Return an empty list in case of an unsuccessful response

    except requests.RequestException as e:
        print("Error fetching data. Please check your connection:", e)
        return []  # Return an empty list in case of an exception


# Function to get cusine types from Edamam API

def get_cuisineType(cuisineType):
    try:
        # API credentials and URL construction
        app_id = '9e8e2d3f'
        app_key = '860c66f5e85ea75f0e0e045f19063202'
        url = f'https://api.edamam.com/search?q=    {cuisineType}&app_id={app_id}&app_key={app_key}'

        # Making a GET request to the Edamam API
        response = requests.get(url)

        # Handling successful response or error
        if response.status_code == 200:
            # Return list of cuisine from the response JSON
            return response.json().get('hits', [])
        else:
            print("Oops! Couldn't get the recipes for this cuisine. Status code:", response.status_code)
            return []  # Return an empty list in case of an unsuccessful response

    except requests.RequestException as e:
        print("Error fetching data. Please check your connection:", e)
        return []  # Return an empty list in case of an exception


# Function to display and choose a recipe
def choose_recipe(recipes):
    if recipes:
        # Display available recipes for selection
        print("Select a recipe to view details:")
        for i, recipe in enumerate(recipes, start=1):
            recipe_details = recipe.get('recipe', {})  # Retrieve recipe details or an empty dictionary
            print(f"{i}. Recipe:", recipe_details.get('label'))  # Print recipe names with their respective numbers

        # Take user input to choose a recipe
        choice = int(input("Enter the number of the recipe you want to view: ")) - 1
        if 0 <= choice < len(recipes):
            chosen_recipe = recipes[choice]
            return chosen_recipe  # Return the chosen recipe
        else:
            print("Invalid choice. Please enter a valid number.")
            return None
    else:
        print("No recipes found with the given ingredient.")
        return None


# Function to get product information from Open Food Facts API based on product name
def search_product_by_name(product_name):
    try:
        # Constructing the URL for Open Food Facts API
        url = f'https://world.openfoodfacts.org/cgi/search.pl?search_terms={product_name}&search_simple=1&action=process&json=1'

        # Making a GET request to Open Food Facts API
        response = requests.get(url)

        # Handling successful response or error
        if response.status_code == 200:
            # Return product information from the response JSON
            return response.json().get('products', [])
        else:
            print("Oops! Couldn't get product info from Open Food Facts. Status code:", response.status_code)
            return []  # Return an empty list in case of an unsuccessful response

    except requests.RequestException as e:
        print("Error fetching data from Open Food Facts. Please check your connection:", e)
        return []  # Return an empty list in case of an exception


# Asking user what cuisine they want
cuisine_type = input('What cuisine do you want?')
cuisines = get_cuisineType(cuisine_type)

# Asking user for an ingredient and getting recipes
ingredient_input = input('Enter your ingredient: ')
recipes = get_recipes(ingredient_input)

# Choosing a recipe from the obtained list
chosen_recipe = choose_recipe(recipes)

if chosen_recipe:  # If a recipe was chosen successfully
    recipe_details = chosen_recipe.get('recipe', {})  # Retrieve recipe details or an empty dictionary
    print("Recipe:", recipe_details.get('label'))  # Print recipe name
    print("URL:", recipe_details.get('url'))  # Print recipe URL
    print("Ingredients:", recipe_details.get('ingredientLines'))  # Print recipe ingredients

    print("=" * 50)  # Print a line of equal signs for separation

# Asking user for a product name and getting product information
product_name_input = input('Enter a product name: ')
products = search_product_by_name(product_name_input)

if products:
    # Display product details
    for product in products:
        print("Product Name:", product.get('product_name'))
        print("Brand:", product.get('brands'))
        print("Ingredients:", product.get('ingredients_text'))
        print("==" * 50)
        print('Thank you')
else:
    print("No products found with the given name.")

# Save results to a file
with open('recipes_and_products.txt', 'w', encoding='utf-8') as file:
    file.write(f"Recipes:\n")
    file.write(f"-------------------\n")
    file.write(f"Recipe: {recipe_details.get('label')}\n")
    file.write(f"URL: {recipe_details.get('url')}\n")
    file.write(f"Ingredients: {recipe_details.get('ingredientLines')}\n")
    file.write(f"-------------------\n\n")
    file.write(f"Products:\n")
    file.write(f"-------------------\n")
    for product in products:
        file.write(f"Product Name: {product.get('product_name')}\n")
        file.write(f"Brand: {product.get('brands')}\n")
        file.write(f"Ingredients: {product.get('ingredients_text')}\n")
        file.write(f"-------------------\n")

