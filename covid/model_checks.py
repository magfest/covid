from .config import c
from uber.model_checks import prereg_validation, validation, ignore_unassigned_and_placeholders


@prereg_validation.Attendee
def read_covid_policy(attendee):
    if False and not attendee.agreed_to_covid_policies:
        return "Please read and agree to the COVID Policies for {}.".format(c.EVENT_NAME_AND_YEAR)


@validation.Attendee
def allowed_to_register(attendee):
    if False and not attendee.age_group_conf['can_register']:
        return 'Per our COVID policies, attendees {} years of age currently may not register. \
                Please email regsupport@magfest.org for more info.'.format(attendee.age_group_conf['desc'].lower())


@validation.Attendee
def checked_in_covid_ready(attendee):
    if False and attendee.checked_in and not attendee.covid_ready:
        return "Attendees must be marked as eligible to attend under our COVID policies before they can be checked in."
