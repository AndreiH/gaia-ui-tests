# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from gaiatest.apps.base import Base


class Settings(Base):

    _back_button_locator = ('id', 'nav-back')
    _sign_in_button_locator = ('css selector', 'a.button.browserid')

    def wait_for_sign_in_displayed(self):
        self.wait_for_element_displayed(*self._sign_in_button_locator)

    def tap_sign_in(self):
        # TODO: click works but not tap
        self.marionette.find_element(*self._sign_in_button_locator).click()
        from gaiatest.apps.persona.app import Persona
        return Persona(self.marionette)

    def tap_back(self):
        self.marionette.tap(self.marionette.find_element(*self._back_button_locator))
        from gaiatest.apps.marketplace.app import Marketplace
        return Marketplace(self.marionette)