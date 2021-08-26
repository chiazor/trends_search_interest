#unit testing for the flask api
try:
    from app import app
    import unittest
except Exception as e:
    print(e)

class FlaskTest(unittest.TestCase):

    #test for 200 response
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/api/search_interest?keyword=ncis")
        status = response.status_code
        self.assertEqual(status, 200)

    # check if json is returned
    def test_json(self):
        tester = app.test_client(self)
        response = tester.get("/api/search_interest?keyword=ncis")
        status = response.status_code
        self.assertEqual(response.content_type, "application/json")


if __name__ == "__main__":
    unittest.main()





