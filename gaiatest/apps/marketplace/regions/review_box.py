# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from gaiatest.apps.base import Base


class AddReview(Base):
    """
    Page for adding reviews.
    """

    _star_rating_locator = ('css selector', '.ratingwidget.stars > label')
    _add_review_input_field_locator = ('id', 'id_body')
    _submit_review_button_locator = ('css selector', '.two-up > button')
    _review_box_locator = ('css selector', '.add-review-form.form-modal')


    def set_review_rating(self, rating):
        self.marionette.find_element(self._star_rating_locator[0],
                                             '%s[data-stars="%s"]' % (self._star_rating_locator[1], rating)).click()

    def enter_review_with_text(self, text):
        self.marionette.find_element(*self._add_review_input_field_locator).clear()
        self.marionette.find_element(*self._add_review_input_field_locator).send_keys(text)

    def write_a_review(self, rating, body):
        self.enter_review_with_text(body)
        self.set_review_rating(rating)
        self.marionette.find_element(*self._submit_review_button_locator).click()
        from gaiatest.apps.marketplace.regions.reviews import Reviews
        return Reviews(self.marionette)