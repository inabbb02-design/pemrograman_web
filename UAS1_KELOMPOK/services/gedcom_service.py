from gedcom.parser import Parser
from gedcom.element.individual import IndividualElement
from config import FILE_PATH

def get_parser():
    parser = Parser()
    parser.parse_file(FILE_PATH)
    return parser

def get_children_ids(parser, all_elements, parent_ids):
    child_ids = []
    for f_el in all_elements:
        if f_el.get_tag() == "FAM":
            husbands = [p.get_pointer() for p in parser.get_family_members(f_el, "HUSB")]
            wives = [p.get_pointer() for p in parser.get_family_members(f_el, "WIFE")]
            if any(p in parent_ids for p in (husbands + wives)):
                child_ids.extend([c.get_pointer() for c in parser.get_family_members(f_el, "CHIL")])
    return list(set(child_ids))

def get_parent_ids(parser, all_elements, child_id):
    parent_ids = []
    for f_el in all_elements:
        if f_el.get_tag() == "FAM":
            children = [c.get_pointer() for c in parser.get_family_members(f_el, "CHIL")]
            if child_id in children:
                parent_ids.extend(
                    [p.get_pointer() for p in parser.get_family_members(f_el, "HUSB")] +
                    [p.get_pointer() for p in parser.get_family_members(f_el, "WIFE")]
                )
    return list(set(parent_ids))

def get_sibling_ids(parser, all_elements, person_id):
    siblings = []
    for f_el in all_elements:
        if f_el.get_tag() == "FAM":
            children = [c.get_pointer() for c in parser.get_family_members(f_el, "CHIL")]
            if person_id in children:
                siblings.extend([c for c in children if c != person_id])
    return list(set(siblings))

def find_individual(all_elements, pointer):
    return next(
        (el for el in all_elements if isinstance(el, IndividualElement) and el.get_pointer() == pointer),
        None
    )
