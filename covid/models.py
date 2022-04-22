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

    """def calculate_shipping_fee_cost(self):
        if self.amount_extra >= c.SEASON_LEVEL:
                return 15
        elif self.amount_extra >= c.SUPPORTER_LEVEL:
            return 10
        elif self.amount_extra >= c.SHIRT_LEVEL:
            return 5"""

    @property
    def is_not_ready_to_checkin(self):
        """
        Returns None if we are ready for checkin, otherwise a short error
        message why we can't check them in.
        """
        
        if self.badge_status == c.WATCHED_STATUS:
            if self.banned or not self.regdesk_info:
                regdesk_info_append = " [{}]".format(self.regdesk_info) if self.regdesk_info else ""
                return "MUST TALK TO SECURITY before picking up badge{}".format(regdesk_info_append)
            return self.regdesk_info or "Badge status is {}".format(self.badge_status_label)

        if self.badge_status not in [c.COMPLETED_STATUS, c.NEW_STATUS]:
            return "Badge status is {}".format(self.badge_status_label)
        
        if self.placeholder:
            return "Placeholder badge"

        if self.is_unassigned:
            return "Badge not assigned"

        if self.is_presold_oneday:
            if self.badge_type_label != localized_now().strftime('%A'):
                return "Wrong day"

        if self.donate_badge_cost:
            return "Asked badge + merch to be shipped to them"

        message = check(self)
        return message
