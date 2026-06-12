import tkinter as tk, time, threading, random; from tkinter import ttk
CIHAZLAR = ["Galaxy S26 Ultra", "Galaxy S25+", "Galaxy S24 FE", "Galaxy Z Fold7", "Galaxy Z Flip7"]
SABIT_DOSYALAR = {"PIT": "partition.pit", "BOOT": "boot.img", "SYSTEM": "system.img", "USERDATA": "userdata.img"}
DOSYA_BOYUTLARI = {"PIT": 4, "BOOT": 96, "SYSTEM": 6450, "USERDATA": 12800}

class UltimateSamsungSuite(tk.Tk):
    def __init__(self):
        super().__init__(); self.title("Samsung Suite v7.0 PRO"); self.geometry("1100x680+40+10"); self.configure(bg="#121212")
        self.secilen = {k: False for k in SABIT_DOSYALAR.keys()}; self.flashing = False; self.current_device = tk.StringVar(value=CIHAZLAR)
        
        # --- LOG PANEL ---
        self.sol = tk.Frame(self, bg="#121212", width=350, bd=2, relief="solid"); self.sol.pack(side="left", fill="both", padx=10, pady=10); self.sol.pack_propagate(False)
        self.log = tk.Text(self.sol, bg="#050505", fg="#00FF00", font=("Courier", 8), bd=2, relief="sunken"); self.log.pack(fill="both", expand=True, padx=5, pady=5)
        self.log_yaz("[INIT] Knox Engine v4.2 Secure Boot Active.\n[SYS] Awaiting smartphone hardware socket input...")
        
        # --- ODIN KONSOL ---
        self.orta = tk.Frame(self, bg="#F5F5F5", width=420, bd=2, relief="raised"); self.orta.pack(side="left", fill="both", pady=10); self.orta.pack_propagate(False)
        self.dev_menu = ttk.Combobox(self.orta, textvariable=self.current_device, values=CIHAZLAR, state="readonly"); self.dev_menu.pack(pady=10); self.dev_menu.bind("<<ComboboxSelected>>", self.ch_dev)
        self.p_var = tk.DoubleVar(); ttk.Progressbar(self.orta, variable=self.p_var, maximum=100).pack(fill="x", padx=10, pady=5)
        
        self.entries = {}; self.cbs = {}
        for k in SABIT_DOSYALAR.keys():
            row = tk.Frame(self.orta, bg="#F5F5F5"); row.pack(fill="x", padx=10, pady=5)
            tk.Button(row, text=k, font=("Arial", 8, "bold"), width=8, command=lambda x=k: self.sec(x)).pack(side="left")
            ent = tk.Entry(row, bg="white", font=("Arial", 8), width=30); ent.pack(side="left", padx=5); self.entries[k] = ent
            v = tk.BooleanVar(); tk.Checkbutton(row, variable=v, bg="#F5F5F5", state="disabled").pack(side="right"); self.cbs[k] = v
            
        tk.Button(self.orta, text="START FLASH", bg="#1f4e79", fg="white", font=("Arial", 9, "bold"), command=self.baslat).pack(side="left", padx=20, pady=20)
        tk.Button(self.orta, text="RESET", bg="#444444", fg="white", font=("Arial", 9, "bold"), command=self.sifirla).pack(side="right", padx=20, pady=20)
        
        # --- TELEFON PANEL ---
        self.sag = tk.Frame(self, bg="#121212", width=280, bd=2, relief="solid"); self.sag.pack(side="left", fill="both", padx=10, pady=10); self.sag.pack_propagate(False)
        self.tel = tk.Frame(self.sag, bg="#008080", bd=4, relief="ridge", width=240, height=440); self.tel.pack(pady=5); self.tel.pack_propagate(False)
        self.t_icon = tk.Label(self.tel, text="⬇", font=("Arial", 40), bg="#008080", fg="white"); self.t_icon.pack(pady=40)
        self.t_lbl = tk.Label(self.tel, text="Downloading...", font=("Arial", 14, "bold"), bg="#008080", fg="white"); self.t_lbl.pack()
        self.t_sub = tk.Label(self.tel, text="Do not turn off target", font=("Arial", 9), bg="#008080", fg="white"); self.t_sub.pack(pady=5)
        self.t_bar_var = tk.DoubleVar(); ttk.Progressbar(self.tel, variable=self.t_bar_var, maximum=100, length=160).pack(pady=10)
        
        # İstatistikler
        self.lbl_cpu = tk.Label(self.sag, text="CPU Temp: 31°C", bg="#121212", fg="white", font=("Courier", 8)); self.lbl_cpu.pack(anchor="w", padx=10)
        self.lbl_data = tk.Label(self.sag, text="Data Copied: 0 MB", bg="#121212", fg="white", font=("Courier", 8)); self.lbl_data.pack(anchor="w", padx=10)
        self.lbl_fan = tk.Label(self.sag, text="Cooling Fan: 0 RPM", bg="#121212", fg="white", font=("Courier", 8)); self.lbl_fan.pack(anchor="w", padx=10)

    def log_yaz(self, m): self.log.insert("end", m + "\n"); self.log.see("end")
    def ch_dev(self, e): self.log_yaz(f"[SYS] Device remapped to: {self.current_device.get()}")
    def sec(self, k): self.secilen[k] = True; self.cbs[k].set(True); self.entries[k].insert(0, f"C:\\Firmware\\{SABIT_DOSYALAR[k]}"); self.log_yaz(f"[QUEUE] {k} allocation successful.")
    
    def istatistik(self, t_mb):
        copied = 0
        while self.flashing:
            time.sleep(0.4); temp = random.randint(54, 73); copied += random.randint(140, 260); rpm = temp * 65
            if copied > t_mb: copied = t_mb
            self.lbl_cpu.configure(text=f"CPU Temp: {temp}°C", fg="#FF5722" if temp > 65 else "white")
            self.lbl_data.configure(text=f"Data Copied: {copied} / {t_mb} MB")
            self.lbl_fan.configure(text=f"Cooling Fan: {rpm} RPM")

    def motor(self):
        self.flashing = True; model = self.current_device.get(); aktifler = [k for k, v in self.secilen.items() if v]
        total_mb = sum([DOSYA_BOYUTLARI[k] for k in aktifler if k in DOSYA_BOYUTLARI])
        threading.Thread(target=self.istatistik, args=(total_mb,), daemon=True).start()
        self.log_yaz(f"[ODIN] Initializing hardware flash session for {model}..."); time.sleep(1.0); current_copied = 0
        
        for k in aktifler:
            f_size = DOSYA_BOYUTLARI[k]; self.log_yaz(f"[FLASH] Open partition link: '{k}' ({f_size} MB)...")
            self.t_sub.configure(text=f"Writing: {k} ({f_size}MB)"); steps = 14 if f_size > 500 else 4
            if k == "SYSTEM":
                self.log_yaz("[WARN] USB protocol latency spike detected! Re-stabilizing..."); time.sleep(0.8)
            for p in range(1, steps + 1):
                if not self.flashing: return
                time.sleep(0.4 if f_size > 500 else 0.1)
                current_copied += (f_size / steps); yuzde = int((current_copied / total_mb) * 100)
                self.p_var.set(yuzde); self.t_bar_var.set(yuzde)
                
        self.log_yaz("[ODIN] Firmware block writing finalized. Checking Knox e-Fuse status..."); time.sleep(1.2)
        self.log_yaz("[SYS] Knox Status: 0x0 VALID. All signatures verified successfully. [PASS]"); self.flashing = False
        
        # Telefon Yeniden Başlatma & Optimizasyon Döngüsü
        self.tel.configure(bg="#000000"); self.t_icon.configure(text="SAMSUNG", font=("Arial", 18, "bold"), bg="#000000")
        self.t_lbl.configure(text=model, font=("Arial", 11), bg="#000000"); self.t_sub.configure(text="Secured by Knox", bg="#000000", fg="gray")
        time.sleep(3); self.t_icon.configure(text="android", fg="#3DDC84"); self.t_lbl.configure(text="Optimizing apps... 32%"); time.sleep(1.0)
        self.t_lbl.configure(text="Optimizing apps... 84%"); time.sleep(1.0); self.t_lbl.configure(text="Starting Android OS..."); time.sleep(1.5); self.sifirla()

    def baslat(self):
        if not any(self.secilen.values()) or self.flashing: return
        threading.Thread(target=self.motor, daemon=True).start()

    def sifirla(self):
        self.p_var.set(0); self.t_bar_var.set(0); self.flashing = False; self.log.delete("1.0", "end")
        for k in self.secilen.keys(): self.secilen[k] = False; self.cbs[k].set(False); self.entries[k].delete(0, "end")
        self.tel.configure(bg="#008080"); self.t_icon.configure(text="⬇", font=("Arial", 40), bg="#008080", fg="white")
        self.t_lbl.configure(text="Downloading...", font=("Arial", 14, "bold"), bg="#008080"); self.t_sub.configure(text="Do not turn off target", bg="#008080", fg="white")
        self.lbl_cpu.configure(text="CPU Temp: 31°C", fg="white"); self.lbl_data.configure(text="Data Copied: 0 MB"); self.lbl_fan.configure(text="Cooling Fan: 0 RPM")

if __name__ == "__main__": app = UltimateSamsungSuite(); app.mainloop()
