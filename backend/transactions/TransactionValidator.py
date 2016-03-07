
def validate(response, new_transaction):
    if new_transaction.project_id == "":
        response.status = 400
        response.write("project id can not be empty")
        return False
    elif new_transaction.user_id == "":
        response.status = 400
        response.write("user id can not be empty")
        return False
    elif new_transaction.money == "":
        response.status = 400
        response.write("money can not be empty")
        # zwyczajnie try catch
        return False
    return True
