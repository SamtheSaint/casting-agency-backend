import os
import json
import unittest
from app import app


assistant = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1kYjl0cGg1NHlzMVdNcnRuY3J2cCJ9.eyJpc3MiOiJodHRwczovL2Rldi0zdjV3ZHI5MS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVlODQ0ZTBjNjVjODcwMDEzOWY0MDdjIiwiYXVkIjpbImFnZW5jeSIsImh0dHBzOi8vZGV2LTN2NXdkcjkxLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTI2MDA1MTEsImV4cCI6MTU5MjY4NjkxMSwiYXpwIjoiejZjM0VJajNSTWtVYUFvYU0zM1cxa0VTZ3JseFRvcXMiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.PfnwUR1ecWrvvFhIi0sgkLlDmjp6VQDp_jbObOVy-GeSS16v4xg2SlbbSgSemHodlV3n0pTeFRisa0C5QJJCJTb_y-fwnm7vd97MmSMDSNfwwMQuuF5xMxA1M7u8HnR_Jc_vjNE1UimTz7Q2KzVJ6V3t1QqzhsSzu-pcVdWqYs3Tf36AkIj7Q5ZxyPzFJQzaJXLYH87Cbz-1kfTT-Qp2TLG6lV04OTyagkxyNPwoQ7mI8-ieOXq27VOABeRx467Yu4MWlZXFayhnOrABSmNddT2fCmPCnb-ebbwVgV5TRpuia9QwN__6EaLcADwdiU3YQ8ZguJG54CbxUjnWltaPBw'
director = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1kYjl0cGg1NHlzMVdNcnRuY3J2cCJ9.eyJpc3MiOiJodHRwczovL2Rldi0zdjV3ZHI5MS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVlODQ0ODVhZGM0ZTkwMDEzMWI2YTg3IiwiYXVkIjpbImFnZW5jeSIsImh0dHBzOi8vZGV2LTN2NXdkcjkxLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTI2MDA1NDIsImV4cCI6MTU5MjY4Njk0MiwiYXpwIjoiejZjM0VJajNSTWtVYUFvYU0zM1cxa0VTZ3JseFRvcXMiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.mRoURXPxjvVKKUfNo5x268EqSGneCS8cSiO_Qwh6ZSBEqb2FEppqwpnO6kedM8WhsVcUrluaXXp7HNH0vvhcA8yMlumhlNvZw8ELqmn9gOvyqCdHWEk3NLJF2g6bQuWQFEsZXeGbfXlIuuIS2nyE9kh2ffj1EOKrh1bEXdb-4_u8zEEBq6NwZCMoYCKVK9RU6C2pt0SE5VdkKo-krD7bd-hzXi9VDn3iVt9G84Q-buGarQl5Nb-OVPUYAzpGQ-eKT5RMKWGDDDiizAqnJh21mHstDx4Tv-hDX7toufk1TR1cXd8lePAygBeYoYd_-yMVSfU-w3cHabGQZiCwpJ7B0A'
producer = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1kYjl0cGg1NHlzMVdNcnRuY3J2cCJ9.eyJpc3MiOiJodHRwczovL2Rldi0zdjV3ZHI5MS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjYTZhYjY3MjgwNDEwYzFiYjQ4MjQ4IiwiYXVkIjpbImFnZW5jeSIsImh0dHBzOi8vZGV2LTN2NXdkcjkxLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTI2MDA1ODEsImV4cCI6MTU5MjY4Njk4MSwiYXpwIjoiejZjM0VJajNSTWtVYUFvYU0zM1cxa0VTZ3JseFRvcXMiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.edUnoG5be90bB9gLiZEL5o-ud-7nxgoU5jDPsy0mtqFOMHG3vxB-XDh_3RLRX6kZIcsEw6BZ6_it9uVxvt1zFSRdYMNIAB98OTbZCpRXYDZAmJVQcO57_TyRgFF538nWJ-wEq3h1NhonsLf0JkyEY7FAyBxqnlZbWpDqgq1vzSWTAFIbo6-rwjzn66yBVjSWnAExk_bJx6GdtTwRdmPDa7Sh2S8nzuG8jVtmCLAK24tjNmOGgMzKOhNzp0TDPIWpveq0japGGQRWF4mhLOXGtw7VDo_pYDacmhloiANy7lSYNU7Bk8ErtxAhhhQX2qwddjNlrk2Z7B7s2cbSY9pGQQ'


