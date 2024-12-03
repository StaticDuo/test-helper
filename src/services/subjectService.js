import { axiosInstance } from "../utils/api";

// 모든 과목 정보 가져오기
// response body: List[SubjectResponse]
// [
//   {
//     "subject_id": 0,
//     "name": "string",
//     "description": "string"
//   }
// ]
export const getAllSubjects = async () => {
  const response = await axiosInstance.get("subjects");
  return response.data;
};

// 새로운 과목 정보 생성
// request body: SubjectRequest
// {
//   "name": "string",
//   "description": "string"
// }
export const createSubject = async (data) => {
  const response = await axiosInstance.post("subjects", data);
  return response.data;
};

// 특정 과목 정보 가져오기
// Args: subject_id
// response body: SubjectResponse
export const getSubject = async (subjectId) => {
  const response = await axiosInstance.get(`subjects/${subjectId}`);
  return response.data;
};

// 특정 과목 정보 수정
// Args: subject_id
// request body: SubjectRequest
// {
//   "name": "string",
//   "description": "string"
// }
export const updateSubject = async (subjectId, data) => {
  const response = await axiosInstance.patch(`subjects/${subjectId}`, data);
  return response.data;
};

// 특정 과목 정보 삭제
export const deleteSubject = async (subjectId) => {
  const response = await axiosInstance.delete(`subjects/${subjectId}`);
  return response.data;
};

// 특정 과목에 해당하는 시험 정보 가져오기
// Args: subject_id
// response body: List[ExamResponse]
// [
//   {
//     "exam_id": 6,
//     "subject_id": 12,
//     "name": "C_TS4FI_2023"
//   }
// ]
export const getExamsBySubject = async (subjectId) => {
  const response = await axiosInstance.get(`subjects/${subjectId}/exams`);
  return response.data;
};

// 특정 과목에 포함된 문제 정보 가져오기
// Args: subject_id, limit, randomize
// response body: List[QuestionResponse]
// [
//   {
//     "question_id": 14,
//     "exam_id": 6,
//     "question_number": 7,
//     "question_text": "You want to post depreciation costs of one asset to two cost centers. How do you do this?",
//     "question_type": "1"
//   },
// ]
export const getQuestionsBySubject = async (subjectId, limit, randomize) => {
  const query = `?limit=${limit}&randomize=${randomize}`;
  const response = await axiosInstance.get(
    `subjects/${subjectId}/questions${query}`
  );
  return response.data;
};
