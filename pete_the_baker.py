import unittest

recipe1 = {"flour": 500, "sugar": 200, "eggs": 1}
available1 = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

recipe2 = {"flour": 100, "sugar": 200, "eggs": 1}
available2 = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

recipe3 = {"flour": 1000, "sugar": 200, "eggs": 1}
available3 = {"flour": 900, "sugar": 1200, "eggs": 5, "milk": 200}

recipe4 = {"flour": 1000, "sugar": 200, "eggs": 1, "olive oil": 10}
available4 = {"flour": 900, "sugar": 1200, "eggs": 5}

def cakes(recipe, available):
    if len(available.keys()) < len(recipe.keys()):
        return 0
    count = 0
    for i in recipe:
        if i in available:
            count+=1
    if count < len(recipe.keys()):
        return 0
    total = []
    for i in recipe:
        total.append(available[i]//recipe[i])
    
    return min(total)

class TestStringMethods(unittest.TestCase):
    def test_1(self):
        self.assertEqual(cakes(recipe1, available1), 2)
    def test_2(self):
        self.assertEqual(cakes(recipe2, available2), 5)
    def test_3_recipe_unavailability(self):
        self.assertEqual(cakes(recipe3, available3), 0)
    def test_4_recipe_insufficiency(self):
        self.assertEqual(cakes(recipe4, available4), 0)

if __name__ == '__main__':
    unittest.main()