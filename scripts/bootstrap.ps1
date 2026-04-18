Write-Host "Copying .env.example to .env if needed..."
if (-not (Test-Path ".env")) {
  Copy-Item ".env.example" ".env"
}

Write-Host "Bootstrap complete. Next steps:"
Write-Host "1. docker compose up -d postgres redis"
Write-Host "2. cd apps/api; pip install -r requirements.txt"
Write-Host "3. npm install"

