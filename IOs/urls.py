def read_urls():
    """
    From the searched_urls file
    :return: a list of urls
    """
    all_urls = []
    with open("C:\\Users\\maxim\\PYTHON\\Appli_alerte\\searched_urls.txt") as file_of_urls:
        for index, line in enumerate(file_of_urls.readlines()):
            all_urls.append(line.strip())
    file_of_urls.close()
    return all_urls
