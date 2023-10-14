from bs4 import BeautifulSoup


SIMPLE_HTML = """
<html>
<head></head>
<body>
    <h1>This is a title</h1>
    <h1> test </h1>
    <p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
    <p>Here's another p without a class</p>
    <ul>
        <li>Sergi</li>
        <li>Mat</li>
        <li>Sophie</li>
        <li>Markus</li>
    </ul>
</body>
</html
"""

# class with 2 arguments: file and document type
simple_soup = BeautifulSoup(SIMPLE_HTML, "html.parser")


def find_title():
    print(simple_soup.find("h1").string)  # Output: This is a title


def find_list_items():
    list_items = simple_soup.findAll("li")
    print(list_items)  # Output: [<li>Sergi</li>, <li>Mat</li>, <li>Sophie</li>,..]
    list_contents = [item.string for item in list_items]
    print(list_contents)  # Output: ['Sergi', 'Mat', 'Sophie', 'Markus']


def find_subtitle():
    paragraph = simple_soup.find("p", {"class": "subtitle"})
    print(paragraph.string)  # Output: Lorem ipsum dolor sit amet..


def find_other_paragraph():
    paragraphs = simple_soup.find_all("p")
    print(paragraphs)
    # Output: [
    #   <p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>,
    #   <p>Here's another p without a class</p>
    # ]
    # in the get("whatever", []), the 2nd argument returns empty list if attr is not found
    other_paragraph = [
        p for p in paragraphs if "subtitle" not in p.attrs.get("class", [])
    ]
    # Output: Here's another p without a class
    print(other_paragraph[0].string)


def test():
    find_title()
    find_list_items()
    find_subtitle()
    find_other_paragraph()
