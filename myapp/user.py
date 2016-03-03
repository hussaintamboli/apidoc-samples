__author__ = 'hussain'


class User:

    """
    @api {get} /user/:id Request User information
    @apiName GetUser
    @apiGroup User

    @apiParam {Number} id Users unique ID.

    @apiSuccess {String} firstname Firstname of the User.
    @apiSuccess {String} lastname  Lastname of the User.

    @apiSuccessExample e.g. Success-Response
    HTTP/1.1 200 OK
    {
        "firstname": "John",
        "lastname": "Doe"
    }

    @apiError UserNotFound The id of the User was not found.
    @apiErrorExample Error-Response:
    HTTP/1.1 404 Not Found
    {
        "error": "UserNotFound"
    }
    """

    def get(self):
        pass

    """
    @api {post} /user Create a user
    @apiName addUser
    @apiGroup User

    @apiParam {String} firstname First Name
    @apiParam {String} [lastname] Last Name
    @apiParam {Number} [age=18] Age

    @apiSuccess {String} id Id of the User
    """
    def post(self):
        pass
