from secret import secret
import sqlite3


class Database(object):
    """sqlite3 database class"""
    __DB_LOCATION = secret['database']

    def __init__(self, db_location=None):
        if db_location is not None:
            self.connection = sqlite3.connect(db_location)
        else:
            self.connection = sqlite3.connect(self.__DB_LOCATION)
        self.cur = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        self.cur.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.commit()
        self.connection.close()

    def close(self):
        self.connection.close()

    def execute(self, new_data):
        self.cur.execute(new_data)

    def executemany(self, table, many_new_data):
        self.create_table(table)
        self.cur.executemany(f"insert into {table} (id, dish_name, website) values (null, ?, ?)", many_new_data)

    def create_table(self, table):
        query = f"create table if not exists {table} (id integer primary key, dish_name text, website text)"
        self.execute(query)

    def commit(self):
        self.connection.commit()


def main():
    fish = [("Shrimp Scampi", "https://www.foodiecrush.com/shrimp-scampi/"),
            ("Dijon Salmon", "https://natashaskitchen.com/baked-salmon-with-garlic-and-dijon/"),
            ("Trout with Lemon Butter", "https://juliasalbum.com/trout-with-garlic-lemon-butter-herb-sauce/"),
            ("Sheet Pan Fajitas", "https://www.number-2-pencil.com/one-sheet-pan-shrimp-fajitas/"),
            ("Honey Salmon", "https://damndelicious.net/2014/02/07/honey-salmon-foil/"),
            ("Crab Cakes", "https://www.dinneratthezoo.com/maryland-crab-cakes/#recipe"),
            ("Tilapia with Creamy Red Pepper Sauce", "https://cooktoria.com/tilapia-roasted-pepper-sauce/#recipe")]
    beef = [("Korean Beef", "https://www.tablefortwoblog.com/korean-beef-recipe/"),
            ("Cheesesteak Stuffed Peppers",
             "https://www.delish.com/cooking/recipe-ideas/recipes/a51551/cheesesteak-stuffed-peppers-recipe/"),
            ("Beef Barbacoa", "https://www.gimmesomeoven.com/barbacoa-recipe/"),
            ("Slow Cooker Cheesesteaks",
             "https://fitslowcookerqueen.com/slow-cooker-philly-cheesesteaks-low-carb-keto/"),
            ("Street Tacos", "https://damndelicious.net/2019/04/18/mexican-street-tacos/"),
            ("Beef and Broccoli", "https://www.lecremedelacrumb.com/slow-cooker-broccoli-beef/"),
            ("Pot Roast", "https://www.mynaturalfamily.com/paleo-pot-roast-crock-pot/"),
            ("Cheeseburger Pasta", "https://www.budgetbytes.com/skillet-cheeseburger-pasta/"),
            ("BBQ Beef and Cabbage", "https://www.budgetbytes.com/bbq-beef-and-cabbage/"),
            ("Corned Beef", "https://www.foodiecrush.com/slow-cooker-corned-beef-and-cabbage/"),
            ("French Dip Sandwiches", "https://www.chelseasmessyapron.com/french-dip-sandwich/"),
            ("Burgers", "https://en.wikipedia.org/wiki/Bob%27s_Burgers")]
    chicken = [("Chipotle Lime Chicken and Rice", "https://www.budgetbytes.com/chipotle-lime-chicken-and-rice/"),
               ("Salsa Chicken and Rice", "https://www.budgetbytes.com/creamy-salsa-chicken-skillet/"),
               ("Cheesy Chicken, Broccoli and Rice",
                "https://www.the-girl-who-ate-everything.com/one-pan-cheesy-chicken-broccoli-rice/"),
               ("Chicken in Sour Cream Sauce",
                "https://bunnyswarmoven.net/chicken-breast-sour-cream-sauce/?epik"
                "=dj0yJnU9ZFVtczBKRVVSaEVlajRZY2JtNEEzS2hTNWt1ZXVmSnImcD0wJm49SFVvYmFqbHpISUI4d01RODNuamxzUSZ0PUFBQUFB\
                R0pVSEpJ"),
               ("Chicken Thighs with Artichokes",
                "https://avocadopesto.com/4-ingredient-artichoke-and-garlic-broiled-chicken-thighs-gf-df/"),
               ("Mustard Chicken", "https://www.tablefortwoblog.com/holy-yum-chicken/"),
               ("Baked Crispy Chicken Legs", "https://www.africanbites.com/baked-crispy-chicken-legs/"),
               ("Chicken, Bacon, Ranch Poppers", "https://40aprons.com/whole30-chicken-bacon-ranch-poppers-paleo/"),
               ("Sour Cream Chicken", "https://www.adishofdailylife.com/2018/06/smothered-cheesy-sour-cream-chicken/"),
               ("Greek Chicken Bake",
                "https://www.thepinningmama.com/easy-dinner-recipe-greek-chicken-bake/#_a5y_p=2936076"),
               ("Baked Wings", "https://healthyrecipesblogs.com/baked-chicken-wings/?5791189602"),
               ("Teriyaki Chicken", "https://modernmealmakeover.com/teriyaki-chicken/"),
               ("Chicken Piccata", "https://thecozycook.com/chicken-piccata/"),
               ("Green Chile Chicken Casserole",
                "https://www.rebootedmom.com/cheesy-green-chile-chicken-cauliflower-enchilada-casserole/"),
               ("Crockpot White Chili Chicken", "https://lovelylittlekitchen.com/creamy-crockpot-white-chicken-chili/"),
               ("Creamy Tuscan Chicken",
                "https://www.paleorunningmomma.com/creamy-tuscan-chicken-paleo-whole30-keto/#wprm-recipe-container\
                -2596\ 0"),
               ("Spinach and Artichoke Chicken", "https://easyfamilyrecipes.com/spinach-and-artichoke-chicken/"),
               ("Everything Bagel Chicken and Veggies",
                "https://whatmollymade.com/sheet-pan-everything-bagel-chicken/"),
               ("Baked Chicken Kabobs", "https://www.cookerru.com/baked-chicken-kabobs/"),
               ("Salsa and Beer Chicken", "https://www.kleinworthco.com/beer-braised-fiesta-pulled-chicken/"),
               ("TJs Chicken Shwarma",
                "https://traderjoesrants.com/2019/04/02/trader-joes-shwarma-marinated-chicken-thighs/"), (
               "Whole Roast Chicken and Chicken Salad",
               "https://www.youtube.com/watch?v=ABtt5y-maO4")]  # list of tuples to be entered into the chicken table
    pork = [("Ham Sliders", "https://realhousemoms.com/ham-and-cheese-sliders/#recipe"),
            ("Slow Cooker Pulled Pork", "https://slowcookergourmet.net/best-slow-cooker-pulled-pork/"),
            ("Pork Chops in Cream Sauce", "https://whatsinthepan.com/pork-chops-in-creamy-white-wine-sauce/"),
            ("Carnitas", "https://cafedelites.com/pork-carnitas-mexican-slow-cooked-pulled-pork/"),
            ("Pork Posole", "https://www.savingdessert.com/slow-cooker-pork-posole-recipe/"),
            ("Kielbasa and Pierogies", "https://jonesinfortaste.com/sheet-pan-kielbasa-pierogies/"),
            ("Sausage and Gnocchi",
             "https://www.thekitchn.com/sheet-pan-gnocchi-mushrooms-sausage-squash-22955997?epik=dj0yJnU9TW5LSVhwNzhUTl\
             FNeUVMSkdGR0xBcFRsTDBUaEplNjUmcD0wJm49QU5YOHNDUUxRTmRfQzE3d3hNNF9fQSZ0PUFBQUFBR0pVTDVn"),
            ("Crockpot Pork Loin", "https://www.eatwell101.com/crockpot-pork-loin-recipe"),
            ("Ham and Corn Soup", "https://moderncrumb.com/ham-red-potato-corn-chowder/"),
            ("Brats and Sauerkraut", "https://www.budgetbytes.com/bratwurst-and-sauerkraut/"),
            ("Bakes Pasta with Sausage and Spinach", "https://www.plainchicken.com/baked-pasta-with-sausage-spinach/"),
            ("Egg Roll Bowl", "https://www.mostlyhomemademom.com/eggroll-in-bowl/"),
            ("Garlic, Bacon Pasta", "https://www.sprinklesandsprouts.com/garlic-bacon-pasta/")]
    vegetarian = [("Tortilla Baked Eggs", "https://www.budgetbytes.com/southwest-tortilla-baked-eggs/"),
                  ("Hummus Breakfast Tacos", "https://www.budgetbytes.com/hummus-breakfast-tacos/"),
                  ("Bean and Cheese Burritos",
                   "https://www.theanthonykitchen.com/black-bean-burrito-hidden-vegetables-kid-friendly-recipe/"),
                  ("Green Chiles Migas", "https://www.budgetbytes.com/green-chile-migas/"),
                  ("Black Bean Taquitos", "https://www.budgetbytes.com/creamy-black-bean-taquitos/"),
                  ("Shakshuka", "https://www.budgetbytes.com/smoky-white-bean-shakshuka/"),
                  ("BBQ Bean Sliders", "https://www.budgetbytes.com/bbq-bean-sliders/"),
                  ("Crockpot Lasagna", "https://pinchofyum.com/super-easy-skinny-veggie-crockpot-lasagna"),
                  ("Egg Drop Soup", "https://www.gimmesomeoven.com/egg-drop-soup/"),
                  ("Vegetables and Gravy", "https://www.budgetbytes.com/vegetables-and-gravy/"),
                  ("Mac and Cheese", "https://www.food.com/recipe/easy-stove-top-macaroni-cheese-60350?soc=pinterest"),
                  ("Risotto", "https://cravinghomecooked.com/basic-risotto/#wprm-recipe-container-3374"),
                  ("Banana Oatmeal Pancakes", "https://whatmollymade.com/wprm_print/6455/"),
                  ("Rice and Cheese Soufflé", "https://www.foodiewithfamily.com/easy-rice-cheese-souffle/"),
                  ("Garlic Chickpea Soup", "https://theclevermeal.com/vegan-chickpea-soup/"),
                  ("Eggplant Parm", "https://www.tablefortwoblog.com/eggplant-parmesan/"),
                  ("Lemon Dill Pasta Salad", "https://www.budgetbytes.com/creamy-lemon-dill-greek-pasta-salad/"),
                  ("Cheddar Broccoli Soup", "https://www.thechunkychef.com/copycat-30-minute-broccoli-cheese-soup/"),
                  ("Veggie Fried Rice", "https://www.budgetbytes.com/vegetable-not-fried-rice/"),
                  ("French Toast", "https://www.allrecipes.com/recipe/7016/french-toast-i/"),
                  ("Egg Salad", "https://www.allrecipes.com/recipe/147103/delicious-egg-salad-for-sandwiches/"),
                  ("Pizza", "https://tasty.co/recipe/pizza-dough"),
                  ("Quesadillas", "https://www.allrecipes.com/recipe/221293/vegan-black-bean-quesadillas/"),
                  ("Spaghetti and Meatballs", "https://www.noracooks.com/spaghetti-and-easy-vegan-meatballs/"),
                  ("Rice, Eggs and Avocado", "https://www.bonappetit.com/recipe/rice-bowl-fried-egg-avocado")]
    with Database() as db:
        db.executemany('fish', fish)
        db.executemany('beef', beef)
        db.executemany('chicken', chicken)
        db.executemany('pork', pork)
        db.executemany('vegetarian', vegetarian)
        db.commit()


if __name__ == "__main__":
    main()
