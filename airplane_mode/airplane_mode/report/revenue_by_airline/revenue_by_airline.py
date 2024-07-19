import frappe

def execute(filters=None):
    frappe.errprint(filters)
    
    columns = [
        {
            "fieldname": "airline",
            "label": "Airline",
            "fieldtype": "Link",
            "width": 200
        },
        {
            "fieldname": "revenue",
            "label": "Revenue", 
            "fieldtype": "Currency",
            "width": 150
        }
    ]
    

    airlines = frappe.get_all("Airplane", fields=["DISTINCT airline"])
    
  
    revenue_by_airline = {airline['airline']: 0 for airline in airlines}
 
    tickets = frappe.get_all("Airplane Ticket", fields=["flight", "total_amount"])
    
    for ticket in tickets:
        flight_name = ticket.get("flight")
        if not flight_name:
            continue
        

        airplane_name = "-".join(flight_name.split("-")[:2])
        
        airline = frappe.get_value("Airplane", airplane_name, "airline")
        if not airline:
            continue
        
       
        revenue_by_airline[airline] += ticket.total_amount
    
    data = [{"airline": airline, "revenue": revenue} for airline, revenue in revenue_by_airline.items()]
    chart = get_chart(data)
    return columns, data, None, chart , None


def get_chart(data):
    return{
        "data":{
            "labels": [d["airline"] for d in data],
            "datasets": [{"name": "Revenue By Airline", "values": [d["revenue"] for d in data]}]
        },
        "type": "donut"
    }
    
