# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from gaiatest.apps.base import Base


class Details(Base):

    _write_review_locator = ('id', 'add-review')
    _app_details_locator = ('css selector', '.detail')

    def __init__(self, marionette):
        Base.__init__(self, marionette)
        self.wait_for_element_present(*self._app_details_locator)

    @property
    def is_app_details_displayed(self):
        return self.is_element_displayed(*self._app_details_locator)

    def tap_write_review(self):
        self.wait_for_element_present(*self._write_review_locator)
        write_review_button = self.marionette.find_element(*self._write_review_locator)
        write_review_button.tap()
