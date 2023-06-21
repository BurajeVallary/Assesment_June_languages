fun main() {
    val story1 = Story()
    story1.getStory()

    val story2 = StoryTeller()
    story2.getStory()

    val story3 = Translator()
    story3.getStory()
}




//// 1. **Ancestral Stories:** In many African cultures, the art of storytelling is passed
//// down from generation to generation. Imagine you're creating an application that
//// records these oral stories and translates them into different languages. The
//// stories vary by length, moral lessons, and the age group they are intended for.
//// Think about how you would model `Story`, `StoryTeller`, and `Translator`
//// objects, and how inheritance might come into play if there are different types of
//// stories or storytellers.
//
//
//
//// -AN APPLICATION THAT WILL RECORD THE ORAL STORIES
//// input
//// -length
//// -moral lesson
//// -age group
//// -translator
//// -storyteller
//
//// the subclasses will include story story tellers and translators
//// process
//// Create a class
//// Have the sub classes
//// have a method that will help me with the other sub classes
//// Create instances
//
//// output
//// time taken for the story
//// the narattor
//// the translator
//// the moral lesson

open class Oral(val length: String, val moralLesson: String, val ageGroup: String, val translator: String, val storyTeller: String) {
    open val story: String = ""

    open fun getStory() {
        println("${this::class.simpleName}: ${this.story} which is ${this.length} and its moral lesson include ${this.moralLesson} and the suitable age group is ${this.ageGroup} and will be presented by ${this.storyTeller} and ${this.translator} will translate it")
    }
}

class Story : Oral("2hours", "obey your parents", "3-7 years", "Jane Mwaura", "Paul Mwangi") {
    override val story: String = "This story is about The old man in town"
}

class StoryTeller : Oral("4hours", "always believe in yourself", "9years-16years", "Petter Kenneth", "Loice Kim") {
    override val story: String = "This story is about The little boy"
}

class Translator : Oral("1hour", "nothing is impossible", "10-15years", "Bruce Otieno", "Javan Juma") {
    override val story: String = "This story is about The poor girl"
}