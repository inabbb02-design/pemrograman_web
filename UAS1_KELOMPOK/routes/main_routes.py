from flask import Blueprint, render_template, request
from gedcom.element.individual import IndividualElement
from services.gedcom_service import get_parser, find_individual

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    query = request.args.get('query', '').lower()
    parser = get_parser()
    results = []

    if query:
        for el in parser.get_root_child_elements():
            if isinstance(el, IndividualElement):
                name = " ".join(el.get_name())
                if query in name.lower():
                    results.append({'id': el.get_pointer(), 'name': name})

    return render_template('index.html', results=results, query=query)

@main_bp.route('/person/<pointer>')
def person_detail(pointer):
    parser = get_parser()
    all_elements = parser.get_root_child_elements()
    element = find_individual(all_elements, pointer)

    if not element:
        return "Data tidak ditemukan", 404

    data = {
        'id': pointer,
        'name': " ".join(element.get_name()),
        'parents': [],
        'siblings': [],
        'families': []
    }

    # Orang tua & saudara
    for fam in all_elements:
        if fam.get_tag() == "FAM":
            children = [c.get_pointer() for c in parser.get_family_members(fam, "CHIL")]
            if pointer in children:
                for h in parser.get_family_members(fam, "HUSB"):
                    data['parents'].append({'id': h.get_pointer(), 'name': " ".join(h.get_name()), 'relation': 'Ayah'})
                for w in parser.get_family_members(fam, "WIFE"):
                    data['parents'].append({'id': w.get_pointer(), 'name': " ".join(w.get_name()), 'relation': 'Ibu'})
                for c in children:
                    if c != pointer:
                        sib = find_individual(all_elements, c)
                        if sib:
                            data['siblings'].append({'id': c, 'name': " ".join(sib.get_name())})

    # Pasangan & anak
    for fam in parser.get_families(element):
        spouse = next(
            ({'id': s.get_pointer(), 'name': " ".join(s.get_name())}
             for s in parser.get_family_members(fam, "HUSB") + parser.get_family_members(fam, "WIFE")
             if s.get_pointer() != pointer),
            None
        )
        children = [{'id': c.get_pointer(), 'name': " ".join(c.get_name())}
                    for c in parser.get_family_members(fam, "CHIL")]

        data['families'].append({'spouse': spouse, 'children': children})

    return render_template('detail.html', person=data)
