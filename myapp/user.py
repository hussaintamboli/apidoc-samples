__author__ = 'hussain'


class User:

    """
    @api {get} /user/:id Request User information
    @apiVersion 0.1.0
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

    @apiUse AuthError
    @apiPermission admin

    @apiError UserNotFound The id of the User was not found.
    @apiErrorExample Error-Response:
    HTTP/1.1 404 Not Found
    {
        "error": "UserNotFound"
    }
    @apiSampleRequest off
    """

    def get(self):
        pass

    """
    @apiDefine UserRegistrationError
    @apiError UserRegistrationError Invalid <code>firstname</code>/<code>age</code>
    """

    """
    @api {post} /uservalidation/ Create a user
    @apiVersion 0.1.0
    @apiName addUser
    @apiGroup User

    @apiParam {String} firstname First Name
    @apiParam {String} [lastname] Last Name
    @apiParam {Number} [age=18] Age

    @apiSuccess {String} id Id of the User

    @apiUse UserRegistrationError
    """
    def post(self):
        pass
