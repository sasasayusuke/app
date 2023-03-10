
PAGE_INDEX = "index"
PAGE_MASTER = "master"
PAGE_LIST = "list"
PAGE_RANDOM = "random"
PAGE_SEARCH_ILLUST = "search_illust"
PAGE_EXTRACT_IMAGE = "extract_image"
PAGE = [
    PAGE_INDEX,
    PAGE_MASTER,
    PAGE_LIST,
    PAGE_RANDOM,
    PAGE_SEARCH_ILLUST,
    PAGE_EXTRACT_IMAGE,
]
APPNAME = "flaskr"
PATH = "static/img/i_ver1"
ALLOWED = {
    PAGE_INDEX : True,
    PAGE_MASTER : True,
    PAGE_LIST : True,
    PAGE_RANDOM : True,
    PAGE_SEARCH_ILLUST : True,
    PAGE_EXTRACT_IMAGE : True,
}
ILLUST_URLS = [
    "https://www.irasutoya.com/search?q=",
    "https://illust8.com/?s=",
    "https://japaclip.com/?s=",
    "https://www.irasuton.com/search?q=",
    # "https://www.ac-illust.com/main/search_result.php?sl=ja&personalized=1&qid=&creator=&ngcreator=&nq=&srt=dlrank&orientation=all&format=all&color=all&search_word=",
]