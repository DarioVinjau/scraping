import json
from matplotlib import markers, pyplot  as plt
from matplotlib import dates as mpl_dates
from datetime import datetime,timedelta

def parsing_json(json_path):
    with open(json_path,'r') as f:
        json_string = f.read()
    return json.loads(json_string)

def disegna_tutti(dati):

    x=[]
    y=[]

    for item in dati:
        
        lista_date=dati[item]['storico']
        
        for chiave, valore in lista_date.items():
        
            x.append(chiave)
            y.append(int(valore))
        
        for i in range(len(x)):
            x[i]=datetime.strptime(x[i], '%Y-%m-%d').date()

        plt.plot(x,y,marker='o')        
        
        plt.title(item)
        # plt.xticks(rotation=90)
        plt.gcf().autofmt_xdate()
        # plt.gca().xaxis.set_major_formatter(mpl_dates.DateFormatter('%d %b %Y'))
        # plt.grid()
        
        plt.show()
        # plt.savefig("grafici\\"+item+".png")

disegna_tutti(parsing_json("src\json_file\dati.json"))