import html5lib


def test_h1_contains_jerbear():
    """Parse index.html and ensure <h1> contains 'Jerbear'."""
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    # Parse using html5lib to ensure proper HTML5 parsing
    tree = html5lib.parse(html_content, treebuilder="etree")

    # Find the first h1 element
    h1_elements = tree.findall(".//{http://www.w3.org/1999/xhtml}h1")
    assert h1_elements, "No <h1> tag found"
    h1_text = "".join(h1_elements[0].itertext()).strip()

    assert "jerbear" in h1_text.lower(), "<h1> does not contain 'Jerbear'"
