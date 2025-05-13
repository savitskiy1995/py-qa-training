from random import randrange

from model.group import Group

def test_edit_group(app):
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Edit group", header="Edit header")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(group, index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)