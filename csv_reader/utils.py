import logging
import sys
import tempfile
from csv import reader
from typing import List

from django.db.models import QuerySet

from .forms import UploadFileForm
from .models import Answers, Question, User


def configure_logging(name: str) -> logging.Logger:
    logging_format = "[%(asctime)s] - [%(name)s] - [%(levelname)s] - [%(message)s]"
    formatter = logging.Formatter(logging_format)
    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(console_handler)
    return logger


logger = configure_logging(__file__)


def get_info(form: UploadFileForm) -> reader:
    tmp_file = tempfile.mktemp("upload.csv")
    with open(tmp_file, "w") as f:
        f.write(form.files["file"].read().decode("utf-8"))
    with open(tmp_file, "r") as f:
        csv_reader = reader(f, delimiter=",")
        questions = next(csv_reader)[20:]
        result = []
        for row in csv_reader:
            result.append({"user": row[:20], "answers": row[20:]})
    return questions, result


def check_questions(questions: List[str]) -> QuerySet[Question]:
    q_db = Question.objects.all()
    for question in questions:
        if not q_db.filter(text_question=question):
            logger.info("Question %s has been added", question)
            q = Question(text_question=question)
            q.save()
    return q_db


def create_user(info: List[str]) -> User:
    user = User(
        user_id=int(info[0]),
        time_create=info[1],
        time_changed=info[2],
        name=info[3],
        group=info[4],
        member_gz_2021_2022=info[5],
        sex=info[6],
        age=info[7],
        marital_status=info[8],
        living=info[9],
        children=info[10],
        work_status=info[11],
        working_in_fishing_or_shipping=info[12],
        working_maritime=info[13],
        working_fishing_industry=info[14],
        working_fishing_technology=info[15],
        working_aquaculture=info[16],
        working_economic=info[17],
        working_it=info[18],
        working_other=info[19],
    )
    user.save()
    logger.info("User %s successfully saved", info[3])
    return user


def create_answers(
    user: User, questions: QuerySet[Question], answers: List[str]
) -> None:
    for answer, question in zip(answers, questions):
        ans = Answers(user=user, question=question, answer=answer)
        ans.save()
    logger.info("Answers for user %s successfully saved", user.name)
