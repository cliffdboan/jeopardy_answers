def clean_data(answer):
    """Strip the answers of any excess characters:
    "A", "The", "<i>", "&"

    Args:
        answer (html): should be a single jepoardy answer in the form of a string/an html tag
    """
    cleaned = answer.get_attribute("innerHTML")
    cleaned = cleaned.replace("&amp;", "")
    cleaned = cleaned.replace("<i>", "")
    cleaned = cleaned.replace("</i>", "")
    cleaned = cleaned.strip('"')
    cleaned = cleaned.lower()
    return cleaned