class GeneralTests(unittest.TestCase):
    """This class represents the general tests"""

    def setUp(self):
        """Define test variables and initialize app."""
        app.config['TESTING'] = True
        self.client = app.test_client()

    def tearDown(self):
        """Executed after reach test"""

    def test_health_check(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)


class ActorTests(unittest.TestCase):
    """This class represents the actor tests"""

    def setUp(self):
        """Define test variables and initialize app."""
        app.config['TESTING'] = True
        self.client = app.test_client()
        self.assistant_token = assistant
        self.director_token = director
        self.producer_token = producer

        self.new_actor = {
            'name': 'Agent Coulson',
            'age': 29,
            'gender': "It's a magical place"
        }

    def tearDown(self):
        """Executed after reach test"""

    def test_get_actors_using_assistant_success(self):
        res = self.client.get('/actors/', headers={
            'Authorization': f'Bearer {self.assistant_token}'
        })
        self.assertEqual(res.status_code, 200)

    def test_get_actors_failure(self):
        res = self.client.get('/actors/')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message']['code'],
                         'authorization_header_missing')

    def test_post_actors_using_director_success(self):
        res = self.client.post('/actors/', json=self.new_actor, headers={
            'Authorization': f'Bearer {self.director_token}',
            'Content-Type': 'application/json'
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['actors'][0]['name'], self.new_actor['name'])

        # cleanup
        res = self.client.delete('/actors/' + str(data['actors'][0]['id']), headers={
            'Authorization': f'Bearer {self.director_token}'
        })

    def test_post_actors_error_unprocessable(self):
        res = self.client.post('/actors/', json={
            'name': 'this-should-really-be-changed'
        }, headers={
            'Authorization': f'Bearer {self.director_token}',
            'Content-Type': 'application/json'
        })
        self.assertEqual(res.status_code, 422)

    def test_post_actors_error_bad_request(self):
        res = self.client.post('/actors/', headers={
            'Authorization': f'Bearer {self.director_token}',
            'Content-Type': 'application/json'
        })
        self.assertEqual(res.status_code, 400)

    def test_post_actors_using_assistant_error(self):
        res = self.client.post('/actors/', json=self.new_actor, headers={
            'Authorization': f'Bearer {self.assistant_token}',
            'Content-Type': 'application/json'
        })
        self.assertEqual(res.status_code, 401)

    def test_patch_actors_using_producer_success(self):
        res = self.client.post('/actors/', json=self.new_actor, headers={
            'Authorization': f'Bearer {self.director_token}',
            'Content-Type': 'application/json'
        })
        data = json.loads(res.data)
        res = self.client.patch('/actors/' + str(data['actors'][0]['id']), json={
            'name': 'Not Agent Coulson'
        }, headers={
            'Authorization': f'Bearer {self.producer_token}',
            'Content-Type': 'application/json'
        })

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['actors'][0]['name'], 'Not Agent Coulson')

        # cleanup
        res = self.client.delete('/actors/' + str(data['actors'][0]['id']), headers={
            'Authorization': f'Bearer {self.director_token}'
        })

    def test_patch_actors_error(self):
        res = self.client.patch('/actors/-1', json={
            'name': 'this-should-really-be-changed'
        }, headers={
            'Authorization': f'Bearer {self.producer_token}',
            'Content-Type': 'application/json'
        })
        self.assertEqual(res.status_code, 404)

    def test_delete_actors_as_director(self):
        res = self.client.post('/actors/', json=self.new_actor, headers={
            'Authorization': f'Bearer {self.director_token}',
            'Content-Type': 'application/json'
        })
        data = json.loads(res.data)
        res = self.client.delete('/actors/' + str(data['actors'][0]['id']), headers={
            'Authorization': f'Bearer {self.director_token}'
        })
        self.assertEqual(res.status_code, 200)

    def test_delete_actors_error(self):
        res = self.client.delete('/actors/-1', headers={
            'Authorization': f'Bearer {self.director_token}'
        })
        self.assertEqual(res.status_code, 404)


