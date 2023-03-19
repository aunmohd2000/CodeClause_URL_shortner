import pyshorteners  # import the library

url = input('Enter the long url: ')   # take input from the user i.e. the url which is to be converted into short url

# creating a function to convert the long url into short
# NOTE - it can also be done without a function but functions make a program easily understandable and editable

def shortenurl(url):     
    s = pyshorteners.Shortener()  # using shortener function of pyshortners
    print(s.tinyurl.short(url))   


shortenurl(url) # calling the shortenurl function that we just created also passing long url as parameter

a = input("Press Any Key to Quit")  

#end of file