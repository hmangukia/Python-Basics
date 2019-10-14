"""
This is a basic example of how to parse webpages using Beautiful Soup.

In this example, we'll create a program to report on the latest cats that are adoptable from the Ottawa Humaine Society!

Note: This was tested on Oct 14, 2019. If the Humaine Society changes their site layout, this script may not work!

Dependencies:
    - Requests (For fetching HTML pages)
    - Beautiful Soup (For parsing HTML pages)
"""
import requests
from bs4 import BeautifulSoup

def parsePage(url):
    # Fetch the page
    page = requests.get(url)

    # Parse the page into an object we can interface with
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def removeWhitespace(input):
    # Strip out newline characters
    output = input.replace('\n', '')

    # Strip out tab characters
    output = output.replace('\t', '')
    return output
    


if __name__ == '__main__':
    # This page contains a list of all adoptable cats from the Ottawa Humaine Society
    url = 'https://ottawahumane.ca/adopt/cats-for-adoption/?orderby=date&sort=ascending'
    soup = parsePage(url)

    # Each of the cat's information is in the following format:
    # <div class="info-card__text">
    #   <div class="info-card__title"><span>Name</span> | Spot</div>
    #   <p>Located at ottawa humane society<br/><br/>in foster home - available for adoption<br/><br/>special needs</p>
    #   <ul class="info-card__list">
    #       <li class="info-card__item">
    #           <span>Breed:</span> domestic sh
    #       </li>
    #       <li class="info-card__item">
    #           <span>Age:</span> 10 years
    #       </li>
    #       <li class="info-card__item">
    #           <span>Sex:</span> Neutered male
    #       </li>
    #       <li class="info-card__item">
    #           <span>Colour:</span> white and brn tabby
    #       </li>
    #       <li class="info-card__item">
    #           <span>Animal ID:</span> A104913
    #       </li>
    #   </ul>
    # </div>

    # So, our strategy is as follows:
    #   1. Fetch all of the div elements, with a class of "info-card__list".
    #   2. For each element found in step 1, isolate the HTML elements that have info that we want.

    # Find the latest cats listed on the website
    # Here, we're finding all div elements that have a class of "info-card__list".
    cats = soup.findAll("div", "info-card__text")
    print("Printing information about {} cats...".format(len(cats)))

    # For each cat we have here, isolate each field we want, and print it to the console
    for c in cats:
        # -- Isolate the name --
        # First, let's fetch the cat's name. It's stored in a div element, with a class of "info-card__title".
        # Sinec there's only one expected, we can call find() instead of findAll(), so that we get one item, instead of an array.
        name = c.find('div', 'info-card__title')

        # Now, let's clean this up a bit. Our value is currently "Name | domestic sh". We should probably clean this up, stripping out the "Name | " part.
        # Let's isolate everything after the vertical line.
        name = name.getText().split('|')[1]
        name = name.strip()


        # -- Isolate the rest of the info --
        # All of the other info we want here is stored in an li element, with a class of "info-card__item". Fetch all of those elements.
        cat_info = c.findAll('li', 'info-card__item')

        # Fetch the contents of the HTML tag, and clean it up a bit.
        breed = cat_info[0].getText()
        breed = removeWhitespace(breed)

        # Our value is currently "Breed : domestic sh". We should probably clean this up, stripping out the "Breed : " part.
        # Let's isolate everything after the colon.
        breed = breed.split(':')[1]
        breed = breed.strip()


        # Great! Let's repeat the same for some of the other fields!
        age = cat_info[1].getText()
        age = removeWhitespace(age)
        age = age.split(':')[1]
        age = age.strip()

        sex = cat_info[2].getText()
        sex = removeWhitespace(sex)
        sex = sex.split(':')[1]
        sex = sex.strip()

        color = cat_info[3].getText()
        color = removeWhitespace(color)
        color = color.split(':')[1]
        color = color.strip()

        # Now, we could do whatever we want with this data.
        # For this example, let's log it to the console.
        print("Name: {}".format(name))
        print("\tBreed: {}".format(breed))
        print("\tAge: {}".format(age))
        print("\tGender: {}".format(sex))
        print("\tColor: {}".format(color))
