from model.group import Group

def test_edit_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="Edit group", header="Edit header")
    group.id = old_groups[0].id
    app.group.edit_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)