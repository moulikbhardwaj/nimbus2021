from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.response import Response

InvalidPasswordResponse = Response({"Message": "Invalid Password"}, HTTP_400_BAD_REQUEST)

FieldsNotPresentErrorResponse = Response({"Message": "Please provide the Required Fields. Password is neccessary"},
                                         HTTP_400_BAD_REQUEST)

InternalServerErrorResponse = Response({"Message": "internal server error"}, HTTP_500_INTERNAL_SERVER_ERROR)

SuccessfullyUpdatedResponse = Response({"Message": "Successfully Updated"}, HTTP_200_OK)

DepartMentNotFoundErrorResponse = Response({"error": "Department not found. Please provide correct Department Name"},
                                           HTTP_404_NOT_FOUND)
InvalidQuizIdResponse = Response({"message": "Invalid QuizId"}, HTTP_400_BAD_REQUEST)

QuizNotStartedResponse = Response({"message": "Quiz Not Started Yet."}, HTTP_400_BAD_REQUEST)

InvalidUserIdResponse = Response({"message": "Invalid UserId."}, HTTP_400_BAD_REQUEST)

QuizAlreadyAttemptedResponse = Response({"message": "Quiz Already Attempted"})

InvalidQuestionIdResponse = Response({"message": "Invalid QuestionId"}, HTTP_400_BAD_REQUEST)
