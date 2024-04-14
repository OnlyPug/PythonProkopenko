a = "ff8081818ed059c0018edd117dfc1b77"
b = "ff8081818ed059c0018edd11836a1b78"


# PUT+GET=>UPDATE+SELECT

def test_put_get_update_select(adapter):
    adapter.update_object(a)
    adapter.select_data()


# UPDATE+SELECT=>PUT+GET
def test_update_select_put_get(adapter):
    adapter.update_from_object(b)
    adapter.select_data()


def test_select_sql(adapter):
    adapter.select_data()
