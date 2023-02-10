
import os
import sys
import glob
import webbrowser

import random
import string


height = 250
width = 350

# n文字のランダム文字列
def randomChar(n):
    return ''.join(random.choice(string.ascii_letters) for x in range(n))

# html作成
def writePictureSoundList(file, str):
    with open(file, 'w', encoding='utf-8') as f:
        f.write(str)
    return 0


if __name__ == '__main__':
    args = sys.argv
    target = ""
    if (2 <= len(args) and os.path.isdir(args[1])):
        print(1)
        target = args[1]
    else:
        print(2)
        target = '\\'.join(os.path.abspath(__file__).split('\\')[:-1])
    jump1s = []
    jump2s = []
    jump3s = []
    tag1s = []
    tag2s = []
    tag3s = []
    abths = [os.path.abspath(i) for i in glob.glob("{}/**/*".format(target), recursive=True)]
    abths = filter(lambda x: os.path.splitext(x)[1].lower() in [".gif", ".webp", ".jpeg", ".jpg", ".png"], abths)
    abths = sorted(abths, key=lambda x: "\\".join(x.split('\\')[:-1]))
    id = ''
    tempOld = ''
    for abth in abths:
        tempNew = "\\".join(abth.split('\\')[:-1])
        if tempOld != tempNew:
            if tempOld != '':
                tag1s.append(f'</div>')
            id = randomChar(len(tempNew))
            jump1s.append(f'<a href="#{id}">{tempNew}</a>')
            tag1s.append(f'<li class="list_frame" data-value="{id}">{tempNew}</li>')
            tag1s.append(f'<div id="{id}">')
            tempOld = tempNew
        name = os.path.abspath(abth).split('\\')[-1]
        tag1s.append(f'<div class="pic_frame"><img src="{abth}" title="{abth}" height="{height}" width="{width}"><p>{name}</p></div>')
    tag1s.append(f'</div>')

    abths = [os.path.abspath(i) for i in glob.glob("{}/**/*".format(target), recursive=True)]
    abths = filter(lambda x: os.path.splitext(x)[1].lower() in [".mp3"], abths)
    abths = sorted(abths, key=lambda x: "\\".join(x.split('\\')[:-1]))
    id = ''
    tempOld = ''
    for abth in abths:
        tempNew = "\\".join(abth.split('\\')[:-1])
        if tempOld != tempNew:
            if tempOld != '':
                tag2s.append(f'</div>')
            id = randomChar(len(tempNew))
            jump2s.append(f'<a href="#{id}">{tempNew}</a>')
            tag2s.append(f'<li class="list_frame" data-value="{id}">{tempNew}</li>')
            tag2s.append(f'<div id="{id}">')
            tempOld = tempNew
        name = os.path.abspath(abth).split('\\')[-1]
        tag2s.append(f'<figure><figcaption>{name}</figcaption><audio controls src="{abth}"><a href="{abth}"></a></audio></figure>')
    tag2s.append(f'</div>')

    abths = [os.path.abspath(i) for i in glob.glob("{}/**/*".format(target), recursive=True)]
    abths = filter(lambda x: os.path.splitext(x)[1].lower() in [".mp4"], abths)
    abths = sorted(abths, key=lambda x: "\\".join(x.split('\\')[:-1]))
    id = ''
    tempOld = ''
    for abth in abths:
        tempNew = "\\".join(abth.split('\\')[:-1])
        if tempOld != tempNew:
            if tempOld != '':
                tag3s.append(f'</div>')
            id = randomChar(len(tempNew))
            jump3s.append(f'<a href="#{id}">{tempNew}</a>')
            tag3s.append(f'<li class="list_frame" data-value="{id}">{tempNew}</li>')
            tag3s.append(f'<div id="{id}">')
            tempOld = tempNew
        name = os.path.abspath(abth).split('\\')[-1]
        tag3s.append(f'<div class="pic_frame"><video controls src="{abth}" title="{abth}" height="{height}" width="{width}"><p>{name}</p></div>')
    tag3s.append(f'</div>')

    str = '''
    <html>
    <head>
        <meta charset="utf-8">
        <title>pictureSoundList</title>
    </head>
    <body>
        <div class="area">
            <input type="radio" name="tab_name" id="tab1" checked>
            <label class="tab_class" for="tab1">jpeg, png, webp, gif</label>
            <div class="content_class">
                <div>
                ''' + "".join(jump1s) + '''
                </div>
                <ul>
                ''' + "".join(tag1s) + '''
                </ul>
            </div>
            <input type="radio" name="tab_name" id="tab2" >
            <label class="tab_class" for="tab2">mp3</label>
            <div class="content_class">
                <div>
                ''' + "".join(jump2s) + '''
                </div>
                <ul>
                ''' + "".join(tag2s) + '''
                </ul>
            </div>
            <input type="radio" name="tab_name" id="tab3" >
            <label class="tab_class" for="tab3">mp4</label>
            <div class="content_class">
                <div>
                ''' + "".join(jump3s) + '''
                </div>
                <ul>
                ''' + "".join(tag3s) + '''
                </ul>
            </div>
        </div>
        <button type=“button” class="fixed-btn" onclick="window.scroll({top: 0, behavior: 'smooth'});">Topへ</button>
    </body>
    </html>
    <script>
        Array.from(document.getElementsByTagName("img"))
            .forEach(v => v.addEventListener("click", event => {
                navigator.clipboard.writeText(event.target.title)
                    .then(e => {
                        alert(event.target.title + "をコピー")
                    })
            }, false))
        Array.from(document.getElementsByTagName("audio"))
            .forEach(v => v.addEventListener("click", event => {
                navigator.clipboard.writeText(event.target.title)
                    .then(e => {
                        alert(event.target.title + "をコピー")
                    })
            }, false))
        Array.from(document.getElementsByTagName("li"))
            .forEach(v => {
                v.addEventListener('click', event => {
                    document.getElementById(v.getAttribute("data-value")).classList.toggle('data_hidden')
                    v.classList.toggle('list_hidden')
                })
            }, false)
    </script>
    <style>
        .area {
                width: 95%;
                margin: auto;
                flex-wrap: wrap;
                display: flex;
            }

        .tab_class {
            width: calc(100%/5);
            height: 50px;
            background-color: darkgrey;
            line-height: 50px;
            font-size: 15px;
            text-align: center;
            display: block;
            float: left;
            order: -1;
        }

        input[name="tab_name"] {
            display: none;
        }

        input:checked + .tab_class {
            background-color: cadetblue;
            color: aliceblue;
        }

        .content_class {
            display: none;
            width: 100%;
        }

        input:checked + .tab_class + .content_class {
            display: block;
        }

        .pic_frame {
            display: inline-block;
            text-align: center;
        }
        .data_hidden {
            display: none;
        }
        .list_frame.list_hidden {
            background-color: lavender;
        }
        .list_frame {
            background-color: pink;
            line-height: 1.5;
            padding: 0.5em 0;
            border-top: medium dashed blue;
        }
        .fixed-btn {
            position:fixed;
            right:20px;
            bottom:20px;
        }
        body {
            background-color: aliceblue;
        }
    </style>
    '''

    path = os.path.dirname(__file__) + "/"
    file = path + "pictureSoundList.html"
    writePictureSoundList(file, str)
    webbrowser.open(file)
