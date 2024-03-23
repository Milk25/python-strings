# reviews = [
#     "This product is really good. I'm impressed with its quality.",
#     "The performance of this product is excellent. Highly recommended!",
#     "I had a bad experience with this product. It didn't meet my expectations.",
#     "Poor quality product. Wouldn't recommend it to anyone.",
#     "The product was average. Nothing extraordinary about it."
# ]

# positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
# negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


# append = []
# def usable_words():
#     great_words = append(positive_words).upper()
#     negative_words = append(negative_words).upper()
#     if reviews == great_words and reviews == negative_words:
#         print(f"The positive {great_words(reviews)} and negative {negative_words(reviews)}")
    


#usable_words()





# reviews = [
#     "This product is really good. I'm impressed with its quality.",
#     "The performance of this product is excellent. Highly recommended!",
#     "I had a bad experience with this product. It didn't meet my expectations.",
#     "Poor quality product. Wouldn't recommend it to anyone.",
#     "The product was average. Nothing extraordinary about it."
# ]

# def first_30_characters(reviews):
#     review = reviews.append("My Python code gotten so much better than previously")
# for review in reviews:
#     if reviews[0:30:1]:
#         print(f"Preview of {reviews} {review}: ", (reviews + review))
        
        
# first_30_characters(reviews)




reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

def first_30_characters():
    review = input("Passing along but getting better at Python Programming also!")
    for review in reviews:
        if reviews[0:30:1]:
            print(f"{review} {reviews}")
            
            
first_30_characters()