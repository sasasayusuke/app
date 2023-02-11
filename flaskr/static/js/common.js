async function commonFetch(url) {
    let columnNames = {}
    // 取得済み(保存用変数から取得)

    let data = await fetch(url)
    let html = await data.text()
    let dom = new DOMParser().parseFromString(html, 'text/html')
    columnNames = JSON.parse(dom.getElementById("Columns").value)
    let obj = {}
    obj[tableId] = {}
    // 保存用変数
    for (let c of columnNames) obj[tableId][c.ColumnName] = c.LabelText
    return obj
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
