# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import random

from gaiatest.apps.base import Base


class AddReview(Base):
    """
    Page for adding reviews.
    """

    _add_review_input_field_locator = ('id', 'id_body')
    _submit_review_button_locator = ('css selector', '.two-up > button')
    _review_box_locator = ('css selector', '.add-review-form.form-modal')
    _rating_locator = ('css selector', ".ratingwidget.stars.stars-0>label[data-stars='%s']")

    def __init__(self, marionette):
        Base.__init__(self, marionette)
        self.wait_for_element_present(*self._review_box_locator)

    def set_review_rating(self, rating):
        self.marionette.tap(self.marionette.find_element(self._rating_locator[0], self._rating_locator[1] % (random.randint(1, 5))))

    def enter_review_with_text(self, text):
        self.marionette.find_element(*self._add_review_input_field_locator).send_keys(text)

    def write_a_review(self, rating, body):
        self.set_review_rating(rating)
        self.enter_review_with_text(body)
        self.marionette.tap(self.marionette.find_element(*self._submit_review_button_locator))
