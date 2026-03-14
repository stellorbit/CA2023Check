# CA2023Check

PowerShellコマンドをPyInstallerでGUI化したツール。
以下のPowerShellコマンドをGUIツールとして実行させる単純なものです。

`[System.Text.Encoding]::ASCII.GetString((Get-SecureBootUEFI -Name db).Bytes) -match "Windows UEFI CA 2023"`

**[ダウンロード](https://github.com/stellorbit/CA2023Check/releases/download/python-gui/CA2023Check.exe)**

## 生成AIを使用して作成したツールです。

このツールは、**GPT-5.4 via Microsoft 365 Copilot**及び、**GPT-5.1 mini via GitHub Copilot** にて生成されたコードをビルドして作成されたものです。

## 使用方法

CA2023Check.exe を実行し、「チェック」ボタンを押下すると、結果が表示されます。

<img width="522" height="232" alt="Image" src="https://github.com/user-attachments/assets/d3c6ea1b-0dc8-4105-b2c1-5e16af8ed52c" />
