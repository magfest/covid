from pockets import classproperty
from pockets.autolog import log
from residue import CoerceUTF8 as UnicodeText, UUID

from uber.config import c
from uber.decorators import presave_adjustment, render
from uber.models import Boolean, MagModel, Choice, DefaultColumn as Column, Session
from uber.tasks.email import send_email
from uber.utils import add_opt, check, localized_now, remove_opt


@Session.model_mixin
class Attendee:
    agreed_to_covid_policies = Column(Boolean, default=False)
    covid_ready = Column(Boolean, default=False)
    #donate_badge_cost = Column(Boolean, default=False)

    @classproperty
    def checkin_bools(self):
        return ['got_merch', 'covid_ready'] if c.MERCH_AT_CHECKIN else ['covid_ready']

    @presave_adjustment
    def keep_covid_agreement(self):
        if self.orig_value_of('agreed_to_covid_policies') and self.orig_value_of('agreed_to_covid_policies') == True:
            # Workaround for a bug on how the admin form handles booleans
            self.agreed_to_covid_policies = True

