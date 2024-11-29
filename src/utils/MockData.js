// get /subjects
export const MockSubjectData = [
  {
    subject_id: 7,
    name: "김태훈 빨리 만들어 놔라",
    description: "김태훈 빨리 만들어 놔라",
  },
  {
    subject_id: 8,
    name: "회계관리 1급 - 재무회계",
    description: "회계관리 1급 - 재무회계",
  },
  {
    subject_id: 9,
    name: "123123123",
    description: "123123123123123",
  },
];

// get /subjects/{subject_id}
// const MockSubjectDetailData =

// get /subjects/{subject_id}/exams
export const MockExamData = [
  {
    exam_id: 5,
    subject_id: 7,
    name: "김태훈 빨리 만들어 놔라",
  },
];

// get /exams
export const MockExamListData = [
  {
    exam_id: 5,
    subject_id: 7,
    name: "김태훈 빨리 만들어 놔라",
  },
];

// get /exams/{exam_id}
export const MockExamDetailData = {
  exam_id: 5,
  subject_id: 7,
  name: "김태훈 빨리 만들어 놔라",
};

// get /questions
export const MockQuestionData = [
  {
    question_id: 4,
    exam_id: 5,
    question_text: "김태훈 빨리 만들어 놔라",
    question_type: "1",
  },
];

// get /questions/{question_id}
export const MockQuestionDetailData = {
  question_id: 4,
  exam_id: 5,
  question_text: "김태훈 빨리 만들어 놔라",
  question_type: "1",
};

// get /answers
export const MockAnswerData = [
  {
    answer_id: 5,
    question_id: 4,
    answer_text: "김태훈 빨리 만들어 놔라",
    is_correct: true,
  },
  {
    answer_id: 6,
    question_id: 4,
    answer_text: "김태훈 빨리 만들어 놔라",
    is_correct: true,
  },
  {
    answer_id: 7,
    question_id: 4,
    answer_text: "김태훈 빨리 만들어 놔라",
    is_correct: true,
  },
  {
    answer_id: 8,
    question_id: 4,
    answer_text: "김태훈 빨리 만들어 놔라",
    is_correct: true,
  },
];

// get /answers/{answer_id}
export const MockAnswerDetailData = {
  answer_id: 5,
  question_id: 4,
  answer_text: "김태훈 빨리 만들어 놔라",
  is_correct: true,
};
