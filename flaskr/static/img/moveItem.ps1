
# ファイル移動
#
# @param    toFolder    目的パス
# @param    fromFile    移動対象
#
Param (
    [parameter(mandatory = $true)][string] $toFolder,
    [parameter(mandatory = $true)][array] $fromFile
)

$current = $PSScriptRoot
Set-Location $current

if (!$toFolder.Contains($current)) {
    Write-Output $toFolder "が外です"
    break
}
$fromFile | ForEach-Object {
    if (!(Test-Path $_)) {
        Write-Output $_ "が存在しません。"
    } elseif (!$_.Contains($current)) {
        Write-Output $_ "が外です"
    } else {
        if(!(Test-Path $toFolder))
        {
            Write-Output $toFolder "を作成しました。"
            New-Item -Path $toFolder -ItemType Directory -Force | Out-Null
        }

        Write-Output $toFolder "へ移動しました。"
        Move-Item $_ $toFolder
    }
}

python .\pictureList.py