# CA2023Check

PowerShellコマンドをPyInstallerでGUI化したツール。
以下のPowerShellコマンドをGUIツールとして実行させる単純なものです。

`[System.Text.Encoding]::ASCII.GetString((Get-SecureBootUEFI -Name db).Bytes) -match "Windows UEFI CA 2023"`

## 生成AIを使用して作成したツールです。

このツールは、**GPT-5.4 via Microsoft 365 Copilot**及び、**GPT-5.1 mini via GitHub Copilot** にて生成されたコードをビルドして作成されたものです。

## 使用方法

CA2023Check.exe を実行し、「チェック」ボタンを押下すると、結果が表示されます。
[!ScreenShot](sc.png)
