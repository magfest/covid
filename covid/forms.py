from wtforms import BooleanField
from markupsafe import Markup

from uber.config import c
from uber.forms import MagForm, SwitchInput
from uber.custom_tags import popup_link, email_to_link

@MagForm.form_mixin
class OtherInfo:
    agreed_to_covid_policies = BooleanField('', widget=SwitchInput())

    def agreed_to_covid_policies_label(self):
        if c.COVID_POLICIES_URL:
            return Markup("""
            By checking this box, I acknowledge that I have read and agree to abide by the {} in their entirety. 
            I understand the <strong>vaccination and face covering requirements</strong> for all individuals, including minors, and I 
            understand that MAGFest has a <strong>no-refunds policy</strong>. I will contact {} 
            no later than <strong>November 15</strong> if I need to request an 
            exemption, and I understand that exemption requests may not be granted if received after this date.
            """.format(
                popup_link(c.COVID_POLICIES_URL, c.EVENT_NAME_AND_YEAR + " COVID Policies"),
                email_to_link("exemptions@magfest.org")
            ))
        else:
            text = Markup("""
            <strong>Yes</strong>, I understand that if accepted, I will need to agree to the {EVENT_NAME} {EVENT_YEAR} 
            COVID Policy in order to complete my application or registration. 
            """)
            if c.PRIOR_COVID_POLICIES_URL:
                text += popup_link(c.PRIOR_COVID_POLICIES_URL, "See last year's policy here")
            
            return text