import customtkinter as ctk
import urllib.request as urllib2
import json

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")


class IPInfoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("IPLoc")
        self.geometry("200x300")

        self.iconbitmap("data/icon.ico")

        self.ip_label = ctk.CTkLabel(self, text="Enter IP")
        self.ip_label.pack(pady=5, padx=5)

        self.ip_entry = ctk.CTkEntry(self, width=300)
        self.ip_entry.pack(pady=5, padx=5)

        self.lookup_button = ctk.CTkButton(self, text="Lookup", command=self.lookup_ip)
        self.lookup_button.pack(pady=5, padx=5)

        self.output_text = ctk.CTkTextbox(self, width=350, height=200)
        self.output_text.pack(pady=5, padx=5)

    def lookup_ip(self):
        ip = self.ip_entry.get()
        if not ip:
            self.output_text.insert("1.0", "Please enter a valid IP address.\n")
            return

        url = "http://ip-api.com/json/"
        try:
            response = urllib2.urlopen(url + ip)
            data = response.read()
            values = json.loads(data)

            if values['status'] == "success":
                result = (
                    f"IP: {values['query']}\n"
                    f"Timezone: {values['timezone']}\n"
                    f"Country: {values['country']}\n"
                    f"Region: {values['region']}\n"
                    f"City: {values['city']}\n"
                    f"Zip: {values['zip']}\n"
                    f"ISP: {values['isp']}\n"
                )
            else:
                result = f"Error: {values['message']}\n"

        except Exception as e:
            result = f"Error fetching data: {e}\n"

        self.output_text.delete("1.0", ctk.END)
        self.output_text.insert("1.0", result)


if __name__ == "__main__":
    app = IPInfoApp()
    app.mainloop()