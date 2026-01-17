from flask import Blueprint, render_template
from services.gedcom_service import (
    get_parser, get_parent_ids, get_children_ids,
    get_sibling_ids, find_individual
)

cousin_bp = Blueprint('cousin', __name__)

@cousin_bp.route('/person/<pointer>/cousins/<int:level>')
def person_cousins(pointer, level):
    parser = get_parser()
    all_elements = parser.get_root_child_elements()
    element = find_individual(all_elements, pointer)

    curr_gen = [pointer]
    for _ in range(level):
        next_gen = []
        for p_id in curr_gen:
            next_gen.extend(get_parent_ids(parser, all_elements, p_id))
        curr_gen = list(set(next_gen))

    uncles_aunts = []
    for anc in curr_gen:
        uncles_aunts.extend(get_sibling_ids(parser, all_elements, anc))

    cousin_ids = list(set(uncles_aunts))
    for _ in range(level):
        cousin_ids = get_children_ids(parser, all_elements, cousin_ids)

    cousins = []
    for cid in cousin_ids:
        indi = find_individual(all_elements, cid)
        if indi:
            cousins.append({'id': cid, 'name': " ".join(indi.get_name())})

    titles = {1: "Sekali", 2: "Dua Kali", 3: "Tiga Kali"}

    return render_template(
        'cousins.html',
        person_name=" ".join(element.get_name()),
        cousins=cousins,
        level_text=titles.get(level, f"{level} Kali"),
        back_id=pointer
    )
