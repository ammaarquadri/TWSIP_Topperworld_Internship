import difflib

# Extensive dictionary of words
dictionary = [
    "apple", "banana", "orange", "grape", "strawberry", "blueberry", "raspberry", "kiwi", "pear", "peach",
    "apricot", "pineapple", "mango", "papaya", "watermelon", "melon", "cherry", "plum", "lemon", "lime",
    "fig", "date", "coconut", "olive", "avocado", "tomato", "potato", "carrot", "onion", "garlic", "ginger",
    "cucumber", "zucchini", "pepper", "spinach", "lettuce", "kale", "cabbage", "broccoli", "cauliflower",
    "asparagus", "green bean", "pea", "corn", "wheat", "rice", "oat", "barley", "rye", "sorghum", "millet",
    "quinoa", "soybean", "peanut", "almond", "walnut", "pecan", "hazelnut", "cashew", "macadamia", "pine nut",
    "chestnut", "coffee", "tea", "chocolate", "vanilla", "cinnamon", "nutmeg", "ginger", "turmeric", "paprika",
    "cumin", "coriander", "cardamom", "cloves", "garam masala", "salt", "pepper", "sugar", "honey", "maple syrup",
    "butter", "oil", "milk", "cream", "yogurt", "cheese", "egg", "meat", "poultry", "fish", "seafood", "tofu",
    "tempeh", "beans", "lentils", "chickpeas", "peas", "bread", "pasta", "rice", "noodles", "pizza", "soup",
    "salad", "sandwich", "burger", "steak", "chops", "roast", "casserole", "stir-fry", "curry", "smoothie",
    "juice", "shake", "cocktail", "beer", "wine", "cookie", "cake", "pie", "muffin", "donut", "pastry",
    "ice cream", "gelato", "sorbet", "pudding", "custard", "mousse", "souffle", "brownie", "blondie", "bar",
    "slice", "tart", "cheesecake", "truffle", "macaron", "candy", "chocolate", "gum", "mint", "chip", "dip",
    "spread", "sauce", "dressing", "marinade", "rub", "brine", "batter", "dough", "mix", "flour", "yeast",
    "baking powder", "baking soda", "salt", "sugar", "butter", "oil", "egg", "milk", "water", "vanilla",
    "almond", "lemon", "lime", "orange", "coconut", "chocolate", "peanut butter", "jelly", "jam", "honey",
    "syrup", "caramel", "peppermint", "spearmint", "wintergreen", "cinnamon", "nutmeg", "ginger", "allspice",
    "cloves", "pumpkin spice", "apple pie spice", "vanilla extract", "almond extract", "lemon extract",
    "lime extract", "orange extract", "coconut extract", "chocolate extract", "peppermint extract",
    "spearmint extract", "wintergreen extract", "cinnamon extract", "nutmeg extract", "ginger extract",
    "allspice extract", "cloves extract", "pumpkin spice extract", "apple pie spice extract", "espresso",
    "coffee", "tea", "matcha", "green tea", "black tea", "white tea", "oolong tea", "herbal tea", "rooibos",
    "yerba mate", "chai", "masala chai", "turmeric latte", "golden milk", "kombucha", "kefir", "sauerkraut",
    "kimchi", "miso", "tempeh", "natto", "pickles", "pickled", "fermented", "probiotic", "prebiotic", "fiber",
    "protein", "fat", "carbohydrate", "sugar", "sodium", "calcium", "iron", "vitamin", "mineral", "antioxidant",
    "phytochemical", "flavonoid", "terpene", "cannabinoid", "omega-3", "omega-6", "gluten", "lactose", "casein",
    "soy", "peanut", "tree nut", "shellfish", "fish", "egg", "dairy", "meat", "poultry", "game", "vegetable",
    "fruit", "nut", "seed", "grain", "legume", "bean", "pulse", "tuber", "root", "leafy green", "cruciferous",
    "allium", "nightshade", "citrus", "berry", "stone fruit", "tropical fruit", "drupe", "pome", "simple fruit",
    "aggregate fruit", "multiple fruit", "accessory fruit", "false fruit", "true fruit", "seedless fruit",
    "organic", "conventional", "heirloom", "hybrid", "GMO", "non-GMO", "hormone-free", "antibiotic-free",
    "grass-fed", "pasture-raised", "wild-caught", "sustainable", "fair trade", "artisanal", "craft", "small-batch",
    "mass-produced", "processed", "refined", "whole", "natural", "raw", "cooked", "baked", "grilled", "roasted",
    "sauteed", "fried", "boiled", "steamed", "poached", "braised", "stewed", "simmered", "broiled", "smoked",
    "cured", "pickled", "fermented", "marinated", "brined", "glazed", "breaded", "battered", "dipped", "stuffed",
    "layered", "rolled", "folded", "twisted", "kneaded", "whipped", "beaten", "mixed", "blended", "pureed", "chopped",
    "diced", "minced", "sliced", "shredded", "grated", "peeled", "pitted", "cored", "zested", "juiced", "segmented",
    "filleted", "deboned", "butchered", "trimmed", "tied", "larded", "basted", "garnished", "plated", "served",
    "portioned", "measured", "weighed", "counted", "estimated", "calculated", "adjusted", "tweaked", "optimized",
    "improved", "enhanced", "elevated", "transformed", "revolutionized", "modernized", "traditional", "classic",
    "vintage", "retro", "contemporary", "fusion", "international", "ethnic", "regional", "local", "seasonal",
    "trending", "popular", "viral", "buzzworthy", "critically acclaimed", "award-winning", "best-selling",
    "top-rated", "highly recommended", "must-try", "signature", "house special", "daily special", "weekly special",
    "monthly special", "holiday special", "event special", "limited-time offer", "exclusive", "premium", "luxury",
    "gourmet", "artisan", "homemade", "handcrafted","hotel"
]

def autocorrect(word, dictionary):
    # Check if the word is already in the dictionary
    if word in dictionary:
        return word  # The word is spelled correctly
    else:
        # Use difflib to find the closest match to the misspelled word
        close_matches = difflib.get_close_matches(word, dictionary, n=1, cutoff=0.6)
        
        # If a close match is found, return the first match
        if close_matches:
            return close_matches[0]
        else:
            # If no close match is found, return the original word
            return word

# Get input from the user
input_word = input("Enter a word to check for spelling: ")

# Correct the input word
corrected_word = autocorrect(input_word, dictionary)

# Print the result
if input_word == corrected_word:
    print(f"The word '{input_word}' is spelled correctly.")
else:
    print(f"The misspelled word '{input_word}' was corrected to '{corrected_word}'.")
