import { axiosInstance } from "../utils/api";

// 모든 시험 정보 가져오기
// response body: List[ExamResponse]
// [
//   {
//     "exam_id": 0,
//     "subject_id": 0,
//     "name": "string"
//   }
// ]
export const getAllExams = async () => {
  const response = await axiosInstance.get("exams");
  return response.data;
};

// 새로운 시험 정보 생성
// Args: ExamRequest
// {
//   "subject_id": 0,
//   "name": "string"
// }
export const createExam = async (data) => {
  const response = await axiosInstance.post("exams", data);
  return response.data;
};

// 특정 시험 정보 가져오기
// Args: exam_id
// response body: ExamResponse
export const getExam = async (examId) => {
  const response = await axiosInstance.get(`exams/${examId}`);
  return response.data;
};

// 특정 시험 정보 수정
// Args: exam_id, exam_data
// exam_data:{
//   "subject_id": 0,
//   "name": "string"
// }
export const updateExam = async (examId, data) => {
  const response = await axiosInstance.patch(`exams/${examId}`, data);
  return response.data;
};

// 특정 시험 정보 삭제
// Args: exam_id
export const deleteExam = async (examId) => {
  const response = await axiosInstance.delete(`exams/${examId}`);
  return response.data;
};

// 특정 시험에 해당하는 문제 정보 가져오기
// Args: exam_id
// response body: List[QuestionResponse]
// [
//   {
//     "question_id": 0,
//     "exam_id": 0,
//     "question_number": 0,
//     "question_text": "string",
//     "question_type": "string"
//   }
// ]
export const getQuestionsByExam = async (examId) => {
  const response = await axiosInstance.get(`exams/${examId}/questions`);
  return response.data;
};
