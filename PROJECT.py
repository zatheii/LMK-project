import tkinter as tk
from tkinter import ttk
import currencyapicom



#api meghivasa
client = currencyapicom.Client('cur_live_KSzQSEMTMP79wPs8FK8cytlM04wAw7UvcaMphCHL')
result = client.latest()

#currencyk kivetele az apibol
class currencies:
    AED = result['data']['AED']['value']
    AFN = result['data']['AFN']['value']
    ALL = result['data']['ALL']['value']
    AMD = result['data']['AMD']['value']
    ANG = result['data']['ANG']['value']
    AOA = result['data']['AOA']['value']
    ARS = result['data']['ARS']['value']
    AUD = result['data']['AUD']['value']
    AWG = result['data']['AWG']['value']
    AZN = result['data']['AZN']['value']
    BAM = result['data']['BAM']['value']
    BBD = result['data']['BBD']['value']
    BDT = result['data']['BDT']['value']
    BGN = result['data']['BGN']['value']
    BHD = result['data']['BHD']['value']
    BIF = result['data']['BIF']['value']
    BMD = result['data']['BMD']['value']
    BND = result['data']['BND']['value']
    BOB = result['data']['BOB']['value']
    BRL = result['data']['BRL']['value']
    BSD = result['data']['BSD']['value']
    BTC = result['data']['BTC']['value']
    BTN = result['data']['BTN']['value']
    BWP = result['data']['BWP']['value']
    BYN = result['data']['BYN']['value']
    BYR = result['data']['BYR']['value']
    BZD = result['data']['BZD']['value']
    CAD = result['data']['CAD']['value']
    CDF = result['data']['CDF']['value']
    CHF = result['data']['CHF']['value']
    CLF = result['data']['CLF']['value']
    CLP = result['data']['CLP']['value']
    CNY = result['data']['CNY']['value']
    COP = result['data']['COP']['value']
    CRC = result['data']['CRC']['value']
    CUC = result['data']['CUC']['value']
    CUP = result['data']['CUP']['value']
    CVE = result['data']['CVE']['value']
    CZK = result['data']['CZK']['value']
    DJF = result['data']['DJF']['value']
    DKK = result['data']['DKK']['value']
    DOP = result['data']['DOP']['value']
    DZD = result['data']['DZD']['value']
    EGP = result['data']['EGP']['value']
    ETB = result['data']['ETB']['value']
    EUR = result['data']['EUR']['value']
    FJD = result['data']['FJD']['value']
    GBP = result['data']['GBP']['value']
    GEL = result['data']['GEL']['value']
    GHS = result['data']['GHS']['value']
    GMD = result['data']['GMD']['value']
    GNF = result['data']['GNF']['value']
    GTQ = result['data']['GTQ']['value']
    GYD = result['data']['GYD']['value']
    HKD = result['data']['HKD']['value']
    HNL = result['data']['HNL']['value']
    HRK = result['data']['HRK']['value']
    HTG = result['data']['HTG']['value']
    HUF = result['data']['HUF']['value']
    IDR = result['data']['IDR']['value']
    ILS = result['data']['ILS']['value']
    INR = result['data']['INR']['value']
    IQD = result['data']['IQD']['value']
    IRR = result['data']['IRR']['value']
    ISK = result['data']['ISK']['value']
    JMD = result['data']['JMD']['value']
    JOD = result['data']['JOD']['value']
    JPY = result['data']['JPY']['value']
    KES = result['data']['KES']['value']
    KGS = result['data']['KGS']['value']
    KHR = result['data']['KHR']['value']
    KMF = result['data']['KMF']['value']
    KRW = result['data']['KRW']['value']
    KWD = result['data']['KWD']['value']
    KYD = result['data']['KYD']['value']
    KZT = result['data']['KZT']['value']
    LAK = result['data']['LAK']['value']
    LBP = result['data']['LBP']['value']
    LKR = result['data']['LKR']['value']
    LRD = result['data']['LRD']['value']
    LSL = result['data']['LSL']['value']
    LTL = result['data']['LTL']['value']
    LVL = result['data']['LVL']['value']
    LYD = result['data']['LYD']['value']
    MAD = result['data']['MAD']['value']
    MDL = result['data']['MDL']['value']
    MGA = result['data']['MGA']['value']
    MKD = result['data']['MKD']['value']
    MMK = result['data']['MMK']['value']
    MOP = result['data']['MOP']['value']
    MRO = result['data']['MRO']['value']
    MUR = result['data']['MUR']['value']
    MVR = result['data']['MVR']['value']
    MWK = result['data']['MWK']['value']
    MXN = result['data']['MXN']['value']
    MYR = result['data']['MYR']['value']
    MZN = result['data']['MZN']['value']
    NAD = result['data']['NAD']['value']
    NGN = result['data']['NGN']['value']
    NIO = result['data']['NIO']['value']
    NOK = result['data']['NOK']['value']
    NPR = result['data']['NPR']['value']
    NZD = result['data']['NZD']['value']
    OMR = result['data']['OMR']['value']
    PAB = result['data']['PAB']['value']
    PEN = result['data']['PEN']['value']
    PGK = result['data']['PGK']['value']
    PHP = result['data']['PHP']['value']
    PKR = result['data']['PKR']['value']
    PLN = result['data']['PLN']['value']


