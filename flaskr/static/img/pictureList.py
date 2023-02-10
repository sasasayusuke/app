
import os
import glob
import webbrowser
import random
import string

# y文字のランダム文字列
def randomChar(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

# html作成
def writePictureList(file, str):
    with open(file, 'w', encoding='utf-8') as f:
        f.write(str)
    return 0

target = '\\'.join(os.path.abspath(__file__).split('\\')[:-1])
tags = []
height = 240
width = 360
abths = [os.path.abspath(i) for i in glob.glob("{}/**/*".format(target), recursive=True)]
abths = filter(lambda x: os.path.splitext(x)[1].lower() in [".gif"], abths)
abths = sorted(abths, key=lambda x: "\\".join(x.split('\\')[:-1]))
id = ''
tempOld = ''
for abth in abths:
    tempNew = "\\".join(abth.split('\\')[:-1])
    if tempOld != tempNew:
        if tempOld != '':
            tags.append(f'</div>')
        id = randomChar(len(tempNew))
        tags.append(f'<li class="list_frame" data-value="{id}">{tempNew}</li>')
        tags.append(f'<div id="{id}">')
        tempOld = tempNew

    name = os.path.abspath(abth).split('\\')[-1]
    tags.append(f'<div class="pic_frame"><img src="{abth}" title="{abth}" height="{height}" width="{width}"><p>{name}</p></div>')
    #elif (os.path.splitext(abth)[1].lower() in [".mp4"]):
    #    body = body + f'<video src="{abth}" title="{abth}" type="video/mp4" controls="" muted="" autoplay="" playinline="" loop="" height="{height}" width="{width}"></video>'
tags.append(f'</div>')


str = '''
<html>
<head>
<meta charset="utf-8">
<title>pictureList</title>
</head>
<body>
<ul>
''' + "".join(tags) + '''
</ul>
</body>
</html>
<script>
Array.from(document.getElementsByTagName("img"))
    .forEach(v => {
        v.addEventListener("click", event => {
            console.log("window.innerWidth:" + window.innerWidth)
            console.log("event.target.naturalWidth:" + event.target.naturalWidth)
            console.log("event.target.naturalHeight:" + event.target.naturalHeight)
            console.log("event.target.width:" + event.target.width)
            console.log("event.target.height:" + event.target.height)

            let widRatio = window.innerWidth / event.target.naturalWidth
            event.target.width = event.target.naturalWidth
            event.target.height = event.target.naturalHeight

            navigator.clipboard.writeText(event.target.title)

	    })
        v.addEventListener("dblclick", event => {
            console.log("window.innerWidth:" + window.innerWidth)
            console.log("event.target.naturalWidth:" + event.target.naturalWidth)
            console.log("event.target.naturalHeight:" + event.target.naturalHeight)
            console.log("event.target.width:" + event.target.width)
            console.log("event.target.height:" + event.target.height)

            let widRatio = window.innerWidth / event.target.naturalWidth
            event.target.width = window.innerWidth
            event.target.height = event.target.naturalHeight * widRatio
	    })
    }, false)
Array.from(document.getElementsByTagName("li"))
    .forEach(v => {
        v.addEventListener('click', event => {
            document.getElementById(v.getAttribute("data-value")).classList.toggle('data_hidden')
            v.classList.toggle('list_hidden')
        })
    }, false)

</script>
<style>
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
body {
    background-color: aliceblue;
}
</style>
'''

path = os.path.dirname(__file__) + "/"
file = path + "pictureList.html"
writePictureList(file, str)
webbrowser.open(file)