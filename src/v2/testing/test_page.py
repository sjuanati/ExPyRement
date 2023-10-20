from unittest import TestCase
from unittest.mock import patch
from .page import PageRequester


class TestPageRequester(TestCase):
    def setUp(self):
        self.page = PageRequester("https://google.com")

    def test_make_request(self):
        # wherever we use `requests.get()` will be replaced by `mocked_get``
        with patch("requests.get") as mocked_get:
            self.page.get()
            mocked_get.assert_called()

    def test_content_returned(self):
        fake_content = "Hello"

        class FakeResponse:
            def __init__(self):
                self.content = fake_content

        with patch("requests.get", return_value=FakeResponse()) as mocked_get:
            result = self.page.get()
            self.assertEqual(result, fake_content)


"""
Usefulness of the `test_make_request`:

This test would fail if the method `requests.get()` is not called within the 
`self.page.get()`. Here are some scenarios where this test would fail:

1. Removal of the Call:  If someone modifies the `get` method of `PageRequester`
to not use `requests.get()`, then the test would fail.

   ```
   def get(self):
       pass  # No longer calling requests.get()
   ```

2. Change in Method Called: If someone decides to use another method instead of
`requests.get()` (e.g., `requests.post()` or another HTTP library entirely), the
test would fail.

   ```
   def get(self):
       return requests.post(self.url).content  # Using POST instead of GET
   ```

3. Conditional Calls: If the call to `requests.get()` is made conditionally
and the condition isn't met, the test would fail.

   ```
   def get(self):
       if "https" not in self.url:
           return requests.get(self.url).content
   ```

   In the above, if the URL doesn't contain "https", the `requests.get()` wouldn't
   be called, causing the test to fail.

4. Exception Before the Call: If there's an exception raised in the `get` method
before `requests.get()` gets called, the test would fail.

   ```
   def get(self):
       raise ValueError("An error occurred!")
       return requests.get(self.url).content
   ```

5. Refactoring without Updating Tests: Sometimes during code refactoring,
developers might change how certain functionalities work without updating the
associated tests. If the call to `requests.get()` is moved to another method or
class, and the test isn't updated accordingly, it would fail.

In summary, any change that prevents `requests.get()` from being called during
the execution of the `get` method will cause this specific test to fail. This
kind of test ensures that certain expected interactions (in this case, the call
to  `requests.get()`) still occur as the code evolves.
"""


"""
Usefulness of the `test_content_returned`:

This test would fail in the following scenarios:

1. Different Return Attribute: If someone modifies the `get` method of
`PageRequester` to return something other than the `content` attribute of the
response. For example:

   ```
   def get(self):
       response = requests.get(self.url)
       return response.status_code  # Returning status code instead of content
   ```

2. Manipulation of Content: If there is any manipulation of the content
before it gets returned.

   ```
   def get(self):
       response = requests.get(self.url)
       return response.content.upper()  # Converting content to uppercase before returning
   ```

3. Exception in Method: If an exception is raised in the `get` method before
returning the content, the test would fail.

4. Refactoring without Updating Tests: As with the previous example, if the
behavior of the `get` method changes and the test isn't updated accordingly,
it would fail.

In essence, this test ensures that the `get` method of `PageRequester` correctly
returns the `content` attribute of the response from `requests.get()`.
"""