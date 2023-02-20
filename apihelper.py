def check_info(sent_data, required_data):
    for data in required_data:
        # if a user misses to fill out the field
        if(sent_data.get(data) == None):
            # then return the  parameter is required
            return f"the {data} field is required"