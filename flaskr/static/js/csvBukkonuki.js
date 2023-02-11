

//
let domain = location.href
let pageCount = Math.max(1, document.querySelectorAll(".pagenavi")[0].querySelectorAll(".part").length)

let idOrClass = "class"
let contentsId = "wrap"
let contentsClass = "datablock"
let pagesClass = "datablock"
let reg = /\d{2}:\d{2}:\d{2}.*ID:/

const main = "(L)本文読み上げ"
const subs = ["スレ民A","スレ民B","スレ民C","スレ民D","スレ民A","スレ民B","スレ民E","スレ民G" ,"スレ民F" ,"スレ民E"]
let IDs = []
let csv = []
let values = []

for (let i=1; i<=pageCount; i++) {
    IDs = []
    csv = []
    values = []
    let site = i == 1 ? `${domain}` : `${domain}${i}.htm`
    let data = await fetch(site)
    let html = await data.text()
    let dom = new DOMParser().parseFromString(html, 'text/html')
    let items = idOrClass == "id" ? dom.getElementById(contentsId).innerText.split("\n") : dom.getElementsByClassName(contentsClass)[0].innerText.split("\n")
    values = [...values, ...items]

    let character = main
    for (let val of values) {
        val = val.trim()
        if (val == "") continue
        if(reg.test(val)) {
            let id = val.split(reg)[1]
            if (!IDs.includes(id)) IDs.push(id)
            let no = IDs.indexOf(id)
            if (no == 0) {
                character = main
            } else {
                character = subs[(no % (subs.length - 1)) + 1]
            }
            continue
        }
        csv.push([character, val])
    }
    commonDownloadCsv(commonConvert2DToCsv(csv), `${domain}-${i}`)
}