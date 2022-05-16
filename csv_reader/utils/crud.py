import tempfile
from csv import reader
from typing import Dict, List

from django.db.models import QuerySet

from csv_reader.forms import GetAnswersForm, UploadFileForm
from csv_reader.models import Answers, Question, User

from .coding import choices_db
from .configure_logging import configure_logging

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
        member_gz_2021_2022=choices_db.get("yes_no").get(info[5]),
        sex=choices_db.get("sex").get(info[6]),
        age=bin(int(info[7]))[2:],
        marital_status=choices_db.get("marital_status").get(info[8]),
        living=choices_db.get("living").get(info[9]),
        children=choices_db.get("children").get(info[10]),
        work_status=choices_db.get("work_status").get(info[11]),
        working_in_fishing_or_shipping=choices_db.get("yes_no").get(info[12]),
        working_maritime=choices_db.get("yes_no").get(info[13]),
        working_fishing_industry=choices_db.get("yes_no").get(info[14]),
        working_fishing_technology=choices_db.get("yes_no").get(info[15]),
        working_aquaculture=choices_db.get("yes_no").get(info[16]),
        working_economic=choices_db.get("yes_no").get(info[17]),
        working_it=choices_db.get("yes_no").get(info[18]),
        working_other=choices_db.get("yes_no").get(info[19]),
    )
    user.save()
    logger.info("User %s successfully saved", info[3])
    return user


def create_answers(
    user: User, questions: QuerySet[Question], answers: List[str]
) -> None:
    for answer, question in zip(answers, questions):
        ans = Answers(
            user=user,
            question=question,
            answer=answer,
            answer_bin=choices_db.get("answer").get(answer),
        )
        ans.save()
    logger.info("Answers for user %s successfully saved", user.name)


def select_info(data: Dict[str, str]) -> Dict[str, str]:
    value = data.get("value")
    field = data.get("field")
    if field in ("sex", "marital_status", "children", "work_status"):
        users = User.objects.filter(**{field: choices_db.get(field).get(value)})
    elif field == "age":
        users = User.objects.filter(**{field: bin(int(value))[2:]})
    else:
        users = User.objects.filter(**{field: value})
    res: Dict[str, str] = {}
    for index, user in enumerate(users):
        answers = Answers.objects.filter(user=user.id)
        res[index] = (
            user.name,
            "".join(answer.answer_bin for answer in answers if answer.answer_bin),
        )
    return res
