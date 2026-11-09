# 自动提交并推送 python-12w
# 由 Windows 计划任务调用，日志写到 .autopush.log
param(
    [string]$Repo = "D:\Code\python-12w"
)

$log = Join-Path $Repo ".autopush.log"

function Write-Log {
    param([string]$Message)
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -Path $log -Value "[$ts] $Message" -Encoding UTF8
}

Set-Location $Repo

if (-not (Test-Path (Join-Path $Repo ".git"))) {
    Write-Log "ERROR: 不是 git 仓库"
    exit 1
}

$changes = git status --porcelain
if (-not $changes) {
    Write-Log "no changes, skip"
    exit 0
}

git add -A 2>&1 | Out-Null

$ts = Get-Date -Format "yyyy-MM-dd HH:mm"
$commit = git commit -m "auto: $ts" 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Log ("commit FAILED: " + ($commit -join " "))
    exit 1
}
Write-Log ("commit ok: auto: $ts")

$push = git push 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Log "push ok"
} else {
    Write-Log ("push FAILED: " + ($push -join " "))
    exit 1
}
