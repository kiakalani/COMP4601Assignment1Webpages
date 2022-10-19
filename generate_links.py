from random import randint

# Some random words that came to my mind :)
PERSONAL_KEYWORDS = [
    'BRUSH',
    'GUITAR',
    'BASS',
    'FAN',
    'FOOD',
    'PANTS',
    'SHIRT',
    'TOOTHPASTE',
    'TOWEL',
    'BAG',
    'AMPLIFIER',
    'AUDIO INTERFACE',
    'Computer',
    'Mouse',
    'Keyboard',
    'Monitor',
    'Television',
    'Pick',
    'Headset',
    'Microphone',
    'Perfume',
    'Coin',
    'Water bottle',
    'Sunglasses',
    'table',
    'chair',
    'guitar stand',
    'book',
    'toothbrush'
]

# We need between 500-1000 pages to crawl. Why not 999 :)
COUNT_PAGES = 10

# So we would not have more than the count of paragraphs
MAX_PARAGRAPH_COUNTS = 5

MAX_LINK_COUNTS = 5

naming_convention = 'Personal_{num}'

def create_html(title: str, paragraphs: list[str], links: list[str]) -> str:
    html_text = \
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

    """ + f'<title>{title}</title></head><body>'

    html_text += f'<h1>{title}</h1>'

    for p in paragraphs:
        html_text += f'<p>{p}</p>'
    for a in links:
        html_text += f'<a href="{a}.html">{a}</a><br>'
    html_text += "</body></html>"
    return html_text

for i in range(COUNT_PAGES):
    title = naming_convention.format(num=i)
    paragraphs = []
    links = []
    for j in range(randint(1, MAX_PARAGRAPH_COUNTS)):
        random_item = PERSONAL_KEYWORDS[randint(0, len(PERSONAL_KEYWORDS) - 1)]
        while random_item in paragraphs:
            random_item = PERSONAL_KEYWORDS[randint(0, len(PERSONAL_KEYWORDS) - 1)]
        paragraphs.append(random_item)
    for j in range(randint(1, MAX_LINK_COUNTS)):
        random_link = naming_convention.format(num=randint(0, COUNT_PAGES - 1))
        while random_link in links or random_link == title:
            random_link = naming_convention.format(num=randint(0, COUNT_PAGES - 1))
        links.append(random_link)
    file = open(title + ".html", "w")
    file.write(create_html(title, paragraphs, links))
    file.close()

index_html = \
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
""" + "<title>" + "Index of Kia Kalani's Personal Items Webpage</title></head>" + \
    "<body><h1>" + "Index of Kia Kalani's Personal Items Webpage</h1>"

for i in range(COUNT_PAGES):
    index_html += f'<a href="{naming_convention.format(num=i)}.html">{naming_convention.format(num=i)}</a><br>'

index_html += "</body></html>"

file = open("index.html", "w")
file.write(index_html)
file.close()

print("Success")