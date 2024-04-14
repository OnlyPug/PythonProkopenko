# POST+GET=>INSERT+SELECT

def test_post_get_insert_select(adapter):
    # create 2 times
    adapter.create_new_object()  # (1 for PUT + GET = > UPDATE + SELECT)
    adapter.create_new_object()  # (2 for UPDATE+SELECT=>PUT+GET)
    adapter.create_new_object()  # just to see
    # and after this copy ids for any 2 object
