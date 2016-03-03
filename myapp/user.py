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
    """

    def get(self):
        pass
