import unittest
import webapp2
import projects.ProjectsHandler
import projects.ProjectConnector
from projects.ProjectConnector import Project
from projects.ProjectConnector import ProjectConnector


class TestHandlers(unittest.TestCase):
    def setUp(self):
        self.sample_project = Project("testName", "testDesc", "1")
        self.sample_project2 = Project("testName2", "testDesc2", "2")
        self.project_conn = ProjectConnector()

    def test_get_all_projects(self):
        self.project_conn.insert_into(self.sample_project)
        self.project_conn.insert_into(self.sample_project2)

        request = webapp2.Request.blank('/projects')
        response = request.get_response(projects.ProjectsHandler.app)

        self.assertEqual(response.status_int, 200)
        print(response.body)
        self.assertTrue("testDesc" in response.body)
        self.assertFalse("testDesc1" in response.body)
        self.assertTrue("testDesc2" in response.body)
