from config.app import *
import pandas as pd

def GenerateReportVentas(app: App):
    conn = app.bd.getConection()
    ventas = pd.read_sql_query("SELECT * FROM VENTAS", conn)
    postalcodes = pd.read_sql_query("SELECT * FROM POSTALCODE", conn)

    reporte = ventas.merge(postalcodes, left_on='postal_code', right_on='code')
    reporte = reporte.groupby(['pais', 'product_id'])['quantity'].sum().reset_index()
    reporte = reporte.sort_values('quantity', ascending=False)
    reporte.columns = ['pais', 'producto', 'total_vendido']
    
    fecha = "10-02-2025" 
    path = f"/workspaces/practica_python_datux/proyecto/files/reporte_ventas_{fecha}.csv"
    reporte.to_csv(path, index=False)
    sendMail(app, path)

def sendMail(app: App, data):
    app.mail.send_email('from@example.com', 'Reporte de ventas', 'Reporte de ventas', data)
