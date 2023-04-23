import unittest

from src import main


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        self.short_log = '8.8.8.8 - foo user [28/Oct/2021:00:18:22 +0100] "GET / HTTP/1.1" 200 77 "-" "foo bar 1"'
        self.long_log = '89.122.76.3 - - [01/Jan/2022:00:00:00 +0100] "POST /foo/admin/formLogin HTTP/1.1" 404 125837 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"'

    def test_get_result_with_regex_match(self):
        result = main.get_result_with_regex_match(self.short_log)
        self.assert_result_short_log_is_ok(result)
        result = main.get_result_with_regex_match(self.long_log)
        self.assert_result_long_log_is_ok(result)

    def test_get_result_with_regex_search(self):
        result = main.get_result_with_regex_search(self.short_log)
        self.assert_result_short_log_is_ok(result)
        result = main.get_result_with_regex_search(self.long_log)
        self.assert_result_long_log_is_ok(result)

    def assert_result_short_log_is_ok(self, result):
        self.assertEqual("8.8.8.8", result.remote_addr)
        self.assertEqual("foo user", result.remote_user)
        self.assertEqual("28/Oct/2021:00:18:22 +0100", result.time_local)
        self.assertEqual("GET / HTTP/1.1", result.request)
        self.assertEqual("200", result.status)
        self.assertEqual("77", result.body_bytes_sent)
        self.assertEqual("-", result.http_referer)
        self.assertEqual("foo bar 1", result.http_user_agent)

    def assert_result_long_log_is_ok(self, result):
        self.assertEqual("89.122.76.3", result.remote_addr)
        self.assertEqual("-", result.remote_user)
        self.assertEqual("01/Jan/2022:00:00:00 +0100", result.time_local)
        self.assertEqual("POST /foo/admin/formLogin HTTP/1.1", result.request)
        self.assertEqual("404", result.status)
        self.assertEqual("125837", result.body_bytes_sent)
        self.assertEqual("-", result.http_referer)
        self.assertEqual("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36", result.http_user_agent)


if __name__ == "__main__":
    unittest.main()