class MovieTests(unittest.TestCase):
    """This class represents the movie tests"""

    def setUp(self):
        """Define test variables and initialize app."""
        app.config['TESTING'] = True
        self.client = app.test_client()
        self.assistant_token = assistant
        self.director_token = director
        self.producer_token = producer

        self.new_movie = {
            'title': 'Agents of SHIELD',
            'date': '2001-02-22'
        }

    def tearDown(self):
        """Executed after reach test"""

    def test_get_movies_using_assistant_success(self):
        res = self.client.get('/movies/', headers={
            'Authorization': f'Bearer {self.assistant_token}'
        })
        self.assertEqual(res.status_code, 200)

    def test_get_movies_failure(self):
        res = self.client.get('/movies/', headers={
            'Authorization': 'Bearer'
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message']['code'],
                         'invalid_header')

    def test_post_movies_using_producer_success(self):
        res = self.client.post('/movies/', json=self.new_movie, headers={
            'Authorization': f'Bearer {self.producer_token}',
            'Content-Type': 'application/json'
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['movies'][0]['date'], self.new_movie['date'])

        # cleanup
        res = self.client.delete('/movies/' + str(data['movies'][0]['id']), headers={
            'Authorization': f'Bearer {self.producer_token}'
        })

    def test_post_movies_error(self):
        res = self.client.post('/movies/', json={
            'title': 'this-should-really-be-changed'
        }, headers={
            'Authorization': f'Bearer {self.producer_token}',
            'Content-Type': 'application/json'
        })
        self.assertEqual(res.status_code, 422)

    def test_patch_movies_using_director_success(self):
        res = self.client.post('/movies/', json=self.new_movie, headers={
            'Authorization': f'Bearer {self.producer_token}',
            'Content-Type': 'application/json'
        })
        data = json.loads(res.data)
        res = self.client.patch('/movies/' + str(data['movies'][0]['id']), json={
            'title': 'New Movie Title'
        }, headers={
            'Authorization': f'Bearer {self.director_token}',
            'Content-Type': 'application/json'
        })

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['movies'][0]['title'], 'New Movie Title')

        # cleanup
        res = self.client.delete('/movies/' + str(data['movies'][0]['id']), headers={
            'Authorization': f'Bearer {self.director_token}'
        })

    def test_patch_movies_error(self):
        res = self.client.patch('/movies/-1', json={
            'title': 'this-should-really-be-changed'
        }, headers={
            'Authorization': f'Bearer {self.producer_token}',
            'Content-Type': 'application/json'
        })
        self.assertEqual(res.status_code, 404)

    def test_delete_movies_as_producer(self):
        res = self.client.post('/movies/', json=self.new_movie, headers={
            'Authorization': f'Bearer {self.producer_token}',
            'Content-Type': 'application/json'
        })
        data = json.loads(res.data)
        res = self.client.delete('/movies/' + str(data['movies'][0]['id']), headers={
            'Authorization': f'Bearer {self.producer_token}'
        })
        self.assertEqual(res.status_code, 200)

    def test_delete_movies_error(self):
        res = self.client.delete('/movies/-1', headers={
            'Authorization': f'Bearer {self.producer_token}'
        })
        self.assertEqual(res.status_code, 404)


if __name__ == '__main__':
    unittest.main()
