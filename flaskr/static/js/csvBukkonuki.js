

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
/**
 * 引数のcsv文字列をCSVでダウンロードする関数です。
 * @param {String} csvStr csv文字列
 * @param {String} title ファイル名
 */
function commonDownloadCsv (csvStr, title = 'test') {

    // a要素を作成する
    const ele = document.createElement('a')
    // a要素にエンコード化した出力データを追加
    ele.setAttribute('href', encodeURI(csvStr))
    // a要素に出力情報を追加
    ele.setAttribute('download', title + '.csv')
    ele.style.visibility = 'hidden'
    document.body.appendChild(ele)
    // HTMLドキュメントに追加したa要素を実行(clickイベント発火)
    ele.click()
    document.body.removeChild(ele)
}
/**
   * 引数の2次元配列をUTF-8のCSVに変換する関数です。
   * @param {Array} array 2次元配列
   *
   * @return {String} csvData
   * 例. [
   *      ['数量', '単価', '合計'],
   *      ['1', '2', '2'],
   *      ['4', '5', '20'],
   *      ['7', '8', '56'],
   *     ]
   *            ⇓
   * 'data:text/csvcharset=utf-8,"数量","単価","合計"\r\n"1","2","2"\r\n"4","5","20"\r\n"7","8","56"\r\n'
   */
function commonConvert2DToCsv (d2array) {
    // csvDataに出力方法を追加
    let csvOutput = 'data:text/csvcharset=utf-8,'
    let csvData = csvOutput
    d2array.forEach(v => {
        const row = '"' + v.join('","') + '"'
        csvData += row + '\r\n'
    })
    return csvData
}