#main class
class main:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry('400x300')
        self.is_dark_mode = False


        #grid
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)

        #currency valasztasi lehetosegek
        self.options = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ETB', 'EUR', 'FJD', 'GBP', 'GEL', 'GHS', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'INR', 'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN']

        #title
        self.title_label = ttk.Label(self.root, text="Valós idejű valutaváltás", font="calibri 16")
        self.title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        #dropbox1
        self.combobox1 = ttk.Combobox(self.root, values=self.options)
        self.combobox1.set("Válassz egy valutát")
        self.combobox1.grid(row=1, column=0, padx=10, pady=10)

        #érték megadása
        self.amount_entry = ttk.Entry(self.root)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10)

        #dropbox2
        self.combobox2 = ttk.Combobox(self.root, values=self.options)
        self.combobox2.set("Válassz egy valutát")
        self.combobox2.grid(row=1, column=2, padx=10, pady=10)

        #convert
        self.button = ttk.Button(self.root, text="Konvertálás", command=self.convert_currency)
        self.button.grid(row=2, column=1, padx=10, pady=20)

        #output
        self.result_label = ttk.Label(self.root, text="Eredmény: ")
        self.result_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        self.dark_mode_button = tk.Button(self.root, text="Váltás sötét módra", command=self.toggledarkmode)
        self.dark_mode_button.grid(row=5, column=2, padx=10, pady=10)

    # Function to convert currency
    def convert_currency(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.combobox1.get()
            to_currency = self.combobox2.get()

            # Get exchange rates from the Currencies class
            from_rate = getattr(currencies, from_currency, None)
            to_rate = getattr(currencies, to_currency, None)

            if from_rate and to_rate:
                # Convert the amount
                converted_amount = amount * (to_rate / from_rate)
                self.result_label.config(text=f"Eredmény: {amount} {from_currency} = {converted_amount:.2f} {to_currency}")
            else:
                self.result_label.config(text="Please select valid currencies.")
        except ValueError:
            self.result_label.config(text="Írj be egy megfelelő összeget.")

    def update_colors(self):
        if self.is_dark_mode:
            self.root.config(bg='black')
            self.title_label.config(bg='black', fg='white')
            self.result_label.config(bg='black', fg='white')
              # Dark mode for convert button
            self.dark_mode_button.config(bg='gray', fg='white', text="Váltás világos módra")
        else:
            self.root.config(bg='white')
            self.title_label.config(bg='white', fg='black')
            self.result_label.config(bg='white', fg='black')

            self.dark_mode_button.config(bg='lightgray', fg='black', text="Váltás sötét módra")

    def toggledarkmode(self):
        self.is_dark_mode = not self.is_dark_mode
        self.update_colors()


# Create the main window and run the app
if __name__ == "__main__":
    window = tk.Tk()
    app = main(window)
    window.mainloop()





