import os
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox

APP_TITLE = "Microsoft Windows UEFI CA 2023 チェッカー"

def get_powershell_path():
    # 64bitプロセスなら System32 をそのまま使える
    windir = os.environ.get("WINDIR", r"C:\Windows")
    return os.path.join(windir, "System32", "WindowsPowerShell", "v1.0", "powershell.exe")

def run_check():
    ps = get_powershell_path()
    ps_script = "[System.Text.Encoding]::ASCII.GetString((Get-SecureBootUEFI -Name db).Bytes) -match 'Windows UEFI CA 2023'"

    try:
        completed = subprocess.run(
            [ps, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass", "-Command", ps_script],
            capture_output=True, text=True, encoding="utf-8", timeout=20
        )
    except FileNotFoundError:
        return ("エラー", "Windows PowerShell が見つかりません。")
    except subprocess.TimeoutExpired:
        return ("エラー", "PowerShell の実行がタイムアウトしました。")

    stdout = (completed.stdout or "").strip()
    stderr = (completed.stderr or "").strip()

    if stderr:
        msg = stderr
        low = stderr.lower()
        if "requires elevated" in low or "administrator" in low:
            return ("権限エラー", "管理者権限での実行が必要です。")
        if "cmdlet not supported" in low or "secure boot is not supported" in low:
            return ("未対応", "このデバイスでは Secure Boot/UEFI 変数の取得がサポートされていません。")
        return ("エラー", msg)

    if stdout.lower() == "true":
        return ("適用済み", "Microsoft Windows UEFI CA 2023 が db に含まれています。")
    elif stdout.lower() == "false":
        return ("未適用", "Microsoft Windows UEFI CA 2023 は見つかりませんでした。")
    else:
        return ("不明", f"想定外の出力: {stdout}")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry("520x200")

        self.status_var = tk.StringVar(value="未チェック")
        self.detail_var = tk.StringVar(value="")

        tk.Label(self, text="Microsoft Windows UEFI CA 2023 の適用状況を確認します", font=("Segoe UI", 12)).pack(pady=(12, 8))
        tk.Label(self, textvariable=self.status_var, font=("Segoe UI", 14, "bold")).pack()
        tk.Label(self, textvariable=self.detail_var, wraplength=480, justify="left").pack(pady=(4, 12))

        btn_frame = tk.Frame(self)
        btn_frame.pack()
        tk.Button(btn_frame, text="チェック", width=12, command=self.on_check).pack(side="left", padx=6)
        tk.Button(btn_frame, text="終了", width=8, command=self.destroy).pack(side="left", padx=6)

        # 起動時に自動チェックしたい場合は以下を有効化
        # self.after(200, self.on_check)

    def on_check(self):
        self.status_var.set("確認中…")
        self.detail_var.set("")
        self.update_idletasks()
        status, detail = run_check()
        self.status_var.set(status)
        self.detail_var.set(detail)

if __name__ == "__main__":
    app = App()
    app.mainloop()