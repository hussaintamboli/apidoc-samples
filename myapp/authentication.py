__author__ = 'hussain'


class Auth:

    """
    @api {post} /auth Authentication
    @apiVersion 0.1.0
    @apiName auth
    @apiGroup Recruiter

    @apiParam {String} user Pass username in JSON
    @apiParam {String} password Password

    @apiSuccess {String} access_token JWT for the Recruiter
    @apiSuccess {String} id Id of recruiter
    @apiSuccess {String} agency_id Agency Id
    @apiSuccess {String} name Name of the recruiter

    @apiHeader {String} Content-Type=application/json content type
    """

    def post(self):
        pass
