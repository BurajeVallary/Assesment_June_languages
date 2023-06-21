# # // 1. **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# // down from generation to generation. Imagine you're creating an application that
# // records these oral stories and translates them into different languages. The
# // stories vary by length, moral lessons, and the age group they are intended for.
# // Think about how you would model `Story`, `StoryTeller`, and `Translator`
# // objects, and how inheritance might come into play if there are different types of
# // stories or storytellers.



# // -AN APPLICATION THAT WILL RECORD THE ORAL STORIES
# // input
# // -length
# // -moral lesson
# // -age group
# // -translator
# // -storyteller

# // the subclasses will include story story tellers and translators
# // process
# // Create a class
# // Have the sub classes
# // have a method that will help me with the other sub classes
# // Create instances

# // output
# // time taken for the story
# // the narattor
# // the translator
# // the moral lesson

class Oral:
    def __init__(self,length,moralLesson,ageGroup,translator,StoryTeller):
        self.length=length

        self.moralLesson=moralLesson
        self.ageGroup=ageGroup
        self.translator=translator
        self.StoryTeller_=StoryTeller


    def getStory(self):
        print(f"{self.__class__.__name__}:{self.story} which is {self.length} and it take its moral lesson include {self.moralLesson} and the suitable age group is {self.ageGroup} and will be presented by {self.StoryTeller_} and {self.translator} will translate it")
        
class Story (Oral):
      story="This story is about The old man in town"

class StoryTeller (Oral):
     story="This story is about The little boy"

class Translator(Oral):
    story="This story is about The poor girl"

story1=  Story("2hours","obey your parents","3-7 years","Paul Mwangi","Jane Mwaura")
story1.getStory()

story2=  StoryTeller("4hours","always believe in yourself","9years-16years","Loice Kim","Petter Kenneth")
story2.getStory()
story3=  StoryTeller("1hour","nothing is impossible","10-15years","Javan Juma","Bruce Otieno")
story3.getStory()


# // Question2 
# // **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# // The app needs to handle recipes from different African countries, each with its
# // unique ingredients, preparation time, cooking method, and nutritional
# // information. Consider creating a `Recipe` class, and think about how you might
# // create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# // `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# // methods.

# // input
# // class recipe is the main class and has subclasses of MorrocanRecipe,EthopianRecipe,NigerianRecipe
# // unique ingerdients,preparation time,cooking method and nutriional information
# // process
# // Create a main class
# // have sub classes that will inherit from the main class which is Class recipe
# // have one method that I will call it getRecipe that I will use it and call the other classes
# // Create instances

# // output
# // My output will be the recipe name which will have the uniques ingerdients,preparation time, coooki8ng method and nutruitional value

class Recipe:
    def __init__(self,uniquesIngredients,preparationTime,CookingMethod,nutritionalValue) :
        self.uniqueIngredients=uniquesIngredients
        self.preparationTime=preparationTime
        self.CookingMethod=CookingMethod
        self.nutritionalValue=nutritionalValue

    def getRecipe(self):
        print(f"{self.__class__.__name__}:{self.recipe} which is made of {self.uniqueIngredients} and it takes  which is {self.preparationTime} and the cooking methodis {self.CookingMethod} which is {self.nutritionalValue}")

class EthiopianRecipe(Recipe):
    recipe= "When preparing an Ethopian recipe you have to consider the type of food to cook"


class NigerianRecipe (Recipe):
    recipe= "When preparing a Nigerian  recipe you have to consider the type of food to cook"

class MorrocanRecipe (Recipe):
   recipe= "When preparing a Morrocan  recipe you have to consider the type of food to cook"


recipe1= EthiopianRecipe("Its unique ingeredients  that include chilly","it takes approximately 2 hours to be ready","one has first to boil the food first","it increases the lifespan in that you will remain healty")
recipe1.getRecipe()

recipe2=  NigerianRecipe ("Its unique ingredients include fufuuu","it takes approximately 3 hous to be ready","one has first to ferment the flour before cooking","it has a high nutrious value")
recipe2.getRecipe()

recipe3= MorrocanRecipe ("its unique ingerdients include the paprika","that takes 4 hous to be ready","one has to stir the ingridients together","and its nutritious value include being healthy")
recipe3.getRecipe()



# // **Wildlife Preservation:** You're a wildlife conservationist working on a
# // program to track different species in a national park. Each species has its own
# // characteristics and behaviors, such as its diet, typical lifespan, migration
# // patterns, etc. Some species might be predators, others prey. 
# // You'll need to create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# // these classes might relate to each other through inheritance.

# input 
# main class wildlife
# species,diet,lifespan,migration pattern
# process
# create a  main class
# pass the attribures
# have the methods and subclasses



class Wildlife:
    def __init__(self, species, diet, typical_lifespan, migration_pattern):
        self.species = species
        self.diet = diet
        self.typical_lifespan = typical_lifespan
        self.migration_pattern = migration_pattern

    def get_relate(self):
        print(f"{type(self).__name__}: {self.relate} {self.species} normally feeds on {self.diet} and the lifespan is {self.typical_lifespan}, and it migrates during {self.migration_pattern}")


class Species(Wildlife):
    relate = "The"

    def __init__(self, species, diet, typical_lifespan, migration_pattern):
        super().__init__(species, diet, typical_lifespan, migration_pattern)


class Predator(Wildlife):
    relate = "The"

    def __init__(self, species, diet, typical_lifespan, migration_pattern):
        super().__init__(species, diet, typical_lifespan, migration_pattern)

class Prey(Wildlife):
    relate = "The"

    def __init__(self, species, diet, typical_lifespan, migration_pattern):
        super().__init__(species, diet, typical_lifespan, migration_pattern)


species1 = Species("Zebra", "grass", "24 years", "rainy")
species1.get_relate()

species2 = Species("Leopard", "meat", "20 years", "sunny")
species2.get_relate()

species3 = Species("Lion", "red meat", "12 years", "rainy")
species3.get_relate()
