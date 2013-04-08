# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from gaiatest import GaiaTestCase
from gaiatest.mocks.mock_contact import MockContact
from gaiatest.apps.contacts.app import Contacts


class TestAddContactToFavorite(GaiaTestCase):

    def setUp(self):
        GaiaTestCase.setUp(self)

        self.contact = MockContact()
        self.data_layer.insert_contact(self.contact)

    def test_add_contact_to_favorite(self):

        contacts_app = Contacts(self.marionette)
        contacts_app.launch()

        contact_details = contacts_app.contact(self.contact['givenName']).tap()
        contact_details.tap_add_remove_favorite()
        self.assertEqual(contact_details.add_remove_text, 'Remove as Favorite')

        contact_details.tap_back()
        self.assertEqual(len(contacts_app.contacts), 2)

        print self.marionette.page_source
