// 1. **Ancestral Stories:** In many African cultures, the art of storytelling is passed
// down from generation to generation. Imagine you're creating an application that
// records these oral stories and translates them into different languages. The
// stories vary by length, moral lessons, and the age group they are intended for.
// Think about how you would model `Story`, `StoryTeller`, and `Translator`
// objects, and how inheritance might come into play if there are different types of
// stories or storytellers.



// -AN APPLICATION THAT WILL RECORD THE ORAL STORIES
// input
// -length
// -moral lesson
// -age group
// -translator
// -storyteller

// the subclasses will include story story tellers and translators
// process
// Create a class
// Have the sub classes
// have a method that will help me with the other sub classes
// Create instances

// output
// time taken for the story
// the narattor
// the translator
// the moral lesson


class Oral{
    constructor(length,moralLesson,ageGroup,translator,StoryTeller){
        this.length=length
        this.moralLesson=moralLesson
        this.ageGroup=ageGroup
        this.StoryTeller=StoryTeller
        this.translator=translator
    }

    getStory(){
        console.log(`${this.constructor.name}:   ${this.story} which is  ${this.length} and its moral lesson include ${this.moralLesson} and the suitable age group is ${this.ageGroup} and will be presented by ${this.StoryTeller} and ${this.translator} will translate it` ); 

    }
}

class Story extends Oral{
    story="This story is about The old man in town"
}

class StoryTeller extends Oral{
    story="This story is about The little boy"
}
class Translator extends Oral{
    story="This story is about The poor girl"

}

const story1= new Story("2hours","obey your parents","3-7 years","Paul Mwangi","Jane Mwaura")
story1.getStory()

const story2= new StoryTeller("4hours","always believe in yourself","9years-16years","Loice Kim","Petter Kenneth")
story2.getStory()

const story3= new StoryTeller("1hour","nothing is impossible","10-15years","Javan Juma","Bruce Otieno")
story3.getStory()




// Question2 
// **African Cuisine:** You're creating a recipe app specifically for African cuisine.
// The app needs to handle recipes from different African countries, each with its
// unique ingredients, preparation time, cooking method, and nutritional
// information. Consider creating a `Recipe` class, and think about how you might
// create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
// `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
// methods.

// input
// class recipe is the main class and has subclasses of MorrocanRecipe,EthopianRecipe,NigerianRecipe
// unique ingerdients,preparation time,cooking method and nutriional information
// process
// Create a main class
// have sub classes that will inherit from the main class which is Class recipe
// have one method that I will call it getRecipe that I will use it and call the other classes
// Create instances

// output
// My output will be the recipe name which will have the uniques ingerdients,preparation time, coooki8ng method and nutruitional value





class Recipe{
    constructor(uniquesIngredients,preparationTime,CookingMethod,nutritionalValue){
        this.uniquesIngredients=uniquesIngredients
        this.preparationTime=preparationTime
        this.CookingMethod=CookingMethod
        this.nutritionalValue=nutritionalValue
    }

    getRecipe(){
        console.log(`${this.constructor.name}:   ${this.recipe} which is made of  ${this.uniquesIngredients} and it takes ${this.preparationTime} and the cooking method is ${this.CookingMethod} which is ${this.nutritionalValue}` );
}
    }

class EthiopianRecipe extends Recipe{
    recipe= "When preparing an Ethopian recipe you have to consider the type of food to cook"
}

class NigerianRecipe extends Recipe{
    recipe= "When preparing a Nigerian  recipe you have to consider the type of food to cook"
}
class MorrocanRecipe  extends Recipe{
   recipe= "When preparing a Morrocan  recipe you have to consider the type of food to cook"
}

const recipe1=new EthiopianRecipe("Its unique ingeredients  that include chilly","it takes approximately 2 hours to be ready","one has first to boil the food first","it increases the lifespan in that you will remain healty")
recipe1.getRecipe()

const recipe2= new NigerianRecipe ("Its unique ingredients include fufuuu","it takes approximately 3 hous to be ready","one has first to ferment the flour before cooking","it has a high nutrious value")
recipe2.getRecipe()

const recipe3=new MorrocanRecipe ("its unique ingerdients include the paprika","that takes 4 hous to be ready","one has to stir the ingridients together","and its nutritious value include being healthy")
recipe3.getRecipe()




// **Wildlife Preservation:** You're a wildlife conservationist working on a
// program to track different species in a national park. Each species has its own
// characteristics and behaviors, such as its diet, typical lifespan, migration
// patterns, etc. Some species might be predators, others prey. 
// You'll need to create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
// these classes might relate to each other through inheritance.




class wildlife{
    constructor(species,diet,typicalLifespan,migrationPattern){
        this.species=species
        this.diet=diet
        this.typicalLifespan=typicalLifespan
        this.migrationPattern=migrationPattern
    }

    getRelate(){
        console.log(`${this.constructor.name}:   ${this.relate}   ${this.species} normally feeds on ${this.diet} and the life span is ${this.typicalLifespan} which it migrates during the ${this.migrationPattern}` );
    }


}

class Species extends wildlife{
    relate="The  "
}

class Predator extends wildlife{
    relate="The  "
}

class Prey extends wildlife{
    relate="The  "
}

const species1= new Species("Zebra","grass","24years","rainy")
species1.getRelate()

const species2= new Species ("Leopard","meat","20 years","sunny")
species2.getRelate()

const species3= new Species ("Lion","red meat","12 years","rainy")
species3.getRelate()