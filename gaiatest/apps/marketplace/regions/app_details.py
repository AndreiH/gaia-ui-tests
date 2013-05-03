# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from gaiatest.apps.base import Base


class Details(Base):

    _write_review_locator = ('id', 'add-first-review')
    _review_details_locator = ('id', 'reviews-detail')
    _write_review_button_loading_locator = ('css selector', '.button.loading-submit')

    @property
    def is_review_details_visible(self):
        return self.is_element_displayed(*self._review_details_locator)

    def tap_write_review(self):
        self.wait_for_element_present(*self._write_review_locator)
        write_review_button = self.marionette.find_element(*self._write_review_locator)
        self.marionette.execute_script("arguments[0].scrollIntoView(false);", [write_review_button])
        # TODO: click works but not tap
        self.marionette.find_element(*self._write_review_locator).click()
        from gaiatest.apps.persona.app import Persona
        return Persona(self.marionette)