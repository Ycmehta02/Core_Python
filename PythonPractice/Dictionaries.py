#group of key & value pairs
#mutable
book = {"Book" : "Kafka on Shore", "Author" : "Murakami"}
print(book)
print(type(book))

print(book.get("Author"))
print(book["Book"])

print(book.keys())
print(book.values())

book["Author"] = "Haruki Murakami"

for k,v in book: #book.keys() / book.values()
    print(k,v)

#book.pop()
#del car["Book"]
#compare dictionaries with == & !=

































