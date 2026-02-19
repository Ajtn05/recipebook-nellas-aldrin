from ledger.models import Recipe, Ingredient, RecipeIngredient

r1 = Recipe()
r1.name = "Recipe 1"
r1.save()

ingredients_r1 = [
    ("tomato", "3pcs"),
    ("onion", "1pc"),
    ("pork", "1kg"),
    ("water", "1L"),
    ("sinigang mix", "1 packet"),
]

for name, qty in ingredients_r1:
    ing, _ = Ingredient.objects.get_or_create(name=name)

    ri = RecipeIngredient()
    ri.recipe = r1
    ri.ingredient = ing
    ri.quantity = qty
    ri.save()


r2 = Recipe()
r2.name = "Recipe 2"
r2.save()

ingredients_r2 = [
    ("garlic", "1 head"),
    ("onion", "1pc"),
    ("vinegar", "1/2 cup"),
    ("water", "1 cup"),
    ("salt", "1 tablespoon"),
    ("whole black peppers", "1 tablespoon"),
    ("pork", "1 kilo"),
]

for name, qty in ingredients_r2:
    ing, _ = Ingredient.objects.get_or_create(name=name)

    ri = RecipeIngredient()
    ri.recipe = r2
    ri.ingredient = ing
    ri.quantity = qty
    ri.save()


print(Recipe.objects.all())
print(Ingredient.objects.all())
print(RecipeIngredient.objects.all())