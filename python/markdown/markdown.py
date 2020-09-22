import re


def parse(md: str):
    """
    Naievly convert Mardown into HTML
    """
    # Start by converting all headings in the document
    for i in range(1, 7):
        md = re.sub(rf"^{'#' * i} (.*?$)", rf"<h{i}>\1</h{i}>", md, flags=re.M)

    # Bold
    md = re.sub(r"__([^\n]+?)__", r"<strong>\1</strong>", md)

    # Italics
    md = re.sub(r"_([^\n]+?)_", r"<em>\1</em>", md)

    # Lists
    md = re.sub(r"^\* (.*?$)", r"<li>\1</li>", md, flags=re.M)
    md = re.sub(r"(<li>.*</li>)", r"<ul>\1</ul>", md, flags=re.S)

    # Paragraphs
    md = re.sub(r"^(?!<[hlu])(.*?$)", r"<p>\1</p>", md, flags=re.M)

    # Remove newlines
    md = re.sub(r"\n", "", md)

    return md
