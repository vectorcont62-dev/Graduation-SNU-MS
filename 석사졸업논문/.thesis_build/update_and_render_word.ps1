$ErrorActionPreference = "Stop"

$workingFile = Get-ChildItem -LiteralPath ".thesis_build" -Filter "*_working.docx" | Select-Object -First 1
if ($null -eq $workingFile) {
    throw "Working DOCX was not found."
}
$workingPath = $workingFile.FullName
$pdfPath = [System.IO.Path]::ChangeExtension($workingPath, ".pdf")

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
$word.Options.UpdateFieldsAtPrint = $true

try {
    $doc = $word.Documents.Open($workingPath, $false, $false, $false)
    try {
        foreach ($field in $doc.Fields) {
            [void]$field.Update()
        }
        foreach ($toc in $doc.TablesOfContents) {
            [void]$toc.Update()
        }
        foreach ($tof in $doc.TablesOfFigures) {
            [void]$tof.Update()
        }
        foreach ($section in $doc.Sections) {
            foreach ($header in $section.Headers) {
                foreach ($field in $header.Range.Fields) {
                    [void]$field.Update()
                }
            }
            foreach ($footer in $section.Footers) {
                foreach ($field in $footer.Range.Fields) {
                    [void]$field.Update()
                }
            }
        }
        [void]$doc.Repaginate()
        $pages = $doc.ComputeStatistics(2)
        $words = $doc.ComputeStatistics(0)
        $doc.Save()
        $doc.ExportAsFixedFormat($pdfPath, 17)
        Write-Output "pages=$pages words=$words pdf=$pdfPath"
    }
    finally {
        $doc.Close($false)
    }
}
finally {
    $word.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}
