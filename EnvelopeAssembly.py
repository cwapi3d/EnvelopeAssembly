# Copyright 2024 Cadwork Informatique Inc.
# All rights reserved.
# This file is part of EnvelopeAssembly,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import cadwork
import attribute_controller as ac
import element_controller as ec
import utility_controller as uc


def get_grouping_attribute(element):
    """
    Returns the grouping attribute of a given element.

    Args:
        element: The element to get the grouping attribute for.

    Returns: The grouping attribute.

    """
    if ac.get_element_grouping_type() == cadwork.element_grouping_type.group:
        return ac.get_group(element)
    elif ac.get_element_grouping_type() == cadwork.element_grouping_type.subgroup:
        return ac.get_subgroup(element)

    raise RuntimeError('unknown element grouping type')


if __name__ == "__main__":
    active_elements = ec.get_active_identifiable_element_ids()

    active_envelopes = {}

    try:
        for active_element in active_elements:
            if ac.is_envelope(active_element):
                grouping_attribute = get_grouping_attribute(active_element)
                active_envelopes[grouping_attribute] = {'assembly': ac.get_assembly_number(active_element), 'elements': []}

        for active_element in active_elements:
            if not ac.is_envelope(active_element):
                grouping_attribute = get_grouping_attribute(active_element)

                if grouping_attribute in active_envelopes:
                    ac.set_assembly_number([active_element], active_envelopes[grouping_attribute]['assembly'])

    except RuntimeError:
        uc.print_error('failed to get envelopes')
