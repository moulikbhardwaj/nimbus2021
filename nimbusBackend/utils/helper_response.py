from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.response import Response

InvalidPasswordResponse = Response({"Message": "Invalid Password"}, status=HTTP_400_BAD_REQUEST)

FieldsNotPresentErrorResponse = Response({"Message": "Please provide the Required Fields. Password is neccessary"},
                                         status=HTTP_400_BAD_REQUEST)

InternalServerErrorResponse = Response({"Message": "internal server error"}, status=HTTP_500_INTERNAL_SERVER_ERROR)

SuccessfullyUpdatedResponse = Response({"Message": "Successfully Updated"}, status=HTTP_200_OK)

DepartMentNotFoundErrorResponse = Response({"error": "Department not found. Please provide correct Department Name"},
                                           status=HTTP_404_NOT_FOUND)
InvalidQuizIdResponse = Response({"message": "Invalid QuizId"}, status=HTTP_400_BAD_REQUEST)

QuizNotStartedResponse = Response({"message": "Quiz Not Started Yet."}, status=HTTP_200_OK)

InvalidUserIdResponse = Response({"message": "Invalid UserId."}, status=HTTP_400_BAD_REQUEST)

QuizAlreadyAttemptedResponse = Response({"message": "Quiz Already Attempted"})

InvalidQuestionIdResponse = Response({"message": "Invalid QuestionId"}, status=HTTP_400_BAD_REQUEST)
