from countryinfo import CountryInfo
import tkinter as tk

def get_info():
    try:
        country = name.get()
        country = CountryInfo(country)
        
        texto_resposta['text'] = f'''
        Native name: {country.native_name().title()}
        Others names: {country.alt_spellings()}
        Capital: {country.capital()}
        Nationality: {country.demonym()}
        Languages: {country.languages()}
        Currencies: $ {country.currencies()}
        Population: {country.population()}
        Timezone: {country.timezones()}
        Area: {country.area()}
        Top Level Domain: {country.tld()}
        ISO Codes: {country.iso()}
        Calling Codes: {country.calling_codes()}
        Region: {country.region()}
        Subregion: {country.subregion()}
        Link Wikipedia: {country.wiki()}
        '''
    except:
        texto_resposta['text'] = 'Country not found!'

janela = tk.Tk()
janela.geometry("850x450")
janela.title("CountryInfo Tool")
#janela.resizable(0, 0)

janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=3)


label_countrytool = tk.Label(text="CountryInfo", borderwidth=2, relief='solid', fg="black", bg="white",font = ('Helvetica',12,'bold'))
label_countrytool.grid(row=0, column=0, sticky='nswe', columnspan=3, padx=10, pady=10)

label_country = tk.Label(text="Enter the name of a country:", anchor='w',font = ('Helvetica',10,'bold'))
label_country.grid(row=1, column=0,padx=10, pady=10, sticky='nswe', columnspan=2)

name = tk.Entry(width=10)
name.grid(row=1, column=1, padx=10, pady=10, sticky='we')

botao_country = tk.Button(text="OK", command=get_info, width=15, font = ('Helvetica',10,'normal'))
botao_country.grid(row=2, column=1, padx=5, pady=5, sticky='e', columnspan=3)

texto_resposta = tk.Label(text="")
texto_resposta.grid(row=3,column=0,padx=10, pady=10, sticky='nswe', columnspan=3)

janela.mainloop()