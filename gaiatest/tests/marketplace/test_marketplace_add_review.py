# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from gaiatest import GaiaTestCase
from gaiatest.apps.marketplace.app import Marketplace
from gaiatest.mocks.persona_test_user import PersonaTestUser
from gaiatest.apps.marketplace.regions.review_box import AddReview


class TestAddReview(GaiaTestCase):

    def setUp(self):
        GaiaTestCase.setUp(self)
        self.connect_to_network()
        self.install_marketplace()

        self.user = PersonaTestUser().create_user(verified=True,
                                                  env={"browserid": "firefoxos.persona.org", "verifier": "marketplace-dev.allizom.org"})

    def test_add_review(self):

        marketplace = Marketplace(self.marionette, 'Marketplace dev')
        marketplace.launch()

        settings = marketplace.tap_settings()
        persona = settings.tap_sign_in()
        persona.login(self.user.email, self.user.password)

        self.marionette.switch_to_frame()
        marketplace.launch()
        settings.wait_for_sign_out_button()

        results = marketplace.search('SoundCloud')
        self.assertGreater(len(results.search_results), 0, 'No results found.')
        details_page = results.search_results[0].tap_app()

        details_page.tap_write_review()

        review_box = AddReview(self.marionette)
        review_box.write_a_review(review_box['rating'], review_box['body'])

        self.marionette.switch_to_frame()
        marketplace.launch()

        self.assertTrue(marketplace.is_notification_message_displayed, "Review not added: %s" % marketplace.notification_message)
        self.assertEqual(marketplace.notification_message, "Your review was posted")
        self.assertEqual(details_page.first_review_rating, review_box['rating'])
        self.assertEqual(details_page.first_review_body, review_box['body'])