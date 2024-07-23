frappe.listview_settings['Airplane Ticket'] = {
    get_indicator(doc) {
        if (doc.status == "Booked") {
            return [__("Booked"), "blue", "status=Booked"];
        } else if (doc.status == "Checked-In") {
            return [__("Checked-In"), "orange", "status=Checked-In"];
        } else if (doc.status == "Boarded") {
            return [__("Boarded"), "green", "status=Boarded"];
        } else {
            return [__("Else"), "darkgrey", "status = else"];
        }
    },
}
