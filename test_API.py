
import json

import requests

id_project="32"
id_packages="60"
host_api="http://127.0.0.1:8080"
headers = {'Content-Type': 'application/json',
               'Authorization': 'Basic YXBpa2V5OmQ2MzQzNmMwMDczMGNmNTIxN2YzMjA5NWM0MzJhN2NlZDk4NTBkODczYTdmMmFjZTY0ZTY4OTVhNDBkYWRkMzc='
               }

def test_T001():

    headers

    payload = {}
    url = host_api+"/api/v3/projects/"+id_project
    resp = requests.get(url, headers=headers, data=json.dumps(payload))
    resp_body = resp.json()
    name = resp_body['name']
    description = resp_body['description']['raw']
    print(resp.text)

    print(name)
    print(description)
    #
    assert resp.status_code == 200
    assert name == "TestProject1"
    assert description == "This is the first test project"



def test_T002():
    url = host_api+"/api/v3/projects/"+id_project

    headers

    payload = {
        "description": {
            "raw": "This is the first test project1"
        }
    }

    resp = requests.patch(url, headers=headers, data=json.dumps(payload))
    resp_body = resp.json()
    name = resp_body['name']
    new_description = resp_body['description']['raw']

    print(new_description)

    assert resp.status_code == 200
    assert name == "TestProject1"
    assert new_description == "This is the first test project1"


def test_T003():
    url = host_api+"/api/v3/projects/"

    headers

    payload = {
        "_embedded": {
            "status": {
                "_type": "ProjectStatus",
                "id": "on_track",
                "name": "On track",
                "_links": {
                    "self": {
                        "href": "/api/v3/project_statuses/on_track",
                        "title": "On track"
                    }
                }
            }
        },
        "_type": "Project",
        "identifier": "newproject",
        "name": "NewProject",
        "active": 'true',
        "public": 'true',
        "description": {
            "format": "markdown",
            "raw": "This is the new test project",
            "html": "<p class=\"op-uc-p\">This is the first test project</p>"
        },
        "status": {
            "href": "/api/v3/project_statuses/on_track",
            "title": "On track"
        }
    }

    resp = requests.post(url, headers=headers, data=json.dumps(payload))
    resp_body = resp.json()
    name1 = resp_body['name']
    id = resp_body['id']
    print(id)
    identifier = resp_body['identifier']
    assert resp.status_code == 201
    assert name1 == "NewProject"
    assert identifier == "newproject"




def test_T004():
    url = host_api+"/api/v3/projects/"+id_project

    headers

    payload = {}

    resp = requests.delete(url, headers=headers, data=json.dumps(payload))
    assert resp.status_code == 404


def test_T005():
    url = 'http://127.0.0.1:8080/api/v3/work_packages/'+id_packages

    headers

    payload = {
    }

    resp = requests.get(url, headers=headers, data=json.dumps(payload))

    resp_body = resp.json()
    task = resp_body['_embedded']['type']['name']
    subject = resp_body['subject']
    print(task)

    assert subject == "My Task 1"
    assert task == "Task"
    assert resp.status_code == 200


def test_T006():
    url = host_api+"/api/v3/work_packages/"+id_packages

    headers

    payload = {

        "lockVersion": 0,
        "description": {
            "raw": "test"
        }

    }

    resp = requests.patch(url, headers=headers, data=json.dumps(payload))

    resp_body = resp.json()
    des = resp_body['description']['raw']

    assert des == "test"
    assert resp.status_code == 200


def test_T007():
    url = host_api+"/api/v3/work_packages/"

    headers

    payload = {

        "subject": "MyTask",
        "description": {
            "format": "markdown",
            "raw": "test",
            "html": "<p class=\"op-uc-p\">test</p>"
        },
        "scheduleManually": 'false',
        "type": {
            "href": "/api/v3/types/1",
            "title": "Task"
        },
        "project": {
            "href": "/api/v3/projects/28",
            "title": "TestProject1"
        }
    }

    resp = requests.post(url, headers=headers, data=json.dumps(payload))

    resp_body = resp.json()
    sub = resp_body['subject']

    assert sub == "MyTask"
    assert resp.status_code == 201


def test_T008():
    url = host_api+"/api/v3/work_packages/"+id_packages

    headers

    payload = {
    }

    resp = requests.delete(url, headers=headers, data=json.dumps(payload))
    assert resp.status_code == 204
    resp1 = requests.delete(url, headers=headers, data=json.dumps(payload))
    assert resp1.status_code == 404

