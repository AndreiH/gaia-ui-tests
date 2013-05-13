# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import random

from gaiatest import GaiaTestCase
from gaiatest.apps.marketplace.app import Marketplace
from gaiatest.apps.marketplace.regions.review_box import AddReview


class TestAddReview(GaiaTestCase):

    def setUp(self):
        GaiaTestCase.setUp(self)
        self.connect_to_network()
        self.install_marketplace()

    def test_add_review(self):
        marketplace = Marketplace(self.marionette, 'Marketplace dev')
        marketplace.launch()

        results = marketplace.search('Twitter')
        self.assertGreater(len(results.search_results), 0, 'No results found.')
        details_page = results.search_results[0].tap_app()

        #self.assertTrue(details_page.is_review_details_visible)
        self.marionette.switch_to_frame()
        details_page.tap_write_review()
       # persona.login(self.testvars['marketplace']['username'], self.testvars['marketplace']['password'])
        review_box = AddReview(self.marionette)
        review_box.write_a_review([random.randint(1, 5)], ['This is a test'])

